import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv("dataset.csv")

print("Dataset loaded successfully!")
print("Total records:", len(data))

# Features and target
X = data.drop("Salary", axis=1)
y = data["Salary"]

# Categorical columns
categorical_columns = [
    "Education",
    "JobRole",
    "Location"
]

# Preprocessing
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

# AI/ML model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

# Complete ML pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
pipeline.fit(X_train, y_train)

# Test model
predictions = pipeline.predict(X_test)

# Performance
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n========== MODEL PERFORMANCE ==========")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))

print("\nModel trained successfully!")