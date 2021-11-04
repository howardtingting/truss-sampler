import os

# build normalizer executable
os.system('python3 compile.py')

# run normalizer
os.system('./normalizer < sample-inputs/sample.csv > sample-outputs/sample-out.csv')
os.system('./normalizer < sample-inputs/sample-with-broken-utf8.csv > sample-outputs/sample-broken-utf-8-out.csv')
