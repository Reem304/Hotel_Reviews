import streamlit as st
import pandas as pd
from models.dummies import *
import joblib
from sklearn.model_selection import train_test_split


scaler = joblib.load('models/scaler.h5')
model = joblib.load('models/SVC_model.h5')


st.title('Global Hotel Reviews')
st.info('Just buiding a model')


year = st.number_input('year', min_value=2011)

Hotel_name_sel= st.selectbox('Hotel_name', [ 'barriere-le-majestic','InterContinental Presidente','Fairmont Monte Carlo','Warwick Geneva','Grand Fiesta Americana','Hyatt Regency Palais'])
Hotel_name=hotels_dummies[Hotel_name_sel]

City_sel=st.selectbox("City",['Cannes','Geneva','Monaco','Nice','Cancun'])
City=City_dummies[City_sel]

Country_sel= st.selectbox('Country', ['Mexico',  'Switzerland', 'France'])
Country=Country_dummies[Country_sel]

st.write(year)

data= year
data=[]
data.append(year)
data.extend(Hotel_name)
data.extend(City)
data.extend(Country)


st.write(data)

result = model.predict([data])


st.write(result)
st.success(f'Predicted Rating: {result[0]:.2f}')




