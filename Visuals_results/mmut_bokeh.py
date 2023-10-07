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

# save the results to a file
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

