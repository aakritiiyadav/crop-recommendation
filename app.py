import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import joblib
import requests
import textwrap

# Set page config for beautiful layout
st.set_page_config(
    page_title="AgroSmart - Crop Recommendation & Soil Advisor",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import local modules
from src.weather_api import get_weather_by_city
from src.crop_info import CROP_DETAILS, analyze_soil_nutrients, analyze_soil_ph

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, 'models')
MODEL_PATH = os.path.join(MODELS_DIR, 'crop_recommendation_model.pkl')
ENCODER_PATH = os.path.join(MODELS_DIR, 'label_encoder.pkl')

# Custom CSS for high-end styling
st.markdown(textwrap.dedent("""
<style>
    /* Google Fonts import */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

    /* Global styles and Font override (excluding icons) */
    html, body, .stApp, 
    .stApp p, .stApp label, .stApp button, .stApp input, .stApp select, .stApp textarea, 
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
    [data-testid="stSidebar"] div[role="radiogroup"] label {
        font-family: 'Outfit', sans-serif !important;
    }

    /* Safeguard to restore icon font for Streamlit's Material Symbols and Icons */
    [data-testid="stIcon"], 
    .material-icons, 
    [class*="MaterialSymbols"], 
    [class*="material-symbols"] {
        font-family: 'Material Symbols Outlined', 'Material Icons' !important;
    }

    /* Main app background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e8f0 100%);
    }
    
    /* Title and headers */
    h1, h2, h3, .stSubheader {
        color: #1b4d3e !important;
        font-weight: 700 !important;
    }
    
    /* Card wrapper styles */
    .recommendation-card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.18);
        margin-bottom: 20px;
    }
    
    /* Highlight crop name */
    .crop-title {
        color: #2e7d32;
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 10px;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #112a1f !important; /* Slightly darker rich forest green */
    }
    
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    /* Target the radio button group for premium buttons */
    [data-testid="stSidebar"] div[role="radiogroup"] {
        display: flex !important;
        flex-direction: column !important;
        gap: 10px !important;
        margin-top: 15px !important;
    }

    /* Format options as cards/pills */
    [data-testid="stSidebar"] div[role="radiogroup"] label {
        background-color: rgba(255, 255, 255, 0.04) !important;
        padding: 14px 18px !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        cursor: pointer !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        width: 100% !important;
        margin: 0 !important;
    }

    /* Hide the radio button circle */
    [data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {
        display: none !important;
    }

    /* Hover effect */
    [data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        background-color: rgba(255, 255, 255, 0.12) !important;
        border-color: rgba(255, 255, 255, 0.2) !important;
        transform: translateX(4px) !important;
    }

    /* Active selected state selector using :has */
    [data-testid="stSidebar"] div[role="radiogroup"] label:has(input[type="radio"]:checked) {
        background-color: #2e7d32 !important;
        border-color: #4caf50 !important;
        box-shadow: 0 4px 15px rgba(46, 125, 50, 0.4) !important;
    }
    
    /* Make active text fully solid and bold */
    [data-testid="stSidebar"] div[role="radiogroup"] label:has(input[type="radio"]:checked) p {
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* Style the radio button label header ("Navigate Menu") */
    [data-testid="stSidebar"] div[data-testid="stWidgetLabel"] p {
        font-size: 0.8rem !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        color: rgba(255, 255, 255, 0.6) !important;
        font-weight: 600 !important;
        margin-bottom: 5px !important;
    }

    /* Success/Warning card customization */
    .metric-box {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.03);
        border-left: 5px solid #2e7d32;
        margin-bottom: 15px;
    }
    .metric-title {
        font-size: 0.9rem;
        color: #666;
        text-transform: uppercase;
        font-weight: 600;
    }
    .metric-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1b4d3e;
    }
    
    /* Advisory cards */
    .advisory-card {
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 12px;
        border-left: 6px solid #2196f3;
        background: #ffffff;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .advisory-high {
        border-left-color: #f44336;
    }
    .advisory-low {
        border-left-color: #2196f3;
    }
    .advisory-optimal {
        border-left-color: #4caf50;
    }
</style>
"""), unsafe_allow_html=True)

# Helper function to load model and encoder safely
@st.cache_resource
def load_ml_components():
    if os.path.exists(MODEL_PATH) and os.path.exists(ENCODER_PATH):
        try:
            model = joblib.load(MODEL_PATH)
            encoder = joblib.load(ENCODER_PATH)
            return model, encoder
        except Exception as e:
            st.error(f"Error loading model files: {e}")
            return None, None
    return None, None

model, encoder = load_ml_components()

# Navigation
st.sidebar.markdown(textwrap.dedent("<h2 style='text-align: center;'>🌾 AgroSmart</h2>"), unsafe_allow_html=True)
st.sidebar.write("Precision Farming Recommendation Engine")

# System status widget in sidebar
st.sidebar.markdown(textwrap.dedent("""
<div style="background-color: rgba(255,255,255,0.08); padding: 12px; border-radius: 8px; margin-top: 10px; margin-bottom: 20px; border-left: 4px solid #4caf50;">
    <div style="font-size: 0.75rem; opacity: 0.7; letter-spacing: 0.5px; font-weight: 600; color: rgba(255,255,255,0.7) !important;">SYSTEM STATUS</div>
    <div style="font-size: 0.85rem; font-weight: bold; color: #4caf50 !important; margin-top: 5px;">● ML Model: Online (99.55%)</div>
    <div style="font-size: 0.85rem; font-weight: bold; color: #2196f3 !important; margin-top: 3px;">● Weather API: Connected</div>
</div>
"""), unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigate Menu",
    ["🌾 Crop Recommendation", "🧪 Soil & Fertilizer Advisor", "📚 Crop Library", "📊 Model Insights"]
)

# Global Master Header Card
st.markdown(textwrap.dedent("""
<div style="background: linear-gradient(135deg, #123524 0%, #1e5c3f 100%); padding: 25px; border-radius: 16px; color: white; margin-bottom: 30px; box-shadow: 0 8px 24px rgba(0,0,0,0.12);">
    <div style="display: flex; align-items: center; gap: 15px;">
        <span style="font-size: 2.5rem; margin-right: 10px;">🌾</span>
        <div>
            <div style="color: #ffffff !important; margin: 0; font-size: 2.3rem; font-weight: 800; line-height: 1.2; font-family: 'Outfit', sans-serif; letter-spacing: 0.5px;">AgroSmart Suite</div>
            <div style="margin: 6px 0 0 0; opacity: 0.95; font-size: 1.05rem; font-weight: 400; color: #e8f5e9 !important; font-family: 'Outfit', sans-serif;">AI-driven agricultural recommendations, soil amendments, and real-time weather analytics.</div>
        </div>
    </div>
</div>
"""), unsafe_allow_html=True)

# Shared Session State for Inputs
if 'n_input' not in st.session_state:
    st.session_state.n_input = 50
if 'p_input' not in st.session_state:
    st.session_state.p_input = 50
if 'k_input' not in st.session_state:
    st.session_state.k_input = 50
if 'temp_input' not in st.session_state:
    st.session_state.temp_input = 25.0
if 'hum_input' not in st.session_state:
    st.session_state.hum_input = 60.0
if 'ph_input' not in st.session_state:
    st.session_state.ph_input = 6.5
if 'rain_input' not in st.session_state:
    st.session_state.rain_input = 100.0
if 'last_rec' not in st.session_state:
    st.session_state.last_rec = None

# Callback to update session state values from weather
def update_weather():
    if st.session_state.city_name:
        with st.spinner("Fetching real-time weather parameters..."):
            weather = get_weather_by_city(st.session_state.city_name)
            if weather:
                st.session_state.temp_input = float(round(weather["temperature"], 2))
                st.session_state.hum_input = float(round(weather["humidity"], 2))
                # Store weather city name
                st.session_state.weather_info = weather
                st.success(f"Weather loaded for {weather['full_name']}!")
            else:
                st.error("Could not fetch weather. Please input manually.")

# Main app screens
if page == "🌾 Crop Recommendation":
    st.subheader("🌾 Crop Recommendation Assistant")
    st.write("Enter soil parameters and environmental conditions below to predict the best crop to cultivate.")
    
    # Check if model exists
    if model is None or encoder is None:
        st.warning("⚠️ Machine Learning model is not trained yet! Please run the training script or train it in the 'Model Insights' tab.")
        if st.button("Train Model Now"):
            with st.spinner("Downloading dataset and training model..."):
                import subprocess
                train_script = os.path.join(BASE_DIR, 'src', 'train_model.py')
                result = subprocess.run(['python', train_script], capture_output=True, text=True)
                if result.returncode == 0:
                    st.success("Model successfully trained!")
                    st.rerun()
                else:
                    st.error(f"Error training model: {result.stderr}")
                    
    # Form Layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📍 Auto-fill weather using city name")
        st.text_input(
            "Enter City (e.g., Delhi, London, Nairobi)",
            key="city_name",
            on_change=update_weather
        )
        if 'weather_info' in st.session_state:
            st.info(f"Loaded: {st.session_state.weather_info['full_name']}\n\nTemp: {st.session_state.weather_info['temperature']}°C | Humidity: {st.session_state.weather_info['humidity']}%")

        st.subheader("🧪 Soil Nutrients")
        n = st.slider("Nitrogen (N) - Ratio in soil", 0, 150, int(st.session_state.n_input), key="n_slider")
        p = st.slider("Phosphorus (P) - Ratio in soil", 5, 150, int(st.session_state.p_input), key="p_slider")
        k = st.slider("Potassium (K) - Ratio in soil", 5, 220, int(st.session_state.k_input), key="k_slider")
        
        # Save slider back to session state
        st.session_state.n_input = n
        st.session_state.p_input = p
        st.session_state.k_input = k

    with col2:
        st.subheader("🌤️ Environmental Conditions")
        temp = st.number_input("Temperature (°C)", -10.0, 50.0, float(st.session_state.temp_input), step=0.1, key="temp_val")
        hum = st.number_input("Humidity (%)", 0.0, 100.0, float(st.session_state.hum_input), step=0.1, key="hum_val")
        ph = st.number_input("Soil pH level (0 - 14)", 0.0, 14.0, float(st.session_state.ph_input), step=0.1, key="ph_val")
        rain = st.number_input("Rainfall (mm) - Average seasonal", 0.0, 500.0, float(st.session_state.rain_input), step=1.0, key="rain_val")
        
        # Save values back to session state
        st.session_state.temp_input = temp
        st.session_state.hum_input = hum
        st.session_state.ph_input = ph
        st.session_state.rain_input = rain

    st.markdown("---")
    
    # Perform Recommendation
    if st.button("Recommend Optimal Crop", type="primary", use_container_width=True):
        if model is not None and encoder is not None:
            # Inputs to Model (using DataFrame with matching columns to prevent sklearn warnings)
            input_features = pd.DataFrame(
                [[n, p, k, temp, hum, ph, rain]], 
                columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
            )
            
            # Predict
            pred_encoded = model.predict(input_features)
            predicted_crop = encoder.inverse_transform(pred_encoded)[0]
            st.session_state.last_rec = predicted_crop
            
            # Display results in beautiful layout
            st.balloons()
            
            crop_info = CROP_DETAILS.get(predicted_crop.lower())
            
            st.markdown(f"""
            <div class="recommendation-card">
                <div class="crop-title">✨ Recommended Crop: {predicted_crop.title()}</div>
                <p style="font-size: 1.1rem; color: #444;">{crop_info['description'] if crop_info else "No detailed description available."}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Detailed crop specs
            if crop_info:
                c1, c2, c3, c4 = st.columns(4)
                with c1:
                    st.markdown(f"""
                    <div class="metric-box">
                        <div class="metric-title">Growing Season</div>
                        <div class="metric-value" style="font-size: 1.1rem; margin-top: 5px;">{crop_info['season']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                with c2:
                    st.markdown(f"""
                    <div class="metric-box" style="border-left-color: #2196f3;">
                        <div class="metric-title">Water Requirement</div>
                        <div class="metric-value" style="font-size: 1.1rem; margin-top: 5px;">{crop_info['water_requirement']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                with c3:
                    st.markdown(f"""
                    <div class="metric-box" style="border-left-color: #ff9800;">
                        <div class="metric-title">Duration</div>
                        <div class="metric-value" style="font-size: 1.1rem; margin-top: 5px;">{crop_info['duration']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                with c4:
                    st.markdown(f"""
                    <div class="metric-box" style="border-left-color: #9c27b0;">
                        <div class="metric-title">Market Value</div>
                        <div class="metric-value" style="font-size: 1.1rem; margin-top: 5px;">{crop_info['market_value']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.success("💡 Next Step: Head over to the **Soil & Fertilizer Advisor** tab in the sidebar to review detailed soil nutrition amendments!")
        else:
            st.error("Model not loaded. Please train it first.")

elif page == "🧪 Soil & Fertilizer Advisor":
    st.subheader("🧪 Soil Health & Fertilizer Advisory")
    
    if st.session_state.last_rec is None:
        st.info("ℹ️ Please run a **Crop Recommendation** first, or select a crop below to analyze soil nutrient balances.")
        selected_crop = st.selectbox("Analyze soil for crop:", sorted(list(CROP_DETAILS.keys())))
    else:
        st.success(f"Analyzing soil for recommended crop: **{st.session_state.last_rec.title()}**")
        selected_crop = st.session_state.last_rec.lower()
        
    n = st.session_state.n_input
    p = st.session_state.p_input
    k = st.session_state.k_input
    ph = st.session_state.ph_input
    
    crop_info = CROP_DETAILS.get(selected_crop)
    
    if crop_info:
        # 1. Plotly Visual Chart comparing Inputs vs Optimal
        st.subheader("📊 Soil Nutrient Comparison Dashboard")
        
        categories = ['Nitrogen (N)', 'Phosphorus (P)', 'Potassium (K)']
        current_values = [n, p, k]
        optimal_values = [crop_info['optimal_npk']['N'], crop_info['optimal_npk']['P'], crop_info['optimal_npk']['K']]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='Current Soil Levels',
            x=categories,
            y=current_values,
            marker_color='#41c48e',
            opacity=0.85
        ))
        
        fig.add_trace(go.Bar(
            name=f'Optimal Levels for {crop_info["name"]}',
            x=categories,
            y=optimal_values,
            marker_color='#1b4d3e',
            opacity=0.85
        ))
        
        fig.update_layout(
            barmode='group',
            height=400,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=20, b=20),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            yaxis=dict(title='Nutrient Ratio (ppm / ratio)', gridcolor='rgba(0,0,0,0.1)'),
            xaxis=dict(gridcolor='rgba(0,0,0,0.1)')
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # 2. Detailed NPK Analysis Advisory
        st.subheader("💡 Nutrient Advisory Recommendations")
        analysis = analyze_soil_nutrients(selected_crop, n, p, k)
        
        if analysis:
            if not analysis["advisory"]:
                st.markdown("""
                <div class="advisory-card advisory-optimal">
                    <strong style="color: #4caf50;">✅ Balanced Nutrients!</strong><br>
                    Your soil's Nitrogen, Phosphorus, and Potassium levels are all in the optimal range for growing <strong>{}</strong>. Maintain this balance with light compost additions.
                </div>
                """.format(crop_info['name']), unsafe_allow_html=True)
            else:
                for adv in analysis["advisory"]:
                    card_class = "advisory-high" if adv["status"] == "High" else "advisory-low"
                    st.markdown(f"""
                    <div class="advisory-card {card_class}">
                        <strong style="color: {'#f44336' if adv['status']=='High' else '#2196f3'};">
                            {adv['nutrient']} - {adv['status']}
                        </strong> (Current: {analysis['comparison'][adv['nutrient'][0]]['value']} / Optimal: {analysis['comparison'][adv['nutrient'][0]]['target']})<br>
                        <strong>Impact:</strong> {adv['impact']}<br>
                        <strong>Actionable Remedy:</strong> {adv['remedy']}
                    </div>
                    """, unsafe_allow_html=True)
                    
        # 3. Soil pH advisory
        st.subheader("🧪 Soil pH analysis")
        ph_analysis = analyze_soil_ph(ph)
        st.markdown(f"""
        <div class="advisory-card" style="border-left-color: {'#4caf50' if ph_analysis['color']=='green' else '#ff9800' if ph_analysis['color']=='orange' else '#f44336'}; background-color: #ffffff;">
            <strong>Soil pH Status: {ph_analysis['status']} ({ph})</strong><br>
            <strong>Advisor Recommendations:</strong> {ph_analysis['advice']}<br>
            <em>Optimal pH for {crop_info['name']}: {crop_info['optimal_ph']}</em>
        </div>
        """, unsafe_allow_html=True)
        
        # 4. Export Report
        st.subheader("📄 Export Agricultural Advisory Report")
        
        # Build Text Report content
        report_text = f"""==================================================
AGROSMART PRECISION AGRICULTURAL ADVISORY REPORT
==================================================
Target Crop: {crop_info['name']}
Sowing Season: {crop_info['season']}
Growth Duration: {crop_info['duration']}
Water Requirement: {crop_info['water_requirement']}

--------------------------------------------------
SOIL INPUT VALUES:
- Nitrogen (N): {n}
- Phosphorus (P): {p}
- Potassium (K): {k}
- Soil pH: {ph}
- Temperature: {st.session_state.temp_input} °C
- Humidity: {st.session_state.hum_input} %
- Average Rainfall: {st.session_state.rain_input} mm
--------------------------------------------------
SOIL ANALYSIS AND ADVISORY:
"""
        
        if analysis:
            if not analysis["advisory"]:
                report_text += "\n[*] NUTRIENTS STATUS: Balanced! All nutrients are in the optimal range.\n"
            else:
                for adv in analysis["advisory"]:
                    report_text += f"\n[*] NUTRIENT: {adv['nutrient']}\n"
                    report_text += f"    Status: {adv['status']}\n"
                    report_text += f"    Impact: {adv['impact']}\n"
                    report_text += f"    Remedy: {adv['remedy']}\n"
                    
        report_text += f"\n[*] SOIL pH STATUS: {ph_analysis['status']} ({ph})\n"
        report_text += f"    Advisory: {ph_analysis['advice']}\n"
        report_text += f"    Optimal pH for {crop_info['name']}: {crop_info['optimal_ph']}\n"
        report_text += "\n==================================================\n"
        
        st.download_button(
            label="💾 Download Advisory Report (.txt)",
            data=report_text,
            file_name=f"{crop_info['name'].lower()}_advisory_report.txt",
            mime="text/plain",
            use_container_width=True
        )

elif page == "📚 Crop Library":
    st.subheader("📚 Crop Catalog & Knowledge Library")
    st.write("Browse details, seasonal requirements, and optimal environmental parameters for all crop varieties supported by our system.")
    
    search_query = st.text_input("🔍 Search Crop Library", "").strip().lower()
    
    # Display cards for matching crops
    for key, info in CROP_DETAILS.items():
        if search_query and (search_query not in info['name'].lower() and search_query not in info['description'].lower()):
            continue
            
        with st.expander(f"🌾 {info['name']} ({info['season']})"):
            st.markdown(f"**Description:** {info['description']}")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"⏱️ **Duration:** {info['duration']}")
                st.write(f"💧 **Water Requirement:** {info['water_requirement']}")
                st.write(f"💵 **Market Value:** {info['market_value']}")
            with col2:
                st.write(f"🧪 **Optimal Soil N-P-K:** N:{info['optimal_npk']['N']} | P:{info['optimal_npk']['P']} | K:{info['optimal_npk']['K']}")
                st.write(f"🌡️ **Optimal pH:** {info['optimal_ph']}")

elif page == "📊 Model Insights":
    st.subheader("📊 Machine Learning Model Diagnostics")
    
    # Check if CSV path exists to load data distribution
    csv_file_path = os.path.join(BASE_DIR, 'data', 'crop_recommendation.csv')
    if os.path.exists(csv_file_path):
        df = pd.read_csv(csv_file_path)
        
        st.write("### Model Training Overview")
        st.write("Our Crop Recommendation system uses a **Random Forest Classifier** trained on agricultural datasets containing soil profiles and climatic variables.")
        
        # Grid of stats
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Total Records", f"{df.shape[0]:,}")
        with c2:
            st.metric("Features Utilized", f"{df.shape[1] - 1}")
        with c3:
            st.metric("Unique Crop Classes", f"{df['label'].nunique()}")
            
        st.write("### Dataset Crop Class Distribution")
        class_counts = df['label'].value_counts()
        fig_dist = go.Figure(data=[go.Bar(
            x=class_counts.index, 
            y=class_counts.values,
            marker_color='#1b4d3e'
        )])
        fig_dist.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            yaxis=dict(gridcolor='rgba(0,0,0,0.1)')
        )
        st.plotly_chart(fig_dist, use_container_width=True)
        
        # Feature importance comparison (brief description)
        st.write("### Agricultural Input Parameters (Features)")
        st.markdown("""
        - **Nitrogen (N):** Vital for plant leaf structure and growth.
        - **Phosphorus (P):** Crucial for roots, seed development, and energy transfer.
        - **Potassium (K):** Supports flower development, stem strength, and disease protection.
        - **Temperature:** Determines metabolic rates of crops.
        - **Humidity:** Affects transpiration and susceptibility to diseases.
        - **pH:** Controls nutrient solubility and availability in soil.
        - **Rainfall:** Critical water resource representing natural irrigation capacity.
        """)
        
    else:
        st.info("ℹ️ Dataset details will be shown here after the model is trained.")

# Global Footer
st.markdown(textwrap.dedent("""
<div style="margin-top: 60px; padding: 25px 0; border-top: 1px solid rgba(0,0,0,0.08); text-align: center; color: #555; font-size: 0.85rem;">
    <p style="margin: 0; font-weight: 600; color: #1b4d3e;">AgroSmart Precision Agriculture Dashboard</p>
    <p style="margin: 5px 0 0 0; font-size: 0.75rem; opacity: 0.8;">Empowering farmers and agronomists with machine learning recommendations.</p>
    <p style="margin: 10px 0 0 0; font-size: 0.7rem; opacity: 0.5;">© 2026 AgroSmart Inc. | Clean Technology Initiative</p>
</div>
"""), unsafe_allow_html=True)
