
### Two Interface
##### matlab stype interface
We interact with the pyplot interface directly. The code try to keep track the current figure and axes, similar to the multiplot process in gnuplot.
 ```python
x = np.linspace(0, 10, 1000) 
plt.figure()
# first subplot
plt.subplot(2, 1, 1) # (rows, columns, panel number) 
plt.plot(x, np.sin(x))
# second subplot
plt.subplot(2, 1, 2) 
plt.plot(x, np.cos(x));
plt.show()       # interactive plot
```
    
##### Object-oriented interface
We use the class method of fig and axes object directly.
- `plt.Figure` is a single container that contain all objects including axes, graphics, texts
- `plt.Axes` is a bounding box with ticks and labels that contain the data plot

```python
fig = plt.figure() 
axs = plt.subplots()
x = np.linspace(0, 10, 1000) 
axs.plot(x, np.sin(x));
fig.savefigure("f1.png")        # file will be saved according to the postfix 
```
    
##### Importing convention
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
```

##### Range, label and title
- Range : `ax.set_xlim(-10, 10)`
- Axis Label : `ax.set_xlabel("x")`
- Title : `ax.set_title(" ")`