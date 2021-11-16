from flask import Flask, jsonify, request
import sys
sys.path.append('controllers')
sys.path.append('models')
import government
import countries_con
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/update/', methods=['POST'])
@app.route('/update/<ids>', methods=['POST'])
def upd(ids=None):
    data = request.get_json()
    country = countries_con.Country_con()
    results = country.updash(ids, data)
    return jsonify(results)

@app.route('/add/', methods=['POST'])
def add():
    data = request.get_json()
    country = countries_con.Country_con()
    results = country.ins(data)
    return jsonify(results)

@app.route('/del/', methods=['GET', 'POST'])
@app.route('/del/<ids>')
def rmv(ids=None): 
    i = countries_con.Country_con()
    results = i.remove(ids)
    return jsonify(results)

@app.route('/show/', methods=['GET'])
@app.route('/show/<ids>')
def show(ids=None):
    i = countries_con.Country_con()
    results = i.select(ids)
    return jsonify(results)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
