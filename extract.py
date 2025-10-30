import pandas as pd

print("Extract data from mysql")

data={
    "id":[1,2,3],
    "name":["a","b","c"],
    "age":[10,20,30]
}

df=pd.DataFrame(data)
print(df)