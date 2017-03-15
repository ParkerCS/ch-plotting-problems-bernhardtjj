import csv

with open("chi_life_expectancy.txt") as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
        print(line)

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
