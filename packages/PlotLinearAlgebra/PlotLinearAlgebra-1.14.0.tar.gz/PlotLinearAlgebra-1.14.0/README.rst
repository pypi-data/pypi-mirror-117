

Librería PlotLinearAlgebra
==========================

La librería **PlotLinearAlgebra** fue creada para la visualización bidimensional y tridimensional de objetos geométricos 
abordados en un curso de *álgebra lineal*, apoyado desde el lenguaje de programación Python, en particular con el uso de
la librería de cálculo simbólico **SymPy**.

Los objetos que se pueden representar en dos y tres dimensiones con esta librería son : puntos, rectas,
vectores y planos, los cuales se pueden definir desde diferentes representaciones algebraicas para facilitar su uso, 
contiene los módulos de graficación **plotvectors**, **plot2d** y **plot3d**, para su realización se utilizó la librería 
de graficación interactiva **Plotly**, la de arreglos multidimensionales **NumPy** y es compatible con las representaciones
algebraicas de ecuaciones y matrices creadas desde la librería de cálculo simbólico **SymPy**.

Esta librería puede servir para la visualización y una mejor comprensión de los conceptos abordados en un curso de álgebra lineal, debido a que se puede usar como herramienta para
la validación del conocimiento, facilita la realización de conjeturas por parte del estudiantes y la resolución de problemas.

|travis| |lgtm| |coveralls| |libraries|

.. |travis| image:: https://img.shields.io/badge/python%20-%2314354C.svg?&style=flat&logo=python&logoColor=white
  :target: https://www.python.org/
  :alt: Tests

.. |lgtm| image::  https://img.shields.io/badge/plotly%20-%233B4D98.svg?&style=flat&logo=plotly&logoColor=white
  :target: https://plotly.com/
  :alt: LGTM

.. |coveralls| image:: https://img.shields.io/badge/numpy%20-%230095D5.svg?&style=flat&logo=numpy&logoColor=white
  :target: https://numpy.org/
  :alt: Coverage

.. |libraries| image:: https://img.shields.io/badge/SymPy%20-%23239120.svg?&style=flat&logo=sympy&logoColor=white
  :target: https://www.sympy.org/es/
  :alt: Dependencies

Instalación
===========

Para utilizar los módulos de la librería **PlotLinearAlgebra** debe realizar la instalación de la siguiente 
manera :

.. code:: python

    !pip install PlotLinearAlgebra

Luego se deben importar los módulos de graficación **plotvectors**, **plot2d** y **plot3d** con la siguiente sintaxis :


.. code:: python

    from PlotLinearAlgebra.plotvectors import *

.. code:: python

    from PlotLinearAlgebra.plot2d import *

.. code:: python

    from PlotLinearAlgebra.plot3d import *

Funciones del módulo plotvectors
================================

El módulo **plotvectors** permite la representación gráfica de vectores bidimensionales y tridimensionales 
(anclados o no en el origen) desde diferentes representaciones algebraicas, sus funciones pueden graficar 
vectores definidos como matriz columna desde la librería SymPy, sirviendo como herramienta para articular
los cálculos realizados con dicha librería y aportando a la resolución de problemas relacionados 
con los conceptos vectoriales.

Contiene la función **plotvectors2D** que permite realizar la visualización 
de vectores en el plano cartesiano y **plotvectors3D** que permite la visualización de vectores en el espacio
tridimensional, para definir puntos en estos módulos se usarán los objetos tipo tupla, por ejemplo el punto 
``P =(x,y)`` o ``P =(x,y,z)`` y para definir vectores se usarán listas, por ejemplo el vector unidimensional
``V =[x]``, bidimensional ``V =[x,y]`` o tridimensional ``V =[x,y,z]``,  también podemos definir vectores 
como una matriz columna, haciendo uso de la librería sympy, de la forma ``V =Matrix([x])``, ``V =Matrix([x,y])`` 
o ``V =Matrix([x,y,z])`` dependiendo de la dimensión del vector.

Función plotvectors2D
---------------------

Permite visualizar múltiples vectores en el plano cartesiano, que pueden tener un punto inicial y un punto final 
dado, estar anclados en el origen del plano, o vectores equipolentes a otro que inicie en un punto dado (traslación de vectores)
y vectores en forma polar anclados en el origen o con un punto inicial dado, acepta como argumento vectores unidimensionales o
bidimensionales definidos como matriz columna en la librería SymPy.

A continuación  se presenta la sintaxis adecuada para el manejo de esta función:

- ``plotvectors2D([x,y])`` permite graficar un vector con punto inicial ``(0,0)`` y punto final ``(x,y)``.
- ``plotvectors2D([x])`` permite graficar un vector unidimensional en la recta numérica con punto inicial  en el origen y punto final ``(x)``.
- ``plotvectors2D(V)`` permite graficar un vector definido como ``V = [x,y]`` o  ``V = [x]``, usando la librería **sympy** se pueden definir como ``V = Matrix([x,y])`` o ``V = Matrix([x])``.
- ``plotvectors2D([P,Q])`` permite graficar un vector con punto inicial ``P = (x1,y1)`` y punto final ``Q = (x2,y2)``.
- ``plotvectors2D([P,V])`` permite graficar un vector equipolente a un vector definido como: ``V = [x,y]``, ``V = [x]``, ``V = Matrix([x,y])`` o ``V = Matrix([x])`` con punto inicial en ``P = (x0,y0)``.
- ``plotvectors2D([a,"b"])`` permite graficar un vector con magnitud ``a`` y ángulo en grados respecto al eje x positivo ``b``.
- ``plotvectors2D([P,a,"b"])`` permite graficar un vector con punto inicial en ``P = (x0,y0)``, magnitud ``a`` y ángulo en grados respecto al eje x positivo ``b``.
- ``plotvectors2D(v1,v2,...,v3)`` permite graficar múltiples vectores en el mismo plano definidos de diferente forma.

Como ejemplo, podemos presentar el siguiente código donde A,B,C,D se definen como vectores y P y Q se definen como puntos:

.. code:: python

  from PlotLinearAlgebra.plotvectors import plotvectors2D
  from sympy import Matrix
 
  A = Matrix([2,4])
  B = Matrix([5])
 
  C = [3,4]
  D = [-4]
 
  P = (6,4)
  Q = (2,8)
 
  plotvectors2D([-3,6],A,B,D,[P,Q],[5,"300"],[(5,8),B],[(2.5,-4.33),5,"30"])
    
.. image:: https://github.com/josorio398/ALGEBRA-LINEAL-CON-PYTHON/blob/master/im%C3%A1genes%20repositorio/libreria1.PNG?raw=true
   :height: 400
   :align: center
   :alt: alternate text 
    
Función plotvectors3D
---------------------

Permite visualizar multiples vectores en el espacio tridimensional, que pueden tener un punto inicial y un punto final dado, estar 
anclados en el origen del espacio, o vectores equipolentes a otro que inicie en un punto dado (traslación de vectores) y vectores
desde una magnitud y un vector director unitario dado, acepta como argumentos vectores columna tridimensionales definidos en la librería SymPy.

A continuación  se presenta la sintaxis adecuada para el manejo de esta función:

- ``plotvectors3D([x,y])`` permite graficar un vector con punto inicial ``(0,0,0)`` y punto final ``(x,y,z)``.
- ``plotvectors3D(V)`` permite graficar un vector definido como ``V = [x,y,z]`` o en la librería **sympy** como ``V = Matrix([x,y,z])``.
- ``plotvectors3D([P,Q])`` permite graficar un vector con punto inicial ``P = (x1,y1,z1)`` y punto final ``Q = (x2,y2,z2)``.
- ``plotvectors3D([P,V])`` permite graficar un vector equipolente al vector  definido como ``V = [x,y,z]`` o  ``V = Matrix([x,y,z])`` con punto inicial en ``P = (x0,y0,z0)``.
- ``plotvectors3D([a,U])`` permite graficar un vector con magnitud ``a`` y vector director unitario definido como ``U = [x,y,z]`` o ``U = Matrix([x,y,z])``.
- ``plotvectors3D([P,a,U])`` permite graficar un vector con punto inicial en ``P = (x0,y0,z0)``, magnitud ``a`` y vector director unitario definido como ``U = [x,y,z]`` o ``U = Matrix([x,y,z])``.
- ``plotvectors3D (v1,v2,...,v3)`` permite graficar múltiples vectores en el mismo espacio definidos de diferente forma.

Como ejemplo, podemos presentar el siguiente código donde A,B se define como vectores, i,j,k como vectores unitario y P y Q como puntos:

.. code:: python
  
    from PlotLinearAlgebra.plotvectors import plotvectors3D
    from sympy import *

    A = Matrix([6,2,3])
    B = [3,4,5]

    P = (-4,2,3)
    Q = (5,4,6)

    i = [1,0,0]
    j = [0,1,0]
    K = [0,0,1]

    norm = A.norm()
  
    U = (1/norm)*A
  
    plotvectors3D([1,2,3],B,A, [P,Q],[P,B],[(6,3,5),A],[(1,-2,3),(5,-4,-6)],
                  [3,i],[(1,2,3),3,j],[5,K],[(4,5,6),8,U]) 

.. image:: https://github.com/josorio398/ALGEBRA-LINEAL-CON-PYTHON/blob/master/im%C3%A1genes%20repositorio/libreria2a.PNG?raw=true
   :height: 400
   :align: center
   :alt: alternate text 
  
Funciones del módulo plot2d
===========================
    
El módulo **plot2d** permite graficar : puntos, rectas y vectores en el espacio
bidimensional, contiene la función **plot2D**, a continuación se describe la 
sintaxis adecuada para representar cada uno de estos objetos :

- **Vectores** : ``plot2D(V)`` permite graficar un vector ``V`` definido desde las 
  diferentes sintaxis como las mencionadas para la función plotvectors2d.

- **Puntos** : ``plot2D(P)`` permite graficar un punto ``P`` de coordenadas (x, y) 
  definido como una tupla de la forma  ``P = (x0,y0)`` o como un diccionario de la 
  forma ``P = {x : x0,y : y0}``.

- **Rectas** : ``plot2D(R)`` permite graficar una recta ``R`` desde su representación 
  algebraica definida como una cadena de la forma ``R = 'ax+by+c=0'`` o como una 
  ecuación de la librería SymPy de la forma ``Eq(a*x + b*y,d)``, también acepta 
  ecuaciones en forma paramétrica definidas como un diccionario de la  forma ``R = {x :a*t+x0, y : b*t + y0}``.
 

- ``plot2D(V,P,R...)`` permite graficar varios objetos en el mismo plano de diferente tipo usando la sintaxis mencionada.

Como ejemplo, podemos presentar el siguiente código donde A se definen como un vector de la librería SymPy
y se usan diferentes sintaxis para definir puntos y rectas:

.. code:: python

  from PlotLinearAlgebra.plot2d import plot2D
  from sympy import *
  
  x,y,t = symbols("x y t")

  A = Matrix([4,3])

  recta1 = "2x+y-12=0"
  recta2 = Eq(-12*x+6*y,8)
  recta3 = {x:4*t+2,y:3*t+3}

  punto1 = (5,7)
  punto2 = {x:2,y:3}

  plot2D(A,recta1,recta2,recta3,punto1,punto2)

.. image:: https://github.com/josorio398/ALGEBRA-LINEAL-CON-PYTHON/blob/master/im%C3%A1genes%20repositorio/libreria3.PNG?raw=true
   :height: 400
   :align: center
   :alt: alternate text 

Funciones del módulo plot3d
===========================

El módulo **plot3d** permite graficar : puntos, rectas, vectores y planos en el espacio
tridimensional, contiene la función **plot3D**, a continuación se describe la 
sintaxis adecuada para representar cada uno de estos objetos:

- **Vectores** : ``plot3D(V)`` permite graficar un vector ``V`` definido desde las 
  diferentes sintaxis como las mencionadas para la función plotvectors3d.

- **Puntos** : ``plot3D(P)`` permite graficar un punto ``P`` de coordenadas (x, y, z) 
  definido como una tupla de la forma  ``P = (x0,y0,z0)`` o como un diccionario de la 
  forma ``P = {x : x0,y : y0,z : z0}``.

- **Rectas** : ``plot3D(R)`` permite graficar una recta ``R`` desde su forma paramétrica 
  definida como una lista de cadenas de la forma ``R =['at+x0','bt+y0','ct+z0']`` o como un diccionario
  de la  forma ``R = {x :a*t+x0, y : b*t + y0,z : c*t + z0}`` , tambien se puede asignar un valor 
  al parámetro ``t`` al definir la recta de la forma ``R = {x :a*t+x0, y : b*t + y0, y : c*t + z0, t : t0}`` 
  donde ``t0`` permite graficar la recta con dominio en el intervalo ``[-t0,t0]``.

- **Planos** : ``plot3D(P)`` permite graficar un plano ``P`` desde su representación 
  algebraica definido como una cadena de la forma ``P = 'ax+by+cz+d=0'`` o como una 
  ecuación de la librería SymPy de la forma ``Eq(a*x + b*y + c*z,d)``.

- ``plot3D(V,P,R...)`` permite graficar varios objetos de diferente tipo en el mismo espacio usando
  la sintaxis mencionada.

Como ejemplo, podemos presentar el siguiente código donde A y B se definen como un vectores
y se usan diferentes sintaxis para definir puntos, rectas y planos:

.. code:: python

  from PlotLinearAlgebra.plot3d import plot3D
  from sympy import *
  
  x,y,z,t =symbols("x y z t")

  A = Matrix([6,-12,24])
  B = [(-8,-1,27),(-38,4,32)]

  plano1 = Eq(x+2*y+4*z,3)
  plano2 = '-y+z-2=0'

  recta1 =["-6t+4","t-3","t+20"]
  recta2 = {x:-6*t-1,y:t+2,z:t,t:10}

  punto1 = (2,7,20)
  punto2 = {x:4,y:-3,z:20}

  plot3D(A,B,plano1,plano2,recta1,recta2,punto1,punto2) 

.. image:: https://github.com/josorio398/ALGEBRA-LINEAL-CON-PYTHON/blob/master/im%C3%A1genes%20repositorio/libreria4.PNG?raw=true
   :height: 400
   :align: center
   :alt: alternate text 


Colaboradores
=============

Jhonny Osorio Gallego

https://github.com/josorio398

osoriojohnny1986@gmail.com


