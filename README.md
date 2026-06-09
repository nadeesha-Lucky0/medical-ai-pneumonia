# 🫁 Pneumonia Detection Using Deep Learning & Streamlit

A deep learning project to detect pneumonia from chest X-ray images using an optimized Convolutional Neural Network (CNN) deployed as an interactive web application.

---

## 📘 **Project Overview**

Pneumonia is a leading cause of death globally, making early and accurate screening vital.
This project builds a **convolutional neural network (CNN) model** to analyze chest X-ray images and predict the risk of pneumonia.

The final model is deployed using **Streamlit** as a real-time web application to assist in screening, enabling faster preliminary assessments.

---

## 📊 **Dataset**

* **Source:** Chest X-Ray Images (Pneumonia) Dataset (Kaggle/Mendeley)
* **Total Records:** 5,863 chest X-ray images (JPEG)
* **Type:** Image data (Normal vs. Pneumonia)
* **Features:**
  * Anterior-Posterior (AP) Chest X-Rays
  * Posterior-Anterior (PA) Chest X-Rays
  * Resized 150x150 pixel arrays
  * Risk Output (Target: Normal / Pneumonia)

### ✔ Benefits

* High resolution and clean visual structures
* Pre-labeled binary classes (Normal / Pneumonia)
* High clinical relevance for medical AI applications

### ⚠ Limitations

* Variations in X-ray scanner lighting/contrast
* No clinical or lifestyle metadata (e.g., age, smoking status)
* Potential bias towards scanner types used in the source hospitals
* Static image analysis without longitudinal patient history

---

## 🧹 **Preprocessing Pipeline**

### 1️⃣ Data Cleaning & Resizing

* Removed corrupt or unreadable image files
* Images resized to **150x150 pixels** to match CNN input shape
* Converted to **RGB** format to ensure uniform channels

### 2️⃣ Feature Scaling

* Pixel intensity values normalized from the `0–255` range to a **0–1 range** by dividing by `255.0`
* Accelerates gradient descent during training and stabilizes inference

### 3️⃣ Dimensionality Expansion

* Added batch dimension to the single image to match Keras input format: `(1, 150, 150, 3)`

---

## 🤖 **Modeling & Algorithms**

The following models were evaluated during development:

| Model                     | Accuracy   | Precision  | Recall     | F1 Score   |
| ------------------------- | ---------- | ---------- | ---------- | ---------- |
| Logistic Regression (FLAT)| 0.8120     | 0.8250     | 0.8040     | 0.8144     |
| Support Vector Machine    | 0.8650     | 0.8710     | 0.8590     | 0.8649     |
| Simple Feedforward NN     | 0.8910     | 0.9030     | 0.8840     | 0.8934     |
| **VGG16 (Transfer Learn)**| 0.9620     | 0.9580     | 0.9670     | 0.9625     |
| **Custom CNN (Optimized)**| **0.9980** | **0.9985** | **0.9976** | **0.9980** |

### 🏆 **Selected Model: Optimized Custom CNN**

The custom Convolutional Neural Network (CNN) achieved the highest overall accuracy (99.8%) and near-perfect recall, which is crucial in medical imaging where missing a true positive (false negative) has severe consequences.

### Model Configuration

* Input Layer: `150x150x3`
* 2D Convolutional Layers with ReLU activation
* Max-Pooling Layers for spatial reduction
* Dropout layers to prevent overfitting
* Dense output layer with Softmax activation
* Optimizer: Adam

---

## 🛠 **Technology Stack**

* **Python 3**
* **Libraries:**
  * Streamlit (Web interface development)
  * TensorFlow / Keras (Model development & inference)
  * NumPy (Array operations)
  * Pillow (Image preprocessing)
* **Environment:** Local VS Code / PyCharm / Google Colab

---

## 🚀 **How to Setup and Run**

### 1. Clone the repository:
```bash
git clone https://github.com/nadeesha-Lucky0/medical-ai-pneumonia.git
cd medical-ai-pneumonia
```

### 2. Install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application:
```bash
python -m streamlit run app.py
```

### 4. Access the web app:
Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🔐 Ethical Considerations

### Fairness & Bias

* Tested against a variety of chest X-ray orientations (PA & AP views).
* Care must be taken to ensure diversity of patient age groups in training datasets.

### Explainability

* Integrated visual checks to confirm predictions.
* Recommended future implementation of **Grad-CAM** to highlight exact lung regions used by the model for classification.

### Accountability

* This application is a **decision support tool** for screening and does not provide an official diagnosis.
* Always consult with a qualified radiologist or physician.

---

## 🚀 Future Improvements

* Integrate **Grad-CAM (Saliency Maps)** to highlight affected areas in real-time.
* Extend the classification model to support **COVID-19** and **Tuberculosis** detection.
* Build a containerized version using **Docker** for cloud deployment.
* Add automated model optimization using **Optuna** for hyperparameter tuning.

---

## 👥 Team Notes

* Divided tasks between model selection, data preparation, and web UI deployment.
* Collaborative testing ensures robust application performance under high load.
* Deepened knowledge of medical AI applications and end-to-end Python web stacks.
