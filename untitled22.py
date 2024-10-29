import pandas as pd
import numpy as np
import streamlit as st


archivo = 'adsblog_res.csv'
def cargar_datos(archivo):
    #Carga y Filtrado de Datos
    data = pd.read_csv(archivo,header = None,names =['MSG','TIPO','C1','C2','IDENT','C3','Fecha_1','Hora_1','Fecha_2','Hora_2','ICAO','ALT','VEL','C4','LAT','LON','C5','C6','C7','C8','C9','C10'] )
    main = data[['MSG','TIPO','IDENT','Fecha_1','Hora_1','Fecha_2', 'Hora_2' ,'ICAO','ALT','VEL','LAT','LON']]
    return main





st.title('Mi primerra aplicación de Streamlit')
st.header('!Hola, Streamlit!')
st.write('Esto es una aplicación simple')
st.image('logo.png')
if st.button('Presiona Aqui',key = 1):
    st.write('Has presionado el botón')

input = st.text_input('Escribe algo',key = 2)
st.write('Escribiste:', input)

st.sidebar.title('Mi Primera barra lateral de Streamlit')
st.sidebar.header('!Hola, Barra Lateral!')
st.sidebar.write('Esto es una barra lateral')
st.sidebar.image('logo.png')

if st.sidebar.button('Presiona Aqui',key = 4):
    st.sidebar.write('Has presionado el botón')

input = st.sidebar.text_input('Escribe algo',key = 3)
st.sidebar.write('Escribiste:', input)



main = cargar_datos(archivo)
msg_counts = main.groupby('TIPO')['MSG'].count()
st.bar_chart(msg_counts.index, msg_counts.values,x_label = 'Tipos de mensaje', y_label = 'Cantidad')
