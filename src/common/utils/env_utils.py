import os
from pathlib import Path
from dotenv import load_dotenv

SRC_ROOT = Path(__file__).resolve().parents[2]

def load_project_env(project: str) -> None:
    env_path = SRC_ROOT / project / "config" / ".env"
    load_dotenv(dotenv_path=env_path, override=False)

def get_env(key: str, default: str | None = None, required: bool = False) -> str:
    value = os.environ.get(key, default)

    if required and not value:
        raise RuntimeError(
            f"Missing required env var '{key}'. "
            f"Check the project's config/.env file (or .env.example)."
        )
    return value if value is not None else ""