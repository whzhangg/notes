
### Legends
##### Adding legends
To add a legend to the plot, we first require desired labels on the curves
```python
plt.plot(x, np.sin(x), '-b', label='Sine')
```
and then call `plt.legend()`

Any customization on the legend can be specified as arguments to `.legend()`
```python
ax.legend(loc='upper left', frameon=False, ncol = 2, title = "curvename")
```

*Possible localtion*: 'best' (default), 'upper right', 'lower left', 'center center'

To make legend only to subset of curves, simply not specify label arguments for the plot that does not need a legend.

##### Customize legend
Some times, we want legends that does not associate with specific data plots. We can do this by plotting labeled data with no entries:

```python
for area in [100, 300, 500]:
		plt.scatter([], [], c='k', alpha=0.3, s=area, label=str(area) + ' km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Area')
# three points is created by scatter, for which the legend is shown
```

##### Multiple legends
To add a second legend, we can create a legend object and add the second legend object to the plot, as shown in the following example:
```python
ax.legend(lines[:2], ['line A', 'line B'], 
				  loc='upper right', frameon=False)    # legend for the first two lines

# Create the second legend explicitly
from matplotlib.legend import Legend
leg = Legend(ax, lines[2:], ['line C', 'line D'], 
					loc='lower right', frameon=False) 

ax.add_artist(leg);      # add the legend as an artist
```

### Text
##### Adding text
Simple text can be added to the plot by `plt.text (ax.text)` command. For example:

```python
ax.text(2012, 4850, "Labor Day", ha='center', size=10, color='gray' )
```
text take *x*, *y* position in data scale as first arguments, followed by a string and other keyword arguments.

##### Text position
We can choose different alignment:

| alignment | option |
| --- | --- |
| horizontalalignment (ha) | ‘center’, ‘left’, or ‘right’ |
| verticalalignment (va) | ‘center’, ‘top’, or ‘bottom’ |

We can specify which relative coordinate we use for text position by `transform` argument (passing pre-defined transformations)
```python
ax.text(0.5, 0.1, ". Axes: (0.5, 0.1)", transform=ax.transAxes)
``` 
will add text at 0.5, 0.1 relative to axis

Basically, we have three different transform argument:
1. ax.transData: position in data coordinates
2. ax.transAxes: position associated with axes (in unit of axes)
3. ax.transFigure: position associated with Figure (in unit of figure dimensions)

##### Other optional arguments
```python
alpha            : scalar
backgroundcolor  : color
color            : text color
font             : font to be used
fontsize or size : size of the font
fontstyle        : 'normal', 'italic' or 'oblique'
linespacing      : float
```

We can add *arrowed annotations* to point out a specific position of the data by:
```python
ax.annotate('local maximum', xy=(6.28, 1), xytext=(10, 4), 	arrowprops=dict(facecolor='black', shrink=0.05))
```
]which points from (10, 4) to position (6.28, 1) of the data with the given text. arrow can be specified by arrow properties

### Arrows
We can add arrows on axes using: 

```python
Axes.arrow(x, y, dx, dy, width = 0.001, length_includes_head = False, head_width = 0.05)
```

We specify the starting point of the arror, as well as the vector dx and dy. By default, length_includes_head is false, we can turn it to true to correctly contain the arrow length by: `length_includes_head = True`

For arrows, refer to the reference: [Matplotlib reference for arrows](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.arrow.html?highlight=arrow#matplotlib.axes.Axes.arrow)