from flask import Flask, redirect, url_for, request, render_template, jsonify, make_response
from pymongo import MongoClient
from entities.container import container
from models.record import record
from models.template import template
import json

app = Flask(__name__)

client = MongoClient( 'mongodb', 27017)

storage = container()
storage.set('db', client.subscriptions)

model = record(storage)

@app.route('/')
def default():
    return jsonify({'Contact': 'Andrei'})


# get matrix
@app.route('/load/<string:instrument>/<string:number1>/<string:number2>', methods=['GET','POST','PUT'])
def generate_matrix(instrument, number1, number2):
    code = 200
    m = template(1,2)
    matrix = {"matrix": m.generate(), "tag": "latest"}
    # record = {'matrix': matrix, 'range' : dict(request.headers)}
    model.save(instrument, matrix)
    return jsonify({instrument: 'OK', 'saved': 'link'}), code


# get matrixes
@app.route('/matrix', methods=['GET'])
@app.route('/matrix/', methods=['GET'])
def get_all():
    output = model.list_buckets()
    return jsonify(output)

# get matrix
@app.route('/matrix/<string:sub_id>', methods=['POST','PUT'])
def new_item(sub_id='default'):
    code = 200
    args = request.args
    if ('code' in args and 'prob' in args):
        try:
            code = int(args['code'])
            prob =  int(args['prob'])
        except:
            prob = 0
            return jsonify({'result' : 'Error ' + str(code) + ' probability %' + str(prob) }), code

    record_merged = {'event': request.json, 'headers' : dict(request.headers)}
    model.save(sub_id, record_merged)
    return jsonify({'result': 'OK'}), code

@app.route('/matrix/<string:sub_id>', methods=['GET'])
@app.route('/matrix/<string:sub_id>/', methods=['GET'])
def webhook_content(sub_id):
    output = model.bucket_list(sub_id)
    if output is None:
        return jsonify({'result' : 'not found'}), 404
    return jsonify(output)

@app.route('/matrix/<string:sub_id>', methods=['DELETE'])
def webhook_delete(sub_id):
    output = model.collection_delete(sub_id)
    if output is None:
        return jsonify({'result' : 'not found'}), 404
    return jsonify({'Webhook [' + sub_id + '] dropped ': output})


# Webhook items
@app.route('/matrix/<string:sub_id>/<string:id>', methods=['GET'])
def find_service(sub_id, id):
    item = model.get_by_id(sub_id, id)
    if item is None:
        return jsonify({'result' : 'not found'}), 404
    return jsonify(item)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
