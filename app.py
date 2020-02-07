import os
from flask import Flask, Response
import rdflib

app = Flask(__name__)

@app.route('/')
def modelById():
    g=rdflib.Graph()
    g.parse('model/model-catalog.ttl', format='turtle')
    return Response(g.serialize(format='turtle', encoding='utf8'), mimetype='text/turtle')

@app.route('/ready', methods=['GET'])
def isReady():
    return "OK"

@app.route('/ping', methods=['GET'])
def isAlive():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
