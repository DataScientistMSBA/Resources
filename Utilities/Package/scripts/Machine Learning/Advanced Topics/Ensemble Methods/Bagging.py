# coding: utf-8



def ComingSoon():
    print("Coming Soon")
    return


# # Function



from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

def Bagging(X, y, base_model=None, n_estimators=10, max_samples=1.0, max_features=1.0, test_size=0.2, random_state=None):
    """
    Performs bagging ensemble classification on a dataset.

    Parameters:
        X (array-like): Feature matrix.
        y (array-like): Target labels.
        base_model (estimator): The base model to use for bagging (default is DecisionTreeClassifier).
        n_estimators (int): Number of estimators in the ensemble.
        max_samples (float): Maximum samples to draw from X for each base estimator.
        max_features (float): Maximum features to draw from X for each base estimator.
        test_size (float): Proportion of the dataset to include in the test split.
        random_state (int): Random state for reproducibility.

    Returns:
        dict: A dictionary containing the trained model, accuracy, and classification report.
    """
    # Use a decision tree as the default base model if none is provided
    if base_model is None:
        base_model = DecisionTreeClassifier()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Initialize the BaggingClassifier with the specified parameters
    bagging_model = BaggingClassifier(
        estimator=base_model,  # Correctly using 'estimator' instead of 'base_estimator'
        n_estimators=n_estimators,
        max_samples=max_samples,
        max_features=max_features,
        random_state=random_state
    )

    # Train the bagging model
    bagging_model.fit(X_train, y_train)

    # Make predictions and evaluate the model
    y_pred = bagging_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    # Return the results
    return {
        "model": bagging_model,
        "accuracy": accuracy,
        "classification_report": report
    }


# # Examples



# Import necessary libraries
import numpy as np
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris  # Example dataset

# Define the Bagging function
def Bagging(X, y, base_model=None, n_estimators=10, max_samples=1.0, max_features=1.0, test_size=0.2, random_state=None):
    """
    Performs bagging ensemble classification on a dataset.

    Parameters:
        X (array-like): Feature matrix.
        y (array-like): Target labels.
        base_model (estimator): The base model to use for bagging (default is DecisionTreeClassifier).
        n_estimators (int): Number of estimators in the ensemble.
        max_samples (float): Maximum samples to draw from X for each base estimator.
        max_features (float): Maximum features to draw from X for each base estimator.
        test_size (float): Proportion of the dataset to include in the test split.
        random_state (int): Random state for reproducibility.

    Returns:
        dict: A dictionary containing the trained model, accuracy, and classification report.
    """
    # Use a decision tree as the default base model if none is provided
    if base_model is None:
        base_model = DecisionTreeClassifier()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Initialize the BaggingClassifier with the specified parameters
    bagging_model = BaggingClassifier(
        base_estimator=base_model,
        n_estimators=n_estimators,
        max_samples=max_samples,
        max_features=max_features,
        random_state=random_state
    )

    # Train the bagging model
    bagging_model.fit(X_train, y_train)

    # Make predictions and evaluate the model
    y_pred = bagging_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    # Return the results
    return {
        "model": bagging_model,
        "accuracy": accuracy,
        "classification_report": report
    }

# Load example data
data = load_iris()
X, y = data.data, data.target

# Run the Bagging function
results = Bagging(X, y, n_estimators=15, max_samples=0.8, random_state=42)

# Output results
print("Accuracy:", results["accuracy"])
print("Classification Report:\n", results["classification_report"])

