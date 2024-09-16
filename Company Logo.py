# importing the required modules
import math
import os
import random 
import re
import sys
from collections import Counter

# Using __name__ variable
if __name__ == '__main__':
    
    # taking imput and then sorting 
    s = sorted(input().strip())
    
    # finiding frequency 
    s_counter =Counter(s).most_common()
    
    # using lambda function sort the items with frequencies in deceding order
    s_counter = sorted(s_counter, key=lambda x: (x[1] * -1, x[0]))

    # printing the first three items
    for i in range(0, 3):
        print(s_counter[i][0], s_counter[i][1])
