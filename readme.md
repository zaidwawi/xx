# Full Stack Casting Agency API Backend

## Casting Agency Specifications

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Motivation for project

This is the final project of Udacity fullstack nanodegree program, this project demonstrate the ability to develop and deploy a RESTful API. 

## Getting Started



#### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

#### PIP Dependencies

pip install -r requirements.txt

## Running the server

To run the server, execute:

```
. ./setup.sh
flask run
```
or 
'''
. ./setup.sh
python app.py
'''

#### Testing

You will need to make sure the tokens in test.py are not expired
To run the tests 

```
python test.py
```
### Roles and permissions

Casting Assistant:
   Can view actors and movies

Casting Director:
   All permissions a Casting Assistant has and…
   Add or delete an actor from the database
   Modify actors or movies

Executive Producer:
   All permissions a Casting Director has and…
   Add or delete a movie from the database

##### API Testing

To test the API use postman to add a bearer authentication header and use the tokens in setup.sh


### Error Handling

Errors are returned as JSON objects:

```
{
    "success": False,
    "error": 400,
    "message": "bad request"
}

```

### Endpoints

GET '/movies'
Returns an array of all movies

```
{
   "movies":[
      {
         "id":1,
         "release_date":"2019-4-22",
         "title":"Avengers: Endgame"
      },
      {
         "id":2,
         "release_date":"2019-4-22",
         "title":"Avengers: Endgame"
      }
   ],
   "success":True
}
```

GET '/actors'
Returns an array of all actors


```
  {
   "actors":[
      {
         "age":16,
         "gender":"male",
         "id":1,
         "name":"Abed"
      }
   ],
   "success":True
}
```

DELETE '/movies/<int:movie_id>'
Deletes an actor from the database using its id

```
}
"deleted_movie"{
    "id":1,
    "release_date":"2019-4-22",
    "title":"Avengers: Endgame"
    }
}
```

DELETE '/actors/<int:actor_id>'
Deletes an actor from the database using its id


```
{
"deleted_actor":{
    "age":16,
    "gender":"male",
    "id":1,
    "name":"Abed"
    }
}
```

POST '/movies'
Post a new movie to the database.

```
{
"created_movie"{
    "id":1,
    "release_date":"2019-4-22",
    "title":"Avengers: Endgame"
    }
}
```

POST '/actors'
Post a new actor to the database.

```
{
"created_actor":{
    "age":16,
    "gender":"male",
    "id":1,
    "name":"Abed"
    }
}
```

PATCH '/movies/<int:movie_id>'
Updates a movie using its id

```
{
   "movie":{
    "id":1,
    "release_date":"2019-4-22",
    "title":"Avengers: Endgame"
    },
   "success":True
}
```

PATCH '/actors/<int:actor_id>'
Updates an actor using its id

```
{
   "actor":{
         "age":16,
         "gender":"male",
         "id":1,
         "name":"Abed"
      },
   "success":True
}
```

## APP is already running at :
https://casting-agency-project.herokuapp.com/