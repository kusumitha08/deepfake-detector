# 🧠 Deepfake Image Detection System

## 📌 Overview

This project focuses on detecting deepfake images using Artificial Intelligence and Deep Learning techniques. Deepfakes are manipulated or synthetic images that can mislead users and pose serious security risks.

The system analyzes facial features and visual inconsistencies to classify whether an image is **Real or Fake**.

---

## 🎯 Objective

* Detect deepfake images accurately
* Improve trust in digital media
* Prevent misuse of AI-generated content

---

## 🧠 Technologies Used

* Python
* Deep Learning (CNN)
* Computer Vision
* PyTorch
* Streamlit (for UI)

---

## ⚙️ How It Works

1. User uploads an image
2. Image is preprocessed (resizing, normalization)
3. Deep learning model extracts features
4. Model predicts whether the image is **Real or Fake**

---

## 📊 Features

* Real vs Fake image classification
* User-friendly interface
* Fast prediction using trained model
* Scalable for real-world applications

---

## 📂 Project Structure

```
deepfake_detector/
│── app.py
│── download_model.py
│── deepfake_detector/
│── flagged/
│── .gitignore
```

---

## ⚠️ Note on Model Files

Due to GitHub file size limitations, trained model files are not included in this repository.

👉 The model can be downloaded using the provided script:

```
python download_model.py
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/kusumitha08/deepfake-detector.git
cd deepfake-detector
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
python app.py
```

---

## 🚀 Applications

* Social media content verification
* Cybersecurity and fraud detection
* Digital forensics

---

## 📈 Future Improvements

* Improve model accuracy with larger datasets
* Extend to video deepfake detection
* Deploy as a full-stack web application

---
## 📸 Preview

### 🔹 Application Interface

<img width="1919" height="950" alt="image" src="https://github.com/user-attachments/assets/92828427-081b-414f-b41d-0e883dd05dce" />


### 🔹 Prediction Result

<img width="1917" height="946" alt="Screenshot 2026-03-19 144047" src="https://github.com/user-attachments/assets/5d122e99-53eb-4b98-9c1d-35a2cf1ce902" />

---
## ⭐ Acknowledgment

This project is developed to demonstrate practical applications of AI/ML in solving real-world problems like deepfake detection.
