'''
Author : hupeng
Time : 2021/8/26 15:00 
Description: 
'''
from flask import Flask, Blueprint
from fairy import BaseService
from fairy.utils import responser

app = Flask(__name__)

from flask_restful import Api
from flask_restful import Resource

bp = Blueprint('bp', __name__)
api = Api(bp)


class server(BaseService):
    def get_response(self, response):
        response.code = 0
        response.message = 'success'
        response.data = {'res': [1, 2, 3]}
        return response


class test(Resource):
    def get(self):
        response = server().make_response()
        return responser(response=response)


api.add_resource(test, '/test')

app.register_blueprint(bp)

if __name__ == '__main__':
    BaseService.init(cfg={}, app=app)
    app.run()
