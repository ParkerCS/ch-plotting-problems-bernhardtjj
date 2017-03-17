import csv

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Patch

with open("chi_life_expectancy.txt") as tsv:
    data = list(csv.reader(tsv, dialect="excel-tab"))

plt.figure(figsize=[5, 10], tight_layout=True)

labels = list()
life_expectancy_2010_list = list()
for dat in data[1:]:
    labels.append(dat[1])
    life_expectancy_2010_list.append(float(dat[8]))

print(labels)

# Make appropriate lists for plotting. Community name will be the x and 2010 life expectancy on the y.
# 4 Plot the life_expectancy_2010_list vs a numpy arange() as a bar graph
# 5 Use ax = plt.gca() to grab the axes object as ax. Use ax.set_xticklabels(community_list)
#  to place the labels on the x axis, use the kwarg rotation=60 to tilt the lettering since there are a lot
#  of communities
# 6  Set an appropriate plt.ylim([min,max])
# 7  Label your axes
# 8  Add a title
# 9  Add text to indicate the minimum and maximum values
# 10 Customize your graph in at least two other ways using documentation from matplotlib.org
# 11  Comment your code as always.

# Note:  If you would like to present something different than the above for your graph using this dataset,
# just let me know your intentions before you start and I will do my best to support you.
colors = ['red', 'blue', 'green']
color_list = [colors[0] for i in life_expectancy_2010_list]
color_list[life_expectancy_2010_list.index(max(life_expectancy_2010_list))] = colors[1]
color_list[life_expectancy_2010_list.index(min(life_expectancy_2010_list))] = colors[2]

# Data to make your bar graph
# y and x must be same length and order (as always)
y_data = life_expectancy_2010_list
x_labels = labels

# Make a bar graph
plt.barh(np.arange(len(y_data)), y_data, 0.8, color=color_list)

plt.title("Li$\int$e $\mathfrak{Expectancy}$ of Chicago 2010")
# # Labels your bars on the x axis
plt.yticks(np.arange(len(y_data)), x_labels, rotation=0)  # x,y,kwarg
#
plt.xlabel("Years")
plt.ylabel("Neighborhood")

plt.legend(
    handles=[Patch(color=a, label=f) for a, f in [["blue", "max"], ["green", "min"]]])

plt.show()
