import math
import collections

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp






combinations =[]
for count_100 in range(1+1):
    for count_50 in range(2+1):
        for count_25 in range(4+1):
            for count_10 in range(10+1):
                for count_5 in range(20+1):
                    for count_1 in range(100+1):
                        if 100*count_100 + 50*count_50 + 25*count_25 + 10*count_10 + 5*count_5 + count_1 == 100:
                            combinations.append([count_100, count_50, count_25, count_10, count_5, count_1])        

print(combinations)

birthdays = {(7,15): 'Michele', (3,14): 'Albert'}
print(birthdays[(7,15)])


rand_2d = np.random.random(size=(8,8))

pp.matshow(rand_2d)
