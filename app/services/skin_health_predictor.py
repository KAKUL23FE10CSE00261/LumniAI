import os
import joblib
import pandas as pd

# ---------------------------------
# Load Trained ML Pipeline
# ---------------------------------

MODEL_PATH = os.path.join(
    "app",
    "models",
    "skin_health_model.joblib"
)

model = joblib.load(MODEL_PATH)


# ---------------------------------
# Prediction Function
# ---------------------------------

def predict_skin_health(data):

    """
    data should be a dictionary like:

    {
        "Age":22,
        "Gender":"Female",
        "Hydration_Level":"Medium",
        "Oil_Level":"High",
        "Sensitivity":"Low",
        "Humidity":65.5,
        "Temperature":30,
        "Skin_Type":"Oily",
        "Sleep_Hours":7,
        "Water_Intake_L":2.5,
        "Exercise":"Moderate",
        "Stress_Level":"Medium",
        "Diet":"Balanced",
        "Smoking":"No",
        "Alcohol":"Never"
    }

    """

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    prediction = round(float(prediction), 2)

    return prediction