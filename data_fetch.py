import csv, time, sys, subprocess
from datetime import datetime

CSV_PATH = "net_metrics.csv"
INTERVAL_SEC = 30  # keep it practical; speed tests every 5s are heavy

try:
    import speedtest  # from speedtest-cli
except ImportError:
    print("Install first: pip install speedtest-cli")
    sys.exit(1)

def ping_google_ms():
    is_win = sys.platform.startswith("win")
    cmd = ["ping", "-n", "1", "8.8.8.8"] if is_win else ["ping", "-c", "1", "8.8.8.8"]
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, timeout=8)
        if is_win:
            for line in out.splitlines():
                if "Average" in line and "ms" in line:
                    return float(line.split("=")[-1].replace("ms","").strip())
        else:
            for part in out.split():
                if part.startswith("time="):
                    return float(part.split("=")[1])
    except Exception:
        pass
    return None

def measure_speeds_mbps():
    st = speedtest.Speedtest()
    st.get_best_server()
    dl_mbps = round(st.download() / 1e6, 2)                 # Change from bits/s → Mbps
    ul_mbps = round(st.upload(pre_allocate=False) / 1e6, 2)  # Change from bits/s → Mbps
    return dl_mbps, ul_mbps

def ensure_header():
    try:
        with open(CSV_PATH, "r") as f:
            if f.readline().startswith("timestamp,"): return
    except FileNotFoundError:
        pass
    with open(CSV_PATH, "w", newline="") as f:
        csv.writer(f).writerow(["timestamp","download_mbps","upload_mbps","ping_ms"])

def main():
    ensure_header()
    print(f"Logging to {CSV_PATH} every {INTERVAL_SEC}s. Ctrl+C to stop.")
    try:
        while True:
            ts = datetime.now().isoformat(timespec="seconds")
            try:
                dl, ul = measure_speeds_mbps()
            except Exception as e:
                dl, ul = None, None
                print(f"[{ts}] speedtest error: {e}")
            ping = ping_google_ms()

            with open(CSV_PATH, "a", newline="") as f:
                csv.writer(f).writerow([ts, dl, ul, ping])

            print(f"[{ts}] DL={dl} Mbps  UL={ul} Mbps  Ping={ping} ms")
            time.sleep(INTERVAL_SEC)
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main()
