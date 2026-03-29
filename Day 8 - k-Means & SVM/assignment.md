# Day 8 - k-Means & SVM

## Part 1: k-Means Clustering (Manual Implementation)

Implement the **k-means clustering algorithm from scratch** (without using `sklearn.cluster.KMeans`).

### Dataset

Generate synthetic 2D data using `sklearn.datasets.make_blobs`:
- `n_samples=500`, `n_features=2`, `centers=3`, `random_state=23`

### Tasks

1. Generate data and plot the initial scatter.
2. Randomly initialize **3 cluster centers**.
3. Plot initial data with centers marked as `*`.
4. Implement the following functions manually:
   - `distance(p1, p2)` — Euclidean distance between two points
   - `assign_clusters(X, clusters)` — assign each point to the nearest center
   - `update_clusters(X, clusters)` — recompute centers as the mean of assigned points
   - `pred_cluster(X, clusters)` — predict cluster label for each point
5. Run one iteration: assign → update → predict.
6. Plot the final clustering with color-coded points and updated centers marked as `^`.

---

## Part 2: Support Vector Machine (SVM)

Train an **SVM classifier** with a linear kernel using `sklearn`.

### Tasks

1. Load a dataset of your choice (e.g., Iris from `sklearn.datasets.load_iris()`).
2. Use only the first 2 features for easy visualization.
3. Split into train (80%) / test (20%) sets.
4. Scale features using `StandardScaler`.
5. Train `SVC(kernel='linear', C=1.0)`.
6. Evaluate using `accuracy_score` and `classification_report`.
7. Visualize the **decision boundary** using a mesh grid plot.
