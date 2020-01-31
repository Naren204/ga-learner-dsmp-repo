# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here

bank = pd.read_csv(path)

categorical_var = bank.select_dtypes(include = 'object')

print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')

print(numerical_var)


# code ends here


# --------------
# code starts here


#code ends here
banks = bank.drop(['Loan_ID'],axis=1)
print(banks.isnull().sum())

bank_mode = banks.mode
print(bank_mode)
banks.fillna(bank_mode, inplace=True)
print(banks.isnull().sum())


# --------------
# Code starts here

#banks['Gender'].unique()

#avg_loan_amount = banks.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)


avg_loan_amount=pd.pivot_table(banks,values = ['LoanAmount'],index=['Gender', 'Married', 'Self_Employed'],aggfunc =np.mean)

print(avg_loan_amount)
# code ends here



# --------------
# code starts here







loan_approved_se = ((banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')).sum()
#print(loan_approved_se)
loan_approved_nse = ((banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')).sum()
c = banks['Loan_Status'].count()
#print(c)
percentage_se = (loan_approved_se*100)/c
percentage_nse = (loan_approved_nse*100)/c

print(percentage_se,percentage_nse)
banks['Self_Employed'].value_counts()
# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x:x/12)



#banks['Loan_Amount_Term'] = banks['Loan_Amount_Term'].apply(loan_amt)

big_loan_term = loan_term.apply(lambda x:x>=25).sum()
print(big_loan_term)

# code ends here


# --------------
# code starts here



loan_groupby = banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]
#loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()
print(mean_values)
# code ends here


