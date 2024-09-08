from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

best_model = joblib.load('best_model.joblib')

class InputData(BaseModel):
    age: float
    hypertension: int
    heart_disease: int
    ever_married: int
    avg_glucose_level: float
    bmi: float
    gender_Male: int
    gender_Female: int
    gender_Other: int
    work_type_Govt_job: int
    work_type_Never_worked: int
    work_type_Private: int
    work_type_Self_employed: int
    work_type_children: int
    Residence_type_Rural: int
    Residence_type_Urban: int
    smoking_status_formerly_smoked: int
    smoking_status_smokes: int
    smoking_status_Unknown: int
    smoking_status_never_smoked: int

@app.post("/predict")
async def predict(data: InputData):
    input_data = np.array([[
        data.age, data.hypertension, data.heart_disease, data.ever_married,
        data.avg_glucose_level, data.bmi, data.gender_Male, data.gender_Female,
        data.gender_Other, data.work_type_Govt_job, data.work_type_Never_worked,
        data.work_type_Private, data.work_type_Self_employed, data.work_type_children,
        data.Residence_type_Rural, data.Residence_type_Urban,
        data.smoking_status_formerly_smoked, data.smoking_status_smokes,
        data.smoking_status_Unknown, data.smoking_status_never_smoked
    ]])
    
    prediction = best_model.predict(input_data)
    
    return {"prediction": int(prediction[0])}

@app.get("/")
async def root():
    return {"message": "Welcome to the Stroke Prediction API"}