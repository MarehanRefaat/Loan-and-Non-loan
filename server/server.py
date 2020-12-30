from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

@app.route('/predict loan or not',methods = ['POST'])
def predict_loan_or_not():
	Gender = request.form['Gender']
	Married = request.form['Married']
	Dependents = request.form['Dependents']
	Education = request.form['Education']
	Self_Employed = request.form['Self_Employed']
	ApplicantIncome = request.form['ApplicantIncome']
	CoapplicantIncome = request.form['CoapplicantIncome']
	LoanAmount = request.form['LoanAmount']
	Loan_Amount_Term = request.form['Loan_Amount_Term']
	Credit_History = request.form['Credit_History']
	Property_Area = request.form['Property_Area']

	response = jsonify({
		'loan_or_not' : util.get_loan(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)
		})
	response.headers.add('Access-Control-Allow-Origin','*')

	return response



if __name__ == '__main__':
    app.run(debug=True)
