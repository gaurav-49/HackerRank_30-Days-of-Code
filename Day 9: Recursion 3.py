#!/bin/python3

import math
import os
import random
import re
import sys


 
def factorial(n):
    # Complete this function
    return 1 if n==1 else factorial(n-1)*n
 
if __name__ == "__main__":
 
    n = int(input().strip())
    result = factorial(n)
    print(result)
