# ❤️ Heart Disease Predictor App

The **Heart Disease Predictor App** is a web-based machine learning application built with **Streamlit**. It uses clinical data inputs like age, cholesterol levels, blood pressure, and other vital parameters to predict the likelihood of a person having heart disease. This tool is intended to assist users and healthcare professionals with early risk detection.

---

## 🔗 Live Demo

👉 Try it here: [https://heart-app-predictor-nt7z2zxxdmsg4xblx3a3m7.streamlit.app](https://heart-app-predictor-nt7z2zxxdmsg4xblx3a3m7.streamlit.app)

---

## 📌 Table of Contents

- [Features](#-features)
- [Dataset](#-dataset)
- [How It Works](#-how-it-works)
- [Screenshots](#-screenshots)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Model Performance](#-model-performance)
- [Technologies Used](#-technologies-used)
- [Future Work](#-future-work)
- [License](#-license)
- [Author](#-author)

---

## ✨ Features

- ✅ Predicts the risk of heart disease based on 13 clinical inputs.
- 🧠 Uses a trained **Random Forest Classifier** for high accuracy.
- 🎛️ Intuitive user interface built using **Streamlit**.
- 📈 Model trained using **UCI Heart Disease Dataset**.
- 🔍 Optional integration with **SHAP** for model explainability.
- 📦 Clean, modular code with separate training and deployment folders.

---

## 📊 Dataset

- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
- **Samples**: 303 rows (patients)
- **Features**: 13 clinical attributes including:
  - Age
  - Sex
  - Chest Pain Type (cp)
  - Resting Blood Pressure (trestbps)
  - Cholesterol (chol)
  - Fasting Blood Sugar (fbs)
  - Maximum Heart Rate Achieved (thalach)
  - Exercise Induced Angina (exang)
  - Oldpeak, Slope, Thal, etc.

- **Target**: `0` (No Heart Disease), `1` (Heart Disease)

---

## ⚙️ How It Works

1. The user opens the app in a browser.
2. Inputs 13 features using sliders and dropdowns.
3. Preprocessing and encoding are applied.
4. A trained **Random Forest model** makes a prediction.
5. The app displays whether the person is at high or low risk.

---

## 🖼️ Screenshots

> *(Optional – You can include screenshots here once available)*

---

## 💻 Installation

Follow these steps to run the app locally:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/heart-disease-predictor.git
cd heart-disease-predictor

