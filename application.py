import streamlit as st
import pickle
import pandas as pd
import numpy as np

# --- 1. Load Data and Model ---
# The loading process remains the same as your Flask app.
try:
    model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
    car = pd.read_csv('clean_car.csv')
except FileNotFoundError:
    st.error("Error: 'LinearRegressionModel.pkl' or 'clean_car.csv' not found.")
    st.info("Please make sure the model and data files are in the same directory as your script.")
    st.stop() # Stop the app from running further if files are not found.


# --- 2. Build The User Interface with Streamlit ---

# Set the title of the web app
st.title("🚗 Car Price Prediction")
st.markdown("Enter the details of the car to get an estimated price.")

# Get unique values for the dropdowns from the dataframe
companies = sorted(car['company'].unique())
years = sorted(car['year'].unique(), reverse=True)
fuel_types = car['fuel_type'].unique()

# Create columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    # Company selection
    # st.selectbox creates a dropdown menu.
    # The first argument is the label, the second is the list of options.
    selected_company = st.selectbox("Select Company", companies)

    # Year selection
    selected_year = st.selectbox("Select Year of Purchase", years)

with col2:
    # Car model selection (dynamically updated based on company)
    # We filter the models based on the selected company for a better user experience.
    filtered_models = sorted(car[car['company'] == selected_company]['name'].unique())
    selected_model = st.selectbox("Select Model", filtered_models)

    # Fuel type selection
    selected_fuel_type = st.selectbox("Select Fuel Type", fuel_types)

# Kilometer input
# st.number_input creates a field for numerical entry.
kms_driven = st.number_input("Enter Kilometers Driven", min_value=0, step=1000)


# --- 3. Prediction Logic ---

# st.button creates a button. The code inside the 'if' block runs when the button is clicked.
if st.button("Predict Price"):
    # Create a pandas DataFrame from the user's inputs
    # This is the same logic as in your Flask app's 'predict' function.
    input_data = pd.DataFrame(
        [[selected_model, selected_company, selected_year, kms_driven, selected_fuel_type]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    )

    try:
        # Use the loaded model to make a prediction
        prediction = model.predict(input_data)

        # Display the prediction
        # st.success is a great way to show a positive result.
        st.success(f"**Predicted Price:** ₹ {np.round(prediction[0], 2):,}")

    except Exception as e:
        # st.error is used to display error messages.
        st.error(f"An error occurred during prediction: {e}")

# --- Optional: Add some instructions or info ---
st.markdown("---")
st.write("This app predicts the price of a used car based on its make, model, year, and mileage.")

