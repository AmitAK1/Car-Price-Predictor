Used Car Price Prediction Web App
This project contains a web application built with Streamlit that predicts the price of used cars. The prediction is based on a Linear Regression model trained on a dataset of used car information from Quikr.

🚀 Live Demo
You can access the live application here:
https://car-price-predictor-dst2q7rnylbxz63dnb2zsz.streamlit.app/

📝 About The Project
The goal of this project is to provide an easy-to-use interface where users can input details of a car (such as company, model, year of purchase, kilometers driven, and fuel type) and get an estimated resale price.

This repository includes:

A Jupyter Notebook detailing the data cleaning, exploratory data analysis (EDA), and model training process.

A trained Linear Regression model saved as a .pkl file using a Scikit-learn pipeline.

The source code for the Streamlit web application.

✨ Features
Interactive UI: A clean and simple user interface built with Streamlit.

Dynamic Filtering: Car models are dynamically filtered based on the selected company.

Real-time Prediction: Get instant price predictions when you click the button.

Easy to Deploy: Deployed for free on Streamlit Community Cloud.

🛠️ Built With
Python: The core programming language.

Pandas & NumPy: For data manipulation and numerical operations.

Scikit-learn: For building and training the machine learning model.

Streamlit: For creating and serving the web application.

Jupyter Notebook: For the data analysis and model development environment.

⚙️ How to Run the Project Locally
To get a local copy up and running, follow these simple steps.

Prerequisites
You need to have Python and pip installed on your system.

Installation
Clone the repository:

git clone https://github.com/your-username/your-repository-name.git

Navigate to the project directory:

cd your-repository-name

Install the required packages:

pip install -r requirements.txt

(Note: You will need to create a requirements.txt file. It should contain streamlit, pandas, numpy, and scikit-learn)

Running the App
Execute the following command in your terminal:

streamlit run streamlit_app.py

Your browser should automatically open with the app running.

📂 Project Structure
.
├── .gitignore
├── LinearRegressionModel.pkl   # The trained machine learning model
├── README.md                   # This file
├── clean_car.csv               # The cleaned dataset used for prediction
├── requirements.txt            # List of Python dependencies
├── streamlit_app.py            # The main Streamlit application script
└── Project1.ipynb              # Jupyter Notebook for analysis and model training

📈 Data Analysis and Model Training
The Project1.ipynb notebook contains all the steps for data processing and model building.

1. Data Cleaning
The initial dataset from quikr_car.csv consisted of 892 entries and had several quality issues.

Initial dataset shape: (892, 6)

Key cleaning steps performed:

Year: Removed non-numeric entries and converted the column to an integer type.

Price: Removed rows with "Ask For Price", stripped commas from numbers, and converted the column to an integer type.

Kms Driven: Removed "kms" suffix and commas, corrected a data entry error where 'Petrol' was listed as a value, and converted the column to an integer type.

Fuel Type: Removed rows with NaN values.

Name: Standardized the car names by keeping only the first three words to maintain consistency (e.g., "Maruti Suzuki Swift" instead of "Maruti Suzuki Swift Dzire VXi").

Outliers: Removed a significant price outlier (a car listed for over 80 lakhs) to prevent it from skewing the model.

Final dataset shape: After cleaning, the dataset was reduced to 815 rows and reset the index.

2. Model Training & Evaluation
A machine learning pipeline was constructed to streamline the preprocessing and training process.

Preprocessing: A OneHotEncoder was used within a ColumnTransformer to convert categorical features (name, company, fuel_type) into a numerical format suitable for the model.

Model Selection: A Linear Regression model was chosen for this prediction task.

Training Pipeline: make_pipeline from Scikit-learn was used to chain the column transformer and the linear regression model. This ensures that the same transformations are applied consistently to both training and new data.

Finding the Best Model: To ensure robustness, the model was trained and evaluated 1000 times using different train-test splits (by varying the random_state). The split that yielded the highest R² score was selected for the final model.

The model achieved a R-squared score of 0.8457 on the test data, indicating a strong fit for predicting car prices.
