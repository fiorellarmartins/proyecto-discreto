import pickle
import os
import pandas as pd
import numpy as np
from Implicantes_esenciales import *
class base:
    def __init__(self,base,pais,comparison):
        self.nombre_pais=pais
        self.base=base
        self.estandarizado=self.binoomo(base)
        self.filaspositivas=self.check(comparison)

    def binoomo(self,df):
        binomo=np.zeros(shape=(len(df),len(df.columns)))
        for j in range(len(binomo[0])):
            avg=df[j].mean()
            for i in range(len(binomo)):
                numero=df.iat[i,j]
                if numero>avg:
                    binomo[i][j]=1
        return binomo

    def check(self,base):
        matrx_xcom=self.estandarizado
        control,valoresconfirmados=[],[]
        for i in range(len(base)):
            c=list(base[i])
            control.append(c)
        for proposicion in range(len(matrx_xcom)):
            for implicante in range(len(control)):
                puntuacion=0
                for variable in range(len(matrx_xcom[proposicion])):
                    if str(control[implicante][variable])=='-':
                        puntuacion+=1
                    elif matrx_xcom[proposicion][variable]==int(control[implicante][variable]):puntuacion+=1
                    else:continue
                if puntuacion==13:
                    valoresconfirmados.append(proposicion)
                    break
        return valoresconfirmados

    def __str__(self):
        return 'Soy '+self.nombre_pais

###Las bases
dat=os.path.dirname(os.path.realpath(__file__))+'\df\lasbases'
ar=open(dat,'rb')
L=pickle.load(ar)
ar.close()

for i in range(len(L)):
    print(L[i])
    print(L[i].filaspositivas)


###GUARDAR LA ESTANDARIZACION EN CSV

'''csvkorea=os.path.dirname(os.path.realpath(__file__))+'\df\korea_estandarizado.csv'
csvbrasil=os.path.dirname(os.path.realpath(__file__))+'\df\sbrasil_estandarizado.csv'
csvjapon=os.path.dirname(os.path.realpath(__file__))+'\df\japon_estandarizado.csv'
csvus=os.path.dirname(os.path.realpath(__file__))+'\df\estdosunidos_estandarizado.csv'
for objeto in range(len(L)):
    matrix=L[objeto].estandarizado.astype(int)
    if L[objeto].pais=="USA":
        ar=open(csvus,'w')
    elif L[objeto].pais=="BRASIL":
        ar=open(csvbrasil,'w')
    elif L[objeto].pais=="KOREA":
        ar=open(csvkorea,'w')
    elif L[objeto].pais=="JAPAN":
        ar=open(csvjapon,'w')
    else: print('wtf')
    for i in range(len(matrix)):
        ar.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}\n".format(matrix[i][0],matrix[i][1],matrix[i][ 2],matrix[i][ 3],matrix[i][ 4],matrix[i][ 5],matrix[i][ 6],matrix[i][ 7],matrix[i][ 8],matrix[i][ 9],matrix[i][ 10],matrix[i][ 11],matrix[i][ 12]))
        #ar.write("{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}\n".format(matrix[i][0],matrix[i][1],matrix[i][ 2],matrix[i][ 3],matrix[i][ 4],matrix[i][ 5],matrix[i][ 6],matrix[i][ 7],matrix[i][ 8],matrix[i][ 9],matrix[i][ 10],matrix[i][ 11],matrix[i][ 12]))
    ar.close()'''

### La he cagado y cambie atributos, el paquete:
'''dat=os.path.dirname(os.path.realpath(__file__))+'\df\lasbases'
csvkorea=os.path.dirname(os.path.realpath(__file__))+'\df\korea.csv'
csvbrasil=os.path.dirname(os.path.realpath(__file__))+'\df\sbrasil.csv'
csvjapon=os.path.dirname(os.path.realpath(__file__))+'\df\japon.csv'
csvus=os.path.dirname(os.path.realpath(__file__))+'\df\estdosunidos.csv'

dfus = pd.read_csv(csvus,header=None)
dfkr = pd.read_csv(csvkorea,header=None)
dfbra = pd.read_csv(csvbrasil,header=None)
dfjap = pd.read_csv(csvjapon,header=None)

USA=base(dfus,"USA",USA)
KOREA=base(dfkr,'KOREA',Corea)
BRA=base(dfbra,'BRASIL',Brasil)
JAP=base(dfjap,'JAPAN',Japon)

#SUBIR CAMBIOS
L=[USA,KOREA,BRA,JAP]
ar=open(dat,'wb')
pickle.dump(L,ar)
ar.close()'''



'''ar=open(csvbrasil,'w')
for i in range(len(lista)):
    ar.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}\n".format(lista.iloc[i, 0],lista.iloc[i, 1],lista.iloc[i, 2],lista.iloc[i, 3],lista.iloc[i, 4],lista.iloc[i, 5],lista.iloc[i, 6],lista.iloc[i, 7],lista.iloc[i, 8],lista.iloc[i, 9],lista.iloc[i, 10],lista.iloc[i, 11],lista.iloc[i, 12]))
ar.close()
'''


