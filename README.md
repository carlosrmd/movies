# movies

Technologies
- Django
- SQLite3
- [roman 3.2](https://pypi.org/project/roman/) (because no need to reinvent the wheel)

### API REST endpoints
Default URL:

http://127.0.0.1:8000/

#### GET /api/movies
Description:

Retrieves all movies stored in database

#### GET /api/movies/[movie_id]
Description:

Retrieves single movie with given movie_id

#### GET /api/persons
Description:

Retrieves all person's documents stored in database

#### GET /api/persons/[person_id]
Description:

Retrieves single person with given person_id

#### POST /api/register
Description:

Service to register admin user in the database

Request body:
```
{
  "user": "string",
  "password": "string",
  "email": "string"
}
```
Responses:

| Http code     | Description                                      |
| ------------- |:------------------------------------------------:|
| 200           | User registered succesfully                      |
| 400           | Bad request                                      |
| 409           | Conflict (Given user information already exists) |

#### GET /admin
Description:

Default url to enter the django admin site with credentials from registered user. In the admin site the admin user will be able to add, edit or delete information about movies, persons and relationships between the enitites.

## How to run debug server locally

1. Clone the repo
```
» git clone https://github.com/carlosrmd/movies.git
```
2. Get into the the project's directory
```
» cd movies
```
3. Install requirements
```
» pip3 install -r requirements.txt
```
4. Make migrations
```
» python3 manage.py makemigrations && python3 manage.py migrate
```
5. Run the debug server
```
» python3 manage.py runserver
```
