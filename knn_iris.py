from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

# define column names
names = ['sepal_length', 'sepal_width', 'petal_length',
         'petal_width', 'class']

df = pd.read_table('iris.data', header=None, names=names, sep=",")
# Separate four data attributes and class data (the 5th attribute)
#  Slice data-frame column wise. When slicing the data frame using iloc,
#    the start bound (0) is included, while the upper bound (4) is excluded.

X = np.array(df.ix[:,0:4]) #input
y = np.array(df['class']) #label

# split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33,
                                                    random_state=42)

clf = neighbors.KNeighborsClassifier(n_neighbors=9)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)

accuracy=accuracy_score(y_test, pred)
print("Predicted model accuracy: "+ str(accuracy))