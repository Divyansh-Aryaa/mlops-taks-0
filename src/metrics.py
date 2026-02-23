
import json

def build_success_metrics(df, version, seed, latency):
    signal_rate = df["signal"].mean()

    return {
        "version": version,
        "rows_processed": int(len(df)),
        "metric":"signal_rate",
        "value": float(signal_rate),
        "latency_ms": int(latency),
        "seed": seed,
        "status": "success"
    }

def build_error_metrics(version, error_message):
    return{
        "version": version,
        "status": "error",
        "error_message": str(error_message),
    }

def write_metrics(metrics, output_path):
    with open(output_path, "w") as f:
        json.dump(metrics, f, indent=2)
       