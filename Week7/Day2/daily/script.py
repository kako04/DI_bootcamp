import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

import seaborn as sns

sns.histplot(data=df, x="Age", hue="Sex", multiple="stack", kde=True)

import matplotlib.pyplot as plt


sns.histplot(data=df, x="Age", hue="Sex", multiple="stack", kde=True)
plt.title("Passengers Age and Gender Distribution")
plt.show()

sns.barplot(x="Sex", y="Survived", data=df, ci=None)
plt.title("Survival Rate by Gender")
plt.show()

sns.catplot(x="Pclass", y="Survived", hue="Sex", kind="bar", data=df)
plt.title("Survival Rate by Passenger Class and Gender")
plt.show()

sns.violinplot(x="Pclass", y="Age", hue="Sex", data=df, split=True)
plt.title("Age Distribution by Passenger Class and Gender")
plt.show()

