import streamlit as st
import pandas as pd

import datetime

st.subheader("filtrar datos y capturar datos")
st.write("el procesamiento de datos a traves ciencia de datos usando Streamlit de python")

dfDatos = pd.read_csv("http://raw.githubusercontent.com/gcastano/datasets/main/gapminder_data.csv")

st.metric("***Registros totales***", len(dfDatos))
st.dataframe(dfDatos, use_container_width=True)
