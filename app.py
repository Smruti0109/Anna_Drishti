from flask import Flask,request, render_template, jsonify
import numpy as np
import sklearn
import joblib
# print(sklearn.__version__)
# #loading models

dtr = joblib.load('C:\\Users\\SMRUTI DESHPANDE\\Mini Project Sem 5\\AnnaDrishti\\dtr_joblib.pkl')

preprocessor = joblib.load('C:\\Users\\SMRUTI DESHPANDE\\Mini Project Sem 5\\AnnaDrishti\\preprocessor_joblib.pkl')

#flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('new.html')
@app.route("/predict",methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve and cast the form inputs as float
        State_Name = request.form['State_Name']
        Crop_Type = request.form['Crop_Type']
        Crop = request.form['Crop']
        rainfall = float(request.form['rainfall'])  # Cast to float
        temperature = float(request.form['temperature'])  # Cast to float
        N = float(request.form['N'])  # Cast to float
        P = float(request.form['P'])  # Cast to float
        K = float(request.form['K'])  # Cast to float
        pH = float(request.form['pH'])  # Cast to float
        Area_in_hectare = float(request.form['Area_in_hectare'])  # Cast to float

        # Prepare the features array
        features = np.array([[State_Name, Crop_Type, Crop, rainfall, N, P, K, pH, temperature, Area_in_hectare]])

        # Transform features using the preprocessor
        transformed_features = preprocessor.transform(features)

        # Predict total production (in tons)
        predicted_value = dtr.predict(transformed_features)

        # Calculate yield per hectare
        yield_per_hectare = predicted_value[0] / Area_in_hectare

        # Render the same template with predictions
        return render_template('new.html',
                               predicted_value=predicted_value[0],
                               yield_per_hectare=yield_per_hectare,
                               State_Name=State_Name,
                               Crop_Type=Crop_Type,
                               Crop=Crop,
                               rainfall=rainfall,
                               temperature=temperature,
                               N=N,
                               P=P,
                               K=K,
                               pH=pH,
                               Area_in_hectare=Area_in_hectare
        )
if __name__=="__main__":
    app.run(debug=True, port=5001)