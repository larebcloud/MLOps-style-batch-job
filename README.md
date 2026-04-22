# 🚀 MLOps Batch Pipeline — Technical Assessment

## 📌 Overview

This project implements a **minimal production-style MLOps batch job** that processes financial time-series data and generates a simple trading signal.

It is designed to demonstrate:

* ✅ **Reproducibility** (config-driven + deterministic execution)
* ✅ **Observability** (structured logs + metrics)
* ✅ **Deployment readiness** (Dockerized, one-command execution)

---

## ⚙️ Problem Statement

Given OHLCV market data (`data.csv`), the system:

1. Loads configuration from YAML
2. Computes a rolling mean on the `close` price
3. Generates a binary signal:

   * `1` → if `close > rolling_mean`
   * `0` → otherwise
4. Outputs structured metrics and logs

---

## 🏗️ Project Structure

```
mlops-task/
│
├── run.py              # Main pipeline script
├── config.yaml         # Configuration (seed, window, version)
├── data.csv            # Input dataset (OHLCV)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container setup
├── README.md           # Documentation
├── metrics.json        # Sample output
├── run.log             # Sample logs
```

---

## ▶️ How to Run

### 🔹 Run Locally

```bash
pip install -r requirements.txt

python run.py \
  --input data.csv \
  --config config.yaml \
  --output metrics.json \
  --log-file run.log
```

---

### 🐳 Run with Docker (Recommended)

```bash
docker build -t mlops-task .
docker run --rm mlops-task
```

✔ No manual setup required
✔ Fully reproducible environment

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

## 📈 Metrics Explained

| Metric         | Description                   |
| -------------- | ----------------------------- |
| rows_processed | Total rows in dataset         |
| signal_rate    | Mean of generated signals     |
| latency_ms     | Total execution time          |
| seed           | Ensures deterministic results |

---

## 🔍 Observability

### Logs (`run.log`) include:

* Job start & end timestamps
* Config validation
* Data loading status
* Processing steps
* Metrics summary
* Error handling

---

## 🧪 Error Handling

The pipeline gracefully handles:

* Missing/invalid input files
* Empty datasets
* Missing `close` column
* Invalid configuration

In case of failure:

* `metrics.json` is still generated
* Error message is logged and returned

---

## 🔁 Reproducibility

* Controlled via `config.yaml`
* Seed ensures deterministic outputs
* Same input → same results every run

---

## 🧠 Design Choices

* **Pandas** for efficient data processing
* **Argparse** for CLI flexibility
* **Logging module** for structured observability
* **Docker** for environment consistency

---

## 🏁 Evaluation Alignment

This implementation directly addresses:

* ✔ Deterministic execution
* ✔ Clean CLI interface
* ✔ Structured metrics output
* ✔ Robust error handling
* ✔ Docker-based deployment

---

## 📬 Author

**Lareb Rehman**
MLOps / Cloud Enthusiast

---

## ⭐ Notes

This project simulates a real-world batch pipeline similar to those used in:

* Trading signal generation
* Data processing systems
* Production ML workflows

---
