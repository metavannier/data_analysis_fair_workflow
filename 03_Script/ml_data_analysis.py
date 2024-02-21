import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
from sklearn import datasets
import seaborn as sns
import graphviz
import pandas as pd

#Import scikit-learn dataset library
from sklearn import datasets
#Load dataset
iris = datasets.load_iris()

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = pd.Series(iris.target)

X = df.iloc[:,:-1]  # define the features
y = df.iloc[:, -1].values  # define the target values

# Import train_test_split function
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test

# Simple SVM with the 2 most important features
from sklearn import svm
kernel = 'linear'
svc1 = svm.SVC(kernel=snakemake.params["kernel"])
svc1.fit(X_train.iloc[:, :2], y_train)

from matplotlib.colors import ListedColormap
from sklearn.inspection import DecisionBoundaryDisplay

def plot_decision_boundaries(clf, X_train, y_train):                                                                      
    cmap_light = ListedColormap(["orange", "cyan", "cornflowerblue"])
    cmap_bold = ["darkorange", "c",  "darkblue" ]

    _, ax = plt.subplots()
    DecisionBoundaryDisplay.from_estimator(
        clf,
        X_train.iloc[:, :2],
        cmap=cmap_light,
        ax=ax,
        response_method="predict",
        plot_method="pcolormesh",
        xlabel=X_train.columns[0],
        ylabel=X_train.columns[1],
        shading="auto",
    )

    # Plot also the training points

    sns.scatterplot(
        x=X_train.iloc[:, 0],
        y=X_train.iloc[:, 1],
        hue=y_train,
        palette=cmap_bold,
        alpha=1.0,
        edgecolor="black",
    )

plot_decision_boundaries(svc1, X_train, y_train)
plt.title("3-Class classification SVM Kernel: " + kernel )
plt.savefig(snakemake.output["decision_boundaries"]) 
