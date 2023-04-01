
# # importing required libraries
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt


# # Generation of variables 
# x=np.arange(0,10) #Array of range 0 to 9
# y=x**3

# # Printing the variables
# print(x)
# print(y)

# plt.plot(x,y) # Function to plot
# plt.title('Line Chart') # Function to give title

# # Functions to give x and y labels
# plt.xlabel('X-Axis') 
# plt.ylabel('Y-Axis')

# # Functionn to show the graph  
# plt.show()

# # importing required libraries
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt


# # Generation of 1 set of variables 
# x = np.arange(0,11)
# y = x**3

# # Generation of 1 set of variables
# x2 = np.arange(0,11)
# y2 = (x**3)/2

# # Printing all variables
# print(x,y,x2,y2,sep="\n")

# # "linewidth" is used to specify the width of the lines
# # "color" is used to specify the colour of the lines
# # "label"is used to specify the name of axes to represent in the lengend 
# plt.plot(x,y,color='r',label='first data', linewidth=5) 
# plt.plot(x2,y2,color='y',linewidth=5,label='second data')
# plt.title('Multiline Chart')

# # Uses the label attribute to display reference in legend
# plt.ylabel('Y axis')
# plt.xlabel('X axis')

# # Shows the legend in the best postion with respect to the graph
# plt.legend()
# plt.show()


# # Importing required libraries
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # Generation of variables 
# x = ["India",'USA',"Japan",'Australia','Italy']
# y = [6,7,8,9,2]

# # Printing the variables
# print(x)
# print(y)

# plt.bar(x,y, label='Bars1', color ='r') # Function to plot

# # Function to give x and y labels 
# plt.xlabel("Country")
# plt.ylabel("Inflation Rate%")

# # Function to give heading of the chart
# plt.title("Bar Graph")

# # Function to show the chart
# plt.show()

# # importing required libraries
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # Generation of 1 set of variables 
# x = ["India",'USA',"Japan",'Australia','Italy']
# y = [6,7,8,9,5]

# # Generation of 2 set of variables
# x2 = ["India",'USA',"Japan",'Australia','Italy']
# y2 = [5,1,3,4,2]

# # Printing all variables
# print(x,y,x2,y2,sep="\n")

# # Functions to plot 
# plt.bar(x,y, label='Inflation', color ='y')
# plt.bar(x2,y2, label='Growth', color ='g')

# # Functions to give x and y labels
# plt.xlabel("Country")
# plt.ylabel("Inflation & Growth Rate%")

# plt.title("Multiple Bar Graph")
# plt.legend()
# plt.show()


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt


# # Generation of variable
# stock_prices = [32,67,43,56,45,43,42,46,48,53,73,55,54,56,43,55,54,20,33,65,62,51,79,31,27]

# # Function to show the chart
# plt.figure(figsize = (8,5))
# plt.hist(stock_prices, bins = 5)


# # Importing required libraries
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # Generation of x and y variables
# x = [1,2,3,4,5,6,7,8]
# y = [5,2,4,2,1,4,5,2]

# # Function to plot the graph
# plt.scatter(x,y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Scatter Plot')




# # Importing required libraries
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # Collection of raw data
# raw_data={'names':['Nick','Sani','John','Rubi','Maya'],
# 'jan_score':[123,124,125,126,128],
# 'feb_score':[23,24,25,27,29],
# 'march_score':[3,5,7,6,9]}

# # Segregating the raw data into usuable form/variables
# df=pd.DataFrame(raw_data,columns=['names','jan_score','feb_score','march_score'])
# df['total_score']=df['jan_score']+df['feb_score']+df['march_score']

# # Printing the data
# print(df)

# # Function to plot the graph
# plt.pie(df['total_score'],labels=df['names'],autopct='%.2f%%')
# plt.axis('equal')
# plt.axis('equal')
# plt.show()



# Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Defining the sixe og the figures
plt.figure(figsize=(10,10))

# Generation of variables
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([5,2,4,2,1,4,5,2])

# Generating 4 subplots in form of 2x2 matrix
# In the line below the arguments of plt.subplot are as follows:
# 2- no. of rows
# 2- no. of columns
# 1- position in matrix
# Position (0,0)
plt.subplot(2,2,1)
plt.plot(x,y,'g')
plt.title('Sub Plot 1')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Position (0,1)
plt.subplot(2,2,2)
plt.plot(y,x,'b')
plt.title('Sub Plot 2')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Position (1,0)
plt.subplot(2,2,3)
plt.plot(y*2,x*2,'y')
plt.title('Sub Plot 3')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Position (1,1)
plt.subplot(2,2,4)
plt.plot(x*2,y*2,'m')
plt.title('Sub Plot 4')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Function for layout and spacing
plt.tight_layout(h_pad=5, w_pad=10)
