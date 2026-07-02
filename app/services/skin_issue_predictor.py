import os
import numpy as np
import tensorflow as tf

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


# -------------------------------
# Load Model
# -------------------------------

MODEL_PATH = os.path.join(
    "app",
    "models",
    "skin_issue_model.keras"
)

model = load_model(MODEL_PATH)


# -------------------------------
# Class Names
# -------------------------------

CLASS_NAMES = [
    "Redness",
    "dark spots",
    "inflammatory acne",
    "non inflammatory acne black heads",
    "non inflammatory acne white heads",
    "pigmentation",
    "pores",
    "wrinkles"
]


# -------------------------------
# Prediction Function
# -------------------------------

def predict_skin_issue(image_path):

    img = image.load_img(
        image_path,
        target_size=(224, 224)
    )

    img = image.img_to_array(img)

    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)

    predicted_index = np.argmax(prediction)

    confidence = float(np.max(prediction))

    return {
        "skin_issue": CLASS_NAMES[predicted_index],
        "confidence": round(confidence * 100, 2)
    }