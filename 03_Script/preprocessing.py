import csv
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
#Import scikit-learn dataset library
from sklearn import datasets

# We use pandas for better manipulation
import pandas as pd

iris = datasets.load_iris()

# load data in a dataframe
# df = pd.read_csv(snakemake.input["iris"])
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = pd.Series(iris.target)

X = df.iloc[:,:-1]  # define the features
y = df.iloc[:, -1].values  # define the target values

# Import train_test_split function
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test

# Save the training set
X_train.to_csv(snakemake.output["X_train"])

from tempfile import TemporaryFile
outfile = snakemake.output["y_train"]
np.save(outfile, y_train)
