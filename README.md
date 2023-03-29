# pandas
Tutorial

## Index
### Reset index 
```python
df = df.rename_axis('Date').reset_index()
```



## Test if dataframe is Empty
```python
if df.empty:
    print("Dataframe is empty")
```

    
## Get last n records of a Pandas DataFrame
```python
n = 10 
df.tail(n)
```

## Compare two dataframes columns 
```python
dados['new_column']=dados['col1'] > dados['col2']
```

# iterate over pandas dataframe
## Using iterrows
```python
for index, row in df.iterrows():
    print(row['c1'], row['c2'])
```    

## using iterrows()
```python
# create a sample dataframe
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})

# iterate over rows
for index, row in df.iterrows():
    print(index, row['col1'], row['col2'])
```    

### iloc
```python
import pandas as pd

# create a sample dataframe
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})

# iterate over rows using iloc
for i in range(len(df)):
    row = df.iloc[i]
    print(row['col1'], row['col2'])
``` 

## using next(row_iterator)
```python
import pandas as pd

# create a sample dataframe
df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [5, 6, 7, 8]})

# get the iterator for rows starting from the third position
row_iterator = df.iterrows()
next(row_iterator)
next(row_iterator)

# iterate over rows starting from the third position
for index, row in row_iterator:
    print(index, row['col1'], row['col2'])
```  

## iterate over two previous rows
```python
# create a sample dataframe
df = pd.DataFrame({'col1': [1, 3, 2, 5, 4], 'col2': [4, 5, 6, 7, 8]})

# initialize the two previous rows
prev_row_1 = None
prev_row_2 = None

# iterate over rows using iterrows
for index, row in df.iterrows():
    # compare the current row with the two previous rows
    if prev_row_2 is not None:
        if row['col1'] > prev_row_2['col1']:
            print(f"Row {index}: col1 > col1 of row before the previous row")
        else:
            print(f"Row {index}: col1 <= col1 of row before the previous row")
    
    # update the two previous rows
    prev_row_2 = prev_row_1
    prev_row_1 = row
```

## iterate over rows using iterrows
```python
for index, row in df.iterrows():
    col1_value = row['col1']
    col2_value = row['col2']
    print(index, col1_value, col2_value)
```
## iterate over rows using itertuples

```python
for row in df.itertuples():
    index = row.Index
    col1_value = row.col1
    col2_value = row.col2
    print(index, col1_value, col2_value)
```

# Drop NA Values
```python
df = df.dropna()
```

# List and Dataframe
## Add a list as new column on dataframe 
```python
pd.concat([pd.DataFrame(GD),dados], axis=1)
```
