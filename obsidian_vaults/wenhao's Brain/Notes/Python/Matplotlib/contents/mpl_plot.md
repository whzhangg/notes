### Plotting
##### axs.plot()
axs.plot() function take arguments that specify line style or dot style. [Link to official reference](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html?highlight=plot#matplotlib.axes.Axes.plot)
    
The simplest way to call plot function is to call
```python
axs.plot(x, y, fmt)
``` 
where *fmt* is a string that describe the format. fmt can be a combined argument: for example `-g` gives a solid green line. `--c` is a dashed cyan. 
    
##### optional parameters
```text
alpha           : transparency
color or c      : specify the color, one of the form ['blue', 'g', '0.75'(grayscale), '#FFDD44', '(1.0,1.0,1.0)']
linestyle       : solid ("-"), dashed ("—"), dashdot ("-."), dotted (":")
linewidth       : float
marker          : marker style ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']
markeredgecolor : color
markeredgewidth : float
markerfacecolor : color
markersize      : float
```

##### Dot style
```python
# additional keyword arguments:
plt.plot(x, y, '-p', color='gray',      # line with pentagon points
    		markersize=15, linewidth=4,
            markerfacecolor='white',
            markeredgecolor='gray',
            markeredgewidth=2)
```

##### linespoints style    
We can combine the dot code, line code and color code together
```python
plt.plot(x, y, '-ok')
```  
create a dotted ("o") line ("-") plot in color black ("k")

### Scatter plots
##### axs.scatter()
axs.scatter() can be used to create scatter plots with variation for individual points and colormap
    
```python
plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')
# create a plot where each individual point has a distinct size and color
 
# x, y       : data positions
# s          : size of the marker
# c          : specify the color, or the scalar values to be mapped by cmap
# marker     : 'o' or 's' etc. the shape of the marker
# cmap       : colormap, string or Colormap
# vmin, vmax : the range for the cmap
# edgecolors : similar as "c" but for the edges only. this is used to make plot of empty circles 
```
    
##### Reference
Scatter() [document](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html?highlight=scatter#matplotlib.axes.Axes.scatter)

Scatter plot with empty circle: [reference](https://stackoverflow.com/questions/4143502/how-to-do-a-scatter-plot-with-empty-circles-in-python)
    


### Plotting with errorbars
##### axs.errorbar()
We use `plt.errorbar()` to plot figures with error bar. See [official reference](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html?highlight=errorbar#matplotlib.axes.Axes.errorbar)
    
```python
x = np.linspace(0, 10, 50)
dy=0.8
y = np.sin(x) + dy * np.random.randn(50)
plt.errorbar(x, y, yerr=dy, fmt='.k')
# fmt is an argument the same as combined argument style of line, dot and color
    
plt.errorbar(x, y, yerr=dy, fmt='o', color='black', 
    		 ecolor='lightgray', elinewidth=3, capsize=0);
# a different style, with wider error bar without topping cap
```
    
##### continuous errors
We can use `plt.fill_between` to plot continuous error, by passing the upper bounds and lower bounds
```python
plt.plot(xdata, ydata, 'or')               # plot the dots 
plt.plot(xfit, yfit, '-', color='gray')    # plot the lines
    
plt.fill_between(xfit, yfit - dyfit, yfit + dyfit,
    			color='gray', alpha=0.2)   # an area colored in grey
plt.xlim(0, 10);                           # alpha give transparency
```
    
The simple `fill_between()` fill the area between y1 and y2, `fill_betweenx()` fill the area specified by two x value: x1 and x2
```python
axs.fill_betweenx(y, x1, x2)
```

See official reference [fill_betweenx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html?highlight=fill_betweenx#matplotlib.axes.Axes.fill_betweenx)
    