# Stroke Risk Prediction API

This repository contains the deployment code for the Stroke Risk Prediction model.

## Table of Contents

- [Project Structure](#project-structure)
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Model Information](#model-information)
- [Authors](#authors)
- [License](#license)
- [Dataset License](#dataset-license)
- [Acknowledgments](#acknowledgments)

## Project Structure

    ```bash
    stroke-risk-prediction-api/
    │
    ├── README.md
    ├── LICENSE
    ├── requirements.txt
    ├── Dockerfile
    ├── .gitignore
    ├── main.py
    ├── best_model.joblib
    └── tests/
        └── test_api.py
    ```

This structure outlines the main components of the project.

## Introduction

The Stroke Risk Prediction API is a machine learning-based service that predicts the risk of stroke based on various health and lifestyle factors.

### Dataset

The project utilizes the [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) from Kaggle.

## Installation

These instructions will get you a copy of the project up and running on your local machine.

1. Clone the repository:

    ```bash
    git clone https://github.com/AgInsideOut/stroke-risk-prediction-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd stroke-risk-prediction-api
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the API locally:

1. Ensure you're in the project directory.
2. Run the following command:

    ```bash
    uvicorn main:app --reload
    ```

3. The API will be available at `http://localhost:8000`.

## API Endpoints

1. **Root Endpoint**
   - URL: `/`
   - Method: GET
   - Description: Welcome message for the API.
   - Response: `{"message": "Welcome to the Stroke Prediction API"}`

2. **Prediction Endpoint**
   - URL: `/predict`
   - Method: POST
   - Description: Predicts stroke risk based on input features.
   - Request Body: JSON object with the following fields:

     ```json
     {
       "age": float,
       "hypertension": int,
       "heart_disease": int,
       "ever_married": int,
       "avg_glucose_level": float,
       "bmi": float,
       "gender_Male": int,
       "gender_Female": int,
       "gender_Other": int,
       "work_type_Govt_job": int,
       "work_type_Never_worked": int,
       "work_type_Private": int,
       "work_type_Self_employed": int,
       "work_type_children": int,
       "Residence_type_Rural": int,
       "Residence_type_Urban": int,
       "smoking_status_formerly_smoked": int,
       "smoking_status_smokes": int,
       "smoking_status_Unknown": int,
       "smoking_status_never_smoked": int
     }
     ```

   - Response: `{"prediction": int}` (0 for low risk, 1 for high risk)

## Model Information

The model used in this API is a machine learning classifier trained to predict stroke risk. Here are some key performance metrics:

- Precision (Class 1): 0.180723
- Recall (Class 1): 0.3
- F1 (Class 1): 0.225564
- F0.5 Score: 0.227273
- F1 Score: 0.225564
- F2 Score: 0.321782
- Prediction Balance (Class 1): 0.081213
- Optimal Threshold (F1): 0.10101

Note: These metrics are for the positive class (high risk of stroke). The model's performance should be interpreted in the context of early risk identification, where higher recall might be preferred over precision.

## Authors

- **Agnieszka Thiel** - *Initial work* - [AgInsideOut](https://github.com/AgInsideOut)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](https://github.com/TuringCollegeSubmissions/athiel-DA.4.1/blob/master/LICENSE) file for details.

## Dataset License

The Stroke Prediction Dataset is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Acknowledgments

- Data Source: [Fedesoriano's Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
- Project Requirements: [Turing College](https://github.com/TuringCollegeSubmissions)
