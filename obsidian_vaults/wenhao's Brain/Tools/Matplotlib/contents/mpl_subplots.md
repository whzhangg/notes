### Creating subplots
##### Adding axes to figures
We can use 
```python
ax2 = plt.axes([left, bottom, width, height])
``` 
to add a new axes to our plots. 

`plt.axes()` without argument default to the whole figure

In OOP, we add axes by `ax1 = fig.add_axes()`
*! adding axes without parameter is depericated, use ax1 = fig.add_subplot()*

##### Subplot on grids
`plt.subplot(a, b, c)` create a subplot, with a, b, c be integer values giving number of rows, columns and index. Index is counted by going over subplots from left to right in the same row, than the next row from left to right

`plt.subplots_adjust(hspace = 0.2, wspace = 0.2)` allow adjusting the spacing between figures, the values are giving in units of subplot size, give the spacing along the height and width of the figures

##### plt.subplots
plt.subplots() return a figure and all the axes in an Numpy array, for the convenience of indexing. We use the axes for the individual plots
```python
fig, axes = plt.subplots(2, 3, sharex='col', sharey='row')
```

sharex and sharey automatically remove the tics and labels in the inner plots

##### GridSpec
We can creating a gridspec by: 
```python
grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
```
which allow we to create subplots that span multiple rows and columns by array slicing.

Example of Gridspec
```python
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 3000).T
    
# Set up the axes with gridspec
fig = plt.figure(figsize=(6, 6))
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax) 
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)
    
# scatter points on the main axes
main_ax.plot(x, y, 'ok', markersize=3, alpha=0.2)
                
# histogram on the attached axes
x_hist.hist(x, 40, histtype='stepfilled', orientation='vertical', color='gray')
x_hist.invert_yaxis()
y_hist.hist(y, 40, histtype='stepfilled', orientation='horizontal', color='gray')
y_hist.invert_xaxis()
```
    
