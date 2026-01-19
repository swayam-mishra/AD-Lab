## Do logistic regression on any of your choice dataset from UCI. Compare the mean square error of linear and logistic regression for the taken dataset

## My Understanding: 

### 1. Scaling the Data

```python
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

```

* **Why do we do this?**
The dataset has features with very different ranges. For example, "Smoothness" might be `0.001`, while "Area" might be `1000.0`.
Without scaling, the algorithm might think "Area" is 1,000,000 times more important just because the number is bigger. Scaling squashes all features so they have a mean of 0 and a standard deviation of 1.
* **Why `fit_transform` on Train but only `transform` on Test?**
* `fit_transform(X_train)`: Calculates the mean and math from the **training data** and scales it.
* `transform(X_test)`: Uses the **training data's mean** to scale the test data. We never "fit" on the test data because that would be "cheating" (peeking at the answers before the test).



### 2. Linear Regression (The "Straight Line")

```python
lr = LinearRegression()
lr.fit(X_train_std, y_train)
preds_lr = lr.predict(X_test_std)

```

* **`lr.fit(...)`**: The model looks at the data and tries to draw the best possible straight line through it.
* **`preds_lr = ...`**: This asks the model to predict the diagnosis for the test set.
* **The Output:** Since this is *Linear* regression, the output will be continuous numbers like `0.85`, `1.2`, or `-0.1`. It doesn't know the answer is supposed to be just 0 or 1.

### 3. Logistic Regression (The "S-Curve")

```python
clf = LogisticRegression()
clf.fit(X_train_std, y_train)
preds_log = clf.predict_proba(X_test_std)[:, 1]

```

* **`clf.fit(...)`**: This fits an "S-shaped" curve (Sigmoid) to separate Malignant (1) from Benign (0).
* **`clf.predict_proba(...)`**: This is the crucial line.
* If we used normal `.predict()`, we would just get `0` or `1`.
* By using `.predict_proba()`, we get the **confidence score** (e.g., "I am 90% sure this is Malignant").
* **`[:, 1]`**: `predict_proba` gives us two numbers: [probability of 0, probability of 1]. We only want the second number (probability of 1) to compare it fairly against the Linear Regression output.



### 4. Comparing the Error (MSE)

```python
mse_linear = mean_squared_error(y_test, preds_lr)
mse_logistic = mean_squared_error(y_test, preds_log)

```

* This calculates the average squared difference between the **Real Answer** (0 or 1) and the **prediction**.
* **Why Linear loses:** If the real answer is `1`, but Linear Regression predicts `1.5` (overshooting), the math punishes it:  error.
* **Why Logistic wins:** Logistic is bounded. It might predict `0.99`. The error is .

**In Summary:** You are proving that Linear Regression is "messy" for classification because it isn't restricted to 0 and 1, whereas Logistic Regression is designed specifically for this task.