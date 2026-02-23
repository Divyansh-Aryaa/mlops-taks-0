
import yaml
import numpy as np

def load_config(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    required = ["seed","window","version"]

    for key in required:
        if key not in config:
            raise ValueError(f"Missing config key: {key}")
    np.random.seed(config["seed"])
    return config        