import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
from sklearn import datasets
import seaborn as sns
import graphviz

# Load the iris data
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

# Use sklearn to fit an SVM model
from sklearn import svm
kernel = snakemake.params["kernel"]
svc1 = svm.SVC(kernel=kernel)
svc1.fit(iris_X_train[:, :2], iris_y_train)

from matplotlib.colors import ListedColormap
from sklearn.inspection import DecisionBoundaryDisplay

def plot_decision_boundaries(clf, iris_X_train, iris_y_train):                                                                      
    cmap_light = ListedColormap(["orange", "cyan", "cornflowerblue"])
    cmap_bold = ["darkblue", "c", "darkorange"]

    _, ax = plt.subplots()
    DecisionBoundaryDisplay.from_estimator(
        clf,
        iris_X_train[:, :2],
        cmap=cmap_light,
        ax=ax,
        response_method="predict",
        plot_method="pcolormesh",
        xlabel=iris.feature_names[0],
        ylabel=iris.feature_names[1],
        shading="auto",
    )

    # Plot also the training points

    sns.scatterplot(
        x=iris_X_train[:, 0],
        y=iris_X_train[:, 1],
        hue=iris.target_names[iris_y_train],
        palette=cmap_bold,
        alpha=1.0,
        edgecolor="black",
    )

plot_decision_boundaries(svc1, iris_X_train, iris_y_train)
plt.title("3-Class classification SVM Kernel: " + kernel )


