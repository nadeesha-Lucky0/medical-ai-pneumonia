# Pneumonia Detection AI Model

This project is a Streamlit web application that uses a trained Convolutional Neural Network (CNN) to detect pneumonia from chest X-ray images.

## Features
- Upload chest X-ray images (JPG, JPEG, PNG).
- Real-time prediction (Normal vs. Pneumonia).
- Interactive web dashboard.

## How to Setup and Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nadeesha-Lucky0/medical-ai-pneumonia.git
   cd medical-ai-pneumonia
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```
   If `streamlit` is not in your system PATH, use:
   ```bash
   python -m streamlit run app.py
   ```

4. **Access the app:**
   Open [http://localhost:8501](http://localhost:8501) in your browser.

## Project Structure
- `app.py`: The main Streamlit web application file.
- `requirements.txt`: Python package requirements.
- `pneumonia_model.h5`: The pre-trained Keras model.
- `index.html`: Project landing page.
- `assets/`: Web interface styles and scripts.
