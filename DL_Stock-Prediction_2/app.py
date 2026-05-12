# app.py
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
from lstm_model import (
    get_historical_data, preprocess_data, create_training_data,
    build_and_train_model, make_predictions, calculate_mae
)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    stock_data = None
    lstm_predictions = None
    gru_predictions = None
    next_day_lstm = None
    next_day_gru = None
    ticker = 'ASIANPAINT.NS'
    plot_div_lstm = None
    plot_div_gru = None
    candlestick_div = None
    next_day_prediction = None

    if request.method == 'POST':
        ticker = request.form.get('ticker')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')

        stock_data = get_historical_data(ticker, start_date, end_date)

        if stock_data.empty or len(stock_data) < 60:
            return render_template('index.html', plot_div_lstm=None, plot_div_gru=None, candlestick_div=None, ticker=ticker, error="Not enough data available for the selected date range.")

        scaled_data, scaler = preprocess_data(stock_data)
        x_train, y_train, train_data_len = create_training_data(scaled_data)
        
        lstm_model = build_and_train_model(x_train, y_train, model_type='LSTM')
        lstm_predictions, next_day_lstm = make_predictions(lstm_model, scaled_data, train_data_len, scaler)

        gru_model = build_and_train_model(x_train, y_train, model_type='GRU')
        gru_predictions, next_day_gru = make_predictions(gru_model, scaled_data, train_data_len, scaler)

        plot_div_lstm = generate_plot(stock_data, train_data_len, lstm_predictions, title='LSTM Model Predictions')
        plot_div_gru = generate_plot(stock_data, train_data_len, gru_predictions, title='GRU Model Predictions')
        candlestick_div = generate_candlestick_plot(stock_data)
        
        next_day_prediction = f"LSTM Model Next Day Prediction: {next_day_lstm[0][0]:.2f}, GRU Model Next Day Prediction: {next_day_gru[0][0]:.2f}"

    return render_template('index.html', plot_div_lstm=plot_div_lstm, plot_div_gru=plot_div_gru, candlestick_div=candlestick_div, ticker=ticker, next_day_prediction=next_day_prediction, error=None)

def generate_plot(stock_data, train_data_len, predictions, title):
    train = stock_data[:train_data_len]
    valid = stock_data[train_data_len:]
    valid['Predictions'] = predictions[:len(valid)]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=train.index, y=train['Close'], mode='lines', name='Train'))
    fig.add_trace(go.Scatter(x=valid.index, y=valid['Close'], mode='lines', name='Actual'))
    fig.add_trace(go.Scatter(x=valid.index, y=valid['Predictions'], mode='lines', name='Prediction'))

    fig.update_layout(
        title=title,
        xaxis_title='Date',
        yaxis_title='Close Price INR (₹)',
        template='plotly_white'
    )

    plot_div = pio.to_html(fig, full_html=False)
    return plot_div

def generate_candlestick_plot(stock_data):
    fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                         open=stock_data['Open'],
                                         high=stock_data['High'],
                                         low=stock_data['Low'],
                                         close=stock_data['Close'])])
    fig.update_layout(
        title='Candlestick chart',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False,
        template='plotly_white'
    )

    candlestick_div = pio.to_html(fig, full_html=False)
    return candlestick_div

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
