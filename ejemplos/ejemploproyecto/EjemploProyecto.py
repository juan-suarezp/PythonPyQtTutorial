# -*- coding: utf-8 -*-
"""
Ejemplo de ventana que procesa archivos .lis de ATP

"""
#Importo las librerías necesarias
import os
import sys
from PyQt5 import QtWidgets, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as Toolbar
import matplotlib.pyplot as plt
import math 


class main(QtWidgets.QMainWindow):
    """
    Esta es la clase principal
    
    """
    def __init__(self, padre=None):
        """        
        Define la ventana y conecta los botones con los métodos
        
        """
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("EjemploProyecto.ui",self) #Carga archivo de designer
        #Botones
        self.psbCarpeta.clicked.connect(self.getDirectory) #Escoger carpeta
        self.psbGraficar.clicked.connect(self.Graficar) #Graficar archivo
        self.lwArchivos.itemClicked.connect(self.SelArchivo) #Selec archivo
        #Crea las gráficas
        self.figure1 = plt.figure(1)
        self.canvas1 = FigureCanvas(self.figure1)
        self.toolbar1 = Toolbar(self.canvas1, self)
        self.figure2 = plt.figure(2)
        self.canvas2 = FigureCanvas(self.figure2)
        self.toolbar2 = Toolbar(self.canvas2, self)
        #Espacio para graficar
        self.mplwindow1.addWidget(self.toolbar1) #Widget para herramientas
        self.mplwindow1.addWidget(self.canvas1) #Widget para graficar
        self.mplwindow2.addWidget(self.toolbar2) #Widget para herramientas
        self.mplwindow2.addWidget(self.canvas2) #Widget para graficar

        self.ax1 = self.figure1.add_subplot(111)
        self.ax2 = self.figure2.add_subplot(111)
   

    def getDirectory(self):
        """
        Obtiene y muestra la ruta de la carpeta seleccionada en el dialogo,
        también lista los archivos .lis que hay en la carpeta
        
        """
        self.cwd = os.getcwd() #Ubicación actual
        #Crea el diálogo para seleccionar carpeta
        self.carpeta = QtWidgets.QFileDialog.getExistingDirectory(
                                            None,'Seleccionar Carpeta',self.cwd, 
                                            QtWidgets.QFileDialog.ShowDirsOnly)
        #Borra los nombres de archivos que se están mostrando en la lista
        self.lwArchivos.clear()
        
        #Evalúa si seleccionó una carpeta
        if len(self.carpeta) > 1:
            #Cambia el texto en el label de la ruta
            self.lblRuta.setText("Ruta archivo: "+ self.carpeta)
            #Lista de los archivos .lis en la carpeta seleccionada
            self.listArchivos = os.listdir(self.carpeta)
            for i in self.listArchivos:
                if ".lis" in i:
                    self.lwArchivos.addItem(i)
        
        
    def SelArchivo(self,item):
        """
        Obtiene y muestra la ruta del archivo seleccionado de la lista
        
        """
        text = item.text() #Nombre del archivo seleccionado
        
        self.ruta = os.path.join(self.carpeta,text) #Ruta del archivo
        
        #Cambia el texto en el label de la ruta
        self.lblRuta.setText("Ruta archivo: "+self.ruta)

        
    def valorRMS(self,lista):
        """
        Recibr una lista con valores numéricos y calcula el valor RMS
        discreto
        
        """
        total = 0
        for i in lista:
            total = total + i**2
        return math.sqrt(total/len(lista))
        
        
    def Graficar(self):
        file = open(self.ruta,encoding="ISO-8859-1") #Abre el archivo
        
        #Lee las primeras líneas y obtiene información de cuantas señales hay 
        for line in file:
            if "Column headings for the" in line:
                numVar = int(line[24:27])
                datos = []
                for i in range(numVar+1):
                    datos.append([])
            if "      0" in line[0:7]:
                lista_tmp = line.split()
                for i in range(1,len(lista_tmp)):
                    datos[i-1].append(float(lista_tmp[i]))
                break
        
        #Lee los datos de las señales y guarda la información en listas 
        for line in file:
            if "\n" == line:
                break
            if not("  % % % % % %" in line or "  Done dumping" in line):
                lista_tmp = line.split()
                for i in range(1,len(lista_tmp)):
                    datos[i-1].append(float(lista_tmp[i]))
            else:
                continue
            
        file.close()
        
        t = datos[0] #tiempo
        v = datos[1] #Voltaje
        
        #Encontrar número de datos en un periodo n
        for i in range(len(v)):
            if v[i] >= 0 and v[i+1] < 0:
                i1 = i
                break
        
        for i in range(i+1,len(v)):
            if v[i] >= 0 and v[i+1] < 0:
                i2 = i
                break    

        Vrms = [] #Valores RMS discretos
        n = int((i2-i1)/2)
        
        for i in range(0,len(v)):
            if i>=n:
                Vrms.append(self.valorRMS(v[i-n:i]))
        
        #Descarta la gráfica anterior
        self.ax1.cla()
        #Grafica la señal
        self.ax1.plot(t, v, label="Voltage signal")
        self.ax1.plot(t[n:], Vrms, label="Voltage RMS")
        self.ax1.set_title("Voltage vs Time")
        self.ax1.set_xlabel("Time (s)") #
        self.ax1.set_ylabel("Voltage (V)")
        self.ax1.grid(True)
        self.ax1.legend(loc="best")
        self.canvas1.draw()
        
        #Encuentra tiempo caída de tensión
        Vref = max(Vrms)
        for i in range(len(Vrms)):
            if Vrms[i] <= Vref *0.9:
                y1 = i
                break
        
        for i in range(i+1,len(Vrms)):
            if Vrms[i] >= Vref*0.9:
                y2 = i
                break
        
        #Descarta la gráfica anterior
        self.ax2.cla()
        #Grafica la parte de la caída en la señal
        self.ax2.plot(t[y1-n*2:y2+n*3], v[y1-n*2:y2+n*3], label="Voltage signal")
        self.ax2.plot(t[n+y1-n*2:y2+n*3+n], Vrms[y1-n*2:y2+n*3], label="Voltage RMS")
        self.ax2.set_title("Voltage vs Time")
        self.ax2.set_xlabel("Time (s)") #
        self.ax2.set_ylabel("Voltage(V)")
        self.ax2.grid(True)
        self.ax2.legend(loc="best")
        self.canvas2.draw()


#EJECUTA LA APLICACIÓN
app = QtWidgets.QApplication(sys.argv)
myWindow = main(None)
myWindow.show()
sys.exit(app.exec_())