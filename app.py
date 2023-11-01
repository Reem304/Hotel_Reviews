import streamlit as st
import pandas as pd
from models.dummies import *
import joblib



scaler = joblib.load('models/scaler.h5')
model = joblib.load('models/SVC_model.h5')


st.title('Global Hotel Reviews')
st.info('Just buiding a model')


year = st.number_input('year', min_value=2012)

Country_sel= st.selectbox('Country', ['Mexico',  'Switzerland', 'France'])
Country=Country_dummies[Country_sel]

if Country_sel == 'Mexico':
    
    City_sel=st.selectbox("City",['Cancun'])
    
    
    Hotel_name_sel= st.selectbox('Hotel_name', ['InterContinental Presidente','Grand Fiesta Americana'])
    
    
elif Country_sel == 'Switzerland':
    
    City_sel=st.selectbox("City",['Geneva'])
    
    Hotel_name_sel= st.selectbox('Hotel_name', ['Warwick Geneva'])
    
    
elif Country_sel == 'France':
    City_sel=st.selectbox("City",['Cannes','Monaco','Nice'])
    
    Hotel_name_sel= st.selectbox('Hotel_name', ['barriere-le-majestic','Fairmont Monte Carlo','Hyatt Regency Palais'])           
    
City=City_dummies[City_sel] 
Hotel_name=hotels_dummies[Hotel_name_sel]


data= year
data=[]
data.append(year)
data.extend(Country)
data.extend(City)
data.extend(Hotel_name)


result = model.predict([data])


st.write(result)
st.success(f'Predicted Rating: {result[0]:.2f}')
