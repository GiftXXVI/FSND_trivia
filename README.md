# Project Documentation

Trivia is an application for running trivia quizzes. It consist of a flask-based backend API and a React based frontend API client.

The motivation behind it's development is to create a simple API and an easy to use, fun frontend application for running quizzes.

### Trivia API Backend

The API is writted according to [pep8 guidelines](http://www.python.org/dev/peps/pep-0008/). 

#### Getting Started

##### Dependencies
Install all dependencies by running the following command from the `./backend` directory:

```bash
pip install aniso8601
pip install click
pip install Flask
pip install Flask-Cors
pip install Flask-RESTful
pip install Flask-SQLAlchemy
pip install itsdangerous
pip install Jinja2
pip install MarkupSafe
pip install psycopg2-binary
pip install pytz
pip install six
pip install SQLAlchemy
pip install Werkzeug
pip install Flask-Migrate
```
##### Databases
The API depends on the presence of a `trivia` postgresql database, properly configured in the `models.py` file.

Unit Tests depend on the presence of a `trivia_test` database, properly configured in the `test_flaskr.py` file.

Both databases (`trivia` and `trivia_test`) can have their schema created and initial data loaded by running the script `trivia.psql` against each database. After running the script, run the migrations to update both databases (`trivia` and `trivia_test`) to the same version level as the application. 

##### Installation
To start the web API; make sure that the database service is running, navigate to the backend directory and run the following commands:
```bash
export DB_NAME={database_name}
export DB_USER={username}
export DB_PASS={password}
export DB_HOST={hostname}
export DB_PORT={port_number}
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
If the database is not running, it can be started using the following command:
```bash
sudo service postgresql start
```
You can then verify that the API is accessible by running the following curl command:
```bash
curl http://127.0.0.1:5000/categories
```
##### Unit Tests
Unit tests have been defined inside the file backend/test_flaskr.py

You should run the tests from the `./backend` directory using the following command to verify that everything has been installed correctly:
```bash
export TEST_NAME={database_name}
export TEST_USER={username}
export TEST_PASS={password}
export TEST_HOST={hostname}
export TEST_PORT={port_number}
python3 test_flaskr.py
```
#### API Reference
>View the API Reference in the [README file within ./backend](./backend/README.md).
#### Deployment
There are no current plans for deployment as this is an academic project.

#### Authors
The started code was provided by Udacity, but there are extensive modifications by Gift Chimphonda.

#### Acknowledgements
The [flask documentation](https://flask.palletsprojects.com/en/2.0.x/) and numerous [StackOverflow](https://stackoverflow.com/) pages have helped me to dig myself out of multiple craters.

### Frontend

The [./frontend](https://github.com/udacity/FSND/blob/master/projects/02_trivia_api/starter/frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. 

>View the [README within ./frontend for more details.](./frontend/README.md)
