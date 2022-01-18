import pandas as pd
from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
df = pd.read_csv("iris.csv", index_col=0)
print("**********************************DATA  SET**********************************\n")
print(df)
df = pd.DataFrame(iris['data'])
print("\nThe target names are: ")
print(iris['target_names'])
print("\nThe Feature names are: ")
print(iris['feature_names'])

y = iris['target']

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.33, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
# var = iris['target_names'][y_pred]

cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", cm)

print("\nCorrect prediction", accuracy_score(y_test, y_pred))
print("Wrong prediction", (1 - accuracy_score(y_test, y_pred)))
