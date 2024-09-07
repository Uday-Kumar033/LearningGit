import pandas as pd
import numpy as np
d ={
  "a" : [20,90,np.nan,np.nan],
  "b" : [32,90,np.nan,90,]
}
df = pd.DataFrame(d)
print("Original data :")
print(df)
print()
filled = df.fillna(df.mean())
print("Filled value of mean in the place of empty")
print(filled)
print()
dropped_row = df.dropna()
print("data after deleting row:")
print(dropped_row)
print()
dropped_col = df.drop("b",axis=1)
print("Dropped empty value of every columns :")
print(dropped_col)