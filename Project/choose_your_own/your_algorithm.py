#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

# KNN
print("KNN")
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(labels_test, pred))


# AdaBoost Classifier
print "AdaBoost"
from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier()

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(labels_test, pred))

# Random Forests Classifier
print "Random Forests"
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(labels_test, pred))
# SVM
print "Support Vector Machines"

from sklearn.svm import SVC
clf = SVC()

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(labels_test, pred))

# Decision Tree
print "Decision Tree"

from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split = 40)
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(labels_test, pred))

# Naive Bayes
print "Naive Bayes"

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()

t0 = time()
clf = gnb.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score

t1 = time()
pred = clf.predict(features_test)
print "Predicting time: ", round(time() - t1, 3), "s"
print "Accuracy score = ", accuracy_score(pred, labels_test)

################################################################################

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
