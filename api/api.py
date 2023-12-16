from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def check_connection():
    return  'Connected'
    # return jsonify({'status': 'success', 'message': 'Database connection is successful'})

