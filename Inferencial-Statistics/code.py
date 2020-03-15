# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings
from statistics import stdev

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]

#Code starts here
data = pd.read_csv(path)

data_sample = data.sample(n=sample_size,random_state=0)

sample_mean = round(data_sample['installment'].mean(),2)
sample_std = round(stdev(data_sample['installment']),2)
margin_of_error =round(z_critical*sample_std/math.sqrt(sample_size),2)
confidence_interval = (sample_mean-margin_of_error, sample_mean+margin_of_error)

true_mean = round(data['installment'].mean(),2)
if true_mean>=sample_mean-margin_of_error and true_mean<=sample_mean+margin_of_error+1:
#if true_mean in range(sample_mean-margin_of_error, sample_mean+margin_of_error+1):
    print(true_mean)







# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
fig, axes = plt.subplots(3,1)

for i in range(len(sample_size)):
    m=[]
    for j in range(1000):
        x= data.sample(n=sample_size[i])['installment'].mean()
        m.append(x)
    mean_series= pd.Series(m)
    plt.subplot(3,1,i+1)
    plt.hist(mean_series)



    


# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
data['int.rate']=data['int.rate'].apply(lambda x:x.split('%')[0]).astype('float')/100
data['int.rate'] = data['int.rate'].apply(lambda x:round(x,4))
z_statistic ,p_value = ztest(x1=data[data['purpose']=='small_business']['int.rate'],value = data['int.rate'].mean(),alternative='larger')

print(z_statistic) 
print(p_value)
# print the results
if p_value<0.05:
    inference = "Reject"
else:
    inference = "Accept"


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
z_statistic ,p_value = ztest(x1=data[data['paid.back.loan']=='No']['installment'],x2= data[data['paid.back.loan']=='Yes']['installment'])

print(z_statistic) 
print(p_value)
# print the results
if p_value<0.05:
    inference = "Reject"
else:
    inference = "Accept"


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = pd.Series(data[data['paid.back.loan']=='Yes']['purpose'].value_counts())
no = pd.Series(data[data['paid.back.loan']=='No']['purpose'].value_counts())

observed = pd.concat([yes.transpose(),no.transpose()],axis=1,keys= ['Yes','No'])

chi2, p, dof, ex = chi2_contingency(observed)

if chi2>critical_value:
    inference = "Reject"
else:
    inference = "Accept"


