from app import app
from flask import Flask, jsonify

tasks = [
    {
        'id': 1,
        'title': 'Data4All',
        'description': 'EC2', 
        'done': False
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
