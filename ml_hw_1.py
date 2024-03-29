# -*- coding: utf-8 -*-
"""ML_HW_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D03BsoQSukfwfQUjxzCqHSN4W6f2bGO7

**MACHINE LEARNING FOR ENGINEERING**

**ELIZABETH AMEKE**

**662055975**

**HOMEWORK 1**

.

1. Consider feature vectors, 𝐱𝟏 = ⌈2 3 4 8 9⌉𝑇 and 𝐱𝟐 = ⌈2 −3 −4 89⌉𝑇.

(a) How many features are there in 𝐱𝟏 and 𝐱𝟐?

Ans:

x1 = 5 features.

x2 = 4 features.

.

(b) What are the 𝐿1, 𝐿2, and 𝐿∞ norms for each feature vector?
"""

#Ans for x1 vector:
import numpy as np

# Defining the given vector 𝐱𝟏
𝐱𝟏 = np.array([2, 3, 4, 8, 9])

# Transposing the vector
transposed_𝐱𝟏 = np.transpose(𝐱𝟏)

# L1 norm (Manhattan norm)
𝐱𝟏_l1_norm = np.linalg.norm(𝐱𝟏, ord=1)
print(f"L1 Norm: {𝐱𝟏_l1_norm}")

# L2 norm (Euclidean norm)
𝐱𝟏_l2_norm = np.linalg.norm(𝐱𝟏, ord=2)
print(f"L2 Norm: {𝐱𝟏_l2_norm}")

# L∞ norm (Max-norm)
𝐱𝟏_l_inf_norm = np.linalg.norm(𝐱𝟏, ord=np.inf)
print(f"L∞ Norm: {𝐱𝟏_l_inf_norm}")

#Ans for x2 vector:
import numpy as np

# Defining the given vector 𝐱2
𝐱2 = np.array([2, -3, -4, 89])

# Transposing the vector
transposed_𝐱2 = np.transpose(𝐱2)

# L1 norm (Manhattan norm)
𝐱2_l1_norm = np.linalg.norm(𝐱2, ord=1)
print(f"L1 Norm: {𝐱2_l1_norm}")

# L2 norm (Euclidean norm)
𝐱2_l2_norm = np.linalg.norm(𝐱2, ord=2)
print(f"L2 Norm: {𝐱2_l2_norm}")

# L∞ norm (Max-norm)
𝐱2_l_inf_norm = np.linalg.norm(𝐱2, ord=np.inf)
print(f"L∞ Norm: {𝐱2_l_inf_norm}")

""".

2. A color image of size 1024x1024 is input to an algorithm which outputs a 64x64 color image representing some important portions of the original image.
[Hint: a color image comprises of multiple channels]

(a) If the input is converted to a vector, 𝐱 , calculate the length of the feature vector.
(b) If the output is converted to a vector, 𝐲, calculate the length of the output vector.
(c) The algorithm relates the input and output vectors, 𝐱 and 𝐲 respectively, as 𝐲 =
𝑊𝐱 + 𝐛, where W is a matrix and 𝐛 is a vector. How many elements are there in
matrix W? How many elements are in vector b?
"""

#Answers:

#(a) The length of the feature vector |𝐱| = 1024x1024x3
#This is because the input of size,1024x1024, is a color image which has three color channels,(Red,Green,Blue).

x_length = 1024*1024*3

#(b)The length of the output vector |𝐲| = 64x64x3
#This is because the output of size,64x64, is a color image which has three color channels,(Red,Green,Blue).

y_length = 64*64*3

print('length of x =', x_length)
print('length of y =', y_length)

#(c) 𝐲 = 𝑊𝐱 + 𝐛

print ('W has', x_length*y_length, 'elements')
print('b has',y_length,'elements')

#Number of elements in matrix W = (64x64x3) x (1024x1024x3)
#This is because 𝐱 has length (1024x1024x3) and 𝐲 has length (64x64x3).

""".

3.Calculate 1-norm, 2-norm, ∞-norm, and Frobenius norm of
𝑊 =([[1 −1],
    [2 0 ]])
"""

#Answer:

import numpy as np

# Defining the given matrix W
W = np.array([[1, -1],
                   [2, 0]])

# Calculating the 1-norm
W_norm_1 = np.linalg.norm(W, ord=1)
print(f"1-norm: {W_norm_1}")

# Calculating the 2-norm
W_norm_2 = np.linalg.norm(W, ord=2)
print(f"2-norm: {W_norm_2}")

# Calculating the Infinity-norm
W_norm_inf = np.linalg.norm(W, ord=np.inf)
print(f"Infinity-norm: {W_norm_inf}")

# Calculating the Frobenius norm
W_frobenius_norm = np.linalg.norm(W, ord='fro')
print(f"Frobenius norm: {W_frobenius_norm}")

""".

4. Use the Iris dataset and the code shown in class, but choose 3 out of the 4 original features instead of two and calculate the accuracy score of classification.
"""

#Answer:
from sklearn import datasets

iris = datasets.load_iris()

iris.data

iris.feature_names

iris.target_names

iris.target

""".

# target = function of feature names
(setosa, versicolor, viriginica) = f(sepal length, sepal width, petal length, petal width)

$y = f(X)$

$y \in [0,1,2]$

$X \in {\rm I\!R}^4 $
"""

X = iris.data
y = iris.target

X.shape

y.shape

# Commented out IPython magic to ensure Python compatibility.
# %notebook inline
import matplotlib.pyplot as plt

plt.scatter(X[:,0],X[:,1])
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

plot = plt.scatter(X[:,0],X[:,1],c=y)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
# plt.legend(handles=plot.legend_elements()[0], labels=iris.target_names.tolist())

""".

Considering only the first three features
(setosa, versicolor, viriginica) = f(sepal length, sepal width,petal length)

𝑦=𝑓(𝑋)
𝑦∈[0,1,2]
𝑋∈IR2
"""

X = iris.data[:, :3] # only selecting first three features
y = iris.target

#Splitting the data and keeping some of the data seperate for testing the model

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test=train_test_split(
    X,y,
    test_size=0.40,
    train_size=0.60,
    random_state=123,
    shuffle=True,
    stratify=y)

#Importing support vector machine model and training it

from sklearn import svm

clf = svm.SVC()
clf.fit(X_train, y_train)

preds = clf.predict(X_test)
print(preds)

print('actual iris species')
print(y_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test,clf.predict(X_test) )
print('accuracy score :', acc)

"""The accuracy score considering the first three features, f(sepal length, sepal width,petal length) is 0.93333333

.

5. In class, we used a neural network to learn how to calculate square root. Use that code and ideas to teach a neural network how to calculate the 7-th root of any integer between 1 and 100.
"""

#Answer

import tensorflow as tf
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
from tensorflow.python.keras.optimizers import *
import numpy as np


#Load dataset
#split into input (X) and output (y)
X = np.array([[1], [4], [7], [10], [13], [16], [19], [22], [25], [28], [31],
[34], [37], [40], [43], [46], [49], [52], [55], [58], [61], [64], [67], [70],
[73], [76], [79], [82], [85],  [88],  [91],  [94],  [97], [100]])
X = X*1.0

y = np.array([[1.0], [1.21901365], [1.32046925], [1.38949549], [1.44256292],
[1.48599429], [1.522927],  [1.55515854], [1.58381961], [1.60967004],
[1.63324625], [1.65494171], [1.67505402], [1.69381398], [1.71140437],
[1.72797253], [1.74363903], [1.7585039], [1.77265101], [1.78615147],
[1.7990661], [1.81144733], [1.82334071], [1.83478607], [1.84581844],
[1.85646881], [1.86676472], [1.87673079], [1.88638909], [1.89575949],
[1.90485997], [1.91370683], [1.92231491], [1.93069773]])
y = y*1.0

#define keras model
model = Sequential()

model.add(Dense(6,input_dim=1,activation='relu'))
model.add(Dense(6,activation='relu'))
model.add(Dense(6,activation='relu'))
model.add(Dense(1))

#compile the keras model
opt = optimizers.Adam(learning_rate=0.001)
mse = tf.keras.losses.MeanSquaredError(
    reduction=tf.keras.losses.Reduction.SUM)
model.compile(loss=mse, optimizer=opt)


#fit the keras model on the dataset (CPU)
model.fit(X,y,epochs=2000,batch_size=10, verbose=0)
model.summary()

#make class predictions with the model
predictions = model.predict(X)

#summarize the first 10 cases
for i in range(34):
    print('%s => %.2f (expected %.2f)' %(X[i].tolist(), predictions[i], y[i]) )

import matplotlib.pyplot as plt
number_grid = np.linspace(1, 100, 100)
plt.scatter(X,y, label='data')
plt.plot(number_grid,model.predict(np.expand_dims(number_grid,axis=1)) , color='red', label='model')
plt.xlabel('number')
plt.ylabel('square root')
plt.legend()

""".

6. Use the Iris dataset and the neural network code shown in class to create a
neural network model that takes sepal length as input and predicts petal length as output.
[Hint: Use Numpy or Pandas to wrangle Iris dataset to help define your input and output.
You are free to define the number of neurons in each layer.]
"""

import tensorflow as tf
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
from tensorflow.python.keras.optimizers import *
import numpy as np

from sklearn.datasets import load_iris
data = load_iris()

#The input data (i.e. sepal length )
iris = datasets.load_iris()
iris.feature_names
x1=iris.data[:,0]
x_array=np.array(x1)
X=x_array[..., None]
X = X*1.0


#The output data (i.e. petal length )
y1=iris.data[:,2]
y_array=np.array(y1)
y=y_array[..., None]
print(y.shape)
y = y*1.0

#Defining keras model
model = Sequential()
model.add(Dense(6,input_dim=1,activation='relu'))
model.add(Dense(6,activation='relu'))
model.add(Dense(6,activation='relu'))
model.add(Dense(1))

#Compiling the keras model
opt = optimizers.Adam(learning_rate=0.001)
mse = tf.keras.losses.MeanSquaredError(
    reduction=tf.keras.losses.Reduction.SUM)
model.compile(loss=mse, optimizer=opt)

#Fitting the keras model on the dataset (CPU)
model.fit(X,y,epochs=2000,batch_size=10, verbose=0)
model.summary()

#making class predictions with the model
predictions = model.predict(X)

#summarizing the first 200 cases
for i in range(20):
     print('%s => %.2f (expected %.2f)' %(X[i].tolist(), predictions[i], y[i]) )

import matplotlib.pyplot as plt
number_grid = np.linspace(1, 10, 10)
plt.scatter(X,y, label='data')
plt.plot(number_grid,model.predict(np.expand_dims(number_grid,axis=1)) , color='red', label='model')
plt.xlabel('Sepal length')
plt.ylabel('Petal length')
plt.legend()

!apt update
!apt install texlive-xetex texlive-fonts-recommended texlive-generic-recommended

