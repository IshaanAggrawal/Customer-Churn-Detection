from flask import Flask, request, render_template
import joblib
import numpy as np

# Load scaler + model
scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect inputs
        age = int(request.form["Age"])
        tenure = int(request.form["Tenure"])
        monthly_charges = float(request.form["MonthlyCharges"])
        total_charges = float(request.form["TotalCharges"])

        # Gender (binary encoded: Female=0, Male=1)
        gender = 1 if request.form["Gender"] == "Male" else 0

        # Contract Type (one-hot: One-Year, Two-Year; baseline = Month-to-Month)
        contract_type = request.form["ContractType"]
        contract_one_year = 1 if contract_type == "One-Year" else 0
        contract_two_year = 1 if contract_type == "Two-Year" else 0

        # Internet Service (one-hot: Fiber Optic, baseline = DSL/None)
        internet_service = request.form["InternetService"]
        internet_fiber = 1 if internet_service == "Fiber Optic" else 0

        # TechSupport (binary: Yes=1, No=0)
        tech_support = 1 if request.form["TechSupport"] == "Yes" else 0

        # Assemble features in the exact same order as training
        features = np.array([[age, gender, tenure, monthly_charges, total_charges,
                              contract_one_year, contract_two_year,
                              internet_fiber, tech_support]])

        # Scale numeric
        features_scaled = scaler.transform(features)

        # Predict
        prediction = model.predict(features_scaled)[0]

        result = "❌ Customer is likely to CHURN" if prediction == 1 else "✅ Customer will STAY"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
