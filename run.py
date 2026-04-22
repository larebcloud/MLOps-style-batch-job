import argparse
import yaml
import pandas as pd
import numpy as np
import time
import json
import logging
import sys


def setup_logging(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def write_metrics(output_path, data):
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--log-file", required=True)
    args = parser.parse_args()

    setup_logging(args.log_file)
    start_time = time.time()

    try:
        logging.info("Job started")

        # Load config
        with open(args.config, "r") as f:
            config = yaml.safe_load(f)

        seed = config.get("seed")
        window = config.get("window")
        version = config.get("version")

        if seed is None or window is None or version is None:
            raise ValueError("Invalid config structure")

        np.random.seed(seed)
        logging.info(f"Config loaded: seed={seed}, window={window}, version={version}")

        # Load dataset
        df = pd.read_csv(args.input)

        if df.empty:
            raise ValueError("Empty dataset")

        if "close" not in df.columns:
            raise ValueError("Missing 'close' column")

        logging.info(f"Rows loaded: {len(df)}")

        # Rolling mean
        df["rolling_mean"] = df["close"].rolling(window=window).mean()

        # Signal
        df["signal"] = (df["close"] > df["rolling_mean"]).astype(int)

        # Drop NaNs for signal rate
        valid_signals = df["signal"].dropna()

        signal_rate = valid_signals.mean()

        latency_ms = int((time.time() - start_time) * 1000)

        metrics = {
            "version": version,
            "rows_processed": len(df),
            "metric": "signal_rate",
            "value": round(float(signal_rate), 4),
            "latency_ms": latency_ms,
            "seed": seed,
            "status": "success"
        }

        write_metrics(args.output, metrics)

        logging.info(f"Metrics: {metrics}")
        logging.info("Job completed successfully")

        print(json.dumps(metrics, indent=4))
        sys.exit(0)

    except Exception as e:
        latency_ms = int((time.time() - start_time) * 1000)

        error_metrics = {
            "version": "v1",
            "status": "error",
            "error_message": str(e)
        }

        write_metrics(args.output, error_metrics)

        logging.error(f"Error: {str(e)}")
        print(json.dumps(error_metrics, indent=4))
        sys.exit(1)


if __name__ == "__main__":
    main()