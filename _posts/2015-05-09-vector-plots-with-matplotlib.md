---
layout:     post
title:      Vector plots with Matplotlib
date:       2015-05-09 10:34:10
summary:    Vector plots can also be made in Matplotlib.
permalink:	vector-plots-with-matplotlib
---

Vector plots can also be made in Matplotlib. Here is a script producing a vector plot and a key showing the scale of the vectors:
{% highlight python lineanchors %}
x = linspace(0,10,11)
y = linspace(0,15,16)
(X,Y) = meshgrid(x,y)
u = 5*X
v = 5*Y
q = plt.quiver(X,Y,u,v,angles='xy',scale=1000,color='r')
p = plt.quiverkey(q,1,16.5,50,"50 m/s",coordinates='data',color='r')
xl = plt.xlabel("x (km)")
yl = plt.ylabel("y (km)")
plt.show()
{% endhighlight %}

![matplotlib](http://i.imgur.com/oDbNgUg.png)

The quiver command produces vector plots from two-dimensional arrays (u and v in this case) containing the vector component values. The grid on which the vectors are plotted is defined by the first two arguments of quiver – the two-dimensional arrays X and Y in this case. However, quiver will accept the original one-dimensional axis vectore x and y as well. The color of the vectors is specified in the usual fashion with the color keyword.

The quiver arguments angles='xy' and scale=1000 are very important. Setting the angles keyword to 'xy' means that the vector components are scaled according to the physical axis units rather than geometrical units on the page. The actual scaling factor which multiplicatively converts vector component units to physical axis units is width/scale where width is the width of the plot in physical units andscale is the number specified by the scale keyword argument of quiver. In our example width = 10 km and scale = 1000, so vectors are plotted to a scale of 0.01 km / ( m / s). The angle keyword argument is not available in versions of Matplotlib earlier than 0.99, which is a serious omission.

The quiverkey command produces a legend consisting of a single vector and a label indicating how long it is in physical units. In order, the positional arguments are (1) the variable returned by the quiver command, (2) and (3) the x and y coordinates of the legend, (4) the length of the arrow in physical units, and (5) the legend label. The keyword argument coordinates tells Matplotlib which units define the legend location; the most useful are ’axes’, in which x and y range from 0 to 1 across the plot and ’data’ in which physical axis coordinates are used. As in the above example, the legend may be located outside of the actual plot.