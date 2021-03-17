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
            self.comboBox.insertItem(self.comboBox.count(), "Elemento {}".format(i))
        
    def agregar(self):
        if self.lineEdit.text() != "":
            self.comboBox.insertItem(self.comboBox.count(), self.lineEdit.text())
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