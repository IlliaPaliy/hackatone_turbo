from flask import Flask, jsonify
from flask_cors import CORS
import api.data_generator
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def check_connection():
    return jsonify({'status': 'success', 'message': 'Database connection is successful'})

@app.route('/get-grades')
def get_grades():
    return jsonify({'status': 'success', 'grades': api.data_generator.get_marks()})
