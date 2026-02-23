# ML/MLOps PrimetradeAI Task 0

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Status](https://img.shields.io/badge/Status-Success-brightgreen)
![MLOps](https://img.shields.io/badge/MLOps-Batch%20Pipeline-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview
This project implements a minimal MLOps-style batch pipeline that demonstrates:

- Reproducibility (config-driven + seed)
- Observability (structured logs + metrics JSON)
- Deployment readiness (Dockerized execution)

The pipeline loads OHLCV data, computes a rolling mean on `close`, generates binary trading signals, and outputs structured metrics.

---

## Project Structure

run.py
config.yaml
data.csv
requirements.txt
Dockerfile
src/


---

## Local Run

python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log

## Build:

docker build -t mlops-task .

## Run:

docker run --rm mlops-task


## Example Output

{

  "version": "v1",
  
  "rows_processed": 10000,
  
  "metric": "signal_rate",
  
  "value": 0.0,
  
  "latency_ms": 30,
  
  "seed": 42,
  
  "status": "success"
  
}

