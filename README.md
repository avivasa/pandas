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

### iterate over pandas dataframe
for index, row in df.iterrows():
    print(row['c1'], row['c2'])

# Drop NA Values
```python
df = df.dropna()
```
