import numpy as np
import matplotlib.pyplot as plt

i = [840,1200,1600,2400]
x = np.array(i)

num = [3273,3829,4447,5682]
y = np.array(num)

f1 = np.polyfit(x,y,1)

p1 = np.poly1d(f1)

print('p1 is:\n',p1)
