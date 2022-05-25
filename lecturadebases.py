import pandas as pd
import numpy as np

def calcular_media(df):
    vector_media=['']
    for i in range(1,df.shape[1]-1):
        media=0.0
        for j in range(df.shape[0]):
            media+=float(df.iat[j,i])
        media=media/df.shape[0]
        vector_media.append(round(media,2))
    return(vector_media)
def binoomo(df,media):
    binomo=np.zeros(shape=(len(df),len(df.columns)-2))
    for i in range(len(binomo)):
        for j in range(len(binomo[i])):
            if j>0:
                if df.iat[i,j]>media[j]:
                    binomo[i][j]=1
    return binomo
            

df = pd.read_csv("test.csv")
print(df)
medias=calcular_media(df)
print(medias)
mat=binoomo(df,medias)
print(mat)



