import os
from pathlib import Path
from typing import Dict

# Project root directory reference
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"


def _read_env_file() -> Dict[str, str]:
    """Return KEY=VALUE pairs from the local .env file (empty dict if the file is missing)."""
    values: Dict[str, str] = {}
    if not ENV_FILE.exists():
        return values
    with open(ENV_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            values[key.strip()] = val.strip().strip("\"'")
    return values


def get_credentials() -> Dict[str, str]:
    """
    Return the test account username and password, read ONLY from the .env file.
    Raises a clear error if either value is missing. Never prints the values.
    """
    env = _read_env_file()
    username = env.get("UBL_USERNAME", "")
    password = env.get("UBL_PASSWORD", "")

    missing = [name for name, val in (("UBL_USERNAME", username), ("UBL_PASSWORD", password)) if not val]
    if missing:
        raise RuntimeError(
            f"Missing {', '.join(missing)} in {ENV_FILE}. "
            "Copy .env.example to .env and fill in your test account values."
        )

    return {"username": username, "password": password}


class Settings:
    """Non-secret settings. Defaults below; can be overridden by shell environment variables."""
    APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
    APP_PACKAGE = os.getenv("APP_PACKAGE", "app.com.brd")
    APP_ACTIVITY = os.getenv("APP_ACTIVITY", "app.com.brd.presentation.main.MainActivity")
    DEVICE_NAME = os.getenv("DEVICE_NAME", "Galaxy A51")
    UDID = os.getenv("DEVICE_UDID", "")
