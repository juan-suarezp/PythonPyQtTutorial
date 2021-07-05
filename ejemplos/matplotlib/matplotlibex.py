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
