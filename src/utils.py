"""Shared utility functions for the GraphRAG project."""

from pathlib import Path


def get_data_dir(phase: int = None) -> Path:
    """Get the data directory path.

    Args:
        phase: Phase number (1-4) for phase-specific output directory.
               If None, returns the main data directory.

    Returns:
        Path to the data directory.
    """
    base_path = Path(__file__).parent.parent / "data"

    if phase is None:
        return base_path

    if phase < 1 or phase > 4:
        raise ValueError("Phase must be between 1 and 4")

    return base_path / f"phase_{phase}_outputs"


def get_raw_data_dir() -> Path:
    """Get the raw data directory path.

    Returns:
        Path to the raw data directory.
    """
    return Path(__file__).parent.parent / "data" / "raw"
