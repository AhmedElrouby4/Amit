import numpy as np

def secure_reshape_and_stack(data1, data2, new_shape):
    """
    1. Validates and converts inputs to NumPy arrays.
    2. Reshapes the first dataset to a specific dimension.
    3. Vertically stacks both datasets into one matrix.
    """
    try:
        # Convert inputs to ndarray
        arr1 = np.array(data1)
        arr2 = np.array(data2)

        # Reshape arr1 to the new shape
        reshaped_arr1 = arr1.reshape(new_shape)

        # Vertical stacking (both must have same number of columns)
        combined_dataset = np.vstack((reshaped_arr1, arr2))

        return combined_dataset

    except ValueError as e:
        raise ValueError(f"Company-grade Error: {e}")
