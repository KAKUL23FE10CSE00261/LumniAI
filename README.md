# Skin Care AI 🌿

AI-powered skin analysis system built with Flask, MongoDB, and OpenCV.

## Features
- 📸 **Photo Upload Analysis** — real computer-vision skin analysis (oiliness, redness, dark spots, texture, dryness)
- 📝 **Profile-Based Routine** — fill your skin profile for tailored skincare plans
- 🤖 **Personalised Dashboard** — skin scores, lifestyle impact, daily routine
- 🥗 **Diet & Product Recommendations** — matched to your detected skin type
- 🔐 **Secure Auth** — bcrypt-hashed passwords, session management

## Quick Start

### 1 — Install MongoDB
Download from https://www.mongodb.com/try/download/community  
Start MongoDB: `mongod --dbpath /data/db`

### 2 — Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3 — Run the app
```bash
python app.py
```
Open http://127.0.0.1:5000

## Project Structure
```
skin_care_ai/
├── app.py                      ← Flask app (all routes)
├── requirements.txt
├── ml/
│   ├── skin_analyzer.py        ← OpenCV CV analysis
│   └── routine_generator.py    ← Routine, product, diet logic
├── static/
│   ├── css/
│   │   ├── style.css           ← Home & shared styles
│   │   ├── auth.css            ← Login / Signup
│   │   ├── update_profile.css  ← Profile form
│   │   └── dashboard.css       ← Dashboard
│   └── uploads/                ← Saved skin photos
└── templates/
    ├── home.html
    ├── login.html / signup.html
    ├── userpage.html
    ├── update_profile.html
    ├── upload.html             ← Photo upload + instant CV results
    ├── loading.html            ← Animated loading screen
    └── dashboard.html          ← Full results dashboard
```

## How CV Analysis Works
The `skin_analyzer.py` module uses OpenCV to:
1. Build a **skin-tone mask** (HSV range) to isolate the face
2. Detect **oiliness** via specular highlights (V-channel brightness)
3. Measure **redness** via LAB A* channel
4. Find **dark spots** by detecting dark blobs on the skin
5. Calculate **texture roughness** with Laplacian variance
6. Estimate **dryness** from brightness + texture
7. Combine into a **skin type decision** and clarity score

## Environment Variable
```bash
MONGO_URI=mongodb://localhost:27017/   # default
SECRET_KEY=your-secret-key
```
