### Ticks
The ticks are contained in Axes instance, just like Axes are contained in Figures
- Each axes has attributes xaxis and yaxis
- Each axes manage major tick and minor tick, minor ticks are not used by default unless in logscale plot
- formatter comes behind ticks: an axis can have ticks but no format, but not the other way. Setting locator to NullLocator also remove any Formatting

##### Logscale
Logscale can be specified by when instantizing the axes: `plt.axes(xscale='log', yscale='log')`

##### Setting the ticks and formats
We customize the ticks and formats by specifing the formatter and locator for the major and minor ticks:
- ax.xaxis.get_major_locator()
- ax.xaxis.get_major_formatter()
- ax.yaxis.set_major_locator(plt.NullLocator())
- ax.xaxis.set_major_formatter(plt.NullFormatter())

##### A list of formatter and locator
```
Locator                    Descriptions   
https://matplotlib.org/stable/gallery/ticks/tick-locators.html?highlight=fixedlocator
NullLocator                No ticks
FixedLocator               Tick locations are fixed
IndexLocator               Locator for index plots (e.g., where x = range(len(y)))
LinearLocator              Evenly spaced ticks from min to max
LogLocator                 Logarithmically ticks from min to max
MultipleLocator            Ticks and range are a multiple of base
MaxNLocator(N)             Finds up to a max number of ticks at nice locations
AutoLocator                (Default) MaxNLocatorwith simple defaults
AutoMinorLocator           Locator for minor ticks

Formatter                 
https://matplotlib.org/stable/gallery/ticks/tick-formatters.html?highlight=fixedlocator
NullFormatter              No labels
IndexFormatter             Set strings from a list of labels
FixedFormatter             Set strings manually for labels
FuncFormatter              Use user-defined function to set value
FormatStrFormatter         Use a format string for each value
ScalarFormatter            Default for scalar values
LogFormatter               Default for log axes
```

We can also use user-defined formatting functions, as the following example:
```python
def format_func(value, tick_number):   
    # find number of multiples of pi/2
    N = int(np.round(2 * value / np.pi)) 
    if N==0:
    	return "0"
    elif N==1:
    	return r"$\pi/2$"                      # matplot lib store latex style
    elif N==2:                                 # string formatting
    	return r"$\pi$"
    elif N%2>0:
    	return r"${0}\pi/2$".format(N)
    else:
    	return r"${0}\pi$".format(N // 2)

ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
```
    