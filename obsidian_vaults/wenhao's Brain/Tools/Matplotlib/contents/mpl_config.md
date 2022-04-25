### Configurations and style
Matplotlib defines a runtime configuration containing the style for all the plot elements.
- custom styles can be created by users
- many defaults styles are included, which is listed in `plt.style.available` list

##### Using a style
We can switch to another style by calling `plt.style.use('stylename')`. In this case, style for the whole session will be changed. 

Available styles are shown here: https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html

We can temporery change the style using context mangeing:
```python
with plt.style.context('stylename'):
    commands_to_make_plot()
```


things to add:
(https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams

https://matplotlib.org/stable/tutorials/introductory/customizing.html