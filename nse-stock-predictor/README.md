# nse-stock-predictor

> Real-time stock price prediction for National Stock Exchange of India using Deep Learning

[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13-orange.svg)](https://tensorflow.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

LSTM and GRU neural networks for predicting NSE stock prices. Analyzes 24+ years of historical data.

## Features

- 📈 **LSTM & GRU Models** - Comparative analysis of deep learning architectures
- 📊 **Technical Indicators** - RSI, Moving Averages, Bollinger Bands
- 🔄 **Real-time Data** - Yahoo Finance API integration
- 📉 **Performance Metrics** - RMSE, MAE, R² Score
- 📄 **Research Paper** - Published findings

## Quick Start

```bash
# Clone repository
git clone https://github.com/umarranginwala/nse-stock-predictor.git
cd nse-stock-predictor

# Install dependencies
pip install -r requirements.txt

# Run prediction
python predict.py --ticker HINDUNILVR.NS --days 30
```

## Dataset

- **Source:** Yahoo Finance
- **Period:** 2000-2024 (6,036 trading days)
- **Stock:** Hindustan Unilever Ltd. (NSE)
- **Features:** Open, High, Low, Close, Volume

## Model Architecture

```
Input (60-day sequences)
    ↓
LSTM (50 units) → Dropout(0.2)
    ↓
LSTM (50 units) → Dropout(0.2)
    ↓
Dense (1 unit)
    ↓
Predicted Price
```

## Results

| Model | RMSE | MAE | Accuracy |
|-------|------|-----|----------|
| LSTM | 2.34 | 1.78 | 94.2% |
| GRU | 2.41 | 1.82 | 93.8% |

## Research

📄 [NSE Stock Price Prediction Using Deep Learning](https://github.com/umarranginwala/ai-ml-portfolio/blob/main/Final-Papers/NSE_stock_price_prediction_umar.pdf)

## Tech Stack

- Python 3.9
- TensorFlow 2.13
- Keras
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## License

MIT License - see [LICENSE](LICENSE) file

---

Built with ❤️ by [Umar Ranginwala](https://github.com/umarranginwala)
