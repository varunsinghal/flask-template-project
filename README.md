## flask template project

<br>

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<br>

### description

The Flask template project is a comprehensive starter template showcasing best practices for building RESTful APIs with Flask. It covers API development, serialization, database interaction, caching, unit testing, and includes Docker for project configuration.

<br>


### features

<br>

_API Development_: The template provides a solid foundation for developing APIs using `Flask`. It demonstrates best practices for designing and implementing API endpoints, and handling request/response formats.

<br>

_Serialization_: The template showcases the use of serialization library `Marshmallow` to transform complex data models into JSON representations. It includes capabilities to define serializers, validate input data, and handle serialization errors.

<br>

_Database Interaction_: The template guides you on integrating `Flask` with a database using `SQLAlchemy`. It demonstrates how to define models, and perform CRUD operations.

<br>

_Docker-based Setup_: The template includes Docker configuration files, enabling you to set up the project using Docker containers. This approach simplifies the setup process by encapsulating the application, its dependencies, and the database into isolated and reproducible environments.

<br>

_Unit Testing with Data Factories_: The template incorporates the use of data factories to facilitate unit testing. These factories make it easy to generate test data objects with predefined attributes, enabling you to set up test scenarios and verify the functionality of the services.

<br>

_Caching with Cachelib_: The template demonstrates how to implement caching using the cachelib library. By caching API results, you can efficiently retrieve previously computed data without making repeated database queries. This improves performance by reducing the workload on the database and improving response times.

<br>

_Query Control during Unit Testing_: The template also validates query during unit testing by initializing a separate session for the database. This approach ensures that unit tests do not interfere with the production database and provides a clean and controlled environment for testing.

<br>

---

<br>

### installation

- docker
- docker-compose
- bash (optional)

### setup

build the project 
```
$ make start
```

load the database with dummy data provided using 
```bash 
$ make load_db
```

run server locally 
```bash
$ make serve
```


### testing

run the test cases
```bash
$ make test
```
print the test coverage report 
```bash 
$ make test_coverage
```

<br>

### developer notes

- PEP 8 compliance can be validated using `make lint_check` 
- apply PEP 8 rules while making changes using `make lint`
- cache used is `SimpleCache` which is in memory cache store.
- `database` has the functions to manage session like initialize, get and close.
- `serializer` is used to translate the WEB request model to SQLAlchemy Model and vice versa.
- `models` have the definition of tables in database
- `factories` is used to create the model with random data

<br>

### authors
[Varun Singhal](https://linkedin.com/in/varunsinghal15/)
