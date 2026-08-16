import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

# --------------------------------
# 1. Load Dataset
# --------------------------------

data = pd.read_csv("dataset.csv")

X = data.drop("Salary", axis=1)
y = data["Salary"]

# --------------------------------
# 2. Categorical Features
# --------------------------------

categorical_columns = [
    "Education",
    "JobRole",
    "Location"
]

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

# --------------------------------
# 3. AI Model
# --------------------------------

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)

# --------------------------------
# 4. Train Model
# --------------------------------

pipeline.fit(X, y)

print("\n========================================")
print("       AI SALARY PREDICTION SYSTEM")
print("========================================\n")

# --------------------------------
# 5. User Input
# --------------------------------

age = int(input("Enter Age: "))

education = input(
    "Enter Education (Bachelors/Masters): "
)

experience = float(
    input("Enter Years of Experience: ")
)

job_role = input(
    "Enter Job Role: "
)

location = input(
    "Enter Location: "
)

previous_salary = float(
    input("Enter Previous Salary (₹): ")
)

# --------------------------------
# 6. Create User Data
# --------------------------------

user_data = pd.DataFrame({
    "Age": [age],
    "Education": [education],
    "Experience": [experience],
    "JobRole": [job_role],
    "Location": [location],
    "PreviousSalary": [previous_salary]
})

# --------------------------------
# 7. Predict Salary
# --------------------------------

predicted_salary = pipeline.predict(user_data)[0]

# --------------------------------
# 8. Display Result
# --------------------------------

print("\n========================================")
print("          SALARY PREDICTION")
print("========================================")

print(
    f"Predicted Salary: ₹{predicted_salary:,.0f}"
)

print(
    f"Predicted Salary: ₹{predicted_salary / 100000:.2f} LPA"
)

print("========================================")