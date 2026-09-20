# ✈️ Análisis de Incidentes Aéreos con Fauna (FAA Bird Strikes)

Proyecto integral de Ciencia de Datos que implementa un pipeline ETL (Extracción, Transformación y Carga) en Python y un dashboard analítico modular utilizando Streamlit. Analiza más de 174.000 registros históricos para identificar tendencias estacionales, operadores más afectados y riesgos por tipo de aeronave.

## 📂 Estructura del Proyecto

La arquitectura del proyecto sigue las mejores prácticas de modularidad, separando la lógica de procesamiento (Back-end) de las vistas interactivas (Front-end):

- `data/raw/`: Datasets originales crudos (ignorado en Git por su peso).
- `data/processed/`: Datasets limpios generados por el pipeline ETL listos para consumo.
- `notebooks/01_exploracion.ipynb`: Exploración estadística inicial y feature engineering paso a paso con Pandas.
- `src/`: Lógica del pipeline de datos.
  - `extract.py`: Lectura y validación de archivos CSV.
  - `transform.py`: Limpieza y transformación de DataFrames (Feature Engineering).
  - `main_etl.py`: Orquestador principal que ejecuta el proceso ETL con gestión de rutas dinámicas mediante `pathlib`.
- `app/`: Interfaz de usuario analítica.
  - `dashboard.py`: Archivo principal (enrutador) del dashboard en Streamlit.
  - `components/`: Módulos de renderizado visual (inspirados en la estructura de componentes de React).
    - `stats_numeric.py`: Vistas y gráficos de tendencias temporales (Años, Meses).
    - `stats_categoric.py`: Vistas y rankings de entidades (Operadores, Aeronaves).

## ⚙️ Instalación y Configuración

1. Clonar el repositorio y crear un entorno virtual:
```bash
git clone [https://github.com/OviedoEmiliano/ETLCDD2026.git](https://github.com/OviedoEmiliano/ETLCDD2026.git)
cd ETLCDD2026
python -m venv .venv
```

2. Activar el entorno virtual:
- En Windows: `.venv\Scripts\activate`
- En Linux o macOS: `source .venv/bin/activate`

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## ⚠️ Configuración de los Datos (Paso Crucial)

Debido a las políticas de límite de tamaño de GitHub, el dataset original (`database.csv` con +174k registros) **no está incluido** en este repositorio. 

Para ejecutar el proyecto localmente:
1. Descargue el dataset oficial de Bird Strikes de la FAA (o provisto en su entorno).
2. Coloque el archivo descargado exactamente en la ruta: `data/raw/database.csv`.

## 🚀 Uso

1. **Ejecutar el proceso ETL:**
   Procesa los datos crudos y genera el dataset analítico en la carpeta `processed`.
```bash
python src/main_etl.py
```

2. **Iniciar el Dashboard interactivo:**
   Levanta el servidor local de Streamlit para visualizar las métricas y gráficos.
```bash
streamlit run app/dashboard.py
```