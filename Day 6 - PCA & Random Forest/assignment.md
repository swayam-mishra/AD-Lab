# Day 6 - PCA & Random Forest

## Assignment

Apply **PCA (Principal Component Analysis)** for dimensionality reduction on the Iris dataset, then train a **Random Forest Classifier** on the reduced data.

### Dataset

Use the built-in Iris dataset from `sklearn.datasets.load_iris()`:
- 150 samples, 4 features (sepal length, sepal width, petal length, petal width)
- 3 classes (Iris-setosa, Iris-versicolor, Iris-virginica)

### Tasks

1. Load the Iris dataset and perform an 80/20 train-test split.
2. Standardize features using `StandardScaler` (required before PCA).
3. Apply `PCA` to reduce from 4 dimensions to **2 principal components**.
4. Train a `RandomForestClassifier` on the PCA-reduced training data.
5. Evaluate the model:
   - Print **accuracy score**
   - Print **confusion matrix**
6. Visualize the PCA 2D scatter plot with data points **color-coded by class label**.

### Libraries

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
```

> No external data file required — Iris dataset is built into sklearn.
