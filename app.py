import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis exploratorio de datos')
st.write('Por favor, seleccione el check box deseado para el analisis deseado')

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')
if build_histogram:  # si la casilla de verificación está seleccionada
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
build_scatter = st.checkbox('Construir un gráfico de dispersión')
if build_scatter:  # si la casilla de verificación está seleccionada
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
