import numpy as np
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd


df = pd.read_csv('faces.csv')


df.drop(['id', 'name'],1,inplace = True)
print(df.head())

#Assigning features and labels
X = np.array(df.drop(['exp'],1))
y = np.array(df['exp'])

#%Train and test split to check classifier accuracy
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.1)


clf = neighbors.KNNeighborsClassifier()

#training classifier
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

#predictions
example_measures = np.array([223,115,25])
example_measures = example_measures.reshape(1, -1)
prediction = clf.predict(example_measures)
print(prediction)
