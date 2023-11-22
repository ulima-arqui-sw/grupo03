se usa una base de datos para analizar:
https://jmcauley.ucsd.edu/data/amazon/

es el texto que se va a mapear
#mapping: Hello World this is my review and it is awesome

Hello, 1
Hello, 1
Hello, 1
Hello, 1
Hello, 1
World, 1
World, 1
World, 1
this, 1
once, 1

pasaria a reducir el tamaño a grupos como:
Hello, 5
World, 3
this, 1
once, 1

requisitos de instalacion prompt
pip install mrjob

**en caso de error, desactiva la opcion "full control" de los permisos de la carpeta de Ptyhon312, o la version que tengas
** actualazacion del la version de python: python.exe -m pip install --upgrade pip
** en caso tengas error con 'distutils': pip install setuptools


**ENLACE A VIDEO EXPLICATIVO:
https://drive.google.com/drive/folders/13clHJN4bDRIa3pFcVrWLf13IUP663i1m?usp=sharing