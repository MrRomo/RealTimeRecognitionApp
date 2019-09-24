# RealTimeRecognitionApp

## Neural Class
La clase Neural tiene 2 componentes principales **neural_detector** y ***neural_recognition***.

**Neural Detector** :Se encarga de tomar los frames de la camara y encontra rostros, reconocer rostros conocidos y comprobar si hay una persona lo suficiente mente cerca.
*Sintaxis*: `Neural.neural_detector()`

Entradas: 

|Variable|Tipo|Descripcion|
|--|--|--|
| N/A |N/A  |N/A| 

Salidas:

|Variable|Tipo|Descripcion|
|--|--|--|
|Frame |NpArray  |Arreglo de numpy con la fotografia y los recuadros de las personas encotradas| 
|isInFront |Bool  |Igual a True cuando hay una persona a menos de 60cm de la camara| 

##### Nota:   esta funcion debe mantenerse dentro de un while para obtener mediciones en tiempo real de la camara

**Neural  Recognition** :  Esta función funciona como servicio, cuando se desea guardar a una persona dentro de la aplicación. Para esto se utiliza un servicio local como es la librería de **face_recognition** y un servicio cloud para obtener características precisas como lo es **Azure Cognitive Face**.
*Sintaxis*: `Neural.neural_recognition(<name>)`

Entradas: 

|Variable|Tipo|Descripcion|
|--|--|--|
| name | String  |Contiene el nombre de la persona a la que se desea guardar| 

Salidas:

|Variable|Tipo|Descripcion|
|--|--|--|
|person |Dict  |Diccionario de caracteristicas de la persona aprendida| 

##### Nota este servicio toma un tiempo dependiendo del Internet, por lo que estará bloqueado hasta que se cumpla la ultima de las peticiones.



# Interfaz Gráfica De Usuario con Python y PyQT5

**Pyqt**  es un binding de la biblioteca gráfica de QT para el lenguaje de programacion Python. Nos permitirá desarrollar aplicaciones con un entorno gráfico agradable.


## Instalación de PyQt 5 y QtDesigner

Una vez instalada  **Anaconda 2**  instalamos **Pyqt5**. Procedemos a abrir el Prompt para ejecutar los siguientes comandos: 

Para actualizar, este código no es necesario si recién has instalado y hecho el update.

>conda update –all

**Instalamos QT (El entorno** **gráfico**):

>conda install qt

**Instalamos PYQT (Binding de QT para el lenguaje Python)**  
>conda install pyqt

Nos preguntara si deseamos proceder y escribimos «Y» e instalamos. Una vez finalizada la instalación podemos abrir QtDesigner:

>designer

Lo cual abrirá **QtDesigner**.

![QtDesigner](https://pythones.net/wp-content/uploads/2019/03/Captura-de-pantalla_2019-03-10_02-55-13-min-1024x576.png)

Revisar: [https://pythones.net/pyqt-instalacion-y-codigo-tutorial/#Tutorial_Instalar_PyQt_5_y_QtDesigner](https://pythones.net/pyqt-instalacion-y-codigo-tutorial/#Tutorial_Instalar_PyQt_5_y_QtDesigner)

## Exportando nuestra ventana .ui a .py

Guarda el diseño en un archivo .ui para luego pasarlo a uno de Python que permita trabajar con el código. 

Una vez generado archivo.ui se convierte a .py. Para eso vamos a la consola y mediante el siguiente comando lo convertimos. (Recuerda que en la consola debes posicionarte donde se encuentra el archivo primero.)

### Opción 1
> pyuic5 -x miventana.ui -o miventana_ui.py

### Opción 2
> pyuic5.exe -x miventana.ui -o miventana_ui.py

### Opción 3 (Recomendada)
> python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py

El archivo debe tener el nombre con el que lo has guardado, así que cambia en el comando por tu nombre y ejecutas. Deberías ver inmediatamente que aparece un archivo.py


