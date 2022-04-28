### Contour images
##### Line contour
```python
plt.contour(x, y, z, 20, colors = 'black')
```
plot a line contour *with 20 intervals* on a 2D figure. When a single color is used, negative values are represented by dashed lines, positive values by solid lines.

A line contour with color map can be made by: 
```python
plt.contour(X, Y, Z, 20, cmap='RdGy') # red-gray
```

##### Filled contour
A filled contour fill color within the contour lines: 
```python
plt.contourf(x, y, z, 20, cmap = 'RdGy')
```

And a color bar can be given by `plt.colorbar()`

##### Density as image
We can plot a 2D image with
```python
plt.imshow(Z, extent = [xmin, xmax, ymin, ymax], origin = 'lower', cmap = 'RdGy')
```
    
`Z` is expected to be a 2D array,` imshow()` do not accept x, y value. instead it takes extent as arguments, origin set the corner where xmin and ymin are located

### Histogram
##### axs.hist()
calculate the distributioin and display the data. See [here](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html) for reference

##### 1D histogram 
1D histogram can be plotted by:

```python
plt.hist(data, bins=30, density=True, alpha=0.5, histtype='stepfilled', color='steelblue', edgecolor='none');
```

Data is expected to be a array of continuous values, which then is divided into number of bins. `normed` option make the distribution sum to 1

##### 2D histogram
2D histogram can be plotted by 
```python
plt.hist2d(x, y, bins = 30, cmap = 'blues')
```


### Colormaps
##### colorbar
To create a colorbar, specify cmap as argument in plotting and use `plt.colorbar()`

Colorbar itself is an instance of Axes and can be customized similarly to plots
For example `plt.clim(-1, 1)` specifies the colormap limit.
    
```python
plt.colorbar(ticks=range(6), label='digit value')
```
specifies the label and ticks
    
Choice of colormap is discussed in this webpage: [Colormap in Matplotlib](https://www.analyticsvidhya.com/blog/2020/09/colormaps-matplotlib/)

##### Discrete colorbars
We can obtain a discrete colormap by `plt.cm.get_cmap("name", bins)`, where we passed the name of a colormap and the number of desired bins

```python
plt.scatter(projection[:, 0], projection[:, 1], lw=0.1,
						c=digits.target, cmap=plt.cm.get_cmap('cubehelix', 6)) 
plt.colorbar(ticks=range(6), label='digit value')
plt.clim(-0.5, 5.5)
# which will plot the data in 6 evenly spaced color
```
