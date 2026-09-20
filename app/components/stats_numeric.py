import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def render_numeric_stats(df, variable):
    st.subheader(f"Estadísticas Numéricas: {variable}")
    
    # KPIs rápidos
    c1, c2, c3 = st.columns(3)
    c1.metric("Media (Promedio)", f"{df[variable].mean():.2f}")
    c2.metric("Mediana (Central)", f"{df[variable].median():.2f}")
    c3.metric("Rango", f"{df[variable].min()} - {df[variable].max()}")
    
    st.divider()
    
    # Lógica de Gráficos de Tiempo
    st.subheader("Visualización Temporal")
    
    if variable == 'Incident Year':
        df_agrupado = df[variable].value_counts().sort_index()
        st.markdown("**Evolución Histórica (Tendencia Anual)**")
        st.line_chart(df_agrupado)
        
    elif variable == 'Incident Day':
        st.markdown("**Distribución Operativa (Día de la Semana)**")
        
        # Validamos que existan las 3 columnas para armar una fecha real
        if all(col in df.columns for col in ['Incident Year', 'Incident Month', 'Incident Day']):
            temp_df = df[['Incident Year', 'Incident Month', 'Incident Day']].dropna().copy()
            temp_df.rename(columns={'Incident Year': 'year', 'Incident Month': 'month', 'Incident Day': 'day'}, inplace=True)
            
            # Convertimos a fechas
            fechas = pd.to_datetime(temp_df, errors='coerce').dropna()
            
            # Extraemos el día de la semana (En Pandas: 0=Lunes, 6=Domingo)
            mapa_dias = {
                6: 'Domingo', 0: 'Lunes', 1: 'Martes', 2: 'Miércoles', 
                3: 'Jueves', 4: 'Viernes', 5: 'Sábado'
            }
            dias_semana = fechas.dt.dayofweek.map(mapa_dias)
            
            # Contamos las frecuencias
            df_agrupado = dias_semana.value_counts()
            
            # Forzamos EXACTAMENTE el orden que pediste
            orden_dias = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
            df_agrupado = df_agrupado.reindex(orden_dias)
            
            # Armamos el gráfico con Seaborn para poner los números arriba
            fig, ax = plt.subplots(figsize=(10, 4))
            sns.barplot(x=df_agrupado.index, y=df_agrupado.values, palette='Blues_d', ax=ax)
            
            # Esta línea mágica es la que dibuja los números exactos arriba de cada barra
            ax.bar_label(ax.containers[0], fmt='%d', padding=3)
            
            ax.set_ylabel("Cantidad de Impactos")
            ax.set_xlabel("Día de la Semana")
            
            st.pyplot(fig)
        else:
            df_agrupado = df[variable].value_counts().sort_index()
            st.bar_chart(df_agrupado)
            
    else:
        df_agrupado = df[variable].value_counts().sort_index()
        st.markdown(f"**Distribución de Frecuencias (Estacionalidad por {variable})**")
        st.bar_chart(df_agrupado)