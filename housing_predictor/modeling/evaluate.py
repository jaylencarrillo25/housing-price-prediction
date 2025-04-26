from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

def evaluate_model(model, X, y, kf):
    """
    Evaluate a model using cross-validation.

    Parameters:
    - model: The model to evaluate.
    - X: Features (DataFrame or array).
    - y: Target variable (Series or array).
    - kf: KFold cross-validator.

    Returns:
    - mean_r2: Mean R2 score across folds.
    - std_r2: Standard deviation of R2 scores across folds.
    - mean_mse: Mean Mean Squared Error across folds.
    - std_mse: Standard deviation of Mean Squared Errors across folds.
    """
    r2_scores = []
    mse_scores = []

    for train_index, test_index in kf.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        r2_scores.append(r2_score(y_test, y_pred))
        mse_scores.append(mean_squared_error(y_test, y_pred))

    mean_r2 = np.mean(r2_scores)
    std_r2 = np.std(r2_scores)
    mean_mse = np.mean(mse_scores)
    std_mse = np.std(mse_scores)

    return mean_r2, std_r2, mean_mse, std_mse