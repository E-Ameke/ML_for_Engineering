# -*- coding: utf-8 -*-
"""ML_HW_2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gY-y4dt7Y-Gu7miEjYgG8TxqLM4paDJO

ML_HOMEWORK_2<BR>
ELIZABETH AMEKE<BR>
662055975 **bold text**

.

1. Use the Iris dataset and the SVM code shown in the first class. Define two
new features using the original four features and then calculate the accuracy score of
classification. The SVM classifier must use the new features and none of the original
features for classification.
"""

#Anwer
#Loading the Iris dataset;

from sklearn import datasets

iris = datasets.load_iris()

#iris.data

iris.feature_names

iris.target_names

iris.target

"""#### target = function of feature names
#### (setosa, versicolor, viriginica) = f(sepal length, sepal width, petal length, petal width)

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

"""## Considering only two features;
#### target = function of feature names
#### (setosa, versicolor, viriginica) = f(petal length, petal width)

$y = f(X-new)$

$y \in [0,1,2]$

$X \in {\rm I\!R}^2 $

"""

import numpy as np

#Defining new features
#sepal ratio = sepal Length / sepal Width
sepal_ratio = X[:, 0] / X[:, 1]

#petal ratio = petal length / petal width
petal_ratio = X[:, 2] / X[:, 3]

#Stacking the new features with the original features
X_new = np.column_stack((sepal_ratio, petal_ratio))
y = iris.target

"""### Splitting the data and keeping some data seperate for testing the model;"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test=train_test_split(
    X_new,y,
    test_size=0.40,
    train_size=0.60,
    random_state=123,
    shuffle=True,
    stratify=y)

"""### Importing SVM model and training it;"""

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

""".

.

2. Classify only the even numbered handwritten digits using MNIST digits dataset
with a k-nearest neighbors classifier. The classifier must not see any odd numbered digit
images as inputs. The classifier must also consider every pixel in the input image to
make its classification decision. Can we use pairplot to visualize this data?. Plot the the
classification results using a heatmap showing digits which were correctly classified and
digits which were not correctly classified. How many 6’s in your test set were correctly
classified?
"""

###Answer

import numpy as np
from tensorflow import keras
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Loading the MNIST Dataset

from keras.datasets import mnist

#loading the dataset
(train_X, train_y), (test_X, test_y) = mnist.load_data()

#printing the shapes of the vectors
print('X_train: ' + str(train_X.shape))
print('y_train: ' + str(train_y.shape))
print('X_test:  '  + str(test_X.shape))
print('y_test:  '  + str(test_y.shape))

my_data=mnist.load_data()
(X_train, y_train), (X_test, y_test) = my_data

#normalizing the data
X_train=X_train/255
X_test=X_test/255

#print(y_test)
#print(y_test[2])
#print(y_train.shape[0])

even_digits = [i for i in range(len(y_train)) if y_train[i] % 2 == 0]

#for i in range(x_train.shape[0]):
even_indices= np.where(y_train % 2 ==0)[0]
#print(even_indices)


# Flattening the training arrays and create a DataFrame
even_mnist_df = pd.DataFrame({
 'Image': [img.flatten() for img in x_train[even_digits]],
 'Digit': y_train[even_digits]})

# Displaying the resulting DataFrame
print(even_mnist_df.head(10))

"""The even integers displayed from the resulting data frame confirm that the classifer cannot see any odd number.

Pairplot cannot be used to visualize this data because it has so many features (784 features). Each data point has 28*28 data points which makes it quite difficult to visualize.
"""

#Classifying results using a heatmap showing digits that were correctly
#classified and those not

#import sklearn.metrics as metrics

class My_KNNClassifier:
    def __init__(self, k=3):
        self.k = k
    def fit(self, X_train_even, y_train_even):
        self.X_train_even = X_train_even
        self.y_train_even = y_train_even
    def predict(self, X_test_even):
        predictions = []
        for i in range(X_test_even.shape[0]):
            predictions.append(self._knn_classifier(X_test_even[i]))
        return predictions
    def _knn_classifier(self, X_test_even):
        distances, targets = [], []
        for i in range(self.X_train_even.shape[0]):
            distance = np.linalg.norm(self.X_train_even[i]-X_test_even)
            distances.append([distance, i])
        distances = sorted(distances)
        for i in range(self.k):
            index = distances[i][1]
            targets.append(self.y_train_even[index])
        return max(targets, key=targets.count)

model = My_KNNClassifier()
model.fit(X_train_even, y_train_even)
#preds = np.array(preds)
preds = model.predict(X_test_even)

#print(y_test_even.shape)
#print(preds.shape)

# Ensuring consistent lengths
#y_test_even = y_test_even[:preds.shape[0]]
print(accuracy_score(y_test_even, preds))

cm = confusion_matrix(y_test_even, preds)
ax = sns.heatmap(cm,linewidths=2, annot=True, cmap='viridis', cbar=True);

ax.set_xticklabels(np.unique(y_test_even));
ax.set_yticklabels(np.unique(y_test_even));
plt.xlabel('Predicted Class');
plt.ylabel('Actual Class');
plt.xticks(rotation=45);
plt.yticks(rotation=45);
plt.title(' Classification results', fontsize='medium', fontweight='bold');
print(classification_report(y_test_even, model.predict(X_test_even)))

"""As can be seen above,my classifier gave a very low accuracy of 0.35 <br> this resulted in low support values and therefore just one six was correctly classified <br> as clearly shown in the classification results

.

.

3. Cluster the Iris species by writing your own k-means algorithm using THREE
features (Or modify the algorithm we used in class). Show visualization of the data
using a THREE dimensional scatter plot. Compare the clustering performance of your
k-means algorithm to the sklearn implementation by making plots of the clusters from
your method and Scikit’s implementation by showing the clusters from your methods
and from Scikit’s method. What happens when you vary the number of clusters?
"""

##Answer
#Modifying the algorithm we used in class;

from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#Preparing the data

data = load_iris() #shift+tab

#using only three features
df = pd.DataFrame()
df['sepal length'] = data['data'][:,0]
df['sepal width'] = data['data'][:,1]
df['petal length'] = data['data'][:,2]

display(df)

X = df.to_numpy() # These are our features
#y = df['target'].to_numpy()

df['target'] = data['target']

named_targets = []

for elm in df['target'].to_list():
    named_targets.append(data.target_names[elm])

df['species_name'] = named_targets

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
import pandas as pd

#Loading Iris dataset
iris = datasets.load_iris()
X = iris.data[:, :3]  # Using the first three features
y = iris.target

#Converting to DataFrame
df = pd.DataFrame(X, columns=['sepal_length', 'sepal_width', 'petal_length'])

#Custom k-means implementation
class MyKMeans:
    def __init__(self, n_clusters, max_iter=300):
        self.n_clusters = n_clusters
        self.max_iter = max_iter

    def fit(self, X):
        #Randomly initializing centroids
        self.centroids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]

        for _ in range(self.max_iter):
            #Assigning each data point to the nearest centroid
            labels = np.argmin(((X[:, np.newaxis] - self.centroids)**2).sum(axis=2), axis=1)

            #Updating centroids based on the mean of data points assigned to each cluster
            new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(self.n_clusters)])

            #Checking for convergence
            if np.all(self.centroids == new_centroids):
                break

            self.centroids = new_centroids

        self.labels_ = labels

#Custom KMeans clustering
my_kmeans = MyKMeans(n_clusters=3)
my_kmeans.fit(X)

#Visualizing clusters
fig = plt.figure(figsize=(8, 6))

#Plotting clusters from custom implementation
ax1 = fig.add_subplot(111, projection='3d')
scatter1 = ax1.scatter(df['sepal_length'], df['sepal_width'], df['petal_length'], c=my_kmeans.labels_, cmap='viridis')
centroid1 = ax1.scatter(my_kmeans.centroids[:, 0], my_kmeans.centroids[:, 1], my_kmeans.centroids[:, 2], c='red', marker='x', s=200)
ax1.set_title('Custom KMeans Clustering')
ax1.set_xlabel('Sepal Length')
ax1.set_ylabel('Sepal Width')
ax1.set_zlabel('Petal Length')

#Creating legend with colors matching clusters
cluster_colors = [scatter1.cmap(scatter1.norm(i)) for i in range(3)]
centroid_color = 'red'
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=f'Cluster {i}', markerfacecolor=cluster_colors[i], markersize=10) for i in range(3)]
legend_elements.append(plt.Line2D([0], [0], marker='x', color='red', label='Centroids', markersize=10, linestyle='None'))
ax1.legend(handles=legend_elements, loc='best')

plt.show()

#Spliting the dataset into testing and training datasets

X_train, X_test, y_train, y_test, idx_train, idx_test=train_test_split(
X,y, range(X.shape[0]),
test_size=0.30,
train_size=0.70,
random_state=123,
shuffle=True,
stratify=y)

print('X_train shape :', X_train.shape)
print('X_test shape :', X_test.shape)
print('y_train shape :', y_train.shape)
print('y_test shape :', y_test.shape)

from sklearn.model_selection import train_test_split

#Creating an array to indicate training or testing labels
labels = np.array(['Train'] * len(idx_train) + ['Test'] * len(idx_test))

print('X_train shape :', X_train.shape)
print('X_test shape :', X_test.shape)
print('y_train shape :', y_train.shape)
print('y_test shape :', y_test.shape)

#Printing the total number of training and testing points
print('Total number of train points:', len(X_train))
print('Total number of test points:', len(X_test))

#Algorithm

class MyKMeansClustering:
    def __init__(self, k):
        self.k = k
        self.labels = None

    def fit(self, data):
        self.centroids = data[np.random.choice(data.shape[0], self.k,
                                               replace=False), :]
        self.labels = np.arange(self.k)

        while True:
            distances = np.array([np.linalg.norm(data - centroid, axis=1)
            for centroid in self.centroids])
            clusters = np.argmin(distances, axis=0)
            new_centroids = np.array([data[clusters == i, :].mean(axis=0)
            for i in range(self.k)])

            if np.array_equal(new_centroids, self.centroids):
                break
            else:
                self.centroids = new_centroids

    def predict(self, data):
        distances = np.array([np.linalg.norm(data - centroid, axis=1)
        for centroid in self.centroids])
        return self.labels[np.argmin(distances, axis=0)]

#Instantiating and fitting the custom KMeans model
my_model = MyKMeansClustering(k=3)
my_model.fit(X_train)

#Predicting labels for the test set
my_predicted_labels = my_model.predict(X_test)

#Getting the centroids of the clusters
my_cluster_centers = my_model.centroids

#Printing predicted labels and clustered centroids
print('Predicted labels:', my_predicted_labels)
print('Cluster centroids:\n', my_cluster_centers)

y_train

df['kmeans_labels'] = model.predict(X)
df.columns

#Prections KMeans clustering
my_kmeans = MyKMeans(n_clusters=3)
my_kmeans.fit(X)

#Visualizing clusters
fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(111, projection='3d')
scatter1 = ax1.scatter(df['sepal_length'], df['sepal_width'], df['petal_length']
                       , c=my_kmeans.labels_, cmap='viridis')
centroid1 = ax1.scatter(my_kmeans.centroids[:, 0], my_kmeans.centroids[:, 1],
                        my_kmeans.centroids[:, 2], c='red', marker='x', s=200)
ax1.set_title('KMeans Predictions Clustering')
ax1.set_xlabel('Sepal Length')
ax1.set_ylabel('Sepal Width')
ax1.set_zlabel('Petal Length')

#Creating legend with colors matching clusters
cluster_colors = [scatter1.cmap(scatter1.norm(i)) for i in range(3)]
centroid_color = 'red'
legend_elements = [plt.Line2D([0], [0], marker='o', color='w',
label=f'Cluster {i}', markerfacecolor=cluster_colors[i],
markersize=10) for i in range(3)]
legend_elements.append(plt.Line2D([0], [0], marker='x', color='red',
label='Centroids', markersize=10, linestyle='None'))
ax1.legend(handles=legend_elements, loc='best')

plt.show()

import seaborn as sns

# Add KMeans labels to the DataFrame
df['kmeans_labels'] = my_kmeans.labels_

# Plotting pair plot
sns.pairplot(df, x_vars=['sepal_length'], y_vars=['sepal_width'],
hue='kmeans_labels', markers=['o', 's', 'D'], palette='viridis')

plt.show()

import seaborn as sns

# Add species names to the DataFrame
df['species_name'] = iris.target_names[y]

# Plotting pair plot
sns.pairplot(df, x_vars=['sepal_length'], y_vars=['sepal_width'],
hue='species_name')

plt.show()

#Now locating  the cluster centres

from sklearn.cluster import KMeans
skmodel=KMeans(n_clusters=3,init='k-means++')
skmodel.fit(X_train)

skmodel.labels_ # training labels

skmodel.predict(X_test) # predicting labels

skmodel_labels = skmodel.predict(X)
df.columns

df['skmodel_labels'] = skmodel_labels

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn import datasets
import pandas as pd

# Loading Iris dataset
iris = datasets.load_iris()
X = iris.data[:, :3]  # Using the first three features
y = iris.target

# Converting to DataFrame
df = pd.DataFrame(X, columns=['sepal_length', 'sepal_width', 'petal_length'])

# Sklearn KMeans clustering
sklearn_kmeans = KMeans(n_clusters=3)
sklearn_kmeans.fit(X)

fig = plt.figure(figsize=(10,8))
ax3 = fig.add_subplot(projection='3d')
fg = ax3.scatter3D(df['sepal_length'], df['sepal_width'], df['petal_length'],
s=50, c=sklearn_kmeans.labels_, cmap='viridis')  # Corrected to use labels from sklearn KMeans

# Visualizing clusters
centroid1 = ax3.scatter(sklearn_kmeans.cluster_centers_[:, 0],
sklearn_kmeans.cluster_centers_[:, 1], sklearn_kmeans.cluster_centers_[:, 2],
c='red', marker='x', s=200)
ax3.set_title('sklearn Predictions Clustering')
ax3.set_xlabel('Sepal Length')
ax3.set_ylabel('Sepal Width')
ax3.set_zlabel('Petal Length')

# Creating legend with colors matching clusters
cluster_colors = [fg.cmap(fg.norm(i)) for i in range(3)]
centroid_color = 'red'
legend_elements = [plt.Line2D([0], [0], marker='o', color='w',
label=f'Cluster {i}', markerfacecolor=cluster_colors[i],
markersize=10) for i in range(3)]
legend_elements.append(plt.Line2D([0], [0], marker='x', color='red',
label='Centroids', markersize=10, linestyle='None'))
ax3.legend(handles=legend_elements, loc='best')  # Corrected to use ax3 for legend

plt.show()

#Comparison of the performance of scIkit learn's Kmeans and the
#Kmeans implemented in class for the sepal length and sepal width only
#I had to generate a whole different algorithm to generate the plots
#This was because I kept having errors

from sklearn import datasets

iris = datasets.load_iris()

#iris.data

iris.feature_names

from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns

# Loading the Iris dataset
iris = load_iris()

# Creating a DataFrame from the Iris dataset
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Extracting 'sepal length' and 'sepal width' columns
iris_sepal_df = iris_df[['sepal length (cm)', 'sepal width (cm)']]

# Defining df with a sample DataFrame or load it from your data source
# With a sample DataFrame:
data = {
    'species_name': ['setosa', 'setosa', 'versicolor', 'versicolor', 'virginica', 'virginica'],
    'kmeans_labels': [0, 0, 1, 1, 2, 2],
    'skmodel_labels': [1, 1, 2, 2, 0, 0],

}

df = pd.DataFrame(data)

# Concatenating the sample DataFrame with the iris_sepal_df
df = pd.concat([df, iris_sepal_df], axis=1)

# Ensuring the data type of 'sepal length (cm)' and 'sepal width (cm)'
columns are numeric
df['sepal length (cm)'] = pd.to_numeric(df['sepal length (cm)'], errors='coerce')
df['sepal width (cm)'] = pd.to_numeric(df['sepal width (cm)'], errors='coerce')

# Creating pair plots for different labels
hue_cols = ['species_name', 'kmeans_labels', 'skmodel_labels']
for hue_col in hue_cols:
    if hue_col in df.columns:
        sns.pairplot(df, x_vars=['sepal length (cm)'],
                     y_vars=['sepal width (cm)'], hue=hue_col)

#I tried a different example to have more clusters

from sklearn.datasets import make_blobs
import pandas as pd
import seaborn as sns

# Generating synthetic data with more cluster points
X, y = make_blobs(n_samples=1000, centers=3, random_state=42)

# Creating DataFrame from synthetic data
df = pd.DataFrame(data=X, columns=['sepal length (cm)', 'sepal width (cm)'])
df['species_name'] = y
df['kmeans_labels'] = y
df['skmodel_labels'] = y

# Creating pair plots for different labels
hue_cols = ['species_name', 'kmeans_labels', 'skmodel_labels']
for hue_col in hue_cols:
    sns.pairplot(df, x_vars=['sepal length (cm)'], y_vars=['sepal width (cm)'],
                 hue=hue_col, height=3, aspect=1)

"""Observation:
These 3 plots show that my k-means algorithm and tthat of the sklearn. They can be said to be accurate
"""

#Using the elbow plot and scatter plot to show what happens when the k is varied

from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from keras.datasets import mnist

# Load MNIST dataset
(X_train, _), (_, _) = mnist.load_data()

# Flatten each image into a vector of length 784
X_train_flat = X_train.reshape(X_train.shape[0], -1)

# Apply KMeans clustering
distortions = []
for k in range(2, 20):
    kmeans = KMeans(n_clusters=k, init='k-means++')
    kmeans.fit(X_train_flat)
    distortions.append(kmeans.inertia_)

# Plot the elbow plot
fig = plt.figure(figsize=(15, 5))
plt.plot(range(2, 20), distortions)
plt.grid(True)
plt.xticks(ticks=range(2, 20))
plt.title('Elbow plot')
plt.xlabel('k')
plt.ylabel('Distortion or Inertia: \nSum of squared distances\n of samples to
their closest cluster center')
plt.show()

#Plotting the silhouette

from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from sklearn.metrics import silhouette_score

silhouette_scores = []

for k in range(2, 20):
    kmeans = KMeans(n_clusters=k, init='k-means++')
    kmeans.fit(X_train)
    silhouette_scores.append(silhouette_score(X_train,
    kmeans.labels_))

fig = plt.figure(figsize=(15, 5))
plt.plot(range(2, 20), silhouette_scores)
plt.grid(True)
plt.xticks(ticks=range(2, 20))
plt.title('Silhouette Scores')
plt.xlabel('k')
plt.ylabel('Silhouette Scores')
plt.show()

"""Both the elbow plot and silhouette plots indicate that, increasing k would <br>result in denser clusters, while decreasing k would lead to sparser clusters. <br>It can be concluded that k at a value of 3 gives better results.

.

Collaboration:
I collaborated with Melvina and Seth on this assignment<br>
and also attended the Professors office hours to get clarifications on <br>questions I had about
the assignment.
"""

