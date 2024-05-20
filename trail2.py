# -*- coding: utf-8 -*-
"""
Created on Mon May 20 04:54:35 2024

@author: user
"""




import pickle
import streamlit as st


# Adjust the file paths as needed
diabetes_model_path = 'diabetes_model.sav'
heart_disease_model_path = 'heart_disease_model.sav'
liver_disease_model_path = 'liver_disease_model.sav'
kidney_disease_model_path = 'kidney_disease_model.sav'

# Load the saved models
try:
    diabetes_model = pickle.load(open(diabetes_model_path, 'rb'))
except FileNotFoundError:
    st.error(f"File not found: {diabetes_model_path}")

try:
    heart_disease_model = pickle.load(open(heart_disease_model_path, 'rb'))
except FileNotFoundError:
    st.error(f"File not found: {heart_disease_model_path}")

try:
    liver_disease_model = pickle.load(open(liver_disease_model_path, 'rb'))
except FileNotFoundError:
    st.error(f"File not found: {liver_disease_model_path}")

try:
    kidney_disease_model = pickle.load(open(kidney_disease_model_path, 'rb'))
except FileNotFoundError:
    st.error(f"File not found: {kidney_disease_model_path}")

# Rest of your Streamlit code
def predict_diabetes(data):
    return diabetes_model.predict([data])[0]

def predict_heart_disease(data):
    return heart_disease_model.predict([data])[0]

def predict_liver_disease(data):
    return liver_disease_model.predict([data])[0]

def predict_kidney_disease(data):
    return kidney_disease_model.predict([data])[0]

def validate_user(username, password):
    if username == 'admin' and password == 'password':
        return True
    return False

def load_css():
    css = """
    <style>
    body {
        background-color: #f0f2f6;
    }

    .stApp {
        background: linear-gradient(to right, #00c6ff, #0072ff);
        color: white;
        text-align: center;
        padding-top: 50px;
        height: 100vh;
    }

    h1 {
        color: white;
        font-size: 3em;
        margin-bottom: 20px;
    }

    .stButton button {
        background-color: #0072ff !important;
        color: white !important;
        border: none !important;
        padding: 10px 20px !important;
        font-size: 1.2em !important;
    }

    .stTextInput input {
        border-radius: 5px;
        padding: 10px;
        font-size: 1.1em;
    }
    
    .sidebar .sidebar-content {
        background-color: #0072ff;
        color: white;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def initialize_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'page' not in st.session_state:
        st.session_state.page = 'Home'

def main():
    initialize_session_state()
    load_css()
    
    if st.session_state.logged_in:
        show_menu()
        if st.session_state.page == 'Home':
            show_homepage()
        elif st.session_state.page == 'Diabetes':
            show_diabetes_page()
        elif st.session_state.page == 'Heart Disease':
            show_heart_disease_page()
        elif st.session_state.page == 'Liver Disease':
            show_liver_disease_page()
        elif st.session_state.page == 'Kidney Disease':
            show_kidney_disease_page()
        elif st.session_state.page == 'Info':
            show_info_page()
        elif st.session_state.page == 'Logout':
            logout()
    else:
        show_login()

def show_login():
    st.title("Login Page")
    with st.form("login_form"):
        st.markdown("<h2>Please enter your credentials</h2>", unsafe_allow_html=True)
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            if validate_user(username, password):
                st.session_state.logged_in = True
                st.session_state.page = 'Home'
                st.experimental_rerun()
            else:
                st.error("Invalid username or password")

def show_menu():
    with st.sidebar:
        st.title("Menu")
        if st.button("Home"):
            st.session_state.page = 'Home'
            st.experimental_rerun()
        if st.button("Diabetes"):
            st.session_state.page = 'Diabetes'
            st.experimental_rerun()
        if st.button("Heart Disease"):
            st.session_state.page = 'Heart Disease'
            st.experimental_rerun()
        if st.button("Liver Disease"):
            st.session_state.page = 'Liver Disease'
            st.experimental_rerun()
        if st.button("Kidney Disease"):
            st.session_state.page = 'Kidney Disease'
            st.experimental_rerun()
        if st.button("Info"):
            st.session_state.page = 'Info'
            st.experimental_rerun()
        if st.button("Logout"):
            st.session_state.page = 'Logout'
            st.experimental_rerun()

def show_homepage():
    st.title("Multiple Disease Classification System")
    st.write("Welcome to the Multiple Disease Classification System.")
    st.write("Use the sidebar to navigate to different disease prediction pages or to learn more about the diseases.")

def show_diabetes_page():
    st.title("Diabetes Prediction using ML")
    st.write("Enter the data for diabetes prediction")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        diab_prediction = predict_diabetes(data)
        
        if diab_prediction == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)

def show_heart_disease_page():
    st.title("Heart Disease Prediction using ML")
    st.write("Enter the data for heart disease prediction")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    heart_diagnosis = ''
    
    if st.button('Heart Disease Test Result'):
        data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        heart_prediction = predict_heart_disease(data)
        
        if heart_prediction == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)

def show_liver_disease_page():
    st.title("Liver Disease Prediction using ML")
    st.write("Enter the data for liver disease prediction")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        total_bilirubin = st.text_input('Total Bilirubin')
        
    with col1:
        direct_bilirubin = st.text_input('Direct Bilirubin')
        
    with col2:
        alk_phos = st.text_input('Alkaline Phosphotase')
        
    liver_diagnosis = ''
    
    if st.button('Liver Disease Test Result'):
        data = [age, sex, total_bilirubin, direct_bilirubin, alk_phos]
        liver_prediction = predict_liver_disease(data)
        
        if liver_prediction == 1:
            liver_diagnosis = 'The person has liver disease'
        else:
            liver_diagnosis = 'The person does not have liver disease'
        
    st.success(liver_diagnosis)

def show_kidney_disease_page():
    st.title("Kidney Disease Prediction using ML")
    st.write("Enter the data for kidney disease prediction")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        blood_pressure = st.text_input('Blood Pressure')
        
    with col3:
        specific_gravity = st.text_input('Specific Gravity')
        
    with col1:
        albumin = st.text_input('Albumin')
        
    with col2:
        sugar = st.text_input('Sugar')
        
    with col3:
        red_blood_cells = st.text_input('Red Blood Cells')
        
    with col1:
        pus_cell = st.text_input('Pus Cell')
        
    with col2:
        pus_cell_clumps = st.text_input('Pus Cell Clumps')
        
    with col3:
        bacteria = st.text_input('Bacteria')
        
    with col1:
        blood_glucose_random = st.text_input('Blood Glucose Random')
        
    with col2:
        blood_urea = st.text_input('Blood Urea')
        
    with col3:
        serum_creatinine = st.text_input('Serum Creatinine')
        
    with col1:
        sodium = st.text_input('Sodium')
        
    with col2:
        potassium = st.text_input('Potassium')
        
    with col3:
        hemoglobin = st.text_input('Hemoglobin')
        
    with col1:
        packed_cell_volume = st.text_input('Packed Cell Volume')
        
    with col2:
        white_blood_cell_count = st.text_input('White Blood Cell Count')
        
    with col3:
        red_blood_cell_count = st.text_input('Red Blood Cell Count')
        
    with col1:
        hypertension = st.text_input('Hypertension')
        
    with col2:
        diabetes_mellitus = st.text_input('Diabetes Mellitus')
        
    with col3:
        coronary_artery_disease = st.text_input('Coronary Artery Disease')
        
    with col1:
        appetite = st.text_input('Appetite')
        
    with col2:
        peda_edema = st.text_input('Pedal Edema')
        
    with col3:
        anemia = st.text_input('Anemia')
        
    kidney_diagnosis = ''
    
    if st.button('Kidney Disease Test Result'):
        data = [age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
                blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, hemoglobin, packed_cell_volume,
                white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus, coronary_artery_disease,
                appetite, peda_edema, anemia]
        kidney_prediction = predict_kidney_disease(data)
        
        if kidney_prediction == 1:
            kidney_diagnosis = 'The person has kidney disease'
        else:
            kidney_diagnosis = 'The person does not have kidney disease'
        
    st.success(kidney_diagnosis)

def show_info_page():
    st.title("Information Page")
    st.write("This page provides information about the diseases predicted by this system.")
    st.write("Diabetes: A chronic condition that affects how your body turns food into energy.")
    st.write("Heart Disease: Refers to several types of heart conditions, including coronary artery disease and heart attacks.")
    st.write("Liver Disease: Includes a variety of conditions, such as hepatitis, fatty liver disease, and cirrhosis.")
    st.write("Kidney Disease: Describes various diseases and disorders that affect the function of the kidneys.")

def logout():
    st.session_state.logged_in = False
    st.session_state.page = 'Home'
    st.experimental_rerun()

if __name__ == '__main__':
    main()
