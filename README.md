# backend-engineer-task

## Project Dependencies

- docker
- docker-compose
- bash (optional)

## Setup

- build the project `make start`
- load the database with dump data provided using `make load_db`
- check the coverage 

## Task Requirements

- implement handlers for routes in app.routes.index
- use the provided postgres database
- - use psycopg2 or an ORM for database queries
- test handlers and aim for maximum test coverage
- implement caching where appropriate

## Remarks

- you can test using `test.sh` or your preferred method
- you're not limited to the packages in the `requirements.txt`, install what you think is appropriate
- if you wish to use an ORM besides psycopg2 you're welcome to, but will have to set up the models yourself

## Notes

- run the test cases using `make test` command
- print the test coverage report using `make test_coverage`
- PEP 8 compliance can be validated using `make lint_check` 
- apply PEP 8 rules while making changes using `make lint`
- cache used is `SimpleCache` which is in memory cache store.
- `commons` have the following modules:
    - `database` has the functions to manage session like initialize, get and close.
    - `serializer` is used to translate the WEB request model to SQLAlchemy Model and vice versa.
    - `models` have the definition of tables in database
    - `factories` is used to create the model with random data
