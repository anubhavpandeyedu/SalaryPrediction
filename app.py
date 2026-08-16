import streamlit as st
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline

# Page settings
st.set_page_config(
    page_title="AI Salary Prediction",
    page_icon="💰",
    layout="centered"
)

# Title
st.title("💰 AI Salary Prediction System")
st.write("Predict your expected salary using Machine Learning.")

# Load dataset
data = pd.read_csv("dataset.csv")

# Features and target
X = data.drop("Salary", axis=1)
y = data["Salary"]

# Categorical columns
categorical_columns = [
    "Education",
    "JobRole",
    "Location"
]

# Preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ],
    remainder="passthrough"
)

# Model
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "regressor",
            RandomForestRegressor(
                n_estimators=100,
                random_state=42
            )
        )
    ]
)

# Train model
model.fit(X, y)

st.divider()

# User inputs
st.subheader("Enter Your Details")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=60,
    value=25
)

education = st.selectbox(
    "Education",
    data["Education"].unique()
)

experience = st.number_input(
    "Experience (Years)",
    min_value=0,
    max_value=40,
    value=1
)

job_role = st.selectbox(
    "Job Role",
    data["JobRole"].unique()
)

location = st.selectbox(
    "Location",
    data["Location"].unique()
)

previous_salary = st.number_input(
    "Previous Salary (₹)",
    min_value=0,
    value=300000,
    step=50000
)

# Prediction
if st.button("🚀 Predict Salary"):

    input_data = pd.DataFrame({
        "Age": [age],
        "Education": [education],
        "Experience": [experience],
        "JobRole": [job_role],
        "Location": [location],
        "PreviousSalary": [previous_salary]
    })

    predicted_salary = model.predict(input_data)[0]

    st.success("Prediction Completed!")

    st.metric(
        "Predicted Salary",
        f"₹{predicted_salary:,.0f}"
    )

    st.info(
        f"Approximately ₹{predicted_salary / 100000:.2f} LPA"
    )