from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Slider, CustomJS, DateSlider,DateRangeSlider
from bokeh.layouts import column
from bokeh.io import output_notebook
from bokeh.sampledata.stocks import AAPL
import pandas as pd
from datetime import date, datetime

# Create a pandas DataFrame from the Bokeh sample data (AAPL stock prices)
df = pd.DataFrame(AAPL)

# Convert the date column to the yyyy-mm-dd hh:mm:ss format
# df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d').dt.strftime('%Y-%m-%d %H:%M:%S')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
print(df.head())
print(type(df['date'][0]))
print(type(df['date'][100]))

df.date = pd.to_datetime(df.date)
print(type(df['date'][100]))
print(len(df.date))
for i in range(len(df.date)):
    df['date'][i] = df['date'][i].date()
    # df['date'][i] = datetime.combine(df['date'][i], datetime.min.time())

print(df['date'][0])
print(type(df['date'][0]))


# for i in range(len(df['date'])):
#     df['date'][i] = df['date'][i].to_pydatetime()
#     print(str(df['date'][i]).split()[0])

# Convert the 'date' column to datetime format
# df['date'] = pd.to_datetime(df['date'])
# df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
# print(df['date'])
# df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%m:%s')
# df['date'] = df['date'].strftime('%Y-%m-%d %H:%M:%S')


# Create a Bokeh ColumnDataSource from the DataFrame
source = ColumnDataSource(df)

# Create a Bokeh figure
p = figure(title="AAPL Stock Prices TS analysis", x_axis_label="Date", y_axis_label="Price",
           x_axis_type="datetime", width=800, height=400)

# Plot the line chart
p.line(x='date', y='close', source=source, line_width=2, legend_label="Close Price")


print(df['date'].min())
min = df['date'].min()
print(df['date'].max())
max = df['date'].max()
# Create a DateSlider widget
date_slider = DateRangeSlider(title="Date Range", start=min, end=max,
                         value=(min, max))

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
# output_notebook()
show(layout)
