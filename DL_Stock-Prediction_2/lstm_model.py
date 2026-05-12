# lstm_model.py
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from statsmodels.tsa.arima.model import ARIMA
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, GRU, Dense, Dropout

def get_historical_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    return df

def preprocess_data(data):
    dataset = data[['Close']].values
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(dataset)
    return scaled_data, scaler

def create_training_data(scaled_data):
    train_data_len = int(np.ceil(len(scaled_data) * .95))
    train_data = scaled_data[0:train_data_len, :]
    x_train, y_train = [], []
    for i in range(60, len(train_data)):
        x_train.append(train_data[i-60:i, 0])
        y_train.append(train_data[i, 0])
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    return x_train, y_train, train_data_len

def build_and_train_model(x_train, y_train, model_type='LSTM'):
    model = Sequential()
    if model_type == 'LSTM':
        model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
        model.add(Dropout(0.2))
        model.add(LSTM(50, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(50, return_sequences=False))
        model.add(Dropout(0.2))
    elif model_type == 'GRU':
        model.add(GRU(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
        model.add(Dropout(0.2))
        model.add(GRU(50, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(GRU(50, return_sequences=False))
        model.add(Dropout(0.2))
    
    model.add(Dense(25))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, batch_size=1, epochs=2)
    return model

def make_predictions(model, scaled_data, train_data_len, scaler):
    test_data = scaled_data[train_data_len - 60:, :]
    x_test = []
    for i in range(60, len(test_data)):
        x_test.append(test_data[i-60:i, 0])
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)
    
    # Predict the next day after the end date
    last_60_days = scaled_data[-60:]
    last_60_days = np.reshape(last_60_days, (1, last_60_days.shape[0], 1))
    next_day_prediction = model.predict(last_60_days)
    next_day_prediction = scaler.inverse_transform(next_day_prediction)
    
    return predictions, next_day_prediction

def build_and_predict_arima(data, train_data_len):
    train = data[:train_data_len]
    test = data[train_data_len:]
    model = ARIMA(train['Close'], order=(5,1,0))
    model_fit = model.fit()
    predictions = model_fit.forecast(steps=len(test))
    return predictions

def build_and_predict_linear_regression(data, train_data_len):
    train = data[:train_data_len]
    test = data[train_data_len:]
    model = LinearRegression()
    x_train = np.arange(len(train)).reshape(-1, 1)
    y_train = train['Close'].values
    x_test = np.arange(len(train), len(train) + len(test)).reshape(-1, 1)
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    return predictions

def calculate_mae(actual, predicted):
    return mean_absolute_error(actual, predicted)
