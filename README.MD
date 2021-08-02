## CATIA

### Recursos para el Desarrollo BACKEND

* [Fastapi](https://fastapi.tiangolo.com/) - Rest Api
* [PyMongo](https://docs.mongodb.com/drivers/pymongo/) - Driver for MongoDB
* [Uvicorn](https://www.uvicorn.org/) -  Lightning-fast ASGI (Asynchronous Server Gateway Interface) server implementation
### Programas 
* [Mongo DB Atlas](https://www.mongodb.com/cloud/atlas) 
* [Robo 3T](https://robomongo.org/) 
* [MongoDB Compass](https://www.mongodb.com/products/compass) 
* [Postman](https://www.postman.com/) 

### Ejecutar como desarrollador
~~~
$ uvicorn app:app --reload
~~~
Probar Backend : http://127.0.0.1:8000/docs

### Ejecutar 
~~~
$ uvicorn app:app 
~~~

### MODELS

#### Institucion

~~~
    {
        "cod":String,
        "institution":String
    }
~~~
#### Specialty
~~~
    {
        "cod":String,
        "specialty":String
    }
~~~
#### Quiz
~~~
    {
        "profession":String,
        "institution":String,
        "answer":String,
        "predict":[
            "classdicador":String,
            "respuesta":Int
        ]

    }
~~~
#### Classificador
~~~
    {
        "name":String,
        "data":[ "Bolsa de Palabras"]

    }
~~~

###
