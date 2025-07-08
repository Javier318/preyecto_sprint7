import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado del proyecto
st.title('Proyecto 7')

# Leer los datos
car_data = pd.read_csv('datasets/vehicles_us.csv')

# Botón para construir histograma
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para mostrar gráfica de dispersión
scatter_button = st.button('Mostrar gráfica de dispersión')
if scatter_button:
    st.write('Gráfica de dispersión: odometer vs. price')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)