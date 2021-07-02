# Ejemplo 3 - FileDialog, QPushButton, QListWidget, QTabWidget y QLabel
Este ejemplo muestra cómo usar botones, listWidget, TabWidget y label para seleccionar carpetas y archivos para obtener su ruta, necesaria para procesarlos. La listWidget es una lista que permite seleccionar los elementos en ella. El TabWidget permite organizar varias ventanas en diferentes pestañas y los label son etiquetas.

## Código
```python
# -*- coding: utf-8 -*-
"""
Ejemplo de ventana básico con QPushButton, QListWidget, QTabWidget, QLabel

"""
#importamos las librerías necesarias
import sys
from PyQt5 import QtWidgets, uic
import os

#Carga la interfaz gráfica y conecta los botones
class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self, padre=None):
        #Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("ejemplo3.ui",self) #Lee el archivo de QtDesigner
        self.cwd = os.getcwd() #directorio de trabajo

        #Conectar botones a funciones
        self.pushButton_2.clicked.connect(self.archivo)
        self.pushButton.clicked.connect(self.carpeta)
        self.listWidget.itemClicked.connect(self.mostrar_archivo)
        
        
    def carpeta(self):
        """
        Abre ventana para seleccionar carpeta y muestra los archivos en la
        QListWidget
        
        """
        #Crea el diálogo para seleccionar carpeta
        carpeta = (QtWidgets.
                   QFileDialog.
                   getExistingDirectory(None, 'Seleccionar Carpeta',
                                        self.cwd, 
                                        QtWidgets.QFileDialog.ShowDirsOnly))
        #Borra los nombres de archivos que se están mostrando en la lista
        self.listWidget.clear()
        
        #Evalúa si seleccionó una carpeta
        if len(carpeta) > 1:
            #Lista de los archivos en la carpeta seleccionada
            listArchivos = os.listdir(carpeta)
            for i in listArchivos:
                self.listWidget.addItem(i)
        

    def archivo(self):
        """
        Abre ventana para seleccionar archivo y lo muestra en el label
        
        """
        archivo = (QtWidgets.
                   QFileDialog.
                   getOpenFileName(self, "Abrir archivo", self.cwd))
        
        self.label_2.setText("Archivo seleccionado: "+archivo[0])

        
    def mostrar_archivo(self, item):
        """
        Obtiene y muestra la ruta del archivo seleccionado de la lista
        
        """
        text = item.text() #Nombre del archivo seleccionado
        
        self.label.setText("Archivo seleccionado: "+text)
        
        

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

![ejemplo3](https://user-images.githubusercontent.com/58320351/124223891-3d340380-daca-11eb-8ac5-f0a4b54dbc80.png)

Los botones están conectados a las funciones `carpeta` y `archivo`. La listWidget está conectada a la función `mostrar_archivo`. Como su nombre lo indica, la función `carpeta` permite seleccionar una carpeta para listar los archivos que contiene en la listWidget que se encuentra en la pestaña carpeta. Por otro lado, la función `archivo` permite seleccionar un archivo para mostrar el nombre del archivo seleccionado en el label que se encuentra en la pestaña archivo. Finalmente, la función `mostrar_archivo` muestra el nombre del archivo seleccionado de la listWidget en el label que se encuentra en la pestaña carpeta.

![ResultadoEjemplo3](https://user-images.githubusercontent.com/58320351/124224372-2215c380-dacb-11eb-9dfd-aa943702483a.png)

```python
# -*- coding: utf-8 -*-
"""
Ejemplo de ventana básico con QPushButton, QListWidget, QTabWidget, QLabel

"""
#importamos las librerías necesarias
import sys
from PyQt5 import QtWidgets, uic
import os

#Carga la interfaz gráfica y conecta los botones
class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self, padre=None):
        #Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("ejemplo3.ui",self) #Lee el archivo de QtDesigner
        self.cwd = os.getcwd() #directorio de trabajo
```
En esta parte del código se importan las librerías, se inicializa la clase `Ventana` y se lee el archivo .ui de QtDesigner, además se obtiene el directorio de trabajo actual.

```python
        #Conectar botones a funciones
        self.pushButton_2.clicked.connect(self.archivo)
        self.pushButton.clicked.connect(self.carpeta)
        self.listWidget.itemClicked.connect(self.mostrar_archivo)
        
        
    def carpeta(self):
        """
        Abre ventana para seleccionar carpeta y muestra los archivos en la
        QListWidget
        
        """
        #Crea el diálogo para seleccionar carpeta
        carpeta = (QtWidgets.
                   QFileDialog.
                   getExistingDirectory(None, 'Seleccionar Carpeta',
                                        self.cwd, 
                                        QtWidgets.QFileDialog.ShowDirsOnly))
        #Borra los nombres de archivos que se están mostrando en la lista
        self.listWidget.clear()
        
        #Evalúa si seleccionó una carpeta
        if len(carpeta) > 1:
            #Lista de los archivos en la carpeta seleccionada
            listArchivos = os.listdir(carpeta)
            for i in listArchivos:
                self.listWidget.addItem(i)
        

    def archivo(self):
        """
        Abre ventana para seleccionar archivo y lo muestra en el label
        
        """
        #Crea el diálogo para seleccionar archivo
        archivo = (QtWidgets.
                   QFileDialog.
                   getOpenFileName(self, "Abrir archivo", self.cwd))
        
        self.label_2.setText("Archivo seleccionado: "+archivo[0])

        
    def mostrar_archivo(self, item):
        """
        Obtiene y muestra la ruta del archivo seleccionado de la lista
        
        """
        text = item.text() #Nombre del archivo seleccionado
        
        self.label.setText("Archivo seleccionado: "+text)
```
Luego, se definen las funciones mencionadas `carpeta`, `archivo` y `mostrar_archivo`, las cuales se conectan a ambos botones y a la listWidget de la ventana.

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
