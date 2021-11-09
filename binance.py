from flask import Flask, render_template, jsonify
from flask_restful import Resource, Api, reqparse
import ast
import requests as rq

app = Flask(__name__)
api = Api(app)

class Binance(Resource):
     def get(self): 
        url = "https://api.binance.com/api/v3/ticker/price"; 
        test = rq.get(url)
        json = test.json()
        return json;
     
#endpoint
api.add_resource(Binance, '/binance')  


if __name__ == '__main__':
    app.run()  # run our Flask app