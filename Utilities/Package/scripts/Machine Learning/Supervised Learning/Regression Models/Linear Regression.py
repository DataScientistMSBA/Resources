# coding: utf-8

# # Linear Regression

# Linear Regression is a statistical method used to understand and predict the relationship between a target variable (or dependent variable) and one or more predictor variables (or independent variables). The objective is to find a line (or plane) that best fits the data points and minimizes the difference between the predicted and actual values.
# 
# Key Concepts
# 1. Relationship Modeling: Linear regression assumes a straight-line relationship between the predictors and the target. The model aims to describe how changes in each predictor influence the target variable.
# 
# 2. Single vs. Multiple Predictors:
# 
#     - Simple Linear Regression involves just one predictor and is ideal for exploring how one factor affects the target.
#     - Multiple Linear Regression uses several predictors to capture more complex relationships.
#     Fitting the Line: Linear regression finds the best line by minimizing the differences (errors) between predicted values and actual observed values. This process is known as "least squares" fitting.
# 
# 3. Interpreting Coefficients:
# 
#     - Each predictor has a coefficient that indicates its influence on the target variable. A positive coefficient suggests that as the predictor increases, the target variable tends to increase as well, and vice versa.
#     - The intercept is the expected value of the target variable when all predictors are zero.
# 
# 4. Goodness of Fit:
# 
#     - R-squared (R²) is a measure of how well the model explains the variability of the target variable. An R² closer to 1 indicates a stronger relationship, meaning the predictors account for a large portion of the target’s variability.
# 
# When to Use Linear Regression
# - Predicting Continuous Outcomes: Linear regression is well-suited for predicting values like house prices, sales, or any other continuous outcome.
# - Examining Relationships: It is helpful for quantifying and understanding the strength and direction of relationships between variables.
# - Interpretability: Linear regression is straightforward, making it easy to interpret and explain relationships in the data.
# 
# Limitations
# - Assumes Linearity: Linear regression requires a linear relationship between predictors and the target, which may not hold in all datasets.
# - Sensitive to Outliers: Extreme values can disproportionately affect the model, potentially skewing results.
# - Multicollinearity: When predictors are highly correlated, it can be difficult to interpret their individual effects.
# 

# # Function



from sklearn.datasets import fetch_california_housing
import statsmodels.api as sm
import pandas as pd

def LinearRegressionWithPValues(X, y):
    """
    Performs linear regression using statsmodels and returns coefficients and p-values.
    """
    # Add a constant term to the predictors (intercept)
    X = sm.add_constant(X)

    # Fit the model
    model = sm.OLS(y, X).fit()

    # Get the summary of the regression
    summary = model.summary()

    # Get coefficients and p-values
    coefficients = model.params
    p_values = model.pvalues

    return {
        "summary": summary,
        "coefficients": coefficients,
        "p_values": p_values
    }


# # Examples



# Load the California housing dataset
housing = fetch_california_housing()
X = pd.DataFrame(housing.data, columns=housing.feature_names)
y = housing.target  # This is the median house value in $100,000s

# Run Linear Regression with p-values
results = LinearRegressionWithPValues(X, y)

# Output results
print("Coefficients:\n", results["coefficients"])
print("P-values:\n", results["p_values"])
print("\nModel Summary:\n", results["summary"])


# # Explanation

# The output from the LinearRegressionWithPValues function provides several key metrics and insights. Here’s a guide to understanding each component of the output:
# 
# 1. Coefficients
#     - The coefficients represent the average change in the target variable (house value) for a one-unit increase in each predictor variable, holding all other variables constant.
#     - A positive coefficient indicates that as the predictor variable increases, the house value also tends to increase.
#     - A negative coefficient suggests an inverse relationship, where an increase in the predictor variable corresponds to a decrease in house value.
#     - For example, if the coefficient for MedInc (median income) is positive, this means higher income levels are associated with higher house values.
# 2. P-values
#     - P-values indicate the statistical significance of each predictor.
#     - A low p-value (typically < 0.05) suggests that the predictor is statistically significant and likely has a meaningful impact on the target variable (house value).
#     - A high p-value (typically > 0.05) implies that the predictor may not have a statistically significant effect on the target variable, meaning its contribution to predicting house value might be minimal.
# 3. R² Score (R-squared)
#     - R² is the coefficient of determination and measures the proportion of variance in the target variable (house value) that is explained by the predictor variables.
#     
#         Interpretation:
#             
#         - An R² closer to 1 indicates a better fit, meaning the model explains a large portion of the variability in house values.
# 
#         - An R² closer to 0 suggests a poor fit, meaning the model explains little of the variability in house values.
#     - Adjusted R²: Unlike R², adjusted R² adjusts for the number of predictors in the model and is generally more reliable, especially when working with multiple predictors.
# 4. Model Summary
#     - The model summary provides an overview of the linear regression results, including:
#         - F-statistic: Tests the overall significance of the model. A high F-statistic with a low p-value suggests that the model is statistically significant as a whole.
#         - Standard Errors: Show the variability of each coefficient estimate. Larger standard errors suggest more uncertainty in the coefficient’s value.
#         - Confidence Intervals: Indicate the range within which we expect the true coefficient values to fall. Narrow intervals suggest more confidence in the estimate.
#     Example Interpretation
#     Suppose the output shows the following:
# 
#     - Positive coefficient for MedInc with a low p-value: This suggests that median income has a statistically significant positive relationship with house value.
#     - Negative coefficient for HouseAge with a low p-value: This implies that as houses get older, their value tends to decrease, and this relationship is statistically significant.
# 
