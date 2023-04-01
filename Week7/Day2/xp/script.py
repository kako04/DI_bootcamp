import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df.describe())


sns.distplot(df["Age"].dropna(), kde=False)
plt.show()


sns.scatterplot(x="Age", y="Fare", data=df)
plt.show()


df["Age"].fillna(df["Age"].median(), inplace=True)


df = pd.get_dummies(df, columns=["Sex", "Embarked"])


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[["Age", "Fare"]] = scaler.fit_transform(df[["Age", "Fare"]])


sns.boxplot(x="Pclass", y="Age", data=df)
plt.show()


df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"], inplace=True)


from sklearn.model_selection import train_test_split

X = df.drop(columns=["Survived"])
y = df["Survived"]
X_train, X_test, y_train


