from flask import Flask, request, jsonify
from flask_cors import CORS
from get_prediction import get_prediction
from ImageConversion import Image

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/upload_image", methods=['POST'])
def lesion():
    """

    :return: the predicted classification of the lesion (benign or malignant)
    """
    image = request.json['fileData']
    the below line is for testing outside the docker container only
    predictions = image
    lesion_image = Image(input_image=image)
    (labels, predictions) = get_prediction(lesion_image.bin_from_64())
    return jsonify(predictions)