#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    
    n = int(input().strip())
 
#a single line for loop
#the loop means that split string 'n' based on the spaces between
#the string 'n' and convert each string to integer and append it
#to list 'arr'
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
 
#reverse the list 'arr' by using reversed function
a= list(reversed(arr))
 
#for loop for printing reverse of input
for x in a:
    print(x, end=' ')
