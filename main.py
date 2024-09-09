import os
import sys
import traceback
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Configure logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Load the model
try:
    model_path = 'best_model.joblib'
    if not os.path.exists(model_path):
        logger.error(f"Model file not found: {model_path}")
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    best_model = joblib.load(model_path)
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    logger.error(traceback.format_exc())
    sys.exit(1)

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
    try:
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
        logger.info(f"Prediction made: {prediction[0]}")
        return {"prediction": int(prediction[0])}
    except Exception as e:
        logger.error(f"Error making prediction: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/")
async def root():
    return {"message": "Welcome to the Stroke Prediction API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)