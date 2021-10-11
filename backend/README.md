# Trivia API Documentation
## Introduction

## Getting Started

## Errors

Errors are returned in the following format:
```javascript
{
  "error": 405,
  "message": "Method Not Allowed",
  "success": false
}
```
## Resource Endpoint Library

### GET `/categories`

* General

* Sample URL: 
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

### GET `/categories/{integer}/questions`

* General

* Sample URL
```bash
curl http://127.0.0.1:5000/categories/4/questions
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
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ],
  "success": true,
  "total_questions": 4
}
```

### GET `/questions?page={integer}`

* General
* Sample URL
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
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Tendons",
      "category": 1,
      "difficulty": 4,
      "id": 25,
      "question": "What tissues connect the muscles to the bones?"
    },
    {
      "answer": "Valentina Tereshkova",
      "category": 1,
      "difficulty": 5,
      "id": 32,
      "question": "What is the name of the first woman in space?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    }
  ],
  "success": true,
  "total_questions": 26
}
```

### DELETE `/questions/{integer}`

* General

* Sample URL

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

* General

* Sample URL

```bash
curl -X POST -H 'Content-Type:application/json' -d '{"question":"Which actor has been killed by an Alien, a Terminator and a Predator?", "answer":"Bill Paxton", "category":5, "difficulty":5}' http://127.0.0.1:5000/questions
```

```javascript
{
  "created": 36,
  "success": true
}
```

### POST `/questions/search`

* General

* Sample URL

```bash
curl -X POST -H 'Content-Type:application/json' -d '{"searchTerm":"Terminator"}' http://127.0.0.1:5000/questions/se
arch
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
      "id": 36,
      "question": "Which actor has been killed by an Alien, a Terminator and a Predator?"
    }
  ],
  "success": true,
  "total_questions": 1
}
```
### POST `/quizzes`

* General

* Sample URL

``` bash
 curl -X POST -H 'Content-Type:application/json' -d '{"quiz_category":{"type":"Entertainment","id":5}, "previous_questions":[4,2]}' http://127.0.0.1:5000/quizzes
```

```javascript
{
  "question": {
    "answer": "Bill Paxton",
    "category": 5,
    "difficulty": 5,
    "id": 36,
    "question": "Which actor has been killed by an Alien, a Terminator and a Predator?"
  },
  "quiz_category_id": 5,
  "success": true
}
```
