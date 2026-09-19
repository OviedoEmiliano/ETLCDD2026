"""Funciones de extracción de datos para el proyecto ETL."""

from pathlib import Path

import pandas as pd


def extract_csv(file_path: str | Path) -> pd.DataFrame:
    """Lee un archivo CSV y devuelve un DataFrame."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"No existe la fuente de datos: {path}")
    return pd.read_csv(path)


def extract_folder(folder_path: str | Path) -> dict[str, pd.DataFrame]:
    """Lee todos los CSV de una carpeta, indexados por nombre de archivo."""
    folder = Path(folder_path)
    if not folder.exists():
        raise FileNotFoundError(f"No existe la carpeta de entrada: {folder}")

    files = sorted(folder.glob("*.csv"))
    return {file.stem: extract_csv(file) for file in files}
