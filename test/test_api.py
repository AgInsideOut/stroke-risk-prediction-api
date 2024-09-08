import requests

url = "https://your-render-url.onrender.com/predict"
data = {
    "age": 65.0,
    "hypertension": 1,
    "heart_disease": 0,
    "ever_married": 1,
    "avg_glucose_level": 100.0,
    "bmi": 28.5,
    "gender_Male": 1,
    "gender_Female": 0,
    "gender_Other": 0,
    "work_type_Govt_job": 0,
    "work_type_Never_worked": 0,
    "work_type_Private": 1,
    "work_type_Self_employed": 0,
    "work_type_children": 0,
    "Residence_type_Rural": 0,
    "Residence_type_Urban": 1,
    "smoking_status_formerly_smoked": 1,
    "smoking_status_smokes": 0,
    "smoking_status_Unknown": 0,
    "smoking_status_never_smoked": 0
}

response = requests.post(url, json=data)
print(response.json())