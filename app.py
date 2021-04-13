from flask import Flask, request, flash, jsonify

import numpy as np
from PIL import Image
from keras.models import load_model

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def Predict():
    if (request.method == 'GET'):
        return "Menthod unsupported"
    if (request.method == 'POST'):

        # Read the image via file.stream
        file = request.files['image']
        # Read the image via file.stream
        try:
            IMG = Image.open(file.stream).convert("RGB")
        except IOError:
            return "NO file or file is not image file"
        IMG = IMG.resize((128, 128))
        IMG = np.array(IMG)
        IMG = np.true_divide(IMG, 255)
        IMG = IMG.reshape(1, 128, 128, 3)
        classifier = load_model('model_Resnet50_k1.h5')
        # Read the folder test
        predictions = classifier.predict(IMG)
        predicted_classes = np.argmax(predictions, axis=1)
        print(predictions, predicted_classes)
        classes = {
            'TEST': ['Front_Men', 'Above_No', 'Side_Pi',
                     'Front_No', 'Front_Gli', 'Above_Pi',
                     'Above_Men', 'Side_No', 'Front_Pi',
                     'Above_Gli', 'Side_Gli', 'Side_Men']}
        # String name
        predicted_class = classes['TEST'][predicted_classes[0]]
        return predicted_class


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
