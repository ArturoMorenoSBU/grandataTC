# grandataTC

#### Hello World! Gracias por dar un vistazo por aquí. Vamos con el desglose de este repositorio

### Docker
En la primera parte, seteamos nuestro ambiente de Jupyter con la versión más reciente de Pyspark con la siguiente composición del docker-compose.+
![alt text](images/dockercompose.png)

Se corre nuestra imagen con **docker-compose up**
![alt text](images/runningcontainer.png)

Es necesario saber el token para ingresar a la UI de Jupyter
![alt text](images/knowingTheSparkToken.png)

Nos conectamos a nuestro workspace en el puerto 8888, **http://localhost:8888/**
![alt text](images/workspace.png)


### Estructura del proyecto.

Dentro de este repositorio se encuentra una carpeta llamda "proyectos", dentro de esta carpeta hay una carpeta "data" con los datos para este proyecto, divididos en:
- raw: datos en crudo tal cual se descragaron
- preprocessed: Datos omitiendo los registros con nulls en alguna de las columnas de **"id_source"** y **"id_destination"** y cambiando los tipos de datos por unos más manejables para el análisis.
- processed: Datos listos para tomar, formar reglas y analizar.

En la carpeta **porject** se encuentran los notebooks del procesamiento y analisis de los datos. No se borraron los outputs para su visibilidad:
- cleaning.ipynb: Procedimiento para analisis exploratorio inicial, drop de nulos 
- data_processing.ipynb: Se agrega la columna **cuota_sms_region** para saber la tarifa de los sms según la región y se escribe estos insumos procesados casteando sus datos por tipos más amnejables.
- analysis.ipynb: Se resuelven los ejercicios, antes agregando una columna que multiplique la tarifa de los sms por el # de sms que se enviaron.

### Respuestas ejercicios.
- 1. $ 391367.0
- 2. ![alt text](images/ej2.png)
- 3. ![alt text](images/ej3.png)

**Nota: Cada uno de los análisis viene mayor documentado en los notebooks**