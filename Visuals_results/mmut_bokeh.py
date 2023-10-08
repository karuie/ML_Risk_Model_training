from bokeh.plotting import figure, output_file, save

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# set output to static HTML file
output_file(filename="../../custom_filename.html", title="Static HTML file")

# create a new plot with a specific size
p = figure(sizing_mode="stretch_width", max_width=500, height=250)

# add a circle renderer
circle = p.circle(x, y, fill_color="red", size=15)

15# save the results to a file
save(p)


from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# create dict as basis for ColumnDataSource
data = {'x_values': [1, 2, 3, 4, 5],
        'y_values': [6, 7, 2, 3, 6]}

# create ColumnDataSource based on dict
source = ColumnDataSource(data=data)

# create a plot and renderer with ColumnDataSource data
p = figure(height=250)
p.circle(x='x_values', y='y_values', size=20, source=source)
show(p)

from bokeh.layouts import layout
from bokeh.models import Div, RangeSlider, Spinner
from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [4, 5, 5, 7, 2, 6, 4, 9, 1, 3]

# create plot with circle glyphs
p = figure(x_range=(1, 9), width=500, height=250)
points = p.circle(x=x, y=y, size=30, fill_color="#21a7df")

# set up textarea (div)
div = Div(
    text="""
          <p>Select the circle's size using this control element:</p>
          """,
    width=200,
    height=30,
)

# set up spinner
spinner = Spinner(
    title="Circle size",
    low=0,
    high=60,
    step=5,
    value=points.glyph.size,
    width=200,
)
spinner.js_link("value", points.glyph, "size")

# set up RangeSlider
range_slider = RangeSlider(
    title="Adjust x-axis range",
    start=0,
    end=10,
    step=1,
    value=(p.x_range.start, p.x_range.end),
)
range_slider.js_link("value", p.x_range, "start", attr_selector=0)
range_slider.js_link("value", p.x_range, "end", attr_selector=1)

# create layout
layout = layout(
    [
        [div, spinner],
        [range_slider],
        [p],
    ],
)

# show result
show(layout)

from bokeh.plotting import figure, show

from bokeh.resources import CDN

from bokeh.embed import file_html

from bokeh.palettes import Spectral4

from bokeh.models import ColumnDataSource

# prepare some data

x = [1, 2, 3, 4, 5]

y = [6, 7, 2, 4, 5]

# create a new plot with a title and axis labels

p = figure(title="Simple line example", x_axis_label="x", y_axis_label="y")

# add a line renderer with legend and line thickness

p.line(x, y, legend_label="Temp.", line_width=2)

# show(p)


# %%

# bok_html_file = reportingdir + "static/test/bok.html"

test_dir = "/mnt/c/python/risk/"

bok_html = file_html(p, CDN, "my plot")

# bok_html_file = outputdir + "bokeh1.html"

bok_html_file = test_dir + "bokeh1.html"

with open(bok_html_file, "w") as f:
    f.write(bok_html)

