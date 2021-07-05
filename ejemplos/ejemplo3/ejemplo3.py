# -*- coding: utf-8 -*-
"""
Ejemplo de ventana básico con FileDialog, QPushButton, QListWidget, QTabWidget
y QLabel

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