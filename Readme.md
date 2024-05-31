# Anomaly Detection in Time Series Data

This project demonstrates various methods for detecting anomalies in time series data using the `adtk` library. The project analyzes historical temperature data and financial data of Tesla's stock price to identify anomalies.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Anomaly Detection Methods](#anomaly-detection-methods)
- [Requirements](#requirements)
- [License](#license)

## Project Overview

The goal of this project is to showcase different techniques for anomaly detection in time series data. Anomalies are data points that deviate significantly from the majority of the data, and their detection is crucial for various applications such as fraud detection, fault detection, and monitoring.

The project uses the `adtk` (Anomaly Detection ToolKit) library, which provides several out-of-the-box methods for anomaly detection. We apply these methods to two datasets:
1. **Historical Temperature Data**: This dataset contains monthly mean temperature values from 1880 to 2016.
2. **Tesla Stock Price Data**: This dataset is obtained using the `yfinance` library and contains daily closing prices of Tesla's stock.

By using these datasets, we demonstrate how to detect different types of anomalies, visualize the results, and interpret the findings.

## Installation

To run this project, you need to have Python installed on your machine. You can install the required Python packages using `pip`:

```bash
pip install pandas matplotlib yfinance adtk
```

## Usage

1. **Prepare the data**: Ensure you have the `temperature.csv` file in the project directory. This file should contain the historical temperature data with at least a 'Date' and 'Mean' column.

2. **Run the script**: Execute the `main.py` script to perform anomaly detection on the data.

```bash
python main.py
```

## Project Structure

```
AnomalyDetectionProject/
│
├── main.py
├── temperature.csv
├── README.md
└── requirements.txt
```

- `main.py`: The main script that performs anomaly detection using various methods.
- `temperature.csv`: The CSV file containing historical temperature data.
- `README.md`: This readme file.
- `requirements.txt`: The file listing all Python dependencies (optional, see below).

## Anomaly Detection Methods

The script employs various anomaly detection methods provided by the `adtk` library:

1. **Threshold Anomaly Detection**: Detects anomalies based on predefined high and low thresholds.
2. **Quantile Anomaly Detection**: Detects anomalies based on specified quantiles.
3. **Inter Quartile Range Anomaly Detection**: Uses the IQR to detect anomalies.
4. **Generalized Extreme Studentized Deviate (ESD) Test**: Detects anomalies assuming a normal distribution.
5. **Persist Anomaly Detection**: Detects anomalies based on persistence (positive or negative changes).
6. **Volatility Shift Anomaly Detection**: Detects anomalies based on shifts in volatility.

The script includes plotting functionalities to visualize the time series data and the detected anomalies.

## Requirements

- Python 3.x
- pandas
- matplotlib
- yfinance
- adtk

You can install all the required packages using the provided `requirements.txt` file (if available):

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

