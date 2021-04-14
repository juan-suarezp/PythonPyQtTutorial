# -*- coding: utf-8 -*-
"""
Ejemplo de Qt Designer GUI con gráfica 3D de matplotlib

"""
#importamos las librerías necesarias
import os
import sys
import numpy as np
from PyQt5 import QtWidgets, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as Toolbar
import matplotlib.pyplot as plt

#Carga la interfaz gráfica y conecta los botones
class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self, padre=None):
        #Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("3D.ui",self) #Lee el archivo de QtDesigner

        #Conectar botones a funciones
        self.pushButton.clicked.connect(self.graficar)

        #Crea la gráfica
        self.figure1 = plt.figure(1)
        self.canvas1 = FigureCanvas(self.figure1)
        self.toolbar1 = Toolbar(self.canvas1, self)
        #Espacio para graficar
        self.mpl.addWidget(self.toolbar1) #Widget para herramientas
        self.mpl.addWidget(self.canvas1) #Widget para graficar
        self.ax1 = self.figure1.add_subplot(1,1,1, projection="3d")

    def graficar(self):
        """
        Grafica dependiendo de la selección del Combobox

        """
        if self.comboBox.currentText() == "":
            pass
        elif self.comboBox.currentText() == "Graph 2":
            self.ax1.cla()
            x = np.linspace(np.random.randint(-5,0), np.random.randint(5,10),
                            40) #X coordinates
            y = np.linspace(np.random.randint(-5,0), np.random.randint(5,10),
                            40) #Y coordinates
            X, Y = np.meshgrid(x, y) #Forming MeshGrid
            Z = np.sin(np.sqrt(X**2+Y**2))
            self.ax1.plot_surface(X, Y, Z) #plots the 3D surface plot
            self.canvas1.draw()
        else:
            self.ax1.cla()
            #Seno
            x = np.linspace(-6,6,30) #X coordinates
            y = np.linspace(-6,6,30) #Y coordinates
            X,Y = np.meshgrid(x,y) #Forming MeshGrid
            Z = np.sin(np.sqrt(X**2+Y**2))
            
            # Esfera
            # u = np.linspace(0, 2 * np.pi, 100)
            # v = np.linspace(0, np.pi, 100)
            # X = 10 * np.outer(np.cos(u), np.sin(v))
            # Y = 10 * np.outer(np.sin(u), np.sin(v))
            # Z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
            
            #Superficie
            # X = np.array([[1, 3], [2, 4]])
            # Y = np.array([[5, 6], [7, 8]])
            # Z = np.array([[9, 12], [10, 11]])
            
            
            self.ax1.plot_surface(X, Y, Z) #plots the 3D surface plot
            self.ax1.set(xlabel='x', ylabel='y', zlabel='z')
            self.canvas1.draw()

# se crea la instancia de la aplicación
app = QtWidgets.QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec_())