import json
from typing import Any

def read_json_file(file_path: str) -> Any:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file no found: {file_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error to parse JSON: {file_path} — {e}")


def write_json_file(file_path: str, data: Any) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)