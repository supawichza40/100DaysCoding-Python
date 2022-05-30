#!/bin/python3

import math
from mimetypes import init
from multiprocessing.dummy import Array
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q:Array):
    # # Write your code here
    #Trial 1
    # initial = [1,2,3,4,5,6,7,8]
    # counter = 0
    # for index in range(len(initial)-1,-1,-1):
        
    #     for val in range(3):
    #         if val >=2:
    #             print("Too chaotic")
    #             return
                
    #         if initial[index]==q[index]:
    #             break
    #         else:
    #             temp =initial[index-1]
    #             initial[index-1]=initial[index]
    #             initial[index]= temp
    #             counter+=1
    #             continue
    # print(counter)
    #Trial 2
    #Since we only want to know the count, we can compare the original position with the new position and divide by half.
    initial = [1,2,3,4,5,6,7,8]
    count = 0
    for index in range(len(q)):
        index_difference = abs(initial.index(q[index])-index)
        print(initial.index(q[index]),index)
        if index_difference>2 and initial.index(q[index])-index>0:
            print("Too chaotic")
        else:
            count+=index_difference
            if index_difference>2 and initial.index(q[index])-index<0:
                count+=abs(initial.index(q[index])-index)-2
    print(count/2)
        
minimumBribes([1,2,5,3,7,8,6,4])
