from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

Activities = {

}

class Activities(Resource):
    def get(self):
    def post(self):


api.add_resource(ActivitiesList, '/activities/')

if __name__ == '__main__': {
    app.run(debug==True)
}