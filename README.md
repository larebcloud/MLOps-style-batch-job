# 🚀 MLOps-Style Batch Job Pipeline

## 📌 Overview

This project implements a **production-style batch data pipeline** designed to simulate real-world MLOps workflows used in trading systems.

It processes OHLCV financial data, computes a rolling statistic, and generates a deterministic signal — all while ensuring **reproducibility, observability, and deployability**.

---

## 🎯 Key Features

* ⚙️ **Config-driven execution** (YAML-based)
* 🔁 **Deterministic results** using fixed random seed
* 📊 **Structured metrics output (JSON)**
* 🧾 **Comprehensive logging**
* 🐳 **Fully Dockerized (one-command execution)**
* 🚫 **Robust error handling**

---

## 🏗️ Project Structure

```bash
mlops-task/
│
├── run.py              # Main pipeline logic
├── config.yaml         # Config (seed, window, version)
├── data.csv            # Input OHLCV dataset
├── requirements.txt    # Dependencies
├── Dockerfile          # Container setup
├── metrics.json        # Output metrics
├── run.log             # Execution logs
└── README.md
```

---

## ⚙️ How It Works

### 1. Configuration

Loads parameters from `config.yaml`:

* `seed`: ensures reproducibility
* `window`: rolling mean window
* `version`: pipeline versioning

---

### 2. Data Processing

* Reads `data.csv`
* Validates input integrity
* Uses only the **`close` price**

---

### 3. Feature Engineering

Rolling mean calculation:

```python
rolling_mean = close.rolling(window)
```

---

### 4. Signal Generation

```python
signal = 1 if close > rolling_mean else 0
```

---

### 5. Metrics Computation

* `rows_processed`
* `signal_rate`
* `latency_ms`

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt

python run.py \
  --input data.csv \
  --config config.yaml \
  --output metrics.json \
  --log-file run.log
```

---

## 🐳 Run with Docker

```bash
docker build -t mlops-task .
docker run --rm mlops-task
```

---

## 📊 Sample Output

```json
{
  "version": "v1",
  "rows_processed": 10000,
  "metric": "signal_rate",
  "value": 0.4989,
  "latency_ms": 12,
  "seed": 42,
  "status": "success"
}
```

---

## 🔍 Observability

### Logs (`run.log`)

Includes:

* Job start/end timestamps
* Config validation
* Data loading
* Processing steps
* Metrics summary
* Error traces

---

## 🧪 Error Handling

Handles:

* Missing input file
* Invalid CSV format
* Empty dataset
* Missing `close` column
* Invalid configuration

👉 Always outputs a valid `metrics.json` (even on failure)

---

## 🔁 Reproducibility

* Controlled via config
* Fixed seed ensures identical outputs
* No randomness in computation pipeline

---

## 🧠 Design Philosophy

This project is intentionally designed to mimic:

* Financial signal pipelines
* Batch ML workflows
* Production data jobs

Focus areas:

* Simplicity with correctness
* Clear observability
* Deployment readiness

---

## 📦 Tech Stack

* Python 3.9
* Pandas
* NumPy
* PyYAML
* Docker

---

## 👤 Author

**Lareb Rehman**
Cloud & MLOps Enthusiast

---

## ⭐ Final Note

This implementation prioritizes **engineering reliability over complexity**, reflecting real-world MLOps systems where correctness, reproducibility, and deployment matter more than model sophistication.

---
