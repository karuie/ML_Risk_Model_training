from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Slider, CustomJS, DateSlider
from bokeh.layouts import column
from bokeh.io import output_notebook
from bokeh.sampledata.stocks import AAPL
import pandas as pd

# Create a pandas DataFrame from the Bokeh sample data (AAPL stock prices)
df = pd.DataFrame(AAPL)

# Convert the 'date' column to datetime format
print(type(df['date'][0]))

# Parse the date string into a datetime object
# date_object = datetime.strptime(date_string, date_format)
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# df['date'] = pd.to_datetime(df['date'])

# Create a Bokeh ColumnDataSource from the DataFrame
source = ColumnDataSource(df)

# Create a Bokeh figure
p = figure(title="AAPL Stock Prices", x_axis_label="Date", y_axis_label="Price",
           x_axis_type="datetime", width=800, height=400)

# Plot the line chart
p.line(x='date', y='close', source=source, line_width=2, legend_label="Close Price")

# Create a DateSlider widget
date_slider = DateSlider(title="Date Range", start=df['date'].min(), end=df['date'].max(),
                         value=(df['date'].min(), df['date'].max()), step=1, format="%b %Y")

# Convert Timestamps to datetime objects for the initial value
date_slider.value = tuple(pd.to_datetime(date_slider.value))

# Define a CustomJS callback to update the data source based on the date range selected in the slider
callback = CustomJS(args=dict(source=source, date_slider=date_slider), code="""
    const data = source.data;
    const start = date_slider.value[0];
    const end = date_slider.value[1];
    const dates = data['date'];
    const close = data['close'];

    const new_dates = [];
    const new_close = [];

    for (let i = 0; i < dates.length; i++) {
        if (dates[i] >= start && dates[i] <= end) {
            new_dates.push(dates[i]);
            new_close.push(close[i]);
        }
    }

    data['date'] = new_dates;
    data['close'] = new_close;

    source.change.emit();
""")

# Attach the callback to the DateSlider widget
date_slider.js_on_change('value', callback)

# Create a layout for the plot and the slider
layout = column(p, date_slider)

# Show the plot in the Jupyter Notebook
output_notebook()
show(layout)
