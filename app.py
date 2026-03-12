import streamlit as st
import pandas as pd

# 1. Simulación de Base de Datos de Trabajadores
data = {
    'Trabajador': ['Juan Perez', 'Ricardo Gomez', 'Luis Torres', 'Matias Sosa'],
    'Rating': [4.9, 4.2, 3.8, 4.5],
    'Seguro AP': ['Vigente', 'Vigente', 'Vigente', 'Vencido'],
    'Herramientas': ['Completas', 'Completas', 'Básicas', 'Completas'],
    'Trabajos Realizados': [150, 85, 40, 92]
}

df = pd.DataFrame(data)

st.title("🚀 ARLINOST - Panel de Asignación Logística")
st.subheader("Optimización de servicios por Rating y Seguridad")

# 2. Lógica de asignación
st.write("### Solicitud de nuevo servicio: Desmalezamiento en Barrio 'El Ombú'")

# Filtramos solo los que tienen seguro vigente
disponibles = df[df['Seguro AP'] == 'Vigente'].sort_values(by='Rating', ascending=False)

if st.button('Asignar Mejor Prestador'):
    mejor = disponibles.iloc[0]
    st.success(f"✅ Prestador Asignado: **{mejor['Trabajador']}**")
    st.info(f"Puntaje: {mejor['Rating']} ⭐ | Experiencia: {mejor['Trabajos Realizados']} servicios.")
    st.balloons()

# 3. Visualización para los socios
st.write("---")
st.write("### Estado de la Red de Prestadores")
st.dataframe(df.style.highlight_max(axis=0, subset=['Rating'], color='#90EE90'))# arlinostapp
Es una app que permite rankear a los proveedores 
