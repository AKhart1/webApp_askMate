# AskMate API

This is a simple Python Flask project that serves as an API for a question-and-answer platform called AskMate. It provides endpoints to retrieve information about questions, answers, and users from a PostgreSQL database.

## API Endpoints
1.Get All Questions: `GET /questions`
- parameters `order_by` Order the results by specific field
2. Get All Answers: `GET /answers`
- parameters `order_by` Order the results by specific field
3. Get All Users `GET /users`

4. Get a Specific Question: `GET /questions/<id>`

5. Get Answers for a Specific Question: `GET /questions/<id>/answers`


### All responses are in JSON format
## Prerequisites

Before running the project, make sure you have the following prerequisites installed:

- Python 3.x
- Flask
- psycopg2

You can install Flask and psycopg2 using the following commands:

```bash
pip install Flask
pip install psycopg2
```

OR

```bash
pip install -r requirements.txt
````

## How to Run
- Clone Repository
```bash
git clone https://github.com/AKhart1/webApp_askMate.git
cd ask-mate-api
```

- Run the application
```bash
python main.py
```


