import os

os.system('python3 normalizer.py < samples/sample.csv > sample-outputs/sample-out.csv')
os.system('python3 normalizer.py < samples/sample-with-broken-utf8.csv > sample-outputs/sample-broken-utf-8-out.csv')
