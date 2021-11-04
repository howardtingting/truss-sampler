import os

# build normalizer executable
src = open('normalizer.py', 'r')
target = open('normalizer', 'w')
prepend = '#!/usr/bin/env python3\n\n'
target.write(prepend)
srcLines = src.readlines()
for line in srcLines:
    target.write(line)
src.close()
target.close()
