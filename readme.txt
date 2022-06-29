Proyecto Discreto - Grupo UwU
###################################  RESUMEN  ###################################

El codigo interpreta una base de dator introducida como csv (no header) como un objeto que posee en sus atributos las herramientas necesarias para 
estandarizarlo en una matriz binaria.

Esta matriz es luego comparada con un juego de expresiones de logica proposicional a traves de las cuales se determina en que interacion
la reaccion es positiva (1) o negativa (0).

En el caso del trabajo, el input es el desempeño de las 13 variables economicas elegidas de uno de los 4 paises (US, JAPON, KOREA y BRASIL). El 
objeto estandariza este dataframe elaborando una matriz binaria. Esta matriz binaria luego es puesto a prueba con el juego de expresiones lógicas de
cada país. El Objeto devuelve las iteraciones positivas, para las cuales se debe tomar la accion de comprar. 

###################################  DETALLE  ###################################

QM_completo.py y tablas_de_verdad.py son ambos documentos con codigos que usamos durante el desarrollo del trabajo. QM_completo.py fue recogido de 
un repositorio de GitHub *Franz llena esto*. tablas_de_verdad.py fue elaborado por un miembro del grupo UwU.

Para el funcionamiento de combinaciones.py se usaron coeficientes obtenidos gracias a una regresion (realizada por el grupo UwU) 
elaborada a la informacion del desempeño económico de los países que son sujeto de estudio. Estos son USA, BRASIL, KOREA y JAPON.

combinaciones.py usa estos coeficientes en una tabla de verdad de 13 variables para hallar cuales de las combinaciones tienen un indice significativo.
Una vez obtenidos estas combinaciones, las procesa por QM_completo.py para reducir la expresion a sus terminos minimos implicantes.

Estos terminos minimos implicantes son rescatados por maincode.py, el cual contiene una clase donde usa de esta informacion, junto a los datos de cada 
país para hallar cuales son las iteraciones donde se debe comprar.

Los datos de cada pais se encuentran en csvs dentro de la carpeta /df, junto con los archivos binarios de los objetos de cada país. Si se desease evaluar
las iteraciones de otro archivo, solo haria falta reemplazar el archivo del país dentro de /df con el que deseases evaluar. 