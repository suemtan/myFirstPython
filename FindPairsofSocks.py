import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dictarr = {x: ar.count(x) for x in ar}

    v = dictarr.values()
    print v
    tarray = v
    count = 0

    for sock in tarray:
        temp = sock
        while temp > 1:
            count += 1
            temp = temp / 2

    return count


ar=[10,20, 20, 10, 10, 30, 50, 10, 20]
ar2=[1, 1, 3, 1, 2, 1, 3, 3, 3, 3]

n = len(ar)
n1 = len(ar2)

print(sockMerchant(n, ar))

print(sockMerchant(n1, ar2))