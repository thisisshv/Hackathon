from flask import Flask, request, render_template
import pickle

with open("d:\Code\Projects\Hackathon\Hackathon\server\Hackathon_Model.pkl", "rb") as file:
    model = pickle.load(file)


app = Flask(__name__)


@app.route('/', methods=["GET"])
def root():
    return render_template('index.html')


@app.route('/predict', methods=["POST"])
def predict_value():
    print(request.form)
    CURRENT_BAL = float(request.form.get("CURRENT_BAL"))
    Loan_Tenure = float(request.form.get("Loan_Tenure"))
    disbursal_cost = float(request.form.get("disbursal_cost"))
    EMI_disbursal = float(request.form.get("EMI_disbursal"))
    EMI_income = float(request.form.get("EMI_income"))
    predictions = model.predict([[CURRENT_BAL, Loan_Tenure, disbursal_cost, EMI_disbursal, EMI_income]])
    return f"<h1>Prediction: {'Customer will exit' if predictions[0] == 0 else 'Customer will not exit'}</h1>"


app.run(host="0.0.0.0", port=8000, debug=True)