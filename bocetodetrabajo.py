from operator import truediv
from random import *
def sentencia_no_B(x):
    a=True
    if x<=50:
        a=False
    return a
def sentencia_B(x):
    a=True
    if int(x)<=lastprom:
        a=False
    return a

variables=['BCI', 'CPI', 'FY2 EPS', 'FY2 P/E', 'ERP']
tabla=[]
m=5
a=""
lastprom=randrange(10,15)
respuesta=True
while True:
    for i in range(2):
        fila=[]
        if i==0:
            fila.append('')
        elif i==1:
            fila.append('USA')
        for j in range(m):
            if i==1 and j==1:
                fila.append(randrange(10,15))
            elif i==0:
                fila.append(variables[j])
            else:
                fila.append(randint(0,100))
        tabla.append(fila)
    for i in range(len(tabla)):
        for j in range(len(tabla[i])):
            if i==1 and j not in [0,2]:
                a=str(tabla[i][j])+'%'
            else: a=str(tabla[i][j])
            if j!=len(tabla[i])-1:
                print('{0:<10}'.format(a),end='')
            else:
                print('{0:<10}'.format(a))
    print('--'*20)
    print('promedio CPI ultimos 3 años {0}'.format(lastprom))
    print('--'*20)
    for i in range(len(tabla[1])-1):
        print(f'sentencia {i+1}')
        if i==1:
            print(sentencia_B(tabla[1][i+1]))
            respuesta=respuesta and sentencia_B(tabla[1][i+1])
        else:
            print(sentencia_no_B(tabla[1][i+1]))
            respuesta=respuesta and sentencia_no_B(tabla[1][i+1])
        print('respuesta ',respuesta)
        print('--'*20)
    print(respuesta)
    if respuesta==True:
        break