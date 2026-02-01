import numpy as np

def apply_threshold(arr, threshold, replacement_value=-1, reshape_to=None, stack_with=None):
    """
    Applies threshold replacement to an array. 
    Optionally reshapes the array and stacks it with another array.
    
    Parameters:
    - arr: list or np.ndarray, input data
    - threshold: numeric, elements >= threshold will be replaced
    - replacement_value: numeric, value to replace elements that meet the condition
    - reshape_to: tuple, new shape for arr (if arr is 1D)
    - stack_with: list or np.ndarray, array to stack vertically with arr
    """
    # Convert to numpy array
    arr = np.array(arr)
    
    # Reshape if needed
    if reshape_to is not None:
        arr = arr.reshape(reshape_to)
    
    # Apply threshold
    arr = np.where(arr >= threshold, replacement_value, arr)
    
    # Stack vertically if stack_with is provided
    if stack_with is not None:
        stack_with = np.array(stack_with)
        arr = np.vstack([arr, stack_with])
    
    return arr
