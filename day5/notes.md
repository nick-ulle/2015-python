
There are many different packages for plotting with Python. These are split
into two ecosystems, "matplotlib" and "javascript". 

* The "matplotlib" ecosystem has highly-customizable tools well-suited for
  printed graphics and interative (offline) applications. Some members:
    + matplotlib - general plotting
    + seaborn - "pretty" statistical plotting
    + ggplot - grammar of graphics plotting
    + basemap - old maps package, using shapefiles
    + cartopy - new maps package, using GeoJSON and recent Python GIS libraries
* The "javascript" ecosystem is less mature, but growing fast. These modules
  are designed for interactive web graphics. Each leverages a javascript
  library. Many require an HTML server to work. Some members:
    + bokeh (D3.js) - general plotting, especially large/streaming data
    + vincent (vega.js) - general plotting
    + folium (leaflet.js) - interactive world maps (similar to Google Maps)
    + kartograph (kartograph.js) - interactive maps

Since it's the most mature, we'll look at matplotlib first.

matplotlib can be used interactively (PyLab) or in a non-interactive style. The
interactive functions are in `matplotlib.pyplot`.

The basic plotting function is `plot()`. It can produce line and scatter plots.
Plots can be customized quickly with format strings, or more verbosely using
parameters. Note the `plot()` can plot several lines in one call.

Other plots are available:

* acorr
* bar
* barh
* boxplot
* contour
* errorbar
* hist
* scatter
* violinplot
* xcorr

Writing non-interactive matplotlib code gives you more control over the
resulting plots. In order to understand the documentation, you need to learn
some jargon:

* Figure - a drawing surface
* Axes - a single plot, including its axes, title, lines, etc...
* Artist - a single element of a plot; for example, a line

It's possible to use non-interactive methods directly at the interpreter, but
easuer to use them in a script. Every Python script is a module, meaning it
can be imported in other scripts. Scripts are also very easy to document using
docstrings (triple-quoted strings).

