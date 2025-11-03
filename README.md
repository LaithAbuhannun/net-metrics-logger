# net-metrics-logger

A tiny, no-frills tool that logs your **download Mbps**, **upload Mbps**, and **latency to 8.8.8.8 (ms)** into a CSV, then plots two simple graphs:
1) **Throughput over time** (Download + Upload in Mbps)  
2) **Ping over time** (Latency in ms)

---

## Why?
When the internet “feels slow,” you want quick evidence. This repo gives you:
- A CSV history you can open in Excel/Sheets.
- Two clear charts to see when/why things dipped.

---

## Example Graphs

**Throughput (Mbps)**
<br>
<img width="640" height="480" alt="Image" src="https://github.com/user-attachments/assets/d3c7c3be-ed03-46ec-ba73-ba7b2345b48e" />

**Ping (ms)**
<br>
<img width="640" height="480" alt="Image" src="https://github.com/user-attachments/assets/da0b726c-9c96-4960-8995-cbb817d7ba26" />


## What’s inside
- `data_fetch.py` — collects metrics every N seconds and appends to `net_metrics.csv`.
- `net_metrics.csv` — your log (timestamp, download_mbps, upload_mbps, ping_ms).
- `plot_simple.py` — reads the CSV and shows **two graphs**:
  - **Throughput (Mbps)** — download & upload together.
  - **Latency (ms)** — ping to 8.8.8.8.

---

## Quick start

### 1) Install
```bash
pip install speedtest-cli pandas matplotlib
```

### 2) Collect Data
```bash
python data_fetch.py
```
Let it run for a while (Ctrl+C to stop). This creates/updates `net_metrics.csv`, e.g.:
```python-repl
timestamp,download_mbps,upload_mbps,ping_ms
2025-11-03T19:00:00,94.21,18.03,21
...
```
### 2) Plot the graphs
```bash
python plot_simple.py
```
---

## CSV schema

| column          | meaning                              |
| --------------- | ------------------------------------ |
| `timestamp`     | ISO time of the measurement          |
| `download_mbps` | download speed (megabits per second) |
| `upload_mbps`   | upload speed (megabits per second)   |
| `ping_ms`       | latency to `8.8.8.8` (milliseconds)  |




