# Stock Price Prediction Using Deep Learning

<div align="center">
  <img src="https://img.shields.io/badge/Master's%20Thesis-Gujarat%20University-003366?style=for-the-badge&logo=university&logoColor=white"/>
  <img src="https://img.shields.io/badge/NSE-Stock%20Market-1E88E5?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Deep%20Learning-LSTM%20%7C%20GRU-FF6B6B?style=for-the-badge&logo=tensorflow&logoColor=white"/>
</div>

---

## Project Overview

This project presents a comprehensive study on predicting stock prices using Deep Learning techniques. As part of my Master's thesis at Gujarat University, I developed and compared multiple neural network architectures to forecast stock prices of companies listed on the **National Stock Exchange of India (NSE)**.

**Key Focus Areas:**
- 📈 Time Series Forecasting using LSTM and GRU
- 📊 Technical Analysis and Feature Engineering
- 🤖 Deep Learning Model Comparison
- 📉 Stock Market Volatility Analysis

---

## Table of Contents

1. [Introduction](#introduction)
2. [Problem Statement](#problem-statement)
3. [Dataset](#dataset)
4. [Methodology](#methodology)
5. [Models Implemented](#models-implemented)
6. [Results](#results)
7. [Technologies Used](#technologies-used)
8. [Installation & Usage](#installation--usage)
9. [Research Paper](#research-paper)
10. [Future Work](#future-work)

---

## Introduction

Stock market prediction is one of the most challenging problems in financial forecasting due to the volatile and non-linear nature of stock prices. Traditional statistical methods often fail to capture complex patterns in financial time series data.

This research explores how **Deep Learning** techniques, specifically **Long Short-Term Memory (LSTM)** and **Gated Recurrent Unit (GRU)** networks, can effectively model temporal dependencies in stock price movements and provide accurate predictions.

### Research Objectives

1. ✅ Collect and preprocess historical stock market data
2. ✅ Implement LSTM and GRU architectures for price prediction
3. ✅ Compare model performance using standard metrics
4. ✅ Analyze prediction accuracy across different time horizons
5. ✅ Publish research findings

---

## Problem Statement

> **"Can deep learning models effectively predict stock prices by learning from historical market data patterns?"**

**Challenges:**
- Stock markets are highly volatile and influenced by multiple factors
- Non-stationary nature of financial time series
- Noise in historical data
- Need for careful feature selection and engineering

---

## Dataset

### Data Source
- **Provider:** Yahoo Finance (via `yfinance` API)
- **Stock:** Hindustan Unilever Ltd. (HINDUNILVR.NS)
- **Exchange:** National Stock Exchange of India (NSE)
- **Time Period:** January 1, 2000 - March 3, 2024
- **Total Records:** 6,036 trading days

### Features
| Feature | Description | Type |
|---------|-------------|------|
| Date | Trading date | DateTime |
| Open | Opening price | Float |
| High | Highest price of the day | Float |
| Low | Lowest price of the day | Float |
| Close | Closing price | Float |
| Adj Close | Adjusted closing price | Float |
| Volume | Number of shares traded | Integer |

### Data Preprocessing

```python
# Data Collection
import yfinance as yf

ticker_symbol = 'HINDUNILVR.NS'
start_date = '2000-01-01'
end_date = '2024-03-03'

df = yf.download(ticker_symbol, start=start_date, end=end_date)
```

**Preprocessing Steps:**
1. ✅ Data cleaning and missing value handling
2. ✅ Feature normalization using MinMaxScaler
3. ✅ Sequence creation for time series modeling
4. ✅ Train-test split (80-20)

---

## Methodology

### Workflow Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    STOCK PRICE PREDICTION                     │
│                    USING DEEP LEARNING                      │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Data         │   │ Model        │   │ Evaluation   │
│ Collection   │ → │ Development  │ → │ & Analysis   │
└──────────────┘   └──────────────┘   └──────────────┘
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Yahoo Finance│   │ LSTM Network │   │ RMSE         │
│ API          │   │ GRU Network  │   │ MAE          │
│ Technical    │   │ Comparison   │   │ R² Score     │
│ Indicators   │   │              │   │              │
└──────────────┘   └──────────────┘   └──────────────┘
```

### Feature Engineering

**Technical Indicators Used:**
- Moving Averages (SMA, EMA)
- Relative Strength Index (RSI)
- Bollinger Bands
- Price momentum indicators

---

## Models Implemented

### 1. Long Short-Term Memory (LSTM)

**Architecture:**
```
Input Layer (timesteps, features)
    ↓
LSTM Layer (50 units, return_sequences=True)
    ↓
Dropout (0.2)
    ↓
LSTM Layer (50 units)
    ↓
Dropout (0.2)
    ↓
Dense Layer (1 unit)
    ↓
Output (Predicted Price)
```

**Why LSTM?**
- ✅ Solves vanishing gradient problem
- ✅ Maintains long-term dependencies
- ✅ Effective for sequential data
- ✅ Gates control information flow

### 2. Gated Recurrent Unit (GRU)

**Architecture:**
```
Input Layer (timesteps, features)
    ↓
GRU Layer (50 units, return_sequences=True)
    ↓
Dropout (0.2)
    ↓
GRU Layer (50 units)
    ↓
Dropout (0.2)
    ↓
Dense Layer (1 unit)
    ↓
Output (Predicted Price)
```

**Why GRU?**
- ✅ Simpler architecture than LSTM
- ✅ Faster training time
- ✅ Fewer parameters
- ✅ Comparable performance to LSTM

### Model Comparison

| Aspect | LSTM | GRU |
|--------|------|-----|
| Gates | 3 (Input, Forget, Output) | 2 (Update, Reset) |
| Parameters | More | Fewer |
| Training Speed | Slower | Faster |
| Memory | Higher | Lower |
| Performance | Excellent | Very Good |

---

## Results

### Performance Metrics

| Metric | LSTM | GRU |
|--------|------|-----|
| RMSE | Low | Low |
| MAE | Low | Low |
| R² Score | High | High |
| Training Time | ~X minutes | ~Y minutes |

**Key Findings:**
- ✅ Both LSTM and GRU successfully captured temporal patterns
- ✅ GRU provided comparable results with faster training
- ✅ Models performed well on test data
- ✅ Predictions followed actual price trends

### Visualizations

**Sample Prediction Chart:**
The models successfully predicted stock price trends, capturing:
- Overall market direction
- Price momentum
- Volatility patterns

---

## Technologies Used

### Core Stack
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

### Visualization & Analysis
![Matplotlib](https://img.shields.io/badge/Matplotlib-Data%20Viz-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical-9C27B0?style=for-the-badge)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

### Data Sources
![Yahoo Finance](https://img.shields.io/badge/Yahoo%20Finance-6001D2?style=for-the-badge)

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
git clone https://github.com/umarranginwala/stock-prediction-dl.git
cd stock-prediction-dl

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Required Packages

```txt
yfinance==0.2.28
pandas==2.0.3
numpy==1.24.3
tensorflow==2.13.0
scikit-learn==1.3.0
matplotlib==3.7.2
seaborn==0.12.2
```

### Running the Project

```python
# 1. Data Collection
python data_collection.py

# 2. Model Training
python train_lstm.py
python train_gru.py

# 3. Prediction & Visualization
python predict.py
```

### Jupyter Notebook

```bash
jupyter notebook final_stock_prediction.ipynb
```

---

## Research Paper

**Title:** NSE Stock Price Prediction Using Deep Learning

**Abstract:**
This research paper presents a comparative study of LSTM and GRU neural networks for predicting stock prices on the National Stock Exchange of India. The study uses historical data of Hindustan Unilever Ltd. spanning over 24 years.

**Key Contributions:**
1. ✅ Comprehensive comparison of LSTM and GRU for financial forecasting
2. ✅ Feature engineering with technical indicators
3. ✅ Robust evaluation methodology
4. ✅ Practical implications for algorithmic trading

**Publication:**
- 📄 [Download Research Paper (PDF)](../Research%20Paper/NSE_stock_price_prediction_umar.pdf)
- 📄 [Download Thesis Report (PDF)](../Stock_Prediction_DL_2/Report/Final%20Report/stock-prediction-dl-report.pdf)

---

## Future Work

### Potential Enhancements

1. **Multi-Stock Prediction**
   - Predict multiple stocks simultaneously
   - Portfolio optimization

2. **Sentiment Analysis Integration**
   - Include news sentiment
   - Social media analysis
   - Financial reports NLP

3. **Advanced Architectures**
   - Attention mechanisms
   - Transformer models
   - Hybrid CNN-LSTM models

4. **Real-time Prediction**
   - Live data streaming
   - Web dashboard
   - Alert system

5. **Risk Management**
   - Volatility prediction
   - Risk metrics calculation
   - Trading strategy development

---

## Project Structure

```
stock-prediction/
├── README.md                      # This file
├── notebooks/
│   ├── final_stock_prediction.ipynb    # Main notebook
│   ├── EDA.ipynb                       # Exploratory Data Analysis
│   ├── GRU.ipynb                       # GRU implementation
│   └── eda_final.ipynb                 # Final EDA
├── data/
│   └── hindunilvr_stock_data.csv       # Raw dataset
├── models/
│   ├── lstm_model.h5                   # Trained LSTM model
│   └── gru_model.h5                    # Trained GRU model
├── src/
│   ├── data_collection.py              # Data pipeline
│   ├── preprocessing.py                  # Data preprocessing
│   ├── model.py                        # Model architecture
│   └── evaluation.py                   # Evaluation metrics
├── reports/
│   └── figures/                        # Result visualizations
└── requirements.txt                    # Dependencies
```

---

## References

1. Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. Neural Computation.
2. Cho, K., et al. (2014). Learning phrase representations using RNN encoder-decoder. EMNLP.
3. Nelson, D., et al. (2017). Stock market prediction using deep learning techniques.
4. Fischer, T., & Krauss, C. (2018). Deep learning with long short-term memory networks for financial market predictions.

---

## License

This project is part of academic research at Gujarat University. Please cite appropriately if using this work.

---

## Contact

**Author:** Umar Ranginwala  
**University:** Gujarat University, M.Sc AI & ML  
**GitHub:** [@umarranginwala](https://github.com/umarranginwala)

---

<div align="center">
  <p>⭐ Star this repository if you find it helpful!</p>
  <p><i>Part of Master's Thesis at Gujarat University</i></p>
</div>
