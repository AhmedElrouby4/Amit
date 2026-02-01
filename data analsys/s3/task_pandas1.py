import pandas as pd
import numpy as np

def automated_stat_analyzer(df, column_name):
    """
    Company Task: Provide a summary report of a specific data variable.
    """

    # Check if column exists
    if column_name not in df.columns:
        return "Error: Column not found in DataFrame."

    column = df[column_name]

    # Drop NaN values for accurate calculations
    column_clean = column.dropna()

    # If column is numerical
    if pd.api.types.is_numeric_dtype(column_clean):
        mean_value = column_clean.mean()
        median_value = column_clean.median()
        std_value = column_clean.std()

        # Identify skewness
        if mean_value > median_value:
            skewness = "Right Skewed"
        elif mean_value < median_value:
            skewness = "Left Skewed"
        else:
            skewness = "Symmetric"

        return {
            "Type": "Numerical",
            "Mean": mean_value,
            "Median": median_value,
            "Standard Deviation": std_value,
            "Skewness": skewness
        }

    # If column is categorical
    else:
        mode_value = column_clean.mode()

        return {
            "Type": "Categorical",
            "Mode": mode_value.tolist()
        }
