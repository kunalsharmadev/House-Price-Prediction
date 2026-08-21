import pandas as pd
import streamlit as st
import joblib

model = joblib.load('house_price_model.jb')

st.title('House Price Prediction')
st.write('Enter the details of the house to predict its price.')

inputs = ['OverallQual', 'GrLivArea', 'GarageArea', '1stFlrSF',
       'FullBath', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'Fireplaces',
       'BsmtFinSF1', 'LotFrontage', 'WoodDeckSF', 'OpenPorchSF', 'LotArea',
       'CentralAir']

input_data ={}

for features in inputs:
    if features == 'CentralAir':
        input_data[features]= st.selectbox(f"{features}", options=['Yes', 'No'], index=0)
    else:
        input_data[features] = st.number_input(
            f"{features}",
            value=0.0,
            step=1.0 if features in ['OverallQual', 'FullBath', 'Fireplaces',] else 0.1
        )

if st.button("Predict Price"):
    input_data['CentralAir'] = 1 if input_data['CentralAir'] == 'Yes' else 0

    input_df = pd.DataFrame([input_data], columns = inputs)

    prediction = model.predict(input_df)
    st.success(f"The predicted house price is: ${prediction[0]:,.2f}")
