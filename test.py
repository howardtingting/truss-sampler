import os
from os import listdir
from os.path import isfile, join
# build normalizer executable
os.system('python3 compile.py')

# run normalizer

mypath = './sample-inputs'
inputs = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for input in inputs:
    os.system(f'python3 normalizer.py < sample-inputs/{input} > sample-outputs/{input}')
