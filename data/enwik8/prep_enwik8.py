#!/usr/bin/env python
# coding=utf-8

import os
import sys
from tqdm import tqdm

for fn in ['train.txt', 'valid.txt', 'test.txt']:

    with open(fn, "rb") as fi:
        part = fi.read()

    print('{} will have {} bytes'.format(fn, len(part)))
    print('- Tokenizing...')
    print('- Writing...')
    
    with open(fn, 'w') as fo:
        for c in tqdm(part):
            fo.write((str(c) if c != ord('\n') else '\n') + " ")

    f = open(fn + '.raw', 'wb').write(part)
