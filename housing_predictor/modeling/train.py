from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

def train_linear_regression(X, y):
    """Train a Linear Regression model."""
    model = LinearRegression()
    model.fit(X, y)
    return model

def train_random_forest(X, y):
    """Train a random forest regressor."""
    model = RandomForestRegressor(random_state=42)
    model.fit(X, y)
    return model