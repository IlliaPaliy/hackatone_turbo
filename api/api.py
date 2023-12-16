from flask import Flask, jsonify
import api.data_generator
app = Flask(__name__)

@app.route('/', methods=['GET'])
def check_connection():
    return jsonify({'status': 'success', 'message': 'Database connection is successful'})

@app.route('/get-grades')
def get_grades():
    return jsonify({'status': 'success', 'grades': api.data_generator.get_marks()})

@app.route('/get-name')
def get_name():
    return jsonify({'status': 'success', 'name': api.data_generator.get_name()})