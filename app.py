import pandas as pd
import pickle as pk
import streamlit as st

# ✅ Load the trained model
model = pk.load(open(r'C:\Users\lalit\OneDrive\Desktop\Data Science\HousePricePrediction\House_prediction_model.pkl', 'rb'))

# ✅ Load the cleaned dataset
data = pd.read_csv(r'C:\Users\lalit\OneDrive\Desktop\Data Science\HousePricePrediction\Cleaned_data.csv')

# ✅ App header
st.header('🏠 Pune House Price Predictor')

# ✅ User inputs
loc = st.selectbox('Choose the Location', sorted(data['site_location'].unique()))
sqft = st.number_input('Enter Total Sqft', min_value=200.0, max_value=20000.0, step=10.0)
beds = st.number_input('Enter No. of Bedrooms', min_value=1, max_value=10, step=1)
bath = st.number_input('Enter No. of Bathrooms', min_value=1, max_value=10, step=1)
balc = st.number_input('Enter No. of Balconies', min_value=0, max_value=5, step=1)

# ✅ Prepare input DataFrame
input_data = pd.DataFrame([[sqft, bath, balc, loc, beds]],
                           columns=['total_sqft', 'bath', 'balcony', 'site_location', 'bedrooms'])

# ✅ Predict Button
if st.button('Predict Price'):
    output = model.predict(input_data)
    price = round(output[0] * 100000, 2)  # converting to INR
    st.success(f'💰 Estimated House Price: ₹ {price:,.2f}')
