# Anna Drishti
Anna Drishti is a web application built using Flask that predicts crop yield based on various parameters such as rainfall, temperature, soil properties, and crop type. The model utilizes a **Decision Tree Regressor (DTR)** to estimate the total crop production and calculates the yield per hectare.

## Features

- **Crop Yield Prediction**: Predicts the total production of crops based on user inputs.
- **Yield per Hectare**: Calculates the yield per hectare based on the total predicted yield and the area input by the user.
- **Dynamic Form**: Users can input the required parameters such as crop type, soil properties, and weather conditions to get predictions.

## Technologies Used

- **Flask**: For building the web application.
- **Scikit-learn**: For implementing the Decision Tree Regressor model.
- **Joblib**: For saving and loading the trained models.
- **NumPy**: For handling numerical operations and preparing data for prediction.

## Installation

Follow the steps below to set up the project on your local machine:

### 1. Clone the repository

```bash
git clone https://github.com/Smruti0109/Anna_Drishti.git
```
### 2. Install dependencies

```bash
pip install -r requirements.txt
```
### 2. Run the Flask Application

```bash
python app.py
```
## How it Works

- **User Inputs**: Users enter parameters such as crop type, rainfall, temperature, soil conditions (N, P, K, pH), and area (in hectares).
- **Data Preprocessing**: The input features are preprocessed using the `preprocessor_joblib.pkl` model.
- **Prediction**: The preprocessed data is passed through the **Decision Tree Regressor** model (`dtr_joblib.pkl`) to predict the total crop yield.
- **Yield per Hectare**: The app calculates the yield per hectare by dividing the total predicted yield by the area entered by the user.
- **Display Results**: The predicted yield and yield per hectare are displayed on the webpage.

## Acknowledgements

- **Scikit-learn**: For providing the **Decision Tree Regressor** model.
- **Flask**: For building the web framework.
- **Joblib**: For saving and loading machine learning models.
- **NumPy**: For numerical data processing.
