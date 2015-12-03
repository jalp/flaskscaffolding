import requests
from flask import Flask, request
from flask.ext.restful import Api, Resource
from elasticsearch import Elasticsearch
from config import configure_app

DEFAULT_INDEX = 'tags'
DOC_TYPE = 'ad'

app = Flask(__name__, instance_relative_config=False)
configure_app(app)

api = Api(app)

DEFAULT_HOST = app.config.get('DEFAULT_HOST')
DEFAULT_PORT = app.config.get('DEFAULT_PORT')


def conn(host, port):
    es = '{}:{}'.format(host, port)
    return Elasticsearch([es])


ES = conn(DEFAULT_HOST, DEFAULT_PORT)


class Tags(Resource):
    def get(self):
        res = {'result': 'There are no tags'}
        q = request.args.get('q', None)
        if q:
            res['result'] = q
            return res, 200
        else:
            return res, 200

    def post(self):
        pass


class Status(Resource):
    def get(self):
        response = requests.get('http://{}:{}/_cat/health?h=st'.format(DEFAULT_HOST, DEFAULT_PORT))
        if response.status_code == 200:
            return {'result': 'We have access to ES'}, 200
        else:
            return '', 500

    def post(self):
        return 'Not yet implemented', 200

    def put(self):
        return 'Not yet implemented', 200

    def delete(self):
        return 'Not yet implemented', 200


api.add_resource(Tags, '/tags', endpoint='tags')
api.add_resource(Status, '/status', endpoint='status')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
