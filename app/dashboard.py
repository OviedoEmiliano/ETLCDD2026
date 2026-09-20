import streamlit as st
import pandas as pd
from pathlib import Path

# Importamos los componentes
from components.stats_numeric import render_numeric_stats
from components.stats_categoric import render_categoric_stats

st.set_page_config(page_title="Análisis de Variables - FAA", layout="wide")

@st.cache_data
def cargar_datos():
    BASE_DIR = Path(__file__).resolve().parent.parent
    ruta_processed = BASE_DIR / "data" / "processed" / "database_clean.csv"
    return pd.read_csv(ruta_processed)

df = cargar_datos()

# ==========================================
# 1. NAVEGACIÓN SIDEBAR
# ==========================================
st.sidebar.title("⚙️ Navegación")
st.sidebar.markdown("Seleccione una variable principal:")

columnas_foco = [
    'Incident Year', 
    'Incident Month', 
    'Incident Day', 
    'Operator', 
    'Aircraft'
]

columnas_disponibles = [col for col in columnas_foco if col in df.columns]

if columnas_disponibles:
    variable_seleccionada = st.sidebar.radio("Variable a analizar:", columnas_disponibles)
else:
    st.sidebar.error("No se encontraron las columnas en el CSV.")
    st.stop()

# ==========================================
# 2. MAIN LAYOUT Y ENRUTAMIENTO
# ==========================================
st.title(f"📊 Análisis de: {variable_seleccionada}")
st.divider()

# Lógica de renderizado (El "condicional de React")
if pd.api.types.is_numeric_dtype(df[variable_seleccionada]):
    render_numeric_stats(df, variable_seleccionada)
else:
    render_categoric_stats(df, variable_seleccionada)