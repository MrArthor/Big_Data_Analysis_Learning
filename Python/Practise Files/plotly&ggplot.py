#simple line plot by uisng plotly

import plotly.express as px  
import pandas as pd
df = pd.read_csv('E:/data/split3.csv')
df
# plotting the line chart using csv file
fig = px.bar(df, x="absences", y="age")  
# showing the plot 
fig.show()
##################################################
# line chart
import plotly.express as px  
import pandas as pd
  
df = pd.read_csv('E:/data/split3.csv')
# plotting the line chart using csv file
fig = px.line(df, x="absences",y="age")  
  
# showing the plot 
fig.show()
##################################################

 # plotting the histogram 
import plotly.express as px  
df = pd.read_csv('E:/data/split3.csv')
# plotting the line chart using csv file
fig = px.histogram(df, y="age")  
# showing the plot 
fig.show()
##################################################
  
# plotting the scatter chart
import plotly.express as px  
df = pd.read_csv('E:/data/split3.csv')
# plotting the line chart using csv file
fig = px.scatter(df, x="absences", y="age")  
# showing the plot 
fig.show()
###############################################
# plotting the pie chart 
import plotly.express as px  
  
df = pd.read_csv('E:/data/split3.csv')
  
fig = px.pie(df, values="absences", names="name")  
  
# showing the plot 
fig.show()
#################################################
# plotting the Box 
import plotly.express as px  
  
df = pd.read_csv('E:/data/split3.csv')
  
fig = px.box(df, x="absences", y="age")  
  
# showing the plot 
fig.show()
###########################################
import plotly.express as px  
  
df = pd.read_csv('E:/data/split3.csv')

# plotting the violin chart 
fig = px.violin(df, x="age") 
  
# showing the plot 
fig.show()
#########################################
# gant chart
import plotly.figure_factory as ff  
  
# Data to be plotted 
df = [dict(Task="A", Start='2020-01-01', Finish='2009-02-02'),
    dict(Task="Job B", Start='2020-03-01', Finish='2020-11-11'),  
    dict(Task="Job C", Start='2020-08-06', Finish='2020-09-21')]  
  
# Creating the plot 
fig = ff.create_gantt(df)  
fig.show()

###########################################################
#3D line graph
import plotly.express as px  
  
# data to be plotted 
df = pd.read_csv('E:/data/split3.csv')
  
# plotting the figure 
fig = px.line_3d(df, x="age", y="absences", z="perc", color="name")  
  
fig.show()
#######################################################################
# plotting #D Scatterd
import plotly.express as px  
  
# Data to be plotted 
df = pd.read_csv('E:/data/split3.csv')
  
# plotting the figure 
fig = px.scatter_3d(df, x="age", y="absences", z="perc", color="name")  
  
 
fig.show() 
###################################################################
import plotly.express as px 
# windgraph
  
# using the wind dataset 
#df = px.data.wind() 
df = pd.read_csv('E:/data/split3.csv')
df1=px.data.wind()
  
fig = px.bar_polar(df, r="age", theta="perc", color="name",) 
fig.show()
##################################################################
import plotly.express as px 
  
 # Data to be plotted 
df = pd.read_csv('E:/data/split3.csv')
  
# plotting the figure 
fig = px.bar_polar(df, r = "age", theta= "absences", color="age") 
  
fig.show()
#####################################################################

import pandas as pd 
from plotnine import ggplot 
  
# reading dataset 
df = pandas.read_csv("Iris.csv") 
  
# passing the data to the ggplot  
# There will be blank output because axis and colm compnonet is not given
ggplot(df)

#############################################################################
#Statistical transformations

import pandas as pd 
from plotnine import ggplot, aes, geom_col 
  
# reading dataset 
df = pd.read_csv("E:/data/split3.csv") 
  
ggplot(df) + aes( x="absences", y="age") + geom_col()

###################################################################
import pandas as pd 
from plotnine import ggplot, aes, geom_col 
  
# reading dataset 
df = pd.read_csv('E:/data/split3.csv')
  # geom_col is for bar chart
ggplot(df) + aes(x="age", y="perc") + geom_col()
###################################################################
import pandas as pd 
from plotnine import ggplot, aes, geom_histogram 
#Geometric Objects (geoms)such as point, line, histogram, bar, boxplot, etc.
  
# reading dataset 
df = pd.read_csv('E:/data/split3.csv')
  
ggplot(df) + aes(x="age") + geom_histogram(bins=25)
##################################################################
coord_flip() function.: plot histogram horizontally.

import pandas as pd 
from plotnine import ggplot, aes, geom_histogram 
#Geometric Objects (geoms)such as point, line, histogram, bar, boxplot, etc.
  
# reading dataset 
df = pd.read_csv('E:/data/split3.csv')
  
ggplot(df) + aes(x="age") + geom_histogram(bins=25) + coord_flip() 

#################################################################
#Themes: improving the looks of the data visualization
#########################################################


import pandas as pd 
import plotnine
from plotnine import ggplot, aes, facet_grid, labs, geom_col, theme_dark

# theme type: theme_classic, theme_gray, theme_light, theme_538()
# reading dataset 
df = pd.read_csv("E:/data/tips.csv") 

plot =( 
	ggplot(df) 
	+ facet_grid() 
	+ aes(x="day", y="total_bill", fill="time") 
	+ labs( 
		x="day", 
		y="total_bill", 
	) 
	+ geom_col() + theme_dark()
	)
plot.show()

# save the plot graph
plot.save("E:/data/abc.png")



#########################################################################################################
#draw the plot using map function

import seaborn 
import matplotlib.pyplot as plt 

# loading of a dataframe from seaborn 
df = seaborn.load_dataset('tips') 


graph = seaborn.FacetGrid(df, col ="sex", hue ="day") 
# map the above form facetgrid with some attributes 
graph.map(plt.scatter, "total_bill", "tip").add_legend() 
# show the object 
plt.show() 


import seaborn 
import matplotlib.pyplot as plt 
  
df = seaborn.load_dataset('tips') 
  
graph = seaborn.FacetGrid(df, row ='smoker', col ='time') 
# map the above form facetgrid with some attributes 
graph.map(plt.hist, 'total_bill', bins = 15, color ='green') 
# The height of each bin shows how many values from that data fall into that range.
#The default value of the number of bins to be created in a histogram is 10
plt.show() 

####################################################################################################
# use of plotnine from ggplot library
from plotnine import ggplot, aes, geom_point, labs, facet_grid, theme, element_text, element_rect
import pandas as pd

df = pd.read_csv("D:/prac/mpg.csv") 

plot=(
    ggplot(df)+ aes(x="model", y="weight")
    + geom_point()
    + labs(x="displacement", y="horsepower")
)
plot.show()

plot = (
    ggplot(df) + aes(x="displ", y="hwy")
    + geom_point()
    + facet_grid("trans") # divide the data in subdata
    + labs(x="displacement", y="horsepower")
)

plot.show()
plot =(
   ggplot(df)+ aes(x="displ", y="hwy")
    + geom_point()
    + facet_grid(cols="year")  # didvide accordingly year of manufactuing
    + labs(x="displacement", y="horsepower")
)
plot.show()

plot = (
    ggplot(df)+ aes(x="displ", y="hwy")
    + geom_point()
    + facet_grid("drv", "cyl")
    + labs(x="displacement", y="horsepower")
)
plot.show()
# facet plot with reorded drv category

plot =(
     ggplot(df)+ aes(x="displ", y="hwy")
    + geom_point()
    + facet_grid("drv", "cyl")
    + labs(x="displacement", y="horsepower")
)
plot.show()

