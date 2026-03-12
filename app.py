import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="ARLINOST Admin", layout="wide")

# 1. Simulación de Base de Datos de Trabajadores
# En el futuro, esto se cargará desde un archivo CSV o base de datos
data = {
    'Trabajador': ['Juan Perez', 'Ricardo Gomez', 'Luis Torres', 'Matias Sosa'],
    'Rating': [4.9, 4.2, 3.8, 4.5],
    'Seguro AP': ['Vigente', 'Vigente', 'Vigente', 'Vencido'],
    'Herramientas': ['Completas', 'Completas', 'Básicas', 'Completas'],
    'Trabajos Realizados': [150, 85, 40, 92]
}

df = pd.DataFrame(data)

# --- INTERFAZ DE LA APP ---
st.title("🚀 ARLINOST - Panel de Gestión Logística")
st.markdown("""
Esta plataforma permite optimizar la asignación de servicios basándose en el 
**Rating de confianza** y el **Cumplimiento legal** de los prestadores.
""")

st.sidebar.header("Filtros de Control")
solo_seguro_ok = st.sidebar.checkbox("Mostrar solo con Seguro Vigente", value=True)

# 2. Lógica de asignación
st.write("---")
st.subheader("📍 Nueva Solicitud: Desmalezamiento en Barrio 'El Ombú'")

# Filtrado lógico
df_filtrado = df.copy()
if solo_seguro_ok:
    df_filtrado = df_filtrado[df_filtrado['Seguro AP'] == 'Vigente']

# Ordenar por el mejor Rating
disponibles = df_filtrado.sort_values(by='Rating', ascending=False)

if st.button('Asignar Mejor Prestador'):
    if not disponibles.empty:
        mejor = disponibles.iloc[0]
        st.success(f"✅ **Prestador Asignado:** {mejor['Trabajador']}")
        st.info(f"**Puntaje:** {mejor['Rating']} ⭐ | **Experiencia:** {mejor['Trabajos Realizados']} servicios finalizados.")
        st.balloons()
    else:
        st.error("No hay prestadores disponibles que cumplan con los requisitos de seguro.")

# 3. Visualización para los socios
st.write("---")
st.subheader("📊 Red de Prestadores")
st.table(df.style.highlight_max(axis=0, subset=['Rating'], color='#90EE90'))

st.caption("Los datos resaltados en verde indican al prestador con mejor desempeño actual.")
