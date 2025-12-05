https://customer-churn-detection.onrender.com/

 # Customer Churn Detection

## Description

This project is a customer churn prediction system. It uses a machine learning model to predict whether a customer is likely to churn or not. The project includes a web application built with Flask that allows users to get predictions from the model through a simple UI.

## Installation

To run this project, you need to have Python and pip installed.

1.  Clone the repository:
    ```bash
    git clone https://github.com/IshaanAggrawal/Customer-Churn-Detection.git
    cd Customer-Churn-Detection
    ```

2.  Install the dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the web application, run the following command:

```bash
python app.py
```

Then, open your web browser and go to `http://127.0.0.1:5000` to use the application.

## Project Structure

```
.
├── app.py                  # Flask application
├── Churn_modelling.ipynb   # Jupyter notebook with model training code
├── customer_churn_data.csv # Dataset
├── model.pkl               # Trained model
├── scaler.pkl              # Preprocessing scaler
├── requirements.txt        # Project dependencies
├── README.md               # This file
└── templates
    └── index.html          # HTML template for the web app
```


## Model

The churn prediction model is a ... *(I will read `Churn_modelling.ipynb` to fill this)*. The model was trained on the `customer_churn_data.csv` dataset. The notebook `Churn_modelling.ipynb` contains all the details of the data preprocessing, model training, and evaluation.

## Dataset

The dataset used for this project is `customer_churn_data.csv`. It contains information about customers, such as ... *(I will inspect the CSV or the notebook to fill this)*.



