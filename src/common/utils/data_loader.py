import json
from pathlib import Path
from typing import Any

SRC_ROOT = Path(__file__).resolve().parents[2]

def load_test_data(project: str, section: str, filename: str) -> Any:
    data_path = SRC_ROOT / project / "testData" / section / filename

    if not data_path.exists():
        raise FileNotFoundError(f"Test data file not found: {data_path}")

    with data_path.open("r", encoding="utf-8") as f:
        return json.load(f)