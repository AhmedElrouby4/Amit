import pandas as pd

def null_handling_strategy(df, strategy="fill_mean"):
    """
    Company Task: Clean a dataset by resolving missing (NaN) values.
    """

    # Check if DataFrame has null values
    if not df.isnull().values.any():
        return df

    df_clean = df.copy()

    if strategy == "drop_rows":
        df_clean = df_clean.dropna()

    elif strategy == "fill_mean":
        numeric_cols = df_clean.select_dtypes(include='number')
        df_clean[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.mean())

    elif strategy == "fill_median":
        numeric_cols = df_clean.select_dtypes(include='number')
        df_clean[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.median())

    else:
        return "Error: Invalid strategy. Use 'drop_rows', 'fill_mean', or 'fill_median'."

    return df_clean
