[![ru](https://img.shields.io/badge/lang-ru-red.svg)](README.md)

# Store Front API
This repository contains the source code for a demo store front with Django Rest Framework and PostgreSQL.

![Static Badge](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Static Badge](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![Static Badge](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![Static Badge](https://img.shields.io/badge/HTML-e34c26?style=flat&logo=html5&logoColor=white)
![Static Badge](https://img.shields.io/badge/CSS-563d7c?&style=flat&logo=css3&logoColor=white)

# Features
- PostgreSQL: scalable relational database
- Django: fully featured highly extensible web framework with admin panel and debug toolbar
- Django Rest Framework: Efficient RESTful API with class-based views
- JWT Authentication: secure authentication using JSON Web Tokens with Djoser
- Docker: containers for development, testing and production
- PyTest: test suite for main features
- Locust: load testing
- Silk: performance profiling
- Waitress: production WSGI server

# Planned Features
- Celery: asynchronous task queue
- Extended API documentation
- Frontend: React.js
- Deploying the project.

# Repository Structure

```
.
├── .devcontainer                       # VSCode dev containers settings
├── .vscode                             # VSCode launch modes
├── apps                                # Django apps
│   ├── core                            # Core functionality with shared logic
│   │   ├── management                  # Django management commands
│   │   │   ├── commands                # -=- 
│   │   │   │   └── seed_db.py          # Script for populating the database
│   │   │   └── seed_db.sql             # PostgreSQL population and index reset
│   ├── likes                           # User likes and interaction
│   ├── playground                      # Experimental features
│   ├── store                           # Main store management functionality
│   └── tags                            # Product tag system
├── locustfiles                         # Load testing
├── storefront                          # Main project settings and configs
│   ├── settings                        # ❗🔧 Project settings
│   │   │   ├── common.py               # Common settings for all environments
│   │   │   ├── dev.py                  # Development settings
│   │   │   ├── prod.py                 # Production settings
│   │   │   ├── secret_key_generator.py # Script for generating Django secret key
│   │   │   └── test.py                 # PyTest settings
│   └── tests                           # PyTest tests
├── .env.example                        # Environment variables example
├── docker-compose.yml                  # Docker compose config
├── docker-entrypoint.sh                # Docker entrypoint script
├── Dockerfile                          # Main Docker instructions
├── manage.py                           # Django management commands
├── Pipfile                             # Pipenv dependencies
├── Pipfile.lock                        # Pipenv dependencies
├── pytest.ini                          # PyTest settings
├── README.en.md                        # Project documentation
├── README.ru.md                        # Project documentation
├── server.py                           # Waitress WSGI server for production
└── wait-for-it.sh                      # Bash script for Docker to wait for dependencies
```

# Installation
## Clone the repository
`git clone https://github.com/mrBrain101/Storefront_Django_PostgreSql.git`

## Set environment variables
- Change the name of the `.env.example` file to `.env`.
- At a minimum set the `DJANGO_SECRET_KEY` environment variable in the `.env` file.<br>
You can generate a secret key with the `storefront/settings/secret_key_generator.py` script or visit [Djecrety](https://djecrety.ir/).
- For development, set the `DEBUG` environment variable to `True`.<br>

## Run the project

### With Docker
- Install [Docker](https://www.docker.com/get-started) if needed.
- Do not run all profiles at once.<br>
- You can optionally populate database with mock product and collection data by setting `POPULATE_DB` to `True` in `.env`.<br>
- Every service can be run individually by 
    - setting uppropriate variables in `.env`;<br>
    - using the `docker compose --profile <service_name> up --build` command.<br>
- For general development:<br>
    - set `DEBUG=True` in `.env`;<br>
    - run `docker compose up --build`
- For development with testing:<br>
    - OPTIONALLY set `TEST_METHOD` in `.env` (options are `pytest` and `ptw`);<br>
    - run `docker compose --profile test up --build`.
- For develpment with [Silk profiling](https://silk.readthedocs.io/en/latest/), [Locust load testing](https://locust.io/), [mock SMTP server](https://github.com/rnwood/smtp4dev) and PyTest testing:<br>
    - OPTIONALLY set `TEST_METHOD` in `.env` (options are `pytest` and `ptw`);<br>
    - set `SILK_PROFILING=True` in `.env`;<br>
    - set `LOAD_TESTING=True` in `.env`;<br>
    - run `docker compose --profile dev up --build`.
- For production to run with Waitress:<br>
    - set `DEBUG=False` in `.env`;<br>
    - run `docker compose --profile production up --build`.

### Manually
#### Install Pipenv
In the project directory, run:
`pip install pipenv`
#### Install dependencies
`pipenv install`
#### Activate local environment
`pipenv shell` / `source venv/bin/activate`
#### Good to go
- You can optionally populate the database with the `apps\core\management\commands\seed_db.py` script:
`python manage.py seed_db`
- You can run tests with PyTest:<br>
`pytest` to run the tests once,<br>
`ptw` to run the tests in watch mode
- You can run the development server:<br>
`python manage.py runserver`
- You can run the production server with Waitress:<br>
`python server.py`
- Or you can build a Docker multicontainer from the source:<br>
`docker compose up --build`

## Available API endpoints:

### Authentication
| Description/scope | Endpoint | Available CRUD actions |
|:--|:--|:--|
| Register a new user | /auth/users/ | POST |
| Create a registration token | /auth/jwt/create/ | POST |
| Obtain a refresh token | /auth/jwt/refresh/ | POST |
     
### Products
| Description/scope | Endpoint | Available CRUD actions |
|:--|:--|:--|
| All products | /store/products/ | GET / POST |
| Specific product | /store/products/{id}/ | GET / PUT / DELETE|

### Collections
| Description/scope | Endpoint | Available CRUD actions |
|:--|:--|:--|
| List collections | /store/collections/ | GET / POST |
| specific collection | /store/collections/{id}/ | GET / PUT / DELETE|

### Orders
| Description/scope | Endpoint | Available CRUD actions |
|:--|:--|:--|
| Order list | /store/orders/ | GET / POST |
| Specific order | /store/orders/{id}/ | GET / PUT / DELETE|

### Carts
| Description/scope | Endpoint | Available CRUD actions |
|:--|:--|:--|
| Carts list | /store/carts/ | GET / POST |
| Specific cart | /store/carts/{id}/ | GET / PUT / DELETE|

### Customers
| Description/scope | Endpoint | Available CRUD actions |
|:--|:--|:--|
| Customers list | /store/customers/ | GET |
| Specific customer | /store/customers/{id}/ | GET |


# Acknowledgement
Thanks to Mosh Hamedani for the [ultimate Django Rest Framework course](codewithmosh.com/p/the-ultimate-django-series).

# License
No licensing. You can use this code however you want.
