import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def render_categoric_stats(df, variable):
    st.subheader(f"Análisis Categórico: {variable}")
    
    # 1. Lógica de Identificados vs Unknown
    df['is_unknown'] = df[variable].astype(str).str.upper() == 'UNKNOWN'
    
    st.markdown("**1. Proporción: Identificados vs No Identificados (UNKNOWN)**")
    
    # --- NUEVO: Tarjetas de valores exactos arriba del Gráfico 1 ---
    count_no_identificados = int(df['is_unknown'].sum())
    count_identificados = int((~df['is_unknown']).sum())
    
    col1, col2 = st.columns(2)
    col1.metric(f"{variable}s Identificados", f"{count_identificados:,}")
    col2.metric(f"{variable}s No Identificados", f"{count_no_identificados:,}")
    # ---------------------------------------------------------------

    estado_counts = df['is_unknown'].replace({True: 'No Identificados', False: 'Identificados'}).value_counts()
    
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    sns.barplot(x=estado_counts.index, y=estado_counts.values, palette=['#1f77b4', '#d62728'], ax=ax1)
    ax1.set_ylabel("Cantidad de Impactos")
    st.pyplot(fig1)

    # 2. Gráfico de los Identificados (Top 15)
    df_identificados = df[df['is_unknown'] == False].copy()
    
    st.divider()
    
    if not df_identificados.empty:
        st.markdown(f"**2. Top 15 de {variable}s (Excluyendo 'Unknown')**")
        
        # --- NUEVO: Tarjetas de valores exactos arriba del Gráfico 2 ---
        total_unicos = df_identificados[variable].nunique()
        top_1_nombre = df_identificados[variable].value_counts().index[0]
        top_1_valor = int(df_identificados[variable].value_counts().values[0])
        
        c1, c2 = st.columns(2)
        c1.metric(f"Total de {variable}s Distintos", f"{total_unicos:,}")
        c2.metric("El Más Frecuente", f"{top_1_nombre} ({top_1_valor:,} impactos)")
        # ---------------------------------------------------------------

        top_15 = df_identificados[variable].value_counts().head(15)
        
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        sns.barplot(x=top_15.values, y=top_15.index, palette='viridis', ax=ax2)
        ax2.set_xlabel("Cantidad de Impactos")
        ax2.set_ylabel(variable)
        st.pyplot(fig2)

        # 3. Lógica Exclusiva para la variable 'Aircraft'
        if variable == 'Aircraft':
            st.divider()
            st.markdown("**3. Clasificación por Tipo de Aeronave**")
            
            def clasificar_aeronave(modelo):
                m = str(modelo).upper()
                if any(x in m for x in ['B-', 'A3', 'BOEING', 'AIRBUS', 'EMB', 'CRJ', 'DC-']):
                    return 'Comercial'
                elif any(x in m for x in ['C-', 'F-', 'T-', 'MILITARY', 'UH-', 'AH-']):
                    return 'Militar'
                elif any(x in m for x in ['CESSNA', 'PIPER', 'BEECH', 'PA-', 'HAWKER']):
                    return 'Aviación General'
                else:
                    return 'Otros / Sin clasificar'
            
            df_identificados['Tipo_Aeronave'] = df_identificados[variable].apply(clasificar_aeronave)
            tipo_counts = df_identificados['Tipo_Aeronave'].value_counts()
            
            # --- NUEVO: Tarjetas de valores exactos arriba del Gráfico 3 ---
            # Creamos tantas columnas como categorías detectadas haya
            cols = st.columns(len(tipo_counts))
            for i, (tipo, cantidad) in enumerate(tipo_counts.items()):
                cols[i].metric(tipo, f"{int(cantidad):,}")
            # ---------------------------------------------------------------
            
            fig3, ax3 = plt.subplots(figsize=(8, 4))
            sns.barplot(x=tipo_counts.index, y=tipo_counts.values, palette='Set2', ax=ax3)
            ax3.set_ylabel("Cantidad de Impactos")
            st.pyplot(fig3)
    else:
        st.warning("No hay datos identificados para graficar.")