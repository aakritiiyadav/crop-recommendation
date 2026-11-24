# Crop Recommendation System & Soil Advisor (AgroSmart)

A modern, machine learning-powered precision agriculture application. It recommends the optimal crop to cultivate based on soil nutrient composition, soil pH, and environmental factors. Additionally, it offers real-time weather integration, fertilizer advisory systems, soil health analytics, and downloadable PDF/text reports.

---

## Features

1. **🌾 Crop Recommendation**:
   - Recommends the best crop from 22 options based on Nitrogen (N), Phosphorus (P), Potassium (K), Soil pH, Temperature, Humidity, and Rainfall.
   - Built using a highly accurate **Random Forest Classifier** model.
   
2. **⛅ Real-Time Weather Integration**:
   - Interfaced with the keyless, free **Open-Meteo API**.
   - Input a city name, and the application will fetch the current temperature and relative humidity to auto-fill the form inputs.

3. **🧪 Soil Health & Fertilizer Advisor**:
   - Visualizes your soil N-P-K levels against the target crop's optimal ranges using **Plotly**.
   - Analyzes soil pH (acidic, neutral, alkaline) and provides chemical/organic soil amendment advice.
   - Recommends corrective soil inputs (e.g. Urea, Bone meal, Potash, Lime, or Sulfur) to optimize crop growth.

4. **📚 Crop Knowledge Library**:
   - Searchable and expandable database of the 22 supported crops, detailing their growth duration, water requirements, seasonal profile, and market value.

5. **📄 Advisory Report Export**:
   - Generates a text summary containing inputs, recommended crop details, and detailed fertilizer advice, downloadable directly from the app.

---

## Directory Structure

```
crop-recommendation-system/
├── data/
│   └── crop_recommendation.csv (Downloaded automatically on training)
├── models/
│   ├── crop_recommendation_model.pkl (Serialized ML model)
│   └── label_encoder.pkl (Serialized label encoder)
├── src/
│   ├── __init__.py
│   ├── train_model.py (Training and evaluation script)
│   ├── weather_api.py (Weather API interaction helper)
│   └── crop_info.py (Crop details and advisory logic)
├── app.py (Streamlit main application)
├── requirements.txt (Dependencies)
└── README.md (This file)
```

---

## Setup & Installation

1. **Clone or Navigate to Project Directory**:
   ```bash
   cd D:\crop-recommendation-system
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the ML Model**:
   Run the model training script to download the dataset and train the Classifier:
   ```bash
   python src/train_model.py
   ```
   *(Alternatively, you can click "Train Model Now" inside the Streamlit web dashboard if you haven't run it yet)*.

4. **Run the Streamlit Dashboard**:
   ```bash
   streamlit run app.py
   ```
   Open the browser URL provided in the terminal output (usually `http://localhost:8501`).

   #testing github contribution

---

## Target Crops Supported
Rice, Maize, Chickpea, Kidney Beans, Pigeon Peas, Moth Beans, Mung Bean, Black Gram, Lentil, Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut, Cotton, Jute, Coffee.
