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
