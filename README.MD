# 🏠 House Price Predictor

This project is a machine learning model that predicts house prices in **Bangalore, India**. The model is built from scratch and deployed as a **Streamlit web application**.

---

## 🚀 Project Workflow

The project follows these steps:

1. **Data Collection**  
   House price data for various areas in Bangalore is collected.

2. **Data Analysis and Pre-processing**  
   The dataset is cleaned and prepared for modeling, which includes:  
   - Dropping irrelevant columns  
   - Handling null values  
   - Cleaning and balancing location data  
   - Extracting numerical data from columns  
   - Handling outliers  

3. **Data Splitting**  
   The dataset is split into **80% training** and **20% testing** sets.

4. **Model Creation**  
   A **Linear Regression model** is created.

5. **Model Training**  
   The model is trained using the training data.

6. **Model Evaluation**  
   The model's performance is evaluated using the test data.

7. **Prediction and Testing**  
   The trained model predicts house prices based on user input.

8. **Deployment**  
   The model is deployed as an interactive **Streamlit web application**.

---

## 💻 Technologies Used

- **NumPy**: For numerical operations  
- **Pandas**: For data manipulation and analysis  
- **Scikit-learn (sklearn)**:
  - `OneHotEncoder`: For converting categorical data  
  - `StandardScaler`: For scaling numerical data  
  - `train_test_split`: For splitting the dataset  
  - `LinearRegression`: For building the predictive model  
  - `Pipeline` and `make_pipeline`: For creating a workflow  
  - `make_column_transformer`: For applying transformations  
- **Jupyter Lab**: For coding and analysis  
- **Pickle**: For exporting and importing the trained model  
- **Streamlit**: For creating the web application interface  
- **Visual Studio Code**: For web app development  

---

## 💿 Installation

To run this project, install Python and the required libraries using:

```bash
pip install numpy pandas scikit-learn streamlit
