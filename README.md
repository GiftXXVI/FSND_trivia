# Project Documentation

Trivia is an application for running trivia quizzes. It consist of a flask-based backend API and a React based frontend API client.

The motivation behind it's development is to create a simple API and an easy to use, fun frontend application for running quizzes.

### Trivia API Backend

The API is writted according to [pep8 guidelines](http://www.python.org/dev/peps/pep-0008/). 

#### Getting Started

##### Dependencies
Install all dependencies by running the following command from the `./backend` directory:

```bash
pip install -r requirements.txt
```

The API depends on the presence of a `trivia` postgresql database, properly configured in the `models.py` file.

Unit Tests depend on the presence of a `trivia_test` database, properly configured in the `test_flaskr.py` file.

Both databases can have their schema created and initial data loaded by running the script `trivia.psql` against each database. 

##### Installation
To start the web API; make sure that the database service is running, navigate to the backend directory and run the following commands:
```bash
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
python3 test_flaskr.py
```
#### API Reference
The API Reference is defined in the [README file within ./backend](./backend/README.md).
#### Deployment
There are no current plans for deployment as this is an academic project.

#### Authors
The started code was provided by Udacity, but there are extensive modifications by Gift Chimphonda.

#### Acknowledgements
The flask documentation and numerous StackOverflow pages have helped me to dig myself out of multiple situations.

### Frontend

The [./frontend](https://github.com/udacity/FSND/blob/master/projects/02_trivia_api/starter/frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. 

>View the [README within ./frontend for more details.](./frontend/README.md)
