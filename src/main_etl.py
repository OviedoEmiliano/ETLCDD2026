"""Punto de entrada para ejecutar el proceso ETL completo."""

from pathlib import Path

from extract import extract_csv

PROJECT_ROOT = Path("data/raw/database.csv").resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

def main() -> None:
    """Extrae, transforma y guarda los datasets procesados."""
    df = extract_csv(RAW_DIR)

if __name__ == "__main__":
    main()
