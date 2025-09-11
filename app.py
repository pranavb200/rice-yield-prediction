from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open("model/rice_yield_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        input_data = np.array([
            data['Crop_Year'],
            data['Area'],
            data['Annual_Rainfall'],
            data['Fertilizer'],
            data['Pesticide'],
            data['Temperature']
        ]).reshape(1, -1)

        prediction = model.predict(input_data)[0]
        return jsonify({'Predicted_Yield': round(prediction, 2)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
