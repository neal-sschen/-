import numpy as np
import matplotlib.pyplot as plt

i = [840,1200,2170,2200,2400,1600,1050,830,1260,1160,1700]
x = np.array(i)

num = [3721,3940,5074,5109,5923,4407,3764,3707,4314,3893,4524]
y = np.array(num)

f1 = np.polyfit(x,y,1)

p1 = np.poly1d(f1)

print('p1 is:\n',p1)
