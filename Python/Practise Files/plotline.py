from plotnine import ggplot, aes, geom_point, labs, facet_grid, theme, element_text, element_rect
import pandas as pd

  
# reading dataset 
df = pd.read_csv("D:/prac/mpg.csv") 
  
# passing the data to the ggplot  
# There will be blank output because axis and colm compnonet is not given
ggplot(df)



df = pd.read_csv("D:/prac/mpg.csv") 

plot=(
    ggplot(df)+ aes(x="model", y="weight")
    + geom_point()
    + labs(x="Car Variants", y="horsepower")
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


import pandas as pd 
from plotnine import ggplot, aes, geom_histogram,coord_flip
#Geometric Objects (geoms)such as point, line, histogram, bar, boxplot, etc.
  
# reading dataset 
df = pd.read_csv('E:/data/split3.csv')
  
ggplot(df) + aes(x="age") + geom_histogram()

import pandas as pd 
from plotnine import ggplot, aes, geom_histogram,coord_flip
#Geometric Objects (geoms)such as point, line, histogram, bar, boxplot, etc.
  
# reading dataset 
df = pd.read_csv('E:/data/split3.csv')
  
ggplot(df) + aes(x="age") + geom_histogram(bins=25) + coord_flip() 

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
plot.save("E:/data/test.png")


import seaborn 
import matplotlib.pyplot as plt 

# loading of a dataframe from seaborn 
df = seaborn.load_dataset('tips') 


graph = seaborn.FacetGrid(df, col ="sex", hue ="day") 
# map the above form facetgrid with some attributes 
graph.map(plt.scatter, "total_bill", "tip").add_legend() 
# show the object 
plt.show() 
