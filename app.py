import streamlit as st
import numpy as np
import joblib
st.set_page_config(
    page_title="AI Smart Irrigation",
    page_icon="🌱",
    layout="wide"
)
model = joblib.load("Farm_Irrigation_System.pkl")
st.markdown(
    """
    <h1 style='text-align:center; color:#27AE60;'>
    🌱 AI Powered Smart Irrigation System
    </h1>

    <h4 style='text-align:center; color:gray;'>
    Smart Farming using Machine Learning & IoT Sensors data
    </h4>

    <hr>
    """,
    unsafe_allow_html=True
)
st.sidebar.title("📡Sensor Dashboard")

st.sidebar.write(
    "Adjust sensor values"
)
sensor_values = []
for i in range(20):
    value = st.sidebar.slider(
        f"🌡 Sensor {i}",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01
    )
    sensor_values.append(value)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        "Total Sensors",
        "20 📡"
    )
with col2:
    avg_value = np.mean(sensor_values)
    st.metric(
        "Average Moisture",
        f"{avg_value:.2f}"
    )
with col3:
    st.metric(
        "AI Model",
        "Active"
    )
st.progress(avg_value)
st.markdown("---")
st.subheader("Sprinkler Prediction")
if st.button("Predict Irrigation Status"):
    input_array = np.array(
        sensor_values
    ).reshape(1,-1)
    prediction = model.predict(
        input_array
    )[0]
    st.success(
        "AI Prediction Completed Successfully!"
    )
    on_count = 0
    off_count = 0
    for i,status in enumerate(prediction):
        if status == 1:
            on_count += 1
            st.markdown(
                f"""
                <div style="
                background-color:#D5F5E3;
                padding:15px;
                border-radius:15px;
                margin:10px;
                color:#145A32;
                font-size:18px;">
                💧 <b>Sprinkler {i}</b>
                (Parcel {i}) : ON
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            off_count += 1
            st.markdown(
                f"""
                <div style="
                background-color:#FADBD8;
                padding:15px;
                border-radius:15px;
                margin:10px;
                color:#922B21;
                font-size:18px;">
                🌾 <b>Sprinkler {i}</b>
                (Parcel {i}) : OFF
                </div>
                """,
                unsafe_allow_html=True
            )
    c1,c2 = st.columns(2)
    with c1:
        st.metric(
            "💧 Active Sprinklers",
            on_count
        )
    with c2:
        st.metric(
            "🌾 Inactive Sprinklers",
            off_count
        )
st.markdown("---")
st.info(
"""
About Project

This AI-Based Smart Irrigation System uses
sensor data and Machine Learning to predict
whether irrigation is required or not.

Technologies:

🐍 Python  
🤖 Machine Learning  
🌐 Streamlit  
📡 IoT Sensors data
"""
)


st.markdown(
"""
<center>
Made by Aman for Smart Agriculture
</center>
""",
unsafe_allow_html=True
)
            
            
