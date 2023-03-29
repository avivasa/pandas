# pandas
Tutorial

## Index
### Reset index 
```python
df = df.assign(index1=df.index)
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
