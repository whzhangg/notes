
### 3D plotting
##### Using 3D plot
3D plotting in matplotlib is imported by 
```python
from mpl_toolkits import mplot3d
```
With the submodule imported, we can create 3D axes by projection argument:
```python
ax = plt.axes(projection='3d')
```
    
We can adjust the viewing angle by `ax.view_init(a, b)`, where *a* gives the elevation (angle relative to x-y plane) and *b* gives the azimuth angle (rotation along z)

The following plotting is similar to the 2D plotting
##### Lines
Lines can be plotted using `ax.plot3D(xline, yline, zline, 'gray')`
##### Points
Points are plotted by `ax.scatter3D(xdata, ydata, zdata, c = zdata, cmp = "Greens")`
##### Contour
Contour is plotted as `ax.contour3D(X, Y, Z, 50, cmap = 'binary')`, note that X, Y, Z need to be 2D that can be indexed by `[i,j]` i.e. the coordinate of a point is given by `X[i,j], Y[i,j], Z[i,j]`
##### Wirefram
Wireframe are plotted `ax.plot_wireframe(X, Y, Z, color = 'black')`
##### Surface
`ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = 'RdGy', edgecolor = 'none')` fill the polygon of the wireframe with color
##### Triangulations
`ax.plot_trisurf(x, y, z, cmap = 'viridis', edgecolor = 'none')` 
For the input, x, y and z are simply 1D array giving sampled points in the 3D space `[x[i], y[i], z[i]]`. trisurf try to create a surface by finding the triangles formed between adjacent points in 3D space.
