# Generate Graphs and Chart
# pip install plotly
import plotly.graph_objects as go
x = [1, 2, 3, 4, 5]
y = [1.0, 2.6, 3.3, 4.2, 5.5]
# Bar Chart
fig = go.Figure(data=[go.Bar(x=x, y=y)])
fig.show()
# Scatter Plot
fig = go.Figure(data=[go.Scatter(x=x, y=y)])
fig.show()
# Line Chart
fig = go.Figure(data=[go.Scatter(x=x, y=y)])
fig.show()
# Pie Chart
fig = go.Figure(data=[go.Pie(labels=x, values=y)])
fig.show()
# 3d Scatter Plot
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z)])
fig.show()
# 3d Line Plot
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z)])
fig.show()
# Histogram
fig = go.Figure(data=[go.Histogram(x=x)])
fig.show()
# Multiple line plot
fig = go.Figure(data=[go.Scatter(x=x, y=y), go.Scatter(x=x, y=z)])
fig.show()
# Save Graph
fig.write_html("plot.html")