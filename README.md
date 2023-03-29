# pandas
Tutorial

## Index
### Reset index 
df = df.assign(index1=df.index)


## Empty
if df.empty:
    print('DataFrame is empty!')
    
## Get last n records of a Pandas DataFrame
df.tail(n)
