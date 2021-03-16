## Este repositorio es una guía para los estudiantes de ingeniería eléctrica que están cursando algoritmos y programación/computación numérica en la Universidad de Antioquia.

# PyQt
PyQt es una librería de Python que permite crear interfaz gráfica de usuario (GUI en inglés) al igual que [Tkinter](https://github.com/juan-suarezp/PythonTkinterTutorial). Aunque PyQt brinda la posibilidad de crear GUI de una forma similar, en este caso haremos uso de la herramienta QtDesigner que facilita mucho el proceso de crear una interfaz.

## GUI con PyQt y Qt Designer
Lo primero es abrir el Qt Designer, nos encontraremos con lo siguiente:

![designer](https://github.com/juan-suarezp/PythonPyQtTutorial/blob/master/designer.png)

Luego seleccionamos "Main window" y presionamos el botón crear. Ahora aparecerá una ventana con dos QWidgets (así se llaman los elementos en Qt) llamados "menubar" y "statusbar".

![designerMainWindow](https://github.com/juan-suarezp/PythonPyQtTutorial/blob/master/designerMainWindow.png)

Los principales elementos, además de la barra superior de herramientas, de Qt designer son:
1. **Caja de Widgets**, como su nombre lo indica, es donde están almacenados todos los QWidgets disponibles en Qt.
2. Aquí se muestran las ventanas que estamos creando.
3. **Inspector de objetos**, donde se listan todos los QWidgets que se estén usando.
4. **Editor de propiedades**, donde se pueden ver y editar las propiedades del QWidget seleccionado en el inspector de objetos (3.).

A continuación, debemos arrastrar desde la caja de widgets (1.) hasta la ventana en 2. los elementos o QWidgets que queremos usar en nuestra interfaz. Por ejemplo, si arrastramos un botón (Push Button) y una etiqueta (Label), el resultado será el siguiente:

![designerEjemplo](https://github.com/juan-suarezp/PythonPyQtTutorial/blob/master/designerEjemplo.png)

Podemos ver en el inspector de objetos (3.) como se agregan los nuevos QWidgets a la lista:

![designerInspector](https://github.com/juan-suarezp/PythonPyQtTutorial/blob/master/designerInspector.png)

Es importante tener en cuenta el nombre que se le da a los QWidgets en el inspector de objetos, debido a que este nombre nos servirá para conectar los objetos de la ventana con los métodos y funciones que vayamos a usar luego. En este ejemplo no usaremos los QWidgets iniciales "menubar" y "statusbar", por lo que los eliminamos dando click derecho sobre su nombre en el inspector de objetos o directamente sobre el objeto en la ventana.

Como se puede observar, con Qt Designer es posible configurar la apariencia inicial de nuestra ventana más fácil que con Tkinter. Por ejemplo, si queremos cambiar el texto inical de la etiqueta o del botón, basta con seleccionar el texto y escribir lo que queremos que aparezca. También permite cambiar los tamaños y demás opciones como el color (ver opción "palette" en el editor de propiedades):

![designerApariencia](https://github.com/juan-suarezp/PythonPyQtTutorial/blob/master/designerApariencia.png)

El siguiente paso es guardar el archivo .ui de Qt designer. En este caso lo llamaremos "Ejemplo.ui". Luego, desde Python abriremos este archivo .ui para conectar funciones y métodos a los elementos que agreguemos a nuestra interfaz, con el siguiente código:

```python
# -*- coding: utf-8 -*-
"""
Ejemplo de ventana básico con botón para cambiar texto

"""
#importamos las librerías necesarias
import sys
from PyQt5 import QtWidgets, uic

#Carga la interfaz gráfica y conecta los botones
class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self, padre=None):
        #Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("Ejemplo.ui",self) #Lee el archivo de Qtdesigner
        
        self.setWindowTitle("Ejemplo") #Título de la ventana
        
        #Conectar botón a función
        self.pushButton.clicked.connect(self.funcion)
        
    def funcion(self):
        if self.label.text() == "":
            self.label.setText("Hola clase")
        else:
            self.label.setText("")


# se crea la instancia de la aplicación
app = QtWidgets.QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec_())
```

Al ejecutar, el resultado es el siguiente:

![resultado](https://github.com/juan-suarezp/PythonPyQtTutorial/blob/master/resultado.png)

En general, el procedimiento para crear una interfaz con PyQt y QtDesigner es el mismo siempre. Se crea la interfaz en QtDesigner y en Python se lee el archivo .ui y se conectan los QWidgets con los métodos y funciones.

```python
# -*- coding: utf-8 -*-
"""
Ejemplo de ventana básico con botón para cambiar texto

"""
#importamos las librerías necesarias
import sys
from PyQt5 import QtWidgets, uic
```
En esta parte del código se importan las liberías necesarias para abrir el archivo .ui y trabajar con PyQt.

```python
class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self, padre=None):
        #Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("Ejemplo.ui",self) #Lee el archivo de Qtdesigner
```

Luego se carga la interfaz y se inicializa la clase `Ventana`. En la última línea podemos ver cómo se carga el archivo.ui que creamos en QtDesigner.

```python
        self.setWindowTitle("Ejemplo") #Título de la ventana
        
        #Conectar botón a función
        self.pushButton.clicked.connect(self.funcion)
        
    def funcion(self):
        if self.label.text() == "":
            self.label.setText("Hola clase")
        else:
            self.label.setText("")
```

En lo que sigue, se cambia el título de la ventana (también se puede cambiar desde QtDesigner) y se conecta el botón con el método `funcion`. Este método cambia el texto del label que hay en la ventana; si está vacío pone el mensaje "Hola clase", si tiene el mensaje, lo quita.

Este es un ejemplo muy sencillo pero muestra el procedimiento general para crear una interfaz usando PyQt y QtDesigner.

## Ejemplos
Como se pudo observar, QtDesigner cuenta con muchos QWidgets disponibles. En esta parte se listan ejemplos usando los QWidgets que más se utilizan. [Aquí](https://doc.qt.io/qt-5/widget-classes.html#the-widget-classes) podemos encontrar las propiedades y señales de los QWidgets necesarias para conectarlos con los métodos y funciones en el código.
- [Ejemplo 1]()
- [Ejemplo 2]()
- [Ejemplo 3]()
- [Ejemplo 4]()
- [Ejemplo 5]()
- [Ejemplo 6]()
- [Ejemplo 7]()
- [Ejemplo 8]()
- [Ejemplo 9]()
- [Ejemplo 10]()
- [Ejemplo 11]()
