def delete_rows_with_zero(df, column):
    """
    Function to delete rows in a DataFrame conditionally based on a value of 0 in a specific column.
    
    Args:
    - df (pd.DataFrame): DataFrame to delete rows from.
    - column (str): Name of the column to check for the value of 0.
    
    Returns:
    - pd.DataFrame: DataFrame with rows deleted based on the condition.
    """
    
    # Drop rows where the column has value 0
    df = df[df[column] != 0]
    
    return df


# Example usage:
# Assuming you have a DataFrame 'df' with a column 'Y'
# Delete rows where 'Y' column has value 0
df = delete_rows_with_zero(df, 'Y')
