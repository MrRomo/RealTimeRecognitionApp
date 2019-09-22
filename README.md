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
