import pandas as pd
import matplotlib.pyplot as plt

# Fetch the csv data
df = pd.read_csv("net_metrics.csv", parse_dates=["timestamp"]).sort_values("timestamp")
df = df.dropna(subset=["download_mbps","upload_mbps","ping_ms"])

# Display the upload speed and the download speed
plt.figure()
plt.plot(df["timestamp"], df["download_mbps"], label="Download (Mbps)")
plt.plot(df["timestamp"], df["upload_mbps"],   label="Upload (Mbps)")
plt.title("Throughput over time")
plt.xlabel("Time")
plt.ylabel("Mbps")
plt.legend()
plt.tight_layout()
plt.show()

# Display the latency
plt.plot(df["timestamp"], df["ping_ms"],   label="Ping (ms)")
plt.xlabel("Time"); plt.ylabel("Ms")
plt.legend()
plt.tight_layout()
plt.show()


