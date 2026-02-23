
import argparse
import time
import json

from src.logger import setup_logger
from src.config import load_config
from src.data import load_data
from src.processing import generate_signal
from src.metrics import (
    build_success_metrics,
    build_error_metrics,
    write_metrics
)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    parser.add_argument("--config")
    parser.add_argument("--output")
    parser.add_argument("--log-file")

    args = parser.parse_args()

    logger = setup_logger(args.log_file)

    start_time = time.time()

    try:
        logger.info("Job started")

        config = load_config(args.config)
        logger.info(f"Config loaded: {config}")

        df = load_data(args.input)
        logger.info(f"Rows loaded: {len(df)}")

        df = generate_signal(df, config["window"])
        logger.info("Rolling mean and signal generated")

        latency = (time.time() - start_time) * 1000

        metrics = build_success_metrics(
            df,
            config["version"],
            config["seed"],
            latency            
        )

        write_metrics(metrics, args.output)

        logger.info(f"Metrics: {metrics}")
        logger.info("Job completed successfully")

        print(json.dumps(metrics, indent=2))

    except Exception as e:

        logger.exception("Job failed")    
        version = "unknown"

        try:
            version = config.get("version", "unknown")
        except:
            pass

        metrics = build_error_metrics(version, str(e))
        write_metrics(metrics, args.output)

        print(json.dumps(metrics, indent=2))
        exit(1)
if __name__ == "__main__":
    main()            



