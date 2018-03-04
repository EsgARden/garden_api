from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

frank = {
    'frank': False
}

class GetFrank(Resource):
    def get(self):
        return {
            'frank' : frank['frank'] #return frank at frank
        }

class PutFrank(Resource):
    def get(self, sfrank):
        frank['frank'] = not frank['frank'] #setting frank at frank to not frank at frank
        return 'frank' #returning frank

api.add_resource(GetFrank, '/')
api.add_resource(PutFrank, '/<string:sfrank>')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
