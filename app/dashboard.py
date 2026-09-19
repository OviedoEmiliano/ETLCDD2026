"""Dashboard interactivo para explorar los datos procesados."""

from pathlib import Path

import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

st.set_page_config(page_title="Dashboard ETL", page_icon="chart", layout="wide")
st.title("Dashboard de datos procesados")

files = sorted(PROCESSED_DIR.glob("*.csv"))
if not files:
    st.info("No hay datasets procesados. Ejecuta primero: python src/main_etl.py")
    st.stop()

selected_file = st.sidebar.selectbox("Dataset", files, format_func=lambda path: path.name)
dataframe = pd.read_csv(selected_file)

st.metric("Filas", len(dataframe))
st.metric("Columnas", len(dataframe.columns))
st.dataframe(dataframe, use_container_width=True)

numeric_columns = dataframe.select_dtypes(include="number").columns.tolist()
if numeric_columns:
    st.subheader("Resumen numérico")
    st.bar_chart(dataframe[numeric_columns].describe().T["mean"])
