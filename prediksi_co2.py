import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

model = pickle.load(open('Prediksi_co2.sav', 'rb'))

dataset = pd.read_excel('CO2 dataset.xlsx')
dataset['Year'] = pd.to_datetime(dataset['Year'], format = '%Y')
dataset.set_index(['Year'], inplace=True)

st.title('Forecasting Kualitas Udara')
year = st.slider("Tentukan Tahun",1,30, step=1)

pred = model.forecast(year)
pred = pd.DataFrame(pred, columns=['CO2'])

if st.button("Predict") :

    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig,ax = plt.subplots()
        dataset['CO2'].plot(style='--', color='blue', legend=True, label='known')
        pred['CO2'].plot(color='green', legend=True, label = 'Prediction')
        st.pyplot(fig)
        
