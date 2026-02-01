import numpy as np

def array_factory(mode, shape, value=None):
    """
    Creates various NumPy arrays based on the mode.
    - 'zeros': Array filled with 0.
    - 'ones': Array filled with 1.
    - 'full': Array filled with a specified 'value'.
    - 'identity': A square identity matrix of size 'shape'.
    """

    if mode == "zeros":
        return np.zeros(shape)

    elif mode == "ones":
        return np.ones(shape)

    elif mode == "full":
        if value is None:
            return "Error: 'value' must be provided for full array."
        return np.full(shape, value)

    elif mode == "identity":
        return np.eye(shape)

    else:
        return "Error: Invalid mode. Use 'zeros', 'ones', 'full', or 'identity'."
