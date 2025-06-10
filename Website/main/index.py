from flask import Flask, jsonify, request
from flask_cors import CORS
from main.test_prototype import recommend_pipeline

import sys
sys.path.append(
    '/Users/np/Desktop/Capstone_SkipTheDishes/main/test_prototype.py')


app = Flask(__name__)

CORS(app)

incomes = [
    {'description': 'salary', 'amount': 5000}
]

item_list = [
    {'item_list': 'bigMac, biriyani'}
]


@app.route('/items')
def get_incomes():
    return jsonify(item_list)


@app.route('/reccomend', methods=['POST'])
def get_reccomendation():
    item_list = request.get_json()
    reccomendations = recommend_pipeline(item_list)
    print(reccomendations)
    return reccomendations, 200

# date
# items