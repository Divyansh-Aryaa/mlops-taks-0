import pandas as pd

def load_data(input_path):
    try:
        
        df = pd.read_csv(input_path, sep=None, engine="python")
        df.columns = df.columns.str.strip().str.lower()

    except Exception as e:
        raise ValueError(f"Invalid CSV file not readable: {e}")

    if df.empty:
        raise ValueError("CSV file is empty")

    if "close" not in df.columns:
        raise ValueError(f"Missing required column: close. Found columns: {df.columns.tolist()}")

    return df