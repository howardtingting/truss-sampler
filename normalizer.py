import os
import sys
import csv

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

def processFooDuration(duration):
    return duration

def processBarDuration(duration):
    return duration

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
    for header in columnDict:
        column = columnDict[header]
        if header == 'FullName':
            columnDict[header] = processArray(processFullName, column)
        elif header == 'Timestamp':
            columnDict[header] = processArray(processTimestamp, column)
        elif header == 'Address':
            columnDict[header] = processArray(processAddress, column)
        elif header == 'ZIP':
            columnDict[header] = processArray(processZip, column)
        elif header == 'FooDuration':
            columnDict[header] = processArray(processFooDuration, column)
        elif header == 'BarDuration':
            columnDict[header] = processArray(processBarDuration, column)
        elif header == 'TotalDuration':
            columnDict[header] = processArray(processTimestamp, column)
        else:
            columnDict[header] = processArray(noProcess, column)
    collector = []
    for header in columnDict:
        collector.append([header] + columnDict[header])
    collector = rotate2DArray(collector)
    for row in collector:
        print(','.join(row))

main()
