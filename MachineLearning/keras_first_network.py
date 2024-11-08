# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 09:40:00 2023

@author: JOSJOHN
"""

# first neural network with keras
from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
# split into input (X) and output (Y) variables
X = dataset[:, 0:8]
Y = dataset[:, 8]
# define the keras model
model = Sequential()
model.add(Dense(12, input_shape=(8,), activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the kera model
model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy'])
# fit the keras model to the dataset
model.fit(X, Y, epochs=150, batch_size=10)
# evaluate the keras model
_, accuracy = model.evaluate(X, Y)
print('Accuracy: %.2f' % (accuracy * 100))
