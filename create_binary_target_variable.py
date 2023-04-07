def create_binary_target_variable(y):
    """
    Function to create a binary target variable from an array with values +1, -1, and 0.
    
    Args:
    - y (np.ndarray): 1D array containing the original target variable.
    
    Returns:
    - np.ndarray: 1D binary target variable containing only +1 and -1 values.
    """

    # Filter out the values with 0
    y_filtered = y[(y == 1) | (y == -1)]

    # Create binary target variable
    y_binary = np.where(y_filtered == 1, 1, -1)

    return y_binary


# Example usage:
# Assuming you have an array 'y' with values +1, -1, and 0
y = np.array([1, -1, 0, -1, 1, 0, 1, -1, 0])
y_binary = create_binary_target_variable(y)
print(y_binary)
