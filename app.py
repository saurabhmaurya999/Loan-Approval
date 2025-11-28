import pandas as pd
import streamlit as st
import pickle as pk

model = pk.load(open('model.pkl','rb'))

st.header('LOAN PREDICTION APP')

No_of_dependents = st.slider('Choose no_of_dependents',0,5)
Education = st.selectbox('Choose Education',['Graduated','Not Graduated'])
Self_Employed = st.selectbox('Self employed?',['Yes','No'])
Annual__Income = st.slider('Choose Annual Income',0,10000000)
Loan_Amount = st.slider('Choose Loan Amount',0,10000000)
Loan_duration = st.slider('Choose Loan duration',0,20)
Cibil_Score = st.slider('Choose Cibil Score',0,1000)
Asset = st.slider('Choose Asset',0,10000000)


# def education(edu):
#     if edu == 'Garaduated':
#         return 1
#     return 0



if(Education == 'Graduated'):
    educ = 1
else:
    educ = 0

if(Self_Employed == 'Yes'):
    emp = 1
else:
    emp = 0

if(st.button("Predict")):
    pred_data = pd.DataFrame([[No_of_dependents,educ,emp,Annual__Income,Loan_Amount,Loan_duration,Cibil_Score,Asset]],
        columns=['no_of_dependents','education','self_employed','income_annum','loan_amount','loan_term','cibil_score','Asset'])
    
    predict = model.predict(pred_data)
    if(predict[0] == 1):
        st.success("🎉 Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    
