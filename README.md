# 💰 SalaryPrediction

### 🤖 AI-Based Salary Prediction using Machine Learning

A Machine Learning based web application that predicts an expected salary based on a user's age, education, experience, job role, location, and previous salary.

## 🚀 Features

- 💰 Salary prediction using Machine Learning
- 🌲 Random Forest Regression model
- 🎨 User-friendly Streamlit interface
- 🎓 Education-based prediction
- 💼 Job role-based prediction
- 📍 Location-based prediction
- 📊 Experience and previous salary analysis
- ⚡ Instant prediction results

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

## 📁 Project Structure

```text
SalaryPrediction/
│
├── app.py
├── train_model.py
├── predict.py
├── dataset.csv
├── requirements.txt
└── README.md
```

## 🧠 Machine Learning Model

The project uses a **Random Forest Regression** model to predict salary.

### Input Features

The model uses the following information:

- Age
- Education
- Experience
- Job Role
- Location
- Previous Salary

### Output

The system predicts the expected salary in Indian Rupees (₹) and also displays the approximate salary in LPA.

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/anubhavpandeyedu/SalaryPrediction.git
```

### 2. Open the project folder

```bash
cd SalaryPrediction
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application using:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

Usually, it will be available at:

```text
http://localhost:8501
```

## 📊 Example

The user enters:

- Age: 25
- Education: Bachelors
- Experience: 1 year
- Job Role: Intern
- Location: Delhi
- Previous Salary: ₹3,00,000

The application then predicts the expected salary using the trained Machine Learning model.

## 🎯 Project Objective

The main objective of this project is to demonstrate how Machine Learning can be used to estimate salaries based on professional and educational factors.

This project can be useful for:

- Students
- Freshers
- Job seekers
- Developers
- Data Science learners
- Career planning

## 🔮 Future Improvements

- 📈 Add more real-world salary data
- 🌎 Add more locations and job roles
- 🤖 Try advanced Machine Learning models
- 📊 Add salary comparison charts
- ☁️ Deploy the application online
- 📱 Improve mobile responsiveness
- 📉 Add model performance metrics

## 👨‍💻 Author

**Anubhav Pandey**

GitHub:  
https://github.com/anubhavpandeyedu

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.

---

### Made with ❤️ using Python, Machine Learning & Streamlit
