"""
----------------------------MATPLOTLIB-------------------------------
Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
It is open source and we can use it freely.
It is mostly written in python, a few segments are written in C 
and Javascript for Platform compatibility.

"""
import numpy as np
import matplotlib
print(matplotlib.__version__)

"""
Pyplot
Most of the Matplotlib utilities lies under the pyplot submodule, 
and are usually imported under the plt alias:

"""
import matplotlib.pyplot as plt

xpoints = np.array([0, 6,10,56])
xpoints
ypoints = np.array([0, 250,45,66])
ypoints
plt.plot(xpoints, ypoints)


# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.plot(xpoints, ypoints)
# Default X-points - ploting without X-points
#xpoint(0,1,2,3,4,5)
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)


"""-----------------------------MATPLOTLIB Scatter Plot-----------------------------
The scatter() function plots one dot for each observation. It needs two arrays of 
the same length, one for the values of the x-axis, and one for values on the y-axis

"""

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

# Comparing tow plots

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color="#00b300")

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color="red")

# method to cahnge the color in the plot
plt.scatter(x, y, color = '#88c999')

"""-----------------------------MATPLOTLIB Bar Graphs----------------------------
Use the bar() function to draw bar graphs: 
"""
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y)
# Horizontal Bar graph
plt.barh(x, y)
plt.bar(x, y, width = 0.1) # bar width


"""----------------------- Mention labels in plot------------------"""

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)
plt.grid()
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

#######################################################
import matplotlib.pyplot as plt   # Matplot library use
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')     # plot method
plt.plot(ypoints, 'o:g')            # notation and color together
plt.plot(ypoints, marker = 'o', ms = 20)  # ms to set the size of the markers
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')  # ms to set the color of the markers edge
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')  # ms to set the color of the markers face
plt.show()

#  Adding label and title name in a graph
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)
plt.title("Sports Watch Data")    # title name 
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()

#  Changing the font color and font style in graph labels anf title
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'black','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.show()

#  Changing the location of title in graph

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.show()

# Multiple graph plot by using subplot()

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()

# draw pie chart

y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show() 
# Adding labels to pie chart

y = np.array([35, 25, 25, 15,87])
mylabels = ["Apples", "Bananas", "Cherries", "Dates","cherry"]
plt.pie(y, labels = mylabels)
plt.show() 

# adding angles 

plt.pie(y, labels = mylabels, startangle = 120)
plt.show() 

# Explode the wedge fro the pie graph

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0.3, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True) 
plt.show()

# Specifying a new color for each wedge:

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "red"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 

# adding legend in pie chart with title

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:", loc = 'top')
plt.show() 
import numpy as np
import matplotlib.pyplot as plt
y = np.array([350, 250, 650, 150])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels, autopct='%1.3f%%')
# 1.2f for the hundreds and 1.3 for thousands
plt.show() 
import numpy as np
import matplotlib.pyplot as plt
y = np.array([50, 60, 30, 40])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels, autopct='%1.1f%%')
# 1.2f for the hundreds and 1.3 for thousands
plt.show() 
# draw pie chart

y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show() 
# Adding labels to pie chart

y = np.array([35, 25, 25, 15,87])
mylabels = ["Apples", "Bananas", "Cherries", "Dates","cherry"]
plt.pie(y, labels = mylabels)
plt.show() 

# adding angles 

plt.pie(y, labels = mylabels, startangle = 120)
plt.show() 

# Explode the wedge fro the pie graph

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0.3, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True) 
plt.show()

# Specifying a new color for each wedge:

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "red"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 

# adding legend in pie chart with title

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:", loc = 'top')
plt.show() 
#########################################
#adding percentage
import numpy as np
import matplotlib.pyplot as plt
y = np.array([350, 250, 650, 150])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels, autopct='%1.3f%%')
# 1.2f for the hundreds and 1.3 for thousands
plt.show() 
import numpy as np
import matplotlib.pyplot as plt
y = np.array([50, 60, 30, 40])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels, autopct='%1.1f%%')
# 1.2f for the hundreds and 1.3 for thousands
plt.show() 
