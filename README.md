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
'''
for index, row in df.iterrows():
    print(row['c1'], row['c2'])
'''    
## iterate over two previous rows
'''
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
'''

# Drop NA Values
```python
df = df.dropna()
```
