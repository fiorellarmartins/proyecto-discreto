import math
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

def sorteo(matriz,betas,int):
    importantes=[]
    for i in range (len(matriz)):
        sumatoria=int
        for j in range(len(matriz[i])):
            sumatoria+=matriz[i][j]*betas[j]
        respuesta = (math.exp(sumatoria))/(1+math.exp(sumatoria))
        if respuesta >= 0.5:
            importantes.append(i)
    return importantes


x = tabla_de_verdad(array, 13)
columnas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
Brasil=[1.4938, -0.7628, -0.7751, 0.6497, 0.8019, -1.4445, 0.5150, -0.2340, 0.8364, 0.2261, 0.1225, -0.2521, -0.2904]
Japón=[-3.1278, 0.6410, 2.3699, 1.6812, 0.1570, -1.8898, 0.4069, 0.2013, 1.0736, 0.3946, 0.1566, -0.1281, 1.0984]
Korea=[0.7297, -0.0063, -3.3829, 1.0923, 2.8307, -1.6043, -2.8971, -0.7064, -0.1085, -2.3713, 1.4496, 0.0605, 0.9827]
Us=[-1.0950, -0.4194, 0.3043, -1.5459, -2.5704, 1.7871, 0.8378, -2.2071, 2.5305, 1.9021, 2.9628, 0.7417, -0.0204]
Int_Br=-0.6085
Int_Jp=-1.6709
Int_Kr=0.7113
Int_Us=-1.1429
brasilcum=sorteo(x,Brasil,Int_Br)
coreacum=sorteo(x,Korea,Int_Kr)
japoncum=sorteo(x,Japón,Int_Jp)
usacum=sorteo(x,Us,Int_Us)

'''print('Brasil: ', brasilcum)
print('Corea: ', coreacum)
print('Japon: ', japoncum)
print('USA: ', usacum)'''



'''for i in range(len(first_try)):
    print(i, first_try[i])'''
'''
df = pd.DataFrame(x, columns=columnas)
print(df)'''

