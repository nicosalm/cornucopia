# Flask API to serve the model

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from model import CropPricePredictor

app = Flask(__name__)
api = Api(app)


class Predict(Resource):
    def post(self):
        # get the data from the POST request
        data = request.get_json()
        date = data['date']
        crop = data['crop']
        crop = int(crop)

        predictor = CropPricePredictor()
        predicted_price = predictor.predict(date, crop)

        # run the model and make a prediction
        # predicted_price = CropPricePredictor.predict(date, crop)

        # return jsonify({'predicted_price': predicted_price})


# add the Predict resource to the API under the route /predict
api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run(debug=True)
