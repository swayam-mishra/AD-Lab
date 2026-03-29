# Application Development Lab

> **Course:** Application Development Lab (6th Semester)
> **Student:** Swayam Mishra
> **Roll No:** 23052120

This repository contains weekly assignments and lab exercises for the Application Development Lab, covering data science fundamentals, machine learning algorithms, deep learning, and web development using Python and HTML.

---

## Repository Structure

Each day folder follows a consistent structure:

```
Day X - Topic/
├── assignment.md     ← problem statement & requirements
├── solution.ipynb    ← Jupyter notebook solution
└── data/             ← datasets (where applicable)
```

---

## Day-by-Day Breakdown

### Day 1 - HTML Fundamentals

Introduction to web development using HTML.

- **Part 1:** Build a résumé webpage using structural tags, lists, links, and images
- **Part 2:** Design a Campus Placement Registration Form using `<form>`, `<input>`, `<select>`, `<fieldset>`, and HTML5 input types

---

### Day 2 - NumPy Essentials

Core NumPy array operations and data cleaning.

- Creating empty, full, zero-filled, and one-filled arrays
- Row-wise validation and checking for specific entries
- Removing rows with non-numeric values and reshaping arrays

---

### Day 3 - Data Preprocessing & EDA

Exploratory Data Analysis pipeline on Spotify track data.

- **Data Cleaning:** Handle missing values, encode categorical features
- **Normalization:** Scale features for analysis
- **Visualization:** Plot feature distributions with `matplotlib`
- **Correlation Analysis:** Seaborn heatmap of the correlation matrix
- **Dataset:** `data/spotify.csv`, `data/track.csv`

---

### Day 4 - Linear Regression

Supervised learning for continuous variable prediction.

- Train a Linear Regression model on music attribute data
- Target variable: Danceability or Energy
- **Dataset:** `data/dataset.csv`

---

### Day 5 - Logistic Regression

Binary classification and model comparison against Linear Regression.

- Feature scaling with `StandardScaler`
- Train and evaluate both Linear and Logistic Regression
- Compare MSE to show why Linear Regression is suboptimal for classification
- **Dataset:** `data/data.csv`

---

### Day 6 - PCA & Random Forest

Dimensionality reduction followed by classification.

- Apply PCA to reduce the Iris dataset from 4 features to 2 principal components
- Train a Random Forest Classifier on the reduced data
- Evaluate with accuracy score and confusion matrix
- Visualize 2D PCA scatter plot with color-coded classes
- **Dataset:** Built-in Iris dataset (`sklearn.datasets`)

---

### Day 7 - k-Nearest Neighbors

Non-parametric regression to predict fish weight.

- Drop categorical `Species` column; target: `Weight`
- Test k = 1 to 20 and plot RMSE vs k
- Optimal k = 3 with RMSE ≈ 47.22
- **Dataset:** `data/Fish.csv` (159 rows, 7 columns)

---

### Day 8 - k-Means & SVM

Unsupervised clustering and supervised classification.

- **k-Means:** Manual implementation (distance, assign, update, predict) on synthetic `make_blobs` data
- **SVM:** Linear-kernel SVM on Iris dataset with decision boundary visualization

---

### Day 9 - Neural Networks

Feedforward neural network with PyTorch for digit recognition.

- Architecture: 784 → 512 (ReLU) → 10
- Trained for 10 epochs with SGD on MNIST
- **Dataset:** MNIST (auto-downloaded via `torchvision`)

---

### Day 10 - Convolutional Neural Networks

Basic CNN for image classification with PyTorch.

- 3-channel input, 5×5 filter (stride 1), Sigmoid on FC layer
- Trained on CIFAR-100 (100 classes)
- **Dataset:** CIFAR-100 (auto-downloaded via `torchvision`)

---

### Day 11 - Django Web Framework

Full-stack web application using Django.

- Titanic survival prediction app with form input and result page
- Django project structure: `titanic_project/` config + `predictor/` app
- Templates: `index.html` (input form), `result.html` (prediction result)

---

## Project: Water Quality Analysis (Maharashtra)

Analysis of NWMP water sampling data from Maharashtra (July–September 2025).

- **PCA** for dimensionality reduction and dataset projection
- **Regression** (Linear + Logistic) to predict potassium and fluoride levels; compare MSE
- **Geospatial visualization** of chemical elements by location (latitude/longitude)
- **Datasets:** `data/july.csv`, `data/august.csv`, `data/september.csv`

---

## Tech Stack

| Category | Tools |
|----------|-------|
| Languages | Python, HTML |
| Data & ML | NumPy, Pandas, Scikit-Learn |
| Deep Learning | PyTorch, torchvision |
| Visualization | Matplotlib, Seaborn |
| Web | Django, SQLite |
| Environment | Jupyter Notebooks |

---

## Contact

23052120@kiit.ac.in
