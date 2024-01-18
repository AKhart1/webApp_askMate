import psycopg2
from psycopg2 import extras
import os

def connect_to_db():
    db_params = {
        'dbname': f'{os.environ["dbname"]}',
        'user': f'{os.environ["user"]}',
        'password': f'{os.environ["password"]}',
        'host': f'{os.environ["host"]}',
        'port': f'{os.environ["port"]}'
    }

    try:
        connection = psycopg2.connect(**db_params)
    except psycopg2.DatabaseError as exception:
        print(f"Db connection error")
        raise exception

    connection.autocommit = True
    return connection


def execute_query(query_string, query_parameters=None):
    with connect_to_db() as connection:
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            cursor.execute(query_string, query_parameters)
            result = cursor.fetchall()
    return result
