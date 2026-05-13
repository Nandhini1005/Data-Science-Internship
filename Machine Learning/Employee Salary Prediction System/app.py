#Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns

#Dataset
employee_csv="C:\\Users\\hp\\Desktop\\Employee_Salary_Prediction_Project\\employee_salary_dataset.csv"
df=pd.read_csv(employee_csv)

#Label Encoder
gender_encoder=LabelEncoder()
education_encoder=LabelEncoder()
department_encoder=LabelEncoder()

#DataFrame
df['Gender']=gender_encoder.fit_transform(df['Gender'])
df['Education']=education_encoder.fit_transform(df['Education'])
df['Department']=department_encoder.fit_transform(df['Department'])

#Features and Target
X = df.drop(['Employee_ID', 'Salary'], axis=1)
y = df['Salary']

#Standardscaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#Train-Test
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

#Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

st.subheader("Enter Employee Details")

age = st.slider("Age", 21, 60)

Gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

Education = st.selectbox(
    "Education",
    ["Bachelor", "Master", "PhD"]
)

Department = st.selectbox(
    "Department",
    ["HR", "IT", "Sales", "Finance", "Marketing"]
)

experience = st.slider(
    "Experience",
    1,
    20
)

working_hours = st.slider(
    "Working Hours",
    35,
    60
)

performance_score = st.slider(
    "Performance Score",
    50,
    100
)

projects_completed = st.slider(
    "Projects Completed",
    1,
    15
)

#Encode User Input
gender_encoded = gender_encoder.transform([Gender])[0]
education_encoded = education_encoder.transform([Education])[0]
department_encoded = department_encoder.transform([Department])[0]

#Input data
input_data = np.array([[
    age,
    gender_encoded,
    education_encoded,
    department_encoded,
    experience,
    working_hours,
    performance_score,
    projects_completed
]])

#Scale Input Data
input_scaled = scaler.transform(input_data)

#Prediction Button
if st.button("Predict Salary"):

    prediction = model.predict(input_scaled)

    st.success(
        f"Predicted Salary: ₹ {prediction[0]:,.2f}"
    )

#Visualization
st.subheader("Salary Distribution")
fig, ax = plt.subplots(figsize=(8,5))
sns.histplot(
    df['Salary'],
    bins=20,
    kde=True,
    ax=ax
)
plt.title("Salary Distribution")
st.pyplot(fig)

#Experience Vs Salary
st.subheader("Experience vs Salary")
fig2, ax2 = plt.subplots(figsize=(8,5))
sns.scatterplot(
    x='Experience',
    y='Salary',
    data=df,
    ax=ax2
)
plt.title("Experience vs Salary")
st.pyplot(fig2)