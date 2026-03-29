# Day 7 - k-Nearest Neighbors

## What is k-NN?

The **k-nearest neighbors algorithm (k-NN)** is a non-parametric method developed by Evelyn Fix and Joseph Hodges (1951), later expanded by Thomas Cover. It is used for both classification and regression:

- **Classification:** An item is assigned the most common class among its k nearest neighbors.
- **Regression:** The output is the average value of its k nearest neighbors.

## Assignment

Use the **k-NN regression** algorithm to predict the **weight of fish** based on physical measurements.

### Dataset

`data/Fish.csv` — 159 rows, 7 columns

| Attribute | Role |
|-----------|------|
| Species | Dropped (not needed) |
| Weight | **Target** (predict this) |
| Length1 | Feature |
| Length2 | Feature |
| Length3 | Feature |
| Height | Feature |
| Width | Feature |

### Tasks

1. Load `data/Fish.csv` and check for null values.
2. Drop the `Species` column.
3. Split the data: **70% train, 30% test**.
4. Train `KNeighborsRegressor` for each k from **1 to 20**.
5. Compute and print the **RMSE** for each k.
6. Plot RMSE vs k to identify the optimal k value.
7. Train a final model with the optimal k and display the prediction results.

### Expected Result

Optimal k = 3 with RMSE ≈ 47.22

### Dataset Source

[Kaggle Fish Market Dataset](https://www.kaggle.com/aungpyaeap/fish-market)
