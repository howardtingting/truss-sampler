import os
import sys
import csv
import math
#usage: python3 normalizer.py < input.csv > out.csv
#test: python3 test.py
    #this test outputs to sample-outputs

def rotate2DArray(arr):
    if not arr:
        return arr
    numRows = len(arr)
    numCols = len(arr[0])
    # check columns and headers are all equal length
    for row in arr:
        if len(row) != numCols:
            return arr
    rotatedArr = []
    for colIndex in range(numCols):
        col = [arr[i][colIndex] for i in range(len(arr))]
        rotatedArr.append(col)
    return rotatedArr

def readCLI():
    #write to temp file
    csvColumnList = []
    tempFileName = 'temp0321.csv'
    with open(tempFileName, 'w') as tempFile:
        out = sys.stdin.readline()
        while(len(out) > 0):
            tempFile.write(out)
            out = sys.stdin.readline()
        tempFile.close()
    with open(tempFileName, 'r') as csvfile:
        reader = csv.DictReader(csvfile, quotechar='"', delimiter=',',
                 quoting=csv.QUOTE_ALL, skipinitialspace=True)
        for row in reader:
            csvColumnList.append(row)
        csvfile.close()
    os.system(f'rm {tempFileName}')
    return csvColumnList

def noProcess(value):
    return str(value)

def processTimestamp(timestamp):
    date, hhmmss, ampm = timestamp.split(' ')
    month, day, year = date.split('/')
    year = '20' + year
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    hh, mm, ss = hhmmss.split(':')
    if hh == '12' and mm == '00' and 'ss' == '00' and ampm == 'AM':
        hh = '00'
    if ampm == 'PM' and hh != '12':
        hh = str(int(hh) + 12)
    hh = str(int(hh) + 3) #convert to eastern from PST
    if int(hh) >= 24:
        hh = str(int(hh) - 24)
        if len(hh) == 1:
            hh = '0' + hh
    timestamp = '-'.join([year, month, day]) + 'T' + ':'.join([hh, mm, ss]) + '-05:00'
    return timestamp

def processZip(zip):
    padLen = len(zip)
    if padLen < 5:
        zeroes = ''.join(['0' for _ in range(5-padLen)])
        zip = zeroes + zip
    return zip

def processFullName(fullName):
    return fullName.upper();

def processAddress(address):
    return address

def durationToSeconds(duration):
    hh,mm,ssms = map(lambda x: float(x), duration.split(':'))
    totalSeconds = str(int((hh * 60 * 60) + (mm * 60) + math.floor(ssms)))
    return totalSeconds

def processFooDuration(duration):
    return durationToSeconds(duration)

def processBarDuration(duration):
    return durationToSeconds(duration)

def processTotalDuration(duration):
    return duration

def processArray(processFn, arr):
    result = []
    for elem in arr:
        result.append(processFn(elem))
    return result

def main():
    csvDictLi = readCLI()
    if not csvDictLi:
        return
    headers = list(csvDictLi[0].keys())
    columnDict = {key: [] for key in headers}
    numRows = len(csvDictLi)
    for header in headers:
        for row in range(numRows):
            columnDict[header].append(csvDictLi[row][header])
    columnDict['FullName'] = processArray(processFullName, columnDict['FullName'])
    columnDict['Timestamp'] = processArray(processTimestamp, columnDict['Timestamp'])
    columnDict['Address'] = processArray(processAddress, columnDict['Address'])
    columnDict['ZIP'] = processArray(processZip, columnDict['ZIP'])
    columnDict['FooDuration'] = processArray(processFooDuration, columnDict['FooDuration'])
    columnDict['BarDuration'] = processArray(processBarDuration, columnDict['BarDuration'])
    columnDict['TotalDuration'] = [str(int((math.floor(float(x) + float(y))))) for (x,y) in zip(columnDict['FooDuration'], columnDict['BarDuration'])];
    collector = []
    for header in columnDict:
        collector.append([header] + columnDict[header])
    collector = rotate2DArray(collector)
    for row in collector:
        print(','.join(row))

main()
