import pandas as pd

from sklearn.preprocessing import StandardScaler


def preprocess(df):
    
    scaler = StandardScaler()


    X_scaled = scaler.fit_transform(df)


    return pd.DataFrame(X_scaled, columns=df.columns, index=df.index)

