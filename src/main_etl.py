from extract import extract_csv
from pathlib import Path

def ejecutar_etl():
    print("Iniciando proceso ETL...")
    
    # Construimos la ruta base del proyecto automáticamente
    # __file__ es este script. parent.parent nos lleva de 'src' a 'ETL'
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    # 1. Extracción
    ruta_raw = BASE_DIR / "data" / "raw" / "database.csv"
    print(f"Extrayendo datos desde: {ruta_raw}")
    df = extract_csv(str(ruta_raw))
    
    # 2. Transformación
    print("Fase de transformación omitida temporalmente...")
    
    # 3. Carga (Load)
    ruta_processed = BASE_DIR / "data" / "processed" / "database_clean.csv"
    
    # Aseguramos que la carpeta de destino exista para evitar el OSError
    ruta_processed.parent.mkdir(parents=True, exist_ok=True)
    
    df.to_csv(ruta_processed, index=False)
    print(f"ETL completado. Dataset guardado en: {ruta_processed}")

if __name__ == "__main__":
    ejecutar_etl()