import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

df = yf.download("000001.SS", start="2024‑01‑01", end="2026‑01‑01")

# 数据清洗
df = df.dropna()
df = df.sort_index()

# pandas计算衍生指标
df["daily_return"] = df["Close"].pct_change()
df["ma5"] = df["Close"].rolling(window=5).mean()
df["ma20"] = df["Close"].rolling(window=20).mean()

# 月度收益聚合
df["month"] = df.index.to_period("M")
month_return = df.groupby("month")["daily_return"].mean()

# 简单绘图
plt.figure(figsize=(12,5))
plt.plot(df.index,df["Close"],label="close")
plt.plot(df.index,df["ma5"],label="MA5")
plt.legend()
plt.title("股价与均线")
plt.show()

print("月度平均收益率：")
print(month_return.head())