# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Visitors by Month (25pts)
# open and read in the "chilib_visitors_2016" file into a list
import csv

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D as Patch

plt.figure(figsize=[10, 5], tight_layout=True)

with open("chilib_visitors_2016") as tsv:
    data = list(csv.reader(tsv, dialect="excel-tab"))
    labels = data[0][1:-1]
    month_visits = [0 for i in labels]
    for i in range(len(data[1:])):
        for n in range(len(data[1:][i][1:-1])):
            month_visits[n] += int(data[1:][i][1:-1][n])
print(labels)
print(month_visits)
# calculate (and make a list of) the total visitors to Chicago libraries each month.
# Do not plot every library individually.  Find the total for all libraries and plot that.
# Additionally, add lines for the three most visited libraries.
# plot the total visitors on the y and month on the x.  You will have 4 separate lines (total and 3 libraries)
# add a legend
# label axes, title the graph

libraries = data[1:]

maximum_brers = [[0, "", 0] for i in range(3)]
saved_value = 10000000000000000000000
for i in range(len(maximum_brers)):
    for brer in range(len(libraries)):
        if saved_value > int(libraries[brer][-1]) > maximum_brers[i][0]:
            maximum_brers[i] = [int(libraries[brer][-1]), libraries[brer][0], brer]
    saved_value = maximum_brers[i][0]

print(maximum_brers)

my_legend = [['darkgreen', '8', 5, ':', 10, "Total for all Libraries"]]

# Data to make your bar graph
# y and x must be same length and order (as always)
y_data = month_visits
x_labels = labels

# Make a bar graph
line, = plt.plot(np.arange(len(y_data)), y_data)
functions = [line.set_color, line.set_marker, line.set_linewidth, line.set_linestyle, line.set_markersize]
for i in range(len(functions)):
    functions[i](my_legend[0][i])

colors = ['blue', 'red', 'purple']
markers = ["v", "*", "s"]
line_width = 3
line_style = '-'
marker_size = 10

for brer in range(len(maximum_brers)):
    y_data = [0 for i in month_visits]
    i = maximum_brers[brer][2]
    for n in range(len(data[1:][i][1:-1])):
        y_data[n] += int(data[1:][i][1:-1][n])
    line, = plt.plot(np.arange(len(y_data)), y_data)
    functions = [line.set_color, line.set_marker, line.set_linewidth, line.set_linestyle, line.set_markersize]

    attributes = [colors[brer], markers[brer], line_width, line_style, marker_size, maximum_brers[brer][1]]
    for i in range(len(functions)):
        functions[i](attributes[i])
    my_legend.append(attributes)

plt.grid()  # turns on major tick grid
plt.title("Total visitors to Chicago Libraries by Month")
# Labels your bars on the x axis
plt.xticks(np.arange(len(y_data)), x_labels, rotation=45)  # x,y,kwarg

plt.xlabel("Month")
plt.ylabel("People")

plt.legend(
    handles=[Patch([], [], color=a, marker=b, linewidth=c, linestyle=d, markersize=e, label=f) for a, b, c, d, e, f in
             my_legend])

plt.show()
