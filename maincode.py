import os
import pandas as pd
import numpy as np

csvkorea=os.path.dirname(os.path.realpath(__file__))+'\db\korea.csv'
csvbrasil=os.path.dirname(os.path.realpath(__file__))+'\db\sbrasil.csv'
csvjapon=os.path.dirname(os.path.realpath(__file__))+'\db\japon.csv'
csvus=os.path.dirname(os.path.realpath(__file__))+'\db\usa.csv'


def binoomo(df):
    binomo=np.zeros(shape=(len(df),len(df.columns)-1))
    for i in range(len(binomo)):
        for j in range(len(binomo[i])+1):
            if j>0:
                if float(df.iat[i,j])>0.5:
                    binomo[i][j-1]=1
    return binomo


df = pd.read_excel("Input Comparacion.xlsx")
print(df.columns)
US=[]

mat=binoomo(df)
print(mat.astype(int))
