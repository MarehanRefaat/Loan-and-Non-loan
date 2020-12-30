import pickle
import json
import numpy as np
import os

__data_columns = None
__model = None
def get_loan(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):

    x = np.zeros(len(__data_columns))
    x[0] = Gender
    x[1] = Married
    x[2] = Dependents
    x[3] = Education
    x[4] = Self_Employed
    x[5] = ApplicantIncome
    x[6] = CoapplicantIncome
    x[7] = LoanAmount
    x[8] = Loan_Amount_Term
    x[9] = Credit_History
    x[10] = Property_Area
   

    return round(__model.predict([x]))


def load_saved_artifacts():
	print("loading saved artificates .....start")
	global __data_columns

	with open ("./artifacts/columns.json",'r') as f:
		__data_columns = json.load(f)['data_columns']


	with open ("./artifacts/classifi_model.pickle",'rb') as f:
		__model = pickle.load(f)

	print("loading saved artifacts......done")




if __name__ == '__main__':
	load_saved_artifacts()
	print(get_loan(0,1,0,1,0,4585,0,115.0,360.0,1.0,2))
		