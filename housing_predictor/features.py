import numpy as np
from sklearn.preprocessing import MinMaxScaler

def clean_data(df):
    """Drop missing values and standardize lot size units."""
    df = df.dropna().copy()
    df.loc[df['lot_size_units'] == 'acre', 'lot_size'] *= 43560
    df['lot_size_units'] = 'sqft'
    df = df.drop(columns=['size_units', 'lot_size_units', 'zip_code'])
    return df

def engineer_features(df):
    """Create new features and scale numeric columns."""
    df['price_per_sqft'] = df['price'] / df['size']
    df['bath_bed_ratio'] = df['baths'] / df['beds'].replace(0, np.nan)

    scaler = MinMaxScaler()
    df[['size', 'lot_size', 'price', 'price_per_sqft']] = scaler.fit_transform(
        df[['size', 'lot_size', 'price', 'price_per_sqft']]
    )

    return df