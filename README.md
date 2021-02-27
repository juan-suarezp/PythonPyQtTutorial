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

El siguiente paso es guardar el archivo .ui de Qt designer. En este caso lo llamaremos "Ejemplo.ui".

