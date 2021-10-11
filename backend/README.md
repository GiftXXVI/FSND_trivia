# Trivia API Documentation

## Introduction

The Trivia API forms the backend of the Trivia App. It connects client applications to the database and allows the client applications to communicate with the database using a set of simple, standards compliant HTTP methods.

## Getting Started

- Base URL: the API can be accessed at the following URL `http://127.0.0.1:5000/`

- Authentication: the API does not yet support any authentication methods or API keys.

## Errors

Errors are returned in the following format:

the returned json object has an `error` value reflecting the HTTP status code of the error, a `message` reflecting the HTTP status code message and a `success` value of `false` indicating that the operation was not successful.

```javascript
{
  "error": 405,
  "message": "Method Not Allowed",
  "success": false
}
```

In the event of an error, the API may return one of the following HTTP status codes and messages:

- 404: Not Found
- 422: Unprocessable Entity
- 400: Bad Request
- 405: Method Not Allowed
- 500: Internal Server Error

## Resource Endpoint Library

### GET `/categories`

#### General
This endpoint is used to retrieve a list of categories. 
##### Request Body
The endpoint responds with an empty request body.

##### Response Body

The endpoint responds with a `id`:`type` list called `categories` and a `success` value of `true` indicating that the operation was a success.

#### Sample URL:

```bash
curl http://127.0.0.1:5000/categories
```

```javascript
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```

### POST `/categories`

#### General
This endpoint is used to create a new category.
##### Request Body
The endpoint expects a json object with a `type` string representing the `type` attribute of the new category. 
##### Response Body
The endpoint responds with a json object with a `success` value of `true` indicating that the operation was a success and a `created` value reflecting the id of the category that has been created.
### Sample URL:
```bash
curl -X POST -H 'Content-Type:application/json' -d '{"type":"Languages"}' http://127.0.0.1:5000/categories
```
```javascript
{
  "created": 7,
  "success": true
}
```

### GET `/categories/{integer}/questions?page={integer}`

#### General

This endpoint is used to retrieve a list of questions under a specified category. 

It has an optional `page` URL parameter which can be used to specify the page number.

##### Request Body
The endpoint expects and empty request body.

##### Response Body

The endpoint responds with the complete list of available categories `categories`, the current page size `curr_page_size`, the current category `current_category`, the total number of available pages `num_pages`, the current page number `page_num`, the set of questions `questions`, whether the retrival operation was successful `success` and the total number of questions available under the category `total_questions`.

#### Sample URL and Response

```bash
curl http://127.0.0.1:5000/categories/4/questions?page=1
```

```javascript
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "curr_page_size": 4,
  "current_category": "History",
  "num_pages": 1,
  "page_num": 1,
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
      "rating": 1
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?",
      "rating": 1
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?",
      "rating": 1
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?",
      "rating": 1
    }
  ],
  "success": true,
  "total_questions": 4
}
```

### GET `/questions?page={integer}`

#### General
This endpoint is used to retrieve a list of questions of all categories. 

Like `/categories/{integer}/questions` above, it also has an optional `page` URL parameter which can be used to specify the page number.

##### Request Body
The endpoint expects and empty request body.

##### Response Body
Just like `/categories/{integer}/questions`, the endpoint responds with the complete list of available categories `categories`, the current page size `curr_page_size`, the current category `current_category`, the total number of available pages `num_pages`, the current page number `page_num`, the set of questions `questions`, a `success` value of `true` indicating that the operation was a success and the total number of questions available under the category `total_questions`.

#### Sample URL and Response

```bash
 curl http://127.0.0.1:5000/questions?page=1
```

```javascript
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "curr_page_size": 10,
  "current_category": "Geography",
  "num_pages": 3,
  "page_num": 1,
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?",
      "rating": 1
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?",
      "rating": 1
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?",
      "rating": 1
    },
    {
      "answer": "Tendons",
      "category": 1,
      "difficulty": 4,
      "id": 25,
      "question": "What tissues connect the muscles to the bones?",
      "rating": 1
    },
    {
      "answer": "Valentina Tereshkova",
      "category": 1,
      "difficulty": 5,
      "id": 32,
      "question": "What is the name of the first woman in space?",
      "rating": 1
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?",
      "rating": 1
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?",
      "rating": 1
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?",
      "rating": 1
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?",
      "rating": 1
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?",
      "rating": 1
    }
  ],
  "success": true,
  "total_questions": 27
}
```

### DELETE `/questions/{integer}`

#### General
This endpoint is used to delete a specified question. 
##### Request Body
The endpoint expects an empty request body.

##### Response Body
The endpoint returns the `id` of the deleted item and a `success` value of `true` indicating that the operation was a success. 

#### Sample URL and Response

```bash
curl -X DELETE http://127.0.0.1:5000/questions/33
```

```javascript
{
  "deleted": 33,
  "success": true
}
```

### POST `/questions`

#### General
This endpoint is used to create a new question. 

##### Request Body
The request is expected to contain a json object with the following attributes:

* `question`: the question statement as a string
* `answer`: the answer statement as a string
* `category`: the valid id of one of the categories defined in the database as an integer
* `difficulty`: the difficulty level of the question as an integer value between 1 and 5

##### Response Body
The endpoint responds with a json object with a `success` value of `true` indicating that the operation was a success and a `created` value reflecting the id of the question that has been created.
#### Sample URL

```bash
curl -X POST -H 'Content-Type:application/json' -d '{"question":"What is the name of the world’s largest ocean?", "answer":"Pacific", "category":5, "difficulty":5, "rating": 1}' http://127.0.0.1:5000/questions
```

```javascript
{
  "created": 38,
  "success": true
}
```

### POST `/questions/search?page={integer}`

#### General
This endpoint is used to search for a question by providing a string that matches part of the question statement. 

##### Request Body
The request is expected to contain a `searchTerm` string to compare against questions in the database and return matching results. There is also an optional `page` parameter to enable paging of the returned results just like in `/questions` and `/categories/{integer}/questions`.

##### Response Body
Just like `/questions/` and `/categories/{integer}/questions`, the endpoint responds with the complete list of available categories `categories`, the current page size `curr_page_size`, the current category `current_category`, the total number of available pages `num_pages`, the current page number `page_num`, the set of questions `questions`, a `success` value of `true` indicating that the operation was a success and the total number of questions available under the category `total_questions`.

#### Sample URL

```bash
curl -X POST -H 'Content-Type:application/json' -d '{"searchTerm":"Terminator"}' http://127.0.0.1:5000/questions/search
```

```javascript
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "curr_page_size": 1,
  "current_category": "Entertainment",
  "num_pages": 1,
  "page_num": 1,
  "questions": [
    {
      "answer": "Bill Paxton",
      "category": 5,
      "difficulty": 5,
      "id": 37,
      "question": "Which actor has been killed by an Alien, a Terminator and a Predator?",
      "rating": 1
    }
  ],
  "success": true,
  "total_questions": 1
}
```

### POST `/quizzes`

#### General
This endpoint is used to run a quiz by maintaining a state object consisting of the category and a set of previous questions. 

##### Request Body
The endpoint expects a json request body consisting of a `quiz_category` object with a string `type` and an integer `id` where `id` is a valid category id. 

##### Response Body
The endpoint responds with a question object, a `quiz_category_id` and a `success` value of `true` indicating that the operation was successful.

#### Sample URL

```bash
 curl -X POST -H 'Content-Type:application/json' -d '{"quiz_category":{"type":"Entertainment","id":5}, "previous_questions":[4,2]}' http://127.0.0.1:5000/quizzes
```

```javascript
{
  "question": {
    "answer": "Edward Scissorhands",
    "category": 5,
    "difficulty": 3,
    "id": 6,
    "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
    "rating": 1
  },
  "quiz_category_id": 5,
  "success": true
}
```
