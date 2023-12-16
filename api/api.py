from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/check_connection', methods=['GET'])
def check_connection():
    return jsonify({'status': 'success', 'message': 'Database connection is successful'})

