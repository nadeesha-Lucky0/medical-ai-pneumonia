import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Pneumonia Detection",
    page_icon="🫁",
    layout="wide"
)

# ---------------- CUSTOM CSS WITH ANIMATIONS ----------------
st.markdown("""
<style>
    /* Import professional font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    /* Global styling */
    * {
        font-family: 'Poppins', sans-serif;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        background-size: 200% 200%;
        animation: gradientShift 15s ease infinite;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    /* Pulse animation */
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }

    /* Fade in animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Slide in from left */
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-50px); }
        to { opacity: 1; transform: translateX(0); }
    }

    /* Slide in from right */
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(50px); }
        to { opacity: 1; transform: translateX(0); }
    }

    /* Glow animation */
    @keyframes glow {
        0%, 100% { box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3); }
        50% { box-shadow: 0 10px 60px rgba(102, 126, 234, 0.6); }
    }

    /* Floating animation */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }

    /* Rotate animation */
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    /* Header Section */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-size: 200% 200%;
        padding: 2.5rem 3rem;
        border-radius: 20px;
        margin-bottom: 2.5rem;
        animation: fadeIn 0.8s ease-out, glow 3s ease-in-out infinite;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .header-title {
        font-size: 2.8rem;
        font-weight: 700;
        color: #ffffff;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        letter-spacing: -0.5px;
        animation: slideInLeft 0.8s ease-out;
    }

    .header-subtitle {
        font-size: 1.05rem;
        color: #f0e6ff;
        margin-top: 0.5rem;
        font-weight: 400;
        letter-spacing: 0.3px;
        animation: slideInLeft 1s ease-out;
    }

    .header-icon {
        font-size: 3.5rem;
        float: right;
        margin-top: -1rem;
        filter: drop-shadow(2px 2px 4px rgba(0, 0, 0, 0.1));
        animation: float 3s ease-in-out infinite;
    }

    .custom-card {
        animation: fadeIn 1s ease-out;
    }

    .card-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #667eea;
        margin-bottom: 1.5rem;
        padding-bottom: 0.8rem;
        border-bottom: 2px solid rgba(102, 126, 234, 0.2);
        animation: slideInRight 0.8s ease-out;
    }

    /* File uploader styling */
    section[data-testid="stFileUploader"] {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        border-radius: 18px;
        padding: 2rem;
        border: 2px dashed #f8b195;
        box-shadow: 0 4px 20px rgba(248, 177, 149, 0.2);
        margin-bottom: 1.5rem;
        transition: all 0.4s ease;
        animation: slideInLeft 1.2s ease-out;
    }

    section[data-testid="stFileUploader"]:hover {
        border-color: #f67280;
        background: linear-gradient(135deg, #ffd6a5 0%, #fdab9f 100%);
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 8px 30px rgba(248, 177, 149, 0.4);
    }

    section[data-testid="stFileUploader"] > label {
        color: #764ba2 !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }

    div[data-testid="stFileUploader"] button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
    }

    div[data-testid="stFileUploader"] button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 25px rgba(102, 126, 234, 0.5);
    }

    /* Instructions box */
    .info-box {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        border-left: 4px solid #667eea;
        border-radius: 12px;
        padding: 1.3rem 1.5rem;
        margin-top: 1.5rem;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.1);
        animation: slideInLeft 1.4s ease-out;
        transition: transform 0.3s ease;
    }

    .info-box:hover {
        transform: translateX(5px);
    }

    .info-box-title {
        font-weight: 600;
        font-size: 1rem;
        margin-bottom: 0.5rem;
        color: #667eea;
    }

    .info-box-text {
        font-size: 0.9rem;
        line-height: 1.7;
        margin: 0;
        color: #4a5568;
    }

    /* Result cards with animations */
    @keyframes scaleIn {
        from { transform: scale(0.8); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }

    .result-card-normal {
        background: linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%);
        border: 2px solid #52c77f;
        border-radius: 18px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 25px rgba(82, 199, 127, 0.3);
        animation: scaleIn 0.6s ease-out;
    }

    .result-card-pneumonia {
        background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
        border: 2px solid #fab1a0;
        border-radius: 18px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 25px rgba(250, 177, 160, 0.3);
        animation: scaleIn 0.6s ease-out, pulse 2s ease-in-out infinite;
    }

    .result-title {
        font-size: 1.7rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .result-title-normal {
        color: #27ae60;
    }

    .result-title-pneumonia {
        color: #e17055;
    }

    .result-confidence {
        font-size: 1.2rem;
        font-weight: 600;
        color: #2d3748;
    }

    .result-icon {
        font-size: 3.5rem;
        float: right;
        margin-top: -0.5rem;
        animation: pulse 2s ease-in-out infinite;
    }

    /* Waiting state with spinning animation */
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    .waiting-box {
        text-align: center;
        padding: 3rem 1rem;
        background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%);
        border-radius: 18px;
        box-shadow: 0 6px 20px rgba(142, 197, 252, 0.3);
        animation: fadeIn 0.8s ease-out;
    }

    .waiting-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        animation: spin 3s linear infinite;
        display: inline-block;
    }

    .waiting-title {
        color: #667eea;
        font-weight: 600;
        font-size: 1.4rem;
        margin-bottom: 0.5rem;
    }

    .waiting-text {
        font-size: 1rem;
        color: #4a5568;
        margin-top: 0.5rem;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        background: white;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.1);
        animation: fadeIn 1.6s ease-out;
    }

    .footer-text {
        color: #718096;
        font-size: 0.95rem;
        line-height: 1.8;
    }

    .footer-highlight {
        color: #667eea;
        font-weight: 600;
    }

    /* Image preview with animation */
    .image-preview {
        border-radius: 15px;
        border: 2px solid rgba(102, 126, 234, 0.2);
        padding: 1rem;
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        margin-top: 1.5rem;
        box-shadow: 0 4px 15px rgba(252, 182, 159, 0.2);
        animation: scaleIn 0.5s ease-out;
        transition: transform 0.3s ease;
    }

    .image-preview:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 25px rgba(252, 182, 159, 0.4);
    }

    /* Override Streamlit defaults */
    .stImage {
        border-radius: 12px;
    }

    /* Alert boxes */
    .stAlert {
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.15);
        animation: slideInRight 0.6s ease-out;
    }

    /* Metrics with animation */
    div[data-testid="stMetricValue"] {
        font-size: 1.5rem;
        color: #667eea;
        font-weight: 700;
        animation: fadeIn 1s ease-out;
    }

    div[data-testid="stMetricLabel"] {
        color: #4a5568;
        font-weight: 500;
    }

    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 2rem 0;
        animation: fadeIn 1.2s ease-out;
    }

    /* Progress bar animation */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #667eea, #764ba2);
    }

    /* Spinner overlay */
    @keyframes fadeInOut {
        0%, 100% { opacity: 0.6; }
        50% { opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)


# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("pneumonia_model.h5")


model = load_model()

# ---------------- HEADER ----------------
st.markdown("""
<div class="header-container">
    <span class="header-icon">🫁</span>
    <h1 class="header-title">Pneumonia Detection System</h1>
    <p class="header-subtitle">
        Advanced AI-powered medical imaging analysis using deep learning and convolutional neural networks
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- MAIN LAYOUT ----------------
col1, col2 = st.columns([1.2, 1], gap="large")

# ---------------- LEFT COLUMN: UPLOAD ----------------
with col1:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="card-title">📤 Upload X-Ray Image</h2>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Drag and drop your chest X-ray image here or click to browse",
        type=["jpg", "jpeg", "png"],
        label_visibility="visible"
    )

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file).convert("RGB")
        st.markdown('<div class="image-preview">', unsafe_allow_html=True)
        st.image(image, caption="✓ Uploaded X-ray Image", use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Information box
    st.markdown("""
    <div class="info-box">
        <div class="info-box-title">ℹ️ Instructions</div>
        <p class="info-box-text">
            • Upload a clear chest X-ray image (PA or AP view)<br>
            • Ensure the image quality is good for accurate prediction<br>
            • The AI model will analyze and provide results instantly<br>
            • Results are for screening purposes only
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- RIGHT COLUMN: RESULTS ----------------
with col2:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="card-title">🔬 Analysis Results</h2>', unsafe_allow_html=True)

    if uploaded_file is None:
        st.markdown("""
        <div class="waiting-box">
            <div class="waiting-icon">⏳</div>
            <h3 class="waiting-title">Waiting for Input</h3>
            <p class="waiting-text">
                Please upload a chest X-ray image to begin the analysis
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # ---------------- IMAGE PREPROCESSING ----------------
        IMG_SIZE = 150
        img = image.resize((IMG_SIZE, IMG_SIZE))
        img = np.array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        # ---------------- PREDICTION WITH PROGRESS ----------------
        progress_bar = st.progress(0)
        status_text = st.empty()

        status_text.text("🔍 Loading image...")
        progress_bar.progress(25)
        time.sleep(0.3)

        status_text.text("🧠 Processing through neural network...")
        progress_bar.progress(50)
        time.sleep(0.3)

        status_text.text("📊 Analyzing patterns...")
        progress_bar.progress(75)

        prediction = model.predict(img)

        status_text.text("✅ Analysis complete!")
        progress_bar.progress(100)
        time.sleep(0.3)

        progress_bar.empty()
        status_text.empty()

        class_index = np.argmax(prediction)
        confidence = prediction[0][class_index]

        if class_index == 1:
            # Pneumonia detected
            st.markdown(f"""
            <div class="result-card-pneumonia">
                <span class="result-icon">⚠️</span>
                <h3 class="result-title result-title-pneumonia">🔴 Pneumonia Detected</h3>
                <p class="result-confidence">Confidence: {confidence * 100:.2f}%</p>
            </div>
            """, unsafe_allow_html=True)

            st.error("""
            **⚠️ Important Notice:**

            The model has detected signs of pneumonia in the X-ray image. 
            This result should NOT be used as a standalone clinical diagnosis.

            **Recommended Actions:**
            - Consult with a qualified radiologist immediately
            - Undergo comprehensive medical examination
            - Follow professional medical advice
            """)

        else:
            # Normal
            st.markdown(f"""
            <div class="result-card-normal">
                <span class="result-icon">✅</span>
                <h3 class="result-title result-title-normal">🟢 Normal X-Ray</h3>
                <p class="result-confidence">Confidence: {confidence * 100:.2f}%</p>
            </div>
            """, unsafe_allow_html=True)

            st.success("""
            **✓ Analysis Complete:**

            The X-ray appears to be normal based on the AI analysis.

            **Please Note:**
            - This is a screening tool, not a diagnostic confirmation
            - Always seek professional medical evaluation
            - Regular check-ups are recommended
            """)

        # Additional metrics
        st.markdown("---")
        st.markdown("### 📊 Prediction Details")

        metrics_col1, metrics_col2 = st.columns(2)
        with metrics_col1:
            st.metric(
                label="Normal Probability",
                value=f"{prediction[0][0] * 100:.1f}%"
            )
        with metrics_col2:
            st.metric(
                label="Pneumonia Probability",
                value=f"{prediction[0][1] * 100:.1f}%"
            )

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    <p class="footer-text">
        <span class="footer-highlight">2nd Year Project</span> • University Research<br>
        Powered by <span class="footer-highlight">Deep Learning (CNN)</span> • 
        TensorFlow • Keras • Streamlit<br>
        <br>
        <em style="font-size: 0.85rem;">
            Disclaimer: This tool is for educational and research purposes only. 
            It should not replace professional medical diagnosis.
        </em>
    </p>
</div>
""", unsafe_allow_html=True)