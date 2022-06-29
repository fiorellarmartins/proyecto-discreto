import numpy as np
import pandas as pd
array = []

num_var = 7

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

x = tabla_de_verdad(array, num_var)
# print(x)
columnas = ["A", "B", "C", "D", "E", "F", "G"]

df = pd.DataFrame(x, columns=columnas)
print(df)
