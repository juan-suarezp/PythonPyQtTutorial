# Matplotlib
Este es un ejemplo que muestra cómo agregar gráficas de matplotlib a una GUI de PyQt.

```python
# -*- coding: utf-8 -*-
"""
Ejemplo de ventana con gráfica de matplotlib

"""
#importamos las librerías necesarias
import sys
import math
from PyQt5 import QtWidgets, uic
# Para trabajar con PyQt y matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as Toolbar
from matplotlib.pyplot import figure


#Carga la interfaz gráfica y conecta los botones
class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self, padre=None):
        #Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("matplotlib.ui",self) #Lee el archivo de QtDesigner
        
        #Crea las gráficas
        figura = figure(tight_layout=True)
        self.canvas = FigureCanvas(figura)
        toolbar = Toolbar(self.canvas, self)
        #Widget para graficar
        self.verticalLayout.addWidget(toolbar)
        self.verticalLayout.addWidget(self.canvas)
        
        self.ax = figura.add_subplot(111)
        
        #Botón
        self.pushButton.clicked.connect(self.make_plot)
        
    
    def make_plot(self):
        #Se verifican los line edit y crea la señal
        if (self.lineEdit_3.text() != "" and 
            self.lineEdit_2.text() != "" and
            self.lineEdit.text() != ""):
            Vp =  float(self.lineEdit_3.text()) # Voltios 
            fre = float(self.lineEdit_2.text()) # Hz
            w = 2*math.pi*fre # rad/s
            fi = float(self.lineEdit.text()) # rad
        
            # Función a graficar
            def f1(t):
                return Vp*math.sin(w*t+fi)
        
            # Listas con datos a graficar
            t = []
            v = []
        
            ciclos = 5 # Ciclos a graficar 
            puntos = 30 # Puntos por ciclo
            T = 1/fre # Periodo 
            deltat = T / puntos # Distancia entre puntos
        
            
            ti = 0 # Tiempo inicial
            # Calculo las parejas de puntos    
            for i in range(puntos*ciclos+1):
                t.append(ti)
                v.append(f1(ti))
                ti = ti + deltat
        
            #Descarta la gráfica anterior
            self.ax.cla()
            #Grafica la señal
            self.ax.plot(t, v)
            self.canvas.draw()
            
        else:
            print("Error en los datos de entrada.\n")
            

# se crea la instancia de la aplicación
app = QtWidgets.QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
miVentana.make_plot() #Se crea la gráfica inicial
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec_())
```
El resultado es el siguiente:

![ventanamatplotlib](https://user-images.githubusercontent.com/58320351/124425846-c51a4780-dd2e-11eb-9670-d680eb4c31ef.png)

La ventana permite ingresar la amplitud en V, la frecuencia en Hz y la fase inicial en Rad. Al llenar todos los campos, con el botón graficar se actualiza la gráfica con los parámetros actuales ingresados.

A continuación se explica el código por partes:

```python
#importamos las librerías necesarias
import sys
import math
from PyQt5 import QtWidgets, uic
# Para trabajar con PyQt y matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as Toolbar
from matplotlib.pyplot import figure
```
Aquí se importan los módulos necesarios como math, sys y algunos de PyQt. Los últimos tres son necesarios para agregar la gráfica a la interfaz.

```python
#Carga la interfaz gráfica y conecta los botones
class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self, padre=None):
        #Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("matplotlib.ui",self) #Lee el archivo de QtDesigner
        
        #Crea las gráficas
        figura = figure(tight_layout=True)
        self.canvas = FigureCanvas(figura)
        toolbar = Toolbar(self.canvas, self)
        #Widget para graficar
        self.verticalLayout.addWidget(toolbar)
        self.verticalLayout.addWidget(self.canvas)
        
        self.ax = figura.add_subplot(111)
        
        #Botón
        self.pushButton.clicked.connect(self.make_plot)
```
En esta parte del código se inicializa la clase Ventana y se lee el archivo .ui de QtDesigner. Además, se crea la figura y la barra de herramientas que se agrega al widget para graficar (llamado `verticalWidget` en QtDesigner pero en el código se usa su nombre `verticalLayout` que se encuentra en la propiedad `layoutName`). También se conecta el botón a la función para graficar.

```python
    def make_plot(self):
        #Se verifican los line edit y crea la señal
        if (self.lineEdit_3.text() != "" and 
            self.lineEdit_2.text() != "" and
            self.lineEdit.text() != ""):
            Vp =  float(self.lineEdit_3.text()) # Voltios 
            fre = float(self.lineEdit_2.text()) # Hz
            w = 2*math.pi*fre # rad/s
            fi = float(self.lineEdit.text()) # rad
        
            # Función a graficar
            def f1(t):
                return Vp*math.sin(w*t+fi)
        
            # Listas con datos a graficar
            t = []
            v = []
        
            ciclos = 5 # Ciclos a graficar 
            puntos = 30 # Puntos por ciclo
            T = 1/fre # Periodo 
            deltat = T / puntos # Distancia entre puntos
        
            
            ti = 0 # Tiempo inicial
            # Calculo las parejas de puntos    
            for i in range(puntos*ciclos+1):
                t.append(ti)
                v.append(f1(ti))
                ti = ti + deltat
        
            #Descarta la gráfica anterior
            self.ax.cla()
            #Grafica la señal
            self.ax.plot(t, v)
            self.canvas.draw()
            
        else:
            print("Error en los datos de entrada.\n")
```
Como su nombre `make_plot` lo indica, se define una función que crea la gráfica y la agrega a la interfaz. La función no tiene parámetros de entrada debido a que las variables para graficar las obtiene a partir de los valores ingresados en los line edit. Esto se hace en las primeras líneas de la función, por ejemplo para `Vp`, por medio de `float(self.lineEdit_3.text())` se obtiene el valor de la amplitud ingresado en el line edit correspondiente de la interfaz. Así mismo para la frecuencia `fre` y la fase inicial `fi`. Si no se ingresan valores válidos en los line edit, se muestra un mensaje de error.

Con los tres valores obtenidos de los line edit, es posible hallar las listas de tiempo y tensión; para esto se define la función `f1` que retorna la función sinusoidal, la cantidad de ciclos a gráficar, el número de puntos por ciclo y el periodo, para finalmente hallar la separación entre puntos. Con esta información y la función `f1` se llenan las listas de tiempo y tensión que se van a graficar.

```python
# se crea la instancia de la aplicación
app = QtWidgets.QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
miVentana.make_plot() #Se crea la gráfica inicial
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec_())
```
Finalmente, se crea la instancia de la clase Ventana y se ejecuta la aplicación. Además se ejecuta el método `make_plot` para mostrar una gráfica con los valores predeterminados en la ventana.
