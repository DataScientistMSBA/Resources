# coding: utf-8

# # Lasso Regression

# Lasso Regression (Least Absolute Shrinkage and Selection Operator) is a type of linear regression that includes a regularization term. This regularization helps prevent overfitting and encourages simpler models, making it especially useful in datasets with many features, some of which may be irrelevant or redundant.
# 
# Key Concepts
# 1. Regularization
# Unlike standard linear regression, which minimizes the sum of squared errors, Lasso introduces a penalty term that discourages large coefficients. This penalty term helps control model complexity and can lead to better generalization on unseen data.
# 
# 2. L1 Regularization (Lasso Penalty)
# Lasso uses L1 regularization, which means it can shrink some coefficients to zero. This differs from Ridge Regression, which uses L2 regularization. The ability to zero out coefficients allows Lasso to act as a form of feature selection, keeping only the most influential predictors in the model.
# 
# 3. Automatic Feature Selection
# By forcing some coefficients to zero, Lasso effectively performs automatic feature selection. This is especially helpful in high-dimensional datasets where many features may be irrelevant.
# 
# 4. Bias-Variance Tradeoff
# By adding regularization, Lasso introduces a bit of bias but reduces variance, resulting in a model that is less likely to overfit and is more robust on new data.
# 
# When to Use Lasso Regression
# - High-dimensional data: Lasso is ideal when you have more features than observations or a large number of features, as it can reduce model complexity by selecting only the most relevant ones.
# - Feature selection: If you need to interpret which features impact the target most, Lasso simplifies the model by eliminating less relevant features.
# - Risk of overfitting: The added regularization helps prevent overfitting, especially in cases with limited data or complex models.
# Limitations
# - Collinearity: Lasso can struggle with highly correlated features, as it may arbitrarily keep one feature while zeroing out others.
# - Small datasets: Regularization introduces some bias, which may lead to underfitting if the dataset is very small.
# - Interpretability: If the regularization strength is too high, too many coefficients may be set to zero, making the model challenging to interpret.
# 
# Summary
# - Lasso Regression is a powerful tool for regression, particularly with high-dimensional data or when feature selection is desired. Its regularization properties and ability to zero out coefficients make it a popular choice in machine learning.

# # Function



from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def LassoRegression(X, y, alpha=1.0, test_size=0.2, random_state=None):
    """
    Performs Lasso regression on a dataset.

    Parameters:
        X (array-like): Feature matrix.
        y (array-like): Target variable.
        alpha (float): Regularization strength; must be a positive float. Default is 1.0.
        test_size (float): Proportion of the dataset to include in the test split.
        random_state (int): Random state for reproducibility.

    Returns:
        dict: A dictionary containing the trained model, mean squared error, and R^2 score for both training and testing sets.
    """
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Initialize and train the Lasso model
    lasso_model = Lasso(alpha=alpha, random_state=random_state)
    lasso_model.fit(X_train, y_train)

    # Make predictions on both training and testing sets
    y_train_pred = lasso_model.predict(X_train)
    y_test_pred = lasso_model.predict(X_test)

    # Calculate metrics
    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)

    # Return the results
    return {
        "model": lasso_model,
        "train_mse": train_mse,
        "test_mse": test_mse,
        "train_r2": train_r2,
        "test_r2": test_r2
    }


# # Examples



from sklearn.datasets import make_regression

# Generate synthetic regression data
X, y = make_regression(n_samples=100, n_features=5, noise=0.1, random_state=42)

# Run Lasso Regression
results = LassoRegression(X, y, alpha=0.5, test_size=0.2, random_state=42)

# Output results
print("Train MSE:", results["train_mse"])
print("Test MSE:", results["test_mse"])
print("Train R^2:", results["train_r2"])
print("Test R^2:", results["test_r2"])


# # Explanation

# The output from running the LassoRegression function provides four key metrics:
# 
# 1. Train MSE (Mean Squared Error): The average squared difference between the predicted and actual target values on the training set.
# 2. Test MSE: The same measure but on the test set. Lower MSE values indicate that the model’s predictions are closer to the actual values.
# 3. Train R² (Coefficient of Determination): A measure of how well the model explains the variance in the target variable on the training set. Values closer to 1 indicate a better fit.
# 4. Test R²: The R² score on the test set. This value also ranges between 0 and 1, where values closer to 1 indicate a better generalization to unseen data.
# 
# 1. Training vs. Testing MSE:
# 
#     - If the Train MSE is significantly lower than the Test MSE, this suggests that the model may be overfitting. It’s performing well on the training data but not generalizing well to new data.
#     - If both Train MSE and Test MSE are relatively close and low, this indicates a good fit, meaning the model generalizes well.
#     - If both values are high, it suggests underfitting, where the model is too simple to capture patterns in the data.
# 2. Training vs. Testing R²:
# 
#     - A high Train R² close to 1 and a lower Test R² suggest that the model is overfitting.
#     - If Train R² and Test R² are close and reasonably high, it indicates the model fits the data well without overfitting.
#     - If both R² values are low, the model is underfitting, meaning it doesn’t explain much of the variance in the target.
# 3. Specific Analysis
#     - Lasso Regularization Effect: If Lasso’s regularization (controlled by alpha) is set appropriately, it will prevent overfitting, keeping Train and Test MSE and R² values close to each other.
#     - Feature Selection: With a suitable alpha, Lasso can reduce the impact of irrelevant or redundant features by shrinking their coefficients to zero, focusing only on the most influential features.
