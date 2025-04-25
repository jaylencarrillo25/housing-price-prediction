import pandas as pd

def load_data(train_path='data/raw/train.csv', test_path='data/raw/test.csv'):
    """Loads training and testing datasets."""
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    return train_df, test_df