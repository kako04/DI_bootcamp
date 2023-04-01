import numpy as np

def create_array(start, length, stop):
    return np.linspace(start, stop, length)

arr = create_array(6, 100, 6 + 4*99)
print(arr)


import numpy as np

a = np.array([1,2,3,np.nan,5,6,7,np.nan])
a = a[~np.isnan(a)]
print(a)


import numpy as np

arr = np.random.randint(low=1, high=101, size=(5, 6))
max_per_row = np.amax(arr, axis=1)
print(max_per_row)


import pandas as pd
import numpy as np

series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
unique_values = series.value_counts()
print(unique_values)


import pandas as pd

series = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])

dates = pd.to_datetime(series)
day_of_month = dates.dt.day
week_number = dates.dt.isocalendar().week
day_of_year = dates.dt.dayofyear
day_of_week = dates.dt.dayofweek

print("Day of month:", day_of_month)
print("Week number:", week_number)
print("Day of year:", day_of_year)
print("Day of week:", day_of_week)


import pandas as pd

url = "https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv"
df = pd.read_csv(url)

# Number of columns of each datatype
print(df.dtypes.value_counts())

# Changing column name and printing head
df = df.rename(columns={"Type": "TypeOfCar"})
print(df.head())

# Number of missing values per column
print(df.isna().sum())

# Column with the most missing values
print(df.isna().sum().idxmax())


import pandas as pd

url = "https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv"
df = pd.read_csv(url)

# Method 1: using del statement
del df["EngineSize"]
# Method 2: using drop() function
df = df.drop("Length", axis=1)

# Checking that columns are gone
print("EngineSize" in df.columns)
print("Length" in df.columns)



import pandas as pd
import numpy as np

df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})
df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})

# Joining dataframes
merged_df = pd.merge(df1, df2, left_on=['fruit', 'weight'], right_on=['pazham', 'kilo'])
merged_df = merged_df.drop(['pazham', 'kilo'], axis=1)


new_df = df['row'].str.split(',|\t', expand=True)
new_df.columns = ['STD', 'City', 'State']


import matplotlib.pyplot as plt

def scatter_plot(df):
    plt.scatter(df['displacement'], df['acceleration'])
    plt.xlabel('Displacement')
    plt.ylabel('Acceleration')
    plt.show()


def bar_plot(df):
    toyota_df = df[df['car_name'].str.contains('toyota', case=False)]
    toyota_78_df = toyota_df[toyota_df['model_year'] == 78]
    counts = toyota_78_df['cylinders'].value_counts()
    plt.bar(counts.index, counts.values)
    plt.xlabel('Cylinders')
    plt.ylabel('Count')
    plt.show()


def line_plot(df):
    toyota_df = df[df['car_name'].str.contains('toyota', case=False)]
    grouped_df = toyota_df.groupby('model_year')['weight'].mean()
    grouped_df.plot()
    plt.xlabel('Model Year')
    plt.ylabel('Weight')
    plt.show()


def horsepower_acceleration_plot(df):
    plt.scatter(df['horsepower'], df['acceleration'], c=df['cylinders'])
    plt.xlabel('Horsepower')
    plt.ylabel('Acceleration')
    plt.colorbar()
    plt.show()
