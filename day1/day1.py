#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 09:29:54 2021

@author: vineeth
"""

import numpy as np
from itertools import combinations

file = open("input.txt", "r")

content=file.readlines()

arr = np.asarray(content, dtype=np.int64)

for num in combinations(arr, 2):

    if num[0] + num[1] == 2020:
        print(num[0] * num[1])

for num in combinations(arr, 3):

    if num[0] + num[1] + num[2] == 2020:
        print(num[0] * num[1] * num[2])
