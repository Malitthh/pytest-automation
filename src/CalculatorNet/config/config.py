from dataclasses import dataclass
from common.utils.env_utils import get_env, load_project_env

load_project_env("CalculatorNet")

@dataclass(frozen=True)
class CalculatorNetConfig:
    base_url: str

def get_config() -> CalculatorNetConfig:
    return CalculatorNetConfig(
        base_url=get_env("BASE_URL", default="https://www.calculator.net")
    )