from sklearn import datasets, neighbors
import numpy as np

# Load iris data from 'datasets module'
iris = datasets.load_iris()

#   Get data-records and record-labels in arrays X and y
X = iris.data
y = iris.target

# Create an instance of KNeighborsClassifier and then fit training data
clf = neighbors.KNeighborsClassifier()
clf.fit(X, y)

# Make class predictions for all observations in X
Z = clf.predict(X)

# Compare predicted class labels with actual class label
accuracy = clf.score(X, y)
print ("Predicted model accuracy: "+ str(accuracy))
# Add a row of predicted classes to y-array for ease of comparison
A = np.vstack([y, Z])
print(A)