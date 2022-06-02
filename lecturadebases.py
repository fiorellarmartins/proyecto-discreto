import pandas as pd
import numpy as np

def binoomo(df):
    binomo=np.zeros(shape=(len(df),len(df.columns)-1))
    for i in range(len(binomo)):
        for j in range(len(binomo[i])+1):
            if j>0:
                if float(df.iat[i,j])>0.5:
                    binomo[i][j-1]=1
    return binomo
            

df = pd.read_csv("test.csv")
print(df)
mat=binoomo(df)
print(mat)



