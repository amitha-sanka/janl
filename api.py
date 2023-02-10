from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

ACTIVITIES = {
    '1': {'activity': 'Seaworld', 'hobby': 'Amusement Park', 'price_range': '$100-$200', 'duration': 'all day'}
}

parser = reqparse.RequestParser()

class ActivitiesList(Resource):
    def get(self):
        return ACTIVITIES

    def post(self):
        parser.add_argument("activity")
        parser.add_argument("hobby")
        parser.add_argument("price_range")
        parser.add_argument("duration")
        args = parser.parse_args()
        
        activity_id = int(max(activity.keys())) + 1
        activity_id = '%i' % activity_id
        activity[activity_id] = {
            "activity": args["activity"],
            "hobby": args["hobby"],
            "price_range": args["price_range"],
            "duration": args["duration"] 
        }

        return ACTIVITIES[activity_id], 201


api.add_resource(ActivitiesList, '/api/')

if __name__ == '__main__': {
    app.run(debug==True)
}