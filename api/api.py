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
        ACTIVITIES[activity_id] = {
            "activity": args["activity"],
            "hobby": args["hobby"],
            "price_range": args["price_range"],
            "duration": args["duration"] 
        }

        return ACTIVITIES[activity_id], 200


class Activities(Resource):
    def get(self, activity_id):
        if activity_id not in ACTIVITIES:
            return 'Not Found', 404
        else: 
            return ACTIVITIES[activity_id]

    def put(self, activity_id):
        parser.add_argument("activity")
        parser.add_argument("hobby")
        parser.add_argument("price_range")
        parser.add_argument("duration")
        args = parser.parse_args()

        if activity_id not in ACTIVITIES:
            return 'Record Not Found', 404
        else: 
            activity = ACTIVITIES[activity_id]
            activity["activity"] = args["activity"] if args["activity"] is not None else activity ["activity"]
            activity["hobby"] = args["hobby"] if args["hobby"] is not None else activity ["hobby"]
            activity["price_range"] = args["price_range"] if args["price_range"] is not None else activity ["price_range"]
            activity["duration"] = args["duration"] if args["duration"] is not None else activity ["duration"]
            return activity, 200


    def delete(self, activity_id):
        if activity_id not in ACTIVITIES:
            return 'Not Found', 404
        else: 
            del ACTIVITIES[activity_id]
            return '', 204

    api.add_resource(ActivitiesList, '/api/')
    api.add_resource(Activity, '/api/<activity_id>')

if __name__ == '__main__': {
    app.run(debug==True)
}