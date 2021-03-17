# Ejemplo 1 - QPushButton, QRadioButton y QCheckBox
Este ejemplo muestra cómo usar los botones, los radiobutton y los checkbox de Qt. La principal diferencia entre los radiobutton y los checkbox, es que los checkbox permiten seleccionar varias opciones de las disponibles, mientras que los radiobutton solo permiten seleccionar una de las opciones entre todos los radiobutton que se encuentren en el mismo QWidget padre.

## Código
```python
# -*- coding: utf-8 -*-
"""
Ejemplo de ventana básico con QCheckBox, QRadioButton y QPushButton

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
        uic.loadUi("ejemplo1.ui",self) #Lee el archivo de QtDesigner

        #Conectar botón a función
        self.pushButton.clicked.connect(self.funcion)

        #Conectar cambio en cualquier QRadioButton a RadioSel
        self.radioButton.toggled.connect(self.RadioSel)
        self.radioButton_2.toggled.connect(self.RadioSel)

    def RadioSel(self):
        #Cuál RadioButton ha sido seleccionado de último
        self.radio = self.sender()

    def funcion(self):
        v1 = self.checkBox.isChecked()
        v2 = self.checkBox_2.isChecked()
        if v1 == True and v2 == True:
            print("CheckBox 1 y 2 activados")
        elif v1 == True and v2 == False:
            print("Checkbox 1 activado y Checkbox 2 desactivado")
        elif v1 == False and v2 == True:
            print("Checkbox 1 desactivado y Checkbox 2 activado")
        else:
            print("Checkbox 1 y 2 desactivados")

        try:
            print(self.radio.text()+" activado")
        except:
            print("RadioButtons desactivados")
        


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

![ejemplo1](https://user-images.githubusercontent.com/58320351/111401204-cdbf1300-8696-11eb-96b1-2ad9e4bc90e6.png)

El botón está conectado a `funcion`, cuyo objetivo es mostrar en la terminal qué checkbox y radiobutton están seleccionados, como se muestra a continuación:

![resultadoEjemplo1](https://user-images.githubusercontent.com/58320351/111401304-04952900-8697-11eb-947d-dfe7fe60f20d.png)

```python
# -*- coding: utf-8 -*-
"""
Ejemplo de ventana básico con QCheckBox, QRadioButton y QPushButton

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
        uic.loadUi("ejemplo1.ui",self) #Lee el archivo de QtDesigner
```
En esta parte del código se importan las librerías, se inicializa la clase `Ventana` y se lee el archivo .ui de QtDesigner.

```python
#Conectar botón a función
        self.pushButton.clicked.connect(self.funcion)

        #Conectar cambio en cualquier QRadioButton a RadioSel
        self.radioButton.toggled.connect(self.RadioSel)
        self.radioButton_2.toggled.connect(self.RadioSel)

    def RadioSel(self):
        #Cuál RadioButton ha sido seleccionado de último
        self.radio = self.sender()

    def funcion(self):
        v1 = self.checkBox.isChecked()
        v2 = self.checkBox_2.isChecked()
        if v1 == True and v2 == True:
            print("CheckBox 1 y 2 activados")
        elif v1 == True and v2 == False:
            print("Checkbox 1 activado y Checkbox 2 desactivado")
        elif v1 == False and v2 == True:
            print("Checkbox 1 desactivado y Checkbox 2 activado")
        else:
            print("Checkbox 1 y 2 desactivados")

        try:
            print(self.radio.text()+" activado")
        except:
            print("RadioButtons desactivados")
```
Luego se definen dos funciones `funcion` y `RadioSel`. La primera se encarga de verificar los checkbox y el radiobutton que están seleccionados para mostrar los mensajes en la terminal. La segunda función cumple un papel importante para los radiobutton, pues se encarga de actualizar el radiobutton que se encuentra seleccionado actualmente. Se puede observar que se conecta el botón a `funcion` y la señal `toggled`, que indica un cambio en la selección, de ambos radiobutton se conecta a la función `RadioSel`.

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
