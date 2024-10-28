import numpy as np
import seaborn as sns
sns.set(style="dark")
 # Generate a random univariate dataset
rs = np.random.RandomState(15)
d = rs.normal(size=80)
 # Plot a simple histogram and kde
sns.histplot(d, kde=True, color="b")

#############################
import numpy as np
from matplotlib import pyplot as plt
def sinplot(flip = 1):
   x = np.linspace(0, 10, 80)
   for i in range(3, 7): 
      plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
sinplot()
plt.show()

#########################################
import numpy as np
from matplotlib import pyplot as plt
def sinplot(flip=1):
   x = np.linspace(0, 14, 100)
   for i in range(1, 5):
      plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
import seaborn as sb
sb.set_style("white")
sinplot()
sb.despine()
plt.show()
#####################################
import numpy as np
from matplotlib import pyplot as plt
def sinplot(flip = 1):
   x = np.linspace(0, 14, 100)
   for i in range(1, 5):
      plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
import seaborn as sb
sb.set_style("darkgrid", {'axes.axisbelow': False})
sinplot()
sb.despine()
plt.show()
##################################
import numpy as np
from matplotlib import pyplot as plt
def sinplot(flip = 1):
   x = np.linspace(0, 14, 100)
   for i in range(1, 5):
      plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

import seaborn as sb
sb.set_style("white")
sb.set_palette("husl")
sinplot()
plt.show()
######################
#Seaborn - Histogram
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
sb.distplot(df['petal_length'],kde = False)
plt.show()
############################seaborn KDE
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
sb.distplot(df['petal_length'],hist=False)
plt.show()

import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
sb.jointplot(x = 'petal_length',y = 'petal_width',data = df,kind = 'hex')
plt.show()
#########seaborn fitting parameter distrubition
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
sb.distplot(df['petal_length'])
plt.show()
#####################################
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
sb.jointplot(x = 'petal_length',y = 'petal_width',data = df)
plt.show()
##########################
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
sb.set_style("ticks")
sb.pairplot(df,hue = 'species',diag_kind = "kde",kind = "scatter",palette = "husl")
plt.show()
##########################bar plot
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('titanic')
sb.barplot(x = "sex", y = "survived", hue = "class", data = df)
plt.show()
###################point plot
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('titanic')
sb.pointplot(x = "sex", y = "survived", hue = "class", data = df)
plt.show()
################### ploting wide range data
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
sb.boxplot(data = df, orient = "h")
plt.show()
######################## factorplot
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('exercise')
#sb.factorplot(x = "time", y = pulse", hue = "kind", data = df)
plt.show()
####################################### Fact grid
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('exercise')
sb.factorplot(x = "time", y = "pulse", hue = "kind", kind = 'violin', col = "diet", data = df);
plt.show()
### implot

import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('tips')
sb.lmplot(x = "size", y = "tip", data = df)
plt.show()
################################# regplot & implot
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('tips')
sb.regplot(x = "total_bill", y = "tip", data = df)
sb.lmplot(x = "total_bill", y = "tip", data = df)
plt.show()
#################################### pair grid
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
g = sb.PairGrid(df)
g.map(plt.scatter);
plt.show()
#############################
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
sb.boxplot(data = df, orient = "h")
plt.show()
###############################
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
def sinplot(flip=1):
   x = np.linspace(0, 14, 100)
   for i in range(1, 5):
      plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
import seaborn as sb
sb.set_style("whitegrid")
sinplot()
plt.show()

#####################################
sns.set(style="white")
 seabornclass
# Generate a random univariate dataset
rs = np.random.RandomState(10)
d = rs.normal(size=100)
 
# Define the colors to use
colors = ["r", "g", "b"]
 
# Plot a histogram with multiple colors
sns.distplot(d, kde=True, hist=True, bins=10,rug=True)

########################################
sns.set(style="dark")
fmri = sns.load_dataset("fmri")
# Plot the responses for different\
# events and regions
sns.lineplot(x="timepoint", y="signal", hue="region", style="event", data=fmri)