"""Utilities for reading and writing data files."""

import json
import yaml
from pathlib import Path
from typing import Any, Union


def load_json(file_path: Union[str, Path]) -> Any:
    """Load data from a JSON file.

    Args:
        file_path: Path to the JSON file.

    Returns:
        Loaded JSON data.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: Any, file_path: Union[str, Path], indent: int = 2) -> None:
    """Save data to a JSON file.

    Args:
        data: Data to save.
        file_path: Path where the JSON file will be saved.
        indent: Number of spaces for indentation (default: 2).
    """
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


def load_yaml(file_path: Union[str, Path]) -> Any:
    """Load data from a YAML file.

    Args:
        file_path: Path to the YAML file.

    Returns:
        Loaded YAML data.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_yaml(data: Any, file_path: Union[str, Path]) -> None:
    """Save data to a YAML file.

    Args:
        data: Data to save.
        file_path: Path where the YAML file will be saved.
    """
    with open(file_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
