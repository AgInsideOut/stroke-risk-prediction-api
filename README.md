# Stroke Risk Prediction API

This repository contains the deployment code for the Stroke Risk Prediction model.

## Table of Contents

- [Project Structure](#project-structure)
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing the API](#testing-the-api)
- [Model Information](#model-information)
- [Authors](#authors)
- [License](#license)
- [Dataset License](#dataset-license)
- [Acknowledgments](#acknowledgments)

## Project Structure

```
stroke-risk-prediction-api/
│
├── README.md
├── LICENSE
├── requirements.txt
├── Dockerfile
├── entrypoints.sh
├── .gitignore
├── main.py
├── best_model.joblib
└── test/
    └── test_api.py
```

This structure outlines the main components of the project.

## Introduction

The Stroke Risk Prediction API is a machine learning-based service that predicts the risk of stroke based on various health and lifestyle factors.

By improving the identification of high-risk individuals, especially those in the minority class, this model could have the potential to enhance early intervention strategies for stroke prevention. While the current models show limitations in precision, their improved recall for the minority class could lead to more comprehensive screening processes, potentially reducing the overall incidence and impact of strokes. The project also highlights the challenges in predicting rare events like strokes and provides a foundation for further research in handling imbalanced healthcare datasets.

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

The API is live and can be accessed at:
<https://stroke-risk-prediction-api.onrender.com>

To run the API locally:

1. Ensure you're in the project directory.
2. Run the following command:

    ```bash
    uvicorn main:app --reload
    ```

3. The API will be available at `http://localhost:8000`.

## API Endpoints

Base URL: <https://stroke-risk-prediction-api.onrender.com>

1. **Root Endpoint**
   - URL: `https://stroke-risk-prediction-api.onrender.com/`
   - Method: GET
   - Description: Welcome message for the API.
   - Response: `{"message": "Welcome to the Stroke Prediction API"}`

2. **Prediction Endpoint**
   - URL: `https://stroke-risk-prediction-api.onrender.com/predict`
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

## Testing the API

You can test the live API using curl or any API testing tool. Here's an example using curl:

```bash
curl -X POST "https://stroke-risk-prediction-api.onrender.com/predict" \
     -H "Content-Type: application/json" \
     -d '{
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
```

## Model Information

The model used in this API is an Easy Ensemble Classifier trained to predict stroke risk. This model was chosen for its ability to handle imbalanced datasets and its high recall for the minority class. Here are some key performance metrics:

Precision (Class 1): 0.1135
Recall (Class 1): 0.8641
F1 (Class 1): 0.2008
Balanced Accuracy: 0.7613
F2 Score: 0.3523

Note: These metrics are for the positive class (high risk of stroke). The model's performance should be interpreted in the context of early risk identification, where higher recall is preferred over precision. This model excels at identifying potential stroke cases, which is crucial for early intervention and prevention strategies.

Key points:

1. High Recall: The model correctly identifies 86.41% of actual stroke cases, which is essential for a health screening tool.
2. Balanced Accuracy: The model achieves a balanced accuracy of 76.13%, indicating good overall performance considering both classes.
3. Trade-off: While precision is low, this is acceptable in a medical context where missing a potential stroke case (false negative) is generally considered more costly than a false positive.

This model is particularly suitable for initial screening, where capturing as many potential stroke cases as possible is the primary goal. Follow-up assessments can then be conducted to confirm the risk for individuals flagged by the model.

## Authors

- **Agnieszka Thiel** - *Initial work* - [AgInsideOut](https://github.com/AgInsideOut)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](https://github.com/TuringCollegeSubmissions/athiel-DA.4.1/blob/master/LICENSE) file for details.

## Dataset License

The Stroke Prediction Dataset is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Acknowledgments

- Data Source: [Fedesoriano's Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
- Project Requirements: [Turing College](https://github.com/TuringCollegeSubmissions)
