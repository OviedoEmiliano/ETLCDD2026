import streamlit as st

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
    
    # Agrupamos contando cuántos impactos hubo por cada valor de la variable
    df_agrupado = df[variable].value_counts().sort_index()
    
    if variable == 'Incident Year':
        st.markdown("**Evolución Histórica (Tendencia Anual)**")
        # Gráfico de líneas para ver la tendencia a lo largo de los años
        st.line_chart(df_agrupado)
    else:
        st.markdown(f"**Distribución de Frecuencias (Estacionalidad por {variable})**")
        # Gráfico de columnas (barras verticales) para los meses o días
        st.bar_chart(df_agrupado)