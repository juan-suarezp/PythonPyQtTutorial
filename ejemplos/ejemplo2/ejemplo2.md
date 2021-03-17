# Ejemplo 2 - QPushButton, QLabel, QFrame, QComboBox y QLineEdit
Este ejemplo muestra cómo usar botones, frames, combobox y line edit para entrada de texto. Los frames som QWidgets contenedores que permiten organizar otros QWidgets dentro de ellos. Los combobox permiten tener una lista de opciones predeterminada o agregar más elementos a la lista, para después seleccionar una de todas las opciones.

## Código
```python
# -*- coding: utf-8 -*-
"""
Ejemplo de ventana básico con QLabel, QFrame, QLineEdit, QComboBox y QPushButton

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
        uic.loadUi("ejemplo2.ui",self) #Lee el archivo de QtDesigner

        #Conectar botones a funciones
        self.pushButton_2.clicked.connect(self.agregar)
        self.pushButton.clicked.connect(self.mostrar)

        #Agregar valores iniciales al QCombobox
        for i in range(20):
            self.comboBox.insertItem(self.comboBox.count(),
                                     "Elemento {}".format(i))
        
    def agregar(self):
        if self.lineEdit.text() != "":
            self.comboBox.insertItem(self.comboBox.count(),
                                     self.lineEdit.text())
            self.lineEdit.clear()
        else:
            pass

    def mostrar(self):
        self.label.setText("Selección "+self.comboBox.currentText())
        

# se crea la instancia de la aplicación
app = QtWidgets.QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec_())
```
El resultado es el siguiente:

![ejemplo2](https://user-images.githubusercontent.com/58320351/111415497-07e8de80-86b0-11eb-95ec-ef320376944f.png)

Los botones están conectados a las funciones `mostrar` y `agregar`. Como su nombre lo indica, la función `mostrar` plasma un mensaje en el label que indica la actual selección del combobox. Por otro lado, la función `agregar` valida que en el line edit efectivamente haya algún texto, de ser así, agrega el texto respectivo a la lista de opciones del combobox, como se observa en la imagen siguiente:

![resultadoEjemplo2](https://user-images.githubusercontent.com/58320351/111416247-8e51f000-86b1-11eb-88c5-0b8f66b4cfe5.png)

```python
# -*- coding: utf-8 -*-
"""
Ejemplo de ventana básico con QLabel, QFrame, QLineEdit, QComboBox y QPushButton

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
        uic.loadUi("ejemplo2.ui",self) #Lee el archivo de QtDesigner
```
En esta parte del código se importan las librerías, se inicializa la clase `Ventana` y se lee el archivo .ui de QtDesigner.

```python
        #Conectar botones a funciones
        self.pushButton_2.clicked.connect(self.agregar)
        self.pushButton.clicked.connect(self.mostrar)

        #Agregar valores iniciales al QCombobox
        for i in range(20):
            self.comboBox.insertItem(self.comboBox.count(),
                                     "Elemento {}".format(i))
        
    def agregar(self):
        if self.lineEdit.text() != "":
            self.comboBox.insertItem(self.comboBox.count(),
                                     self.lineEdit.text())
            self.lineEdit.clear()
        else:
            pass

    def mostrar(self):
        self.label.setText("Selección "+self.comboBox.currentText())
```
Luego, se definen las funciones mencionadas, `agregar` y `mostrar`, las cuales se conectan a ambos botones de la ventana. También se agregan los 20 valores iniciales al combobox. En esta parte, cabe mencionar que `self.comboBox.count()` cuenta el número de elementos presentes en el combobox que, en este caso, se utiliza para asignar la posición donde se va a insertar el nuevo elemento en el combobox; es decir, pasar como parámetro a `insertItem` el número de elementos de la lista significa que se insertará al final cada nuevo elemento `(self.lineEdit.text())`.

```python
# se crea la instancia de la aplicación
app = QtWidgets.QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec_())
```
Finalmente, se crea la instancia de la clase `Ventana` y se ejecuta la aplicación.
