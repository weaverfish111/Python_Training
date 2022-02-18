### plotting graph - "f(x) = x(squared)"
### between x = 0 to x = 1.5 (steps of 0.01) use blue line
### plot the minimum of function with red dot

import numpy as np
import math
import matplotlib.pyplot as plt

list_x = []
list_y = []
list_xmin = []
my=0
mx=0

# Create x and y lists
for x in np.arange(0, 1.5, 0.01):
    list_x.append(x)
    y=x**x
    list_y.append(y)

# Create min points for x and y by working out min position in list_y
for i in range(len(list_y)):
    if list_y[i]<list_y[my]:
        my=i
ymin = round(list_y [my], 2)
xmin = list_x [my]
print(f"(xmin, ymin) = ({xmin}, {ymin})")

# Now create the graph
plt.plot(list_x, list_y, 'b-')
plt.plot(xmin, ymin, 'ro')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.text(0.2, 1.6, "(xmin, ymin) = (0.37, 0.69)", color = 'black', fontsize = 15)
plt.show()
