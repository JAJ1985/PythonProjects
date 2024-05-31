# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 08:53:01 2019

@author: josjohn
"""

# Check the versions of libraries
 
# Python version 
import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))

# Load libraries: Import all modules, functions and objects needed.
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
#url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
#src = 'P:\WI\Teams\Programs\J&J CCC\QMS\JOSJOHN\Python\Doc(s)\iris.csv'
src = r'\\altaresources\dfs\shares\WI\Teams\Programs\J&J CCC\Operations\Analyst\JOSJOHN\Python\Doc(s)\iris.csv'
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(src, names=names)

#shape: Allows for a quick idea of how many instances (rows) and how many attributes (columns) the data contains with the shape property.
print(dataset.shape)

#head: Allows us to review the data.
print(dataset.head(20))

#descriotions: Includes the count, mean, min, and max values as well as some percentiles.
print(dataset.describe())

#class distribution: looks at the number of instances (rows) that belong to each class. This can be viewed as an absolute count.
print(dataset.groupby('class').size())

######Look at two plot types#######
#1. Univariate plots to better understand each attribute. 
#2. Multivariate plots to better understand the relationships between attributes.

#box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

#histograms of each input variable can be used to get an idea of the distribution. 
dataset.hist()
pyplot.show()

#A scatter plot matrix is helpful tp spot structured relationships between input variables.
scatter_matrix(dataset)
pyplot.show()

#Evaluating Algorythms: Create data models and estimate their accuracy on unseen data.
#1.Separate out a validation dataset.
#2.Set-up the test harness to use 10-fold cross validation.
#3.Build multiple different models to predict species from flower measurements.
#4.Select the best model.

# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=0.20, random_state=1)


# Test Harness: Use a stratified 10-fold cross validation to estimate model accuracy.
# Test options and evaluation metric
kfold = StratifiedKFold(n_splits=10, random_state=1)
cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')

# Build Models/Test Algorithm(s)
# 1. Logistic Regression (LR)
# 2. Linear Discriminant Analysis (LDA) 
# 3. K-Nearest Neighbors (KNN).
# 4. Classification and Regression Trees (CART).
# 5. Gaussian Naive Bayes (NB).
# 6. Support Vector Machines (SVM).
# These area a mix of simple linear (LR and LDA), and nonlinear (KNN, CART, NB and SVM) algorithms.

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# Compare Algorithms
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()

# Make predictions on validation dataset
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

# Evaluate predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
