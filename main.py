import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import ThresholdAD, QuantileAD, InterQuartileRangeAD, GeneralizedESDTestAD, PersistAD, VolatilityShiftAD

# Read the CSV file
s_train = pd.read_csv("temperature.csv", parse_dates=True)

# Convert 'Date' column to datetime and set as index
s_train["Date"] = pd.to_datetime(s_train["Date"])
s_train = s_train.set_index("Date")

# Use only the 'Mean' column for anomaly detection
s_train = s_train['Mean']

# Validate the series
s_train = validate_series(s_train)
print(s_train)

# Use a different style for plotting
plt.style.use("ggplot")

# Plot the time series data
plot(s_train)
plt.show()

# Threshold Anomaly Detection
threshold_ad = ThresholdAD(high=0.75, low=-0.5)
anomalies = threshold_ad.detect(s_train)
plot(s_train, anomaly=anomalies, anomaly_color="red", anomaly_tag="marker")
plt.show()

# Quantile Anomaly Detection
quantile_ad = QuantileAD(high=0.99, low=0.01)
anomalies = quantile_ad.fit_detect(s_train)
plot(s_train, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_markersize=5, anomaly_color='red', anomaly_tag="marker")
plt.show()

# Inter Quartile Range Anomaly Detection
iqr_ad = InterQuartileRangeAD(c=1.5)
anomalies = iqr_ad.fit_detect(s_train)
plot(s_train, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_markersize=5, anomaly_color='red', anomaly_tag="marker")
plt.show()

# Generalized Extreme Studentized Deviate (ESD) Test
esd_ad = GeneralizedESDTestAD(alpha=0.3)
anomalies = esd_ad.fit_detect(s_train)
plot(s_train, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_markersize=5, anomaly_color='red', anomaly_tag="marker")
plt.show()

# Persist Anomaly Detection (positive changes)
persist_ad = PersistAD(c=3.0, side='positive')
anomalies = persist_ad.fit_detect(s_train)
plot(s_train, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_color='red')
plt.show()

# Persist Anomaly Detection (negative changes)
persist_ad = PersistAD(c=1.5, side='negative')
anomalies = persist_ad.fit_detect(s_train)
plot(s_train, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_color='red')
plt.show()

# Adjust window for mid- to long-term detection
persist_ad.window = 24
anomalies = persist_ad.fit_detect(s_train)
plot(s_train, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_color='red')
plt.show()

# Volatility Shift Anomaly Detection on TSLA stock data
s_train = yf.download("TSLA")['Close']
s_train = validate_series(s_train)

volatility_shift_ad = VolatilityShiftAD(c=6.0, side='positive', window=30)
anomalies = volatility_shift_ad.fit_detect(s_train)
plot(s_train, anomaly=anomalies, anomaly_color='red')
plt.show()
