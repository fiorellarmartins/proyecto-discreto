import numpy as np
import pandas as pd
array = []

def tabla_de_verdad(array, num_var):
    for i in range(0, 2**num_var):
        binario_corto = format(i, "b")
        string = str(binario_corto)
        binario_largo = "0"*(num_var-len(string))+string

        vector = np.array([])
        for j in range(0, num_var):
            vector = np.append(vector, int(binario_largo[j]))
        array.append(vector)

    array = np.array(array)
    array = array.astype(int)
    return(array)

def menor(lista):
    min = lista[0];
    for x in lista:
        if x < min:
            min = x
    return min

def sorteo(matriz,betas):
    importantes=[]
    for i in range (len(matriz)):
        sumatoria=0.73646
        for j in range(len(matriz[i])):
            sumatoria+=matriz[i][j]*betas[j]
        if sumatoria > 1:
            importantes.append(i)
    return importantes


x = tabla_de_verdad(array, 7)
columnas = ["A", "B", "C", "D", "E", "F", "G"]
betas= [-0.09194,0.20075,-0.22522,0.32197,-0.11367,0.13933,-0.21328]

first_try=sorteo(x,betas)
'''for i in range(len(first_try)):
    print(i, first_try[i])'''
print(first_try)
#df = pd.DataFrame(x, columns=columnas)


