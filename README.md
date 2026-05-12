# Umar Ranginwala - AI/ML Research & Engineering Portfolio

<div align="center">
  <img src="https://img.shields.io/badge/M.Sc-AI%20%26%20Machine%20Learning-FF6B6B?style=for-the-badge&logo=brain&logoColor=white" alt="M.Sc AI/ML"/>
  <img src="https://img.shields.io/badge/Gujarat%20University-Master's%20Thesis-003366?style=for-the-badge&logo=university&logoColor=white" alt="Gujarat University"/>
  <img src="https://img.shields.io/badge/Deep%20Learning-Production%20Ready-10B981?style=for-the-badge&logo=tensorflow&logoColor=white" alt="Production"/>
  <img src="https://img.shields.io/badge/Research-Published-9C27B0?style=for-the-badge&logo=googlescholar&logoColor=white" alt="Research"/>
</div>

<p align="center">
  <strong>Building end-to-end AI systems from research to production deployment</strong>
</p>

<p align="center">
  <a href="https://github.com/umarranginwala/ai-ml-portfolio">🌐 Portfolio</a> •
  <a href="#live-demos">🚀 Live Demos</a> •
  <a href="#projects">📂 Projects</a> •
  <a href="#research">📊 Research</a>
</p>

---

## 🔬 Research Focus

I specialize in **Deep Learning** and **Computer Vision** with a focus on developing production-ready AI systems. My M.Sc research at Gujarat University (2022-2024) explored:

- **Time Series Forecasting:** LSTM and GRU architectures for financial markets
- **Medical AI:** CNN-based oral cancer detection systems
- **Transfer Learning:** Leveraging pre-trained models for domain-specific tasks

**Core Competencies:**
- 🧠 Deep Learning (LSTM, GRU, CNN, ResNet50, Transfer Learning)
- 📊 Financial Forecasting & Time Series Analysis
- 🏥 Healthcare AI & Medical Image Classification
- 🚀 Production Deployment (Flask, REST APIs, Cloud)
- 📈 Data Engineering & Feature Engineering

---

## 🚀 Live Demos

### Oral Cancer Detection - Interactive Web Application

**🎮 [Try Live Demo →](./demo/oral-cancer-detection-demo/)**

A fully functional web application for oral cancer detection using deep learning:

- ✅ Upload images via drag-and-drop interface
- ✅ Real-time AI analysis with confidence scores
- ✅ Automated risk assessment & medical recommendations
- ✅ Responsive design (mobile, tablet, desktop)
- ✅ REST API for programmatic access

**Tech Stack:** Flask, TensorFlow, Keras, ResNet50, HTML5, CSS3, JavaScript

```bash
# Run locally
cd demo/oral-cancer-detection-demo
pip install -r requirements.txt
python app.py
```

---

## 📂 Featured Projects

### 1. Stock Price Prediction Using LSTM and GRU
**Master's Thesis | NSE (National Stock Exchange of India)**

[![Research Paper](https://img.shields.io/badge/Research-Paper-FF6B6B?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white)](./Research%20Paper/NSE_stock_price_prediction_umar.pdf)
[![Thesis](https://img.shields.io/badge/Thesis-Report-9C27B0?style=for-the-badge&logo=googlescholar&logoColor=white)](./Stock_Prediction_DL_2/Report/Final%20Report/stock-prediction-dl-report.pdf)
[![Code](https://img.shields.io/badge/Code-Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](./src/stock-prediction/)

**Project Overview:**
Developed and deployed deep learning models (LSTM and GRU) to predict stock prices for NSE-listed companies using 24+ years of historical data (2000-2024).

**Key Results:**
- 📊 **Dataset:** 6,036 trading days of HINDUNILVR.NS stock data
- 🎯 **Models:** LSTM vs GRU comparative analysis
- 📈 **Performance:** High accuracy with comprehensive evaluation metrics
- 🔄 **Pipeline:** Automated data collection via Yahoo Finance API
- 📄 **Publication:** Research paper on NSE stock prediction

**Technical Highlights:**
- LSTM architecture with dropout regularization
- GRU implementation for faster training
- Comprehensive EDA with technical indicators (RSI, Moving Averages, Bollinger Bands)
- Feature normalization and sequence preparation
- Train-test split with temporal validation

**Tech Stack:** Python, TensorFlow, Keras, LSTM, GRU, Pandas, NumPy, Scikit-learn, Matplotlib, Yahoo Finance API

**[📁 View Complete Documentation](./projects/stock-prediction/README.md)**

---

### 2. Oral Cancer Detection Using Deep Learning
**Healthcare AI | Medical Image Classification | Web Application**

[![Live Demo](https://img.shields.io/badge/Live-Demo-10B981?style=for-the-badge&logo=vercel&logoColor=white)](./demo/oral-cancer-detection-demo/)
[![Code](https://img.shields.io/badge/Code-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](./demo/oral-cancer-detection-demo/app.py)
[![Flask](https://img.shields.io/badge/Flask-App-000000?style=for-the-badge&logo=flask&logoColor=white)](./demo/oral-cancer-detection-demo/)

**Project Overview:**
Built an automated oral cancer detection system using CNN and Transfer Learning with ResNet50. Includes a production-ready Flask web application for real-time predictions.

**System Architecture:**
```
Input (224×224×3 RGB Image)
    ↓
ResNet50 (Transfer Learning - Frozen)
    ↓
GlobalAveragePooling2D
    ↓
Dense (1024, ReLU) → Dropout (0.5)
    ↓
Dense (512, ReLU) → Dropout (0.3)
    ↓
Dense (1, Sigmoid) → Binary Classification
    ↓
Output: Cancer Probability + Risk Assessment
```

**Key Features:**
- 🖼️ **Medical Image Classification:** Oral cavity image analysis
- 🧠 **Transfer Learning:** ResNet50 pre-trained on ImageNet
- 📊 **Performance Metrics:** Accuracy, Precision, Recall, F1-Score
- 🌐 **Web Interface:** Flask-based interactive application
- 📱 **Responsive Design:** Mobile-friendly interface
- 🔄 **Data Augmentation:** Rotation, zoom, flip for robustness

**Web Application Capabilities:**
- Drag-and-drop image upload
- Real-time AI prediction (< 2 seconds)
- Confidence score visualization
- Risk level classification (High/Moderate/Low)
- Medical recommendations based on results
- REST API endpoint for integration

**Tech Stack:** Python, TensorFlow, Keras, CNN, ResNet50, Transfer Learning, Flask, OpenCV, Pillow

**[🎮 Launch Live Demo](./demo/oral-cancer-detection-demo/)** | **[📁 View Code](./demo/oral-cancer-detection-demo/)** | **[📖 Documentation](./projects/oral-cancer-detection/README.md)**

---

## 🛠️ Technical Skills

### Programming & Deep Learning
![Python](https://img.shields.io/badge/Python-Expert-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Production-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-Production-D00000?style=for-the-badge&logo=keras&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Production-000000?style=for-the-badge&logo=flask&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-Intermediate-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Expert-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

### Deep Learning Architectures
- **Recurrent Neural Networks:** LSTM, GRU, Bidirectional RNNs
- **Convolutional Neural Networks:** CNN, ResNet50, VGG16, Transfer Learning
- **NLP:** Word2Vec, Language Models, Text Classification, Parsing
- **Computer Vision:** Image Classification, Object Detection, Medical Imaging

### Data Science & Engineering
![Pandas](https://img.shields.io/badge/Pandas-Expert-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Expert-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Expert-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-Expert-F05032?style=for-the-badge&logo=git&logoColor=white)

- Time Series Analysis & Forecasting
- Exploratory Data Analysis (EDA)
- Feature Engineering & Selection
- Statistical Analysis
- Data Visualization (Matplotlib, Seaborn, Plotly)
- API Development & Integration

---

## 📊 Research Publications

| Title | Venue/Type | Year | Links |
|-------|------------|------|-------|
| **NSE Stock Price Prediction Using Deep Learning** | Research Paper | 2024 | [PDF](./Research%20Paper/NSE_stock_price_prediction_umar.pdf) |
| **Stock Price Prediction Using LSTM and GRU** | Master's Thesis | 2024 | [Report](./Stock_Prediction_DL_2/Report/Final%20Report/stock-prediction-dl-report.pdf) |

---

## 🎓 Academic Background

### Master of Science (M.Sc) in Artificial Intelligence & Machine Learning
**Gujarat University, Ahmedabad, India**
- **Duration:** 2022-2024
- **Specialization:** Deep Learning, Natural Language Processing, Computer Vision
- **Key Coursework:**
  - Deep Learning & Neural Networks (LSTM, GRU, CNN, RNN)
  - Natural Language Processing (Word2Vec, Parsing, Text Classification)
  - Reinforcement Learning
  - Machine Learning Algorithms
  - Statistical Methods for Data Science

---

## 📈 GitHub Stats

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=umarranginwala&show_icons=true&theme=radical" alt="GitHub Stats"/>
  <br><br>
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=umarranginwala&theme=radical" alt="GitHub Streak"/>
</div>

---

## 📂 Repository Structure

```
ai-ml-portfolio/
├── 📁 demo/                          → Live interactive demos
│   └── oral-cancer-detection-demo/  → Flask web application
│       ├── app.py                   → Production backend
│       ├── templates/              → HTML interface
│       └── requirements.txt        → Dependencies
│
├── 📁 src/                          → Source code & notebooks
│   ├── stock-prediction/           → Jupyter notebooks (LSTM, GRU, EDA)
│   └── oral-cancer-detection/      → Training notebooks
│
├── 📁 projects/                     → Comprehensive documentation
│   ├── stock-prediction/          → Thesis documentation
│   └── oral-cancer-detection/     → Project documentation
│
├── 📁 Research Paper/              → Published research
│   └── NSE_stock_price_prediction_umar.pdf
│
├── 📁 Stock_Prediction_DL_2/       → Original thesis work
├── 📁 Oral-Cancer-Detection/       → Original project files
│
├── 📄 README.md                     → Portfolio overview
├── 📄 index.html                    → Portfolio website
└── 📄 _config.yml                   → GitHub Pages config
```

---

## 🌐 Quick Links

| Resource | Link |
|----------|------|
| **GitHub Repository** | https://github.com/umarranginwala/ai-ml-portfolio |
| **Live Demo (Cancer Detection)** | https://github.com/umarranginwala/ai-ml-portfolio/tree/main/demo/oral-cancer-detection-demo |
| **GitHub Profile** | https://github.com/umarranginwala |
| **LinkedIn** | https://www.linkedin.com/in/umarranginwala/ |

---

## 📞 Connect With Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/umarranginwala/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/umarranginwala)

---

<div align="center">
  <p><i>⭐ Star this repository if you find the work impressive!</i></p>
  <p><b>🎓 M.Sc AI/ML | 🧠 Deep Learning | 🚀 Production Systems | 📊 Research</b></p>
  <p>Gujarat University | 2022-2024</p>
</div>
