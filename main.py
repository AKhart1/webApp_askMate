import flask
from flask import request

from database import *

app = flask.Flask(__name__)


@app.route("/questions", methods=['GET'])
def get_questions():
    order_by = request.args.get('order_by', 'id')
    query = f'SELECT * FROM questions ORDER BY {order_by};'
    res = execute_query(query, order_by)
    return flask.jsonify(res)


@app.route('/answers', methods=['GET'])
def list_answers():
    order_by = request.args.get('order_by', 'id')
    query = f"SELECT * FROM answers ORDER BY {order_by};"
    res = execute_query(query, order_by)
    return flask.jsonify(res)


@app.route('/users', methods=['GET'])
def list_users():
    query = "SELECT * FROM users;"
    res = execute_query(query)
    return flask.jsonify(res)


@app.route('/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    query = f"SELECT * FROM questions WHERE id = {question_id};"
    res = execute_query(query)
    return flask.jsonify(res)

@app.route('/questions/<int:question_id>/answers', methods=['GET'])
def list_answers_for_question(question_id):
    query = f"SELECT * FROM answers WHERE question_id = {question_id};"
    res = execute_query(query)
    return flask.jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)
