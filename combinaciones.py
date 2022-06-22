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
        if sumatoria > 0.5:
            importantes.append(i)
    return importantes


x = tabla_de_verdad(array, 13)
columnas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
brasil= []
corea= []
japon= []
usa=[]
brasilcum=sorteo(x,brasil)
coreacum=sorteo(x,corea)
japoncum=sorteo(x,japon)
usacum=sorteo(x,usa)

print('Brasil: ', brasilcum)
print('Corea: ', coreacum)
print('Japon: ', japoncum)
print('USA: ', usacum)


'''for i in range(len(first_try)):
    print(i, first_try[i])'''

#df = pd.DataFrame(x, columns=columnas)


