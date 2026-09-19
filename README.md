# proyecto_cdd

Proyecto de Ciencia de Datos con un flujo ETL en Python y un dashboard de Streamlit.

## Estructura

- `data/raw/`: datasets originales. No se sobrescriben.
- `data/processed/`: datasets limpios generados por el ETL.
- `notebooks/01_exploracion.ipynb`: exploracion paso a paso con Pandas.
- `src/extract.py`: lectura de archivos CSV.
- `src/transform.py`: limpieza y transformacion de DataFrames.
- `src/main_etl.py`: orquestacion del proceso ETL.
- `app/dashboard.py`: dashboard interactivo.

## Instalacion

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

En Linux o macOS, activa el entorno con `source .venv/bin/activate`.

## Uso

1. Coloca uno o varios archivos `.csv` en `data/raw/`.
2. Ejecuta el proceso ETL:

```bash
python src/main_etl.py
```

3. Inicia el dashboard:

```bash
streamlit run app/dashboard.py
```

4. Abre `notebooks/01_exploracion.ipynb` en VS Code o Jupyter para explorar los datos.
