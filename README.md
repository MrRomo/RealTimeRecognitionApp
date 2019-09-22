# RealTimeRecognitionApp

## Neural Class
La clase Neural tiene 2 componentes principales **neural_detector** y ***neural_recognition***.

**Neural Detector** : El primero se encarga de tomar los frames de la camara y encontra rostros, reconocer rostros conocidos y comprobar si hay una persona lo suficiente mente cerca.

Entradas: 

|Variable|Tipo|Resultado|
|--|--|--|
| N/A |N/A  |N/A|

Salidas:

|Variable|Tipo|Resultado|
|--|--|--|
|Frame |NpArray  |Arreglo de numpy con la fotografia y los recuadros de las personas encotradas| 
|isInFront |Bool  |Igual a True cuando hay una persona a menos de 60cm de la camara| 


