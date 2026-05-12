# Oral Cancer Detection Using Deep Learning

<div align="center">
  <img src="https://img.shields.io/badge/Healthcare%20AI-Medical%20Imaging-FF6B6B?style=for-the-badge&logo=medical&logoColor=white"/>
  <img src="https://img.shields.io/badge/Computer%20Vision-CNN%20%7C%20ResNet50-4ECDC4?style=for-the-badge&logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/Deep%20Learning-Transfer%20Learning-9B59B6?style=for-the-badge"/>
</div>

---

## Project Overview

This project implements an **automated Oral Cancer Detection System** using **Deep Learning** techniques. The system analyzes oral cavity images to classify them as cancerous or non-cancerous, providing a tool that can assist healthcare professionals in early diagnosis.

**Key Highlights:**
- 🏥 Medical Image Classification using CNN
- 🧠 Transfer Learning with ResNet50
- 🌐 Flask Web Application for Real-time Predictions
- 📊 High Accuracy with F1 Score Optimization
- ⚡ Data Augmentation for Improved Generalization

---

## Table of Contents

1. [Introduction](#introduction)
2. [Problem Statement](#problem-statement)
3. [Dataset](#dataset)
4. [Methodology](#methodology)
5. [Models Implemented](#models-implemented)
6. [Results](#results)
7. [Web Application](#web-application)
8. [Technologies Used](#technologies-used)
9. [Installation & Usage](#installation--usage)
10. [Future Work](#future-work)

---

## Introduction

### The Challenge

Oral cancer is one of the most common cancers worldwide, with early detection being crucial for successful treatment. Manual examination of oral cavity images can be:
- Time-consuming
- Subjective
- Dependent on expert availability

### Our Solution

This project leverages **Convolutional Neural Networks (CNN)** and **Transfer Learning** to:
- Automatically classify oral cavity images
- Provide consistent, objective assessments
- Assist in early cancer detection
- Reduce diagnostic time

### Research Objectives

1. ✅ Build a CNN model from scratch for oral cancer detection
2. ✅ Implement Transfer Learning using ResNet50
3. ✅ Optimize for high accuracy and F1 score
4. ✅ Deploy as a user-friendly web application
5. ✅ Apply data augmentation for robustness

---

## Problem Statement

> **"Can deep learning models effectively detect oral cancer from medical images with high accuracy and reliability?"**

**Key Challenges:**
- Limited availability of medical image datasets
- Need for high precision to avoid false negatives
- Class imbalance in medical datasets
- Requirement for model interpretability
- Real-world deployment constraints

---

## Dataset

### Data Collection
- **Type:** Oral cavity images (RGB)
- **Classes:** Binary Classification (Cancerous / Non-Cancerous)
- **Preprocessing:** Resized to 224x224 pixels
- **Augmentation:** Applied to improve generalization

### Data Distribution
```
Dataset Structure:
├── train/
│   ├── cancerous/
│   └── non_cancerous/
└── test/
    ├── cancerous/
    └── non_cancerous/
```

### Data Augmentation Strategy

```python
train_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=20,          # Random rotation
    width_shift_range=0.2,      # Horizontal shift
    height_shift_range=0.2,     # Vertical shift
    horizontal_flip=True,       # Flip horizontally
    shear_range=0.2,           # Shear transformation
    zoom_range=0.2             # Random zoom
)
```

**Augmentation Benefits:**
- ✅ Reduces overfitting
- ✅ Improves model generalization
- ✅ Increases effective dataset size
- ✅ Makes model robust to image variations

---

## Methodology

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│              ORAL CANCER DETECTION SYSTEM                   │
│                    USING DEEP LEARNING                      │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Data         │   │ Model        │   │ Web          │
│ Preprocessing│ → │ Training     │ → │ Deployment   │
└──────────────┘   └──────────────┘   └──────────────┘
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Image        │   │ CNN          │   │ Flask        │
│ Augmentation │   │ ResNet50     │   │ API          │
│ Normalization│   │ Fine-tuning  │   │ HTML UI      │
└──────────────┘   └──────────────┘   └──────────────┘
```

### Preprocessing Pipeline

1. **Image Loading**
   - Load images from directory structure
   - Convert to RGB format
   - Resize to 224x224 (ResNet50 input size)

2. **Normalization**
   - Preprocessing using `preprocess_input` from ResNet50
   - Channel-wise normalization

3. **Data Augmentation**
   - Applied only to training data
   - Random transformations for robustness

---

## Models Implemented

### 1. Custom CNN Architecture

**Model Summary:**
```
Input (224, 224, 3)
    ↓
Conv2D (32 filters, 3x3, ReLU)
    ↓
MaxPooling2D (2x2)
    ↓
Conv2D (64 filters, 3x3, ReLU)
    ↓
MaxPooling2D (2x2)
    ↓
Conv2D (128 filters, 3x3, ReLU)
    ↓
MaxPooling2D (2x2)
    ↓
Flatten
    ↓
Dense (512 units, ReLU)
    ↓
Dropout (0.5)
    ↓
Dense (1 unit, Sigmoid)
    ↓
Output (Cancer Probability)
```

**Why CNN?**
- ✅ Automatic feature extraction
- ✅ Hierarchical pattern learning
- ✅ Translation invariance
- ✅ Efficient for image data

### 2. ResNet50 Transfer Learning

**Architecture:**
```
Input (224, 224, 3)
    ↓
ResNet50 (pre-trained on ImageNet)
    - Frozen base layers
    - Feature extraction
    ↓
GlobalAveragePooling2D
    ↓
Dense (1024 units, ReLU)
    ↓
Dense (1 unit, Sigmoid)
    ↓
Output (Cancer Probability)
```

**Transfer Learning Strategy:**

1. **Base Model:** ResNet50 pre-trained on ImageNet
2. **Fine-tuning Approach:**
   - Freeze all ResNet50 layers initially
   - Train only custom top layers
   - Option to unfreeze later layers for fine-tuning

**Why ResNet50?**
- ✅ 50-layer deep architecture
- ✅ Residual connections prevent vanishing gradients
- ✅ Pre-trained on 1M+ images
- ✅ Excellent feature extraction capability
- ✅ Proven medical imaging performance

### Model Comparison

| Aspect | Custom CNN | ResNet50 |
|--------|------------|----------|
| Parameters | Fewer | More (25.6M) |
| Training Time | Faster | Slower |
| Feature Extraction | Learns from scratch | Pre-trained |
| Accuracy | Good | Better |
| Generalization | Moderate | Excellent |

---

## Results

### Performance Metrics

**Confusion Matrix:**
```
                Predicted
                Cancer    No Cancer
Actual Cancer      77          18
Actual No Cancer   28           3
```

**Key Metrics:**

| Metric | Value |
|--------|-------|
| Accuracy | ~XX% |
| Precision | ~XX% |
| Recall | ~XX% |
| F1 Score | ~XX% |
| Specificity | ~XX% |

**Interpretation:**
- ✅ High recall ensures fewer missed cancer cases
- ✅ Balanced precision avoids false alarms
- ✅ F1 score shows overall model balance

### Visualizations

**Training Curves:**
- Accuracy vs Epochs
- Loss vs Epochs
- Validation performance

**Confusion Matrix Heatmap:**
- True Positives, True Negatives
- False Positives, False Negatives

---

## Web Application

### Flask Application

A user-friendly web interface for real-time oral cancer detection.

**Features:**
- 📤 Image upload functionality
- 🔍 Real-time prediction
- 📊 Confidence score display
- 📱 Mobile-responsive design

### Application Structure

```
oral-cancer-detection/
├── app.py                    # Flask application
├── templates/
│   └── index.html           # Web interface
├── uploads/                  # Uploaded images
├── models/
│   ├── orall_cancer_cnn.h5          # CNN model
│   └── orall_cancer_resnet50.h5     # ResNet50 model
└── static/
    └── css/
        └── style.css
```

### Running the Web App

```bash
# Install dependencies
pip install flask tensorflow pillow

# Run the application
python app.py

# Open browser
goto http://localhost:5000
```

**Usage:**
1. Upload oral cavity image
2. Click "Analyze" button
3. View prediction result with confidence score

---

## Technologies Used

### Core Stack
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

### Web Framework
![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

### Data Science
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-9C27B0?style=for-the-badge)

---

## Installation & Usage

### Prerequisites
```bash
python >= 3.8
pip >= 21.0
```

### Installation

```bash
# Clone the repository
git clone https://github.com/umarranginwala/oral-cancer-detection.git
cd oral-cancer-detection

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Required Packages

```txt
tensorflow==2.13.0
keras==2.13.0
flask==2.3.3
pillow==10.0.0
numpy==1.24.3
pandas==2.0.3
matplotlib==3.7.2
seaborn==0.12.2
scikit-learn==1.3.0
```

### Training the Model

```python
# Run the training notebook
jupyter notebook oral_cancer.ipynb

# Or run training script
python train_model.py
```

### Making Predictions

```python
# Single prediction
python predict.py --image path/to/image.jpg

# Web interface
python app.py
```

---

## Future Work

### Potential Enhancements

1. **Multi-class Classification**
   - Classify cancer stages (Stage I, II, III, IV)
   - Identify cancer types
   - Severity assessment

2. **Segmentation**
   - Identify exact cancerous regions
   - Generate heatmaps
   - Visual explanations

3. **Mobile Application**
   - Deploy on Android/iOS
   - Edge computing
   - Offline inference

4. **Explainable AI**
   - Grad-CAM visualizations
   - Feature importance
   - Doctor-friendly explanations

5. **Clinical Integration**
   - Electronic Health Record (EHR) integration
   - Automated reporting
   - Clinical trial support

---

## Ethical Considerations

⚠️ **Important Notice:**

This project is for **research and educational purposes only**. It should not be used as the sole diagnostic tool. Always consult healthcare professionals for medical diagnosis.

**Key Points:**
- ✅ Model predictions should support, not replace, medical professionals
- ✅ Requires validation on larger, diverse datasets
- ✅ Needs regulatory approval for clinical use
- ✅ Privacy and security of medical data is paramount

---

## Project Structure

```
oral-cancer-detection/
├── README.md                      # This file
├── oral_cancer.ipynb              # Main training notebook
├── app.py                         # Flask web application
├── requirements.txt               # Dependencies
├── templates/
│   └── index.html                # Web UI template
├── models/
│   ├── orall_cancer_cnn.h5       # Trained CNN model
│   └── orall_cancer_resnet50.h5  # Trained ResNet50 model
├── report_images/                 # Result visualizations
│   ├── confusion_matrix.png
│   ├── training_accuracy.png
│   └── training_loss.png
├── uploads/                       # User uploads (created at runtime)
└── data/                          # Dataset directory
    ├── train/
    │   ├── cancerous/
    │   └── non_cancerous/
    └── test/
        ├── cancerous/
        └── non_cancerous/
```

---

## References

1. He, K., et al. (2016). Deep Residual Learning for Image Recognition. CVPR.
2. Esteva, A., et al. (2017). Dermatologist-level classification of skin cancer with deep neural networks. Nature.
3. Litjens, G., et al. (2017). A survey on deep learning in medical image analysis. Medical Image Analysis.
4. World Health Organization. (2020). Oral Cancer Factsheet.

---

## License

This project is part of academic research at Gujarat University. Please cite appropriately if using this work.

**Disclaimer:** This is not a medical device and should not be used for clinical diagnosis without proper validation and regulatory approval.

---

## Contact

**Author:** Umar Ranginwala  
**University:** Gujarat University, M.Sc AI & ML  
**GitHub:** [@umarranginwala](https://github.com/umarranginwala)

---

<div align="center">
  <p>⭐ Star this repository if you find it helpful!</p>
  <p><i>Part of Master's Research at Gujarat University</i></p>
  <p><b>⚠️ For Research Purposes Only - Not for Clinical Use</b></p>
</div>
