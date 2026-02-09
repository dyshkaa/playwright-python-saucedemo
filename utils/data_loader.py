import json
from pathlib import Path

def load_products():
    base_path = Path(__file__).parent.parent
    file_path = base_path / "data" / "products.json"
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: file {file_path} is not found!")
        return []