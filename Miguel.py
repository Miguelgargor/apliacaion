import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import io
import base64


# Cambiar el título de la pestaña del navegador y añadir icono: (TÍTULO, URL ICONO (Subido a GitHub))
URL_ICONO= 'https://raw.githubusercontent.com/Miguelgargor/apliacaion/main/Imagen1.png'
st.set_page_config(page_title="HOLA", page_icon=URL_ICONO, layout="centered", initial_sidebar_state="auto")



def funcion_prueba(peso=0.5, color_especial_arista='red', color_normal_arista='black', tamaño_letra=8, tamaño_fig= (1,1)):
    # Create a graph
    G = nx.Graph()
    G.add_node('A'); G.add_node('B'); G.add_node('C'); G.add_node('D')
    G.add_edge('A', 'B', weight=peso); G.add_edge('B', 'C', weight=peso); G.add_edge('C', 'D', weight=peso)
    
    plt.figure(figsize=tamaño_fig)
    nx.draw(G, font_size=tamaño_letra, with_labels=True, 
            node_color=[('lightblue' if nodo in ['A', 'B'] else 'lightgreen') for nodo in G.nodes()],
            edge_color=[(color_especial_arista if edge == ('A', 'B') else color_normal_arista) for edge in G.edges()],
            width = [G[edge[0]][edge[1]]['weight'] for edge in G.edges()],
            pos= nx.spring_layout(G, k=0.5))
    st.pyplot(plt)
    nx.write_graphml(G, "grafo_prueba.graphml")

def main():
    st.title('Aplicación de prueba')
    #st.markdown("<b>Peso</b>", unsafe_allow_html=True)
    peso = st.slider('**Peso**', min_value=0.0, max_value=1.0, value=0.5, step=0.01) # Step is float
    color_especial_arista = st.color_picker('Color especial arista', value='#00FFAA')
    color_normal_arista = st.color_picker('Color normal arista', value='#00FFAA')
    tamaño_letra = st.slider('**Tamaño Fuente**', min_value=1, max_value=20, value=8, step=1) # Step is integer
    width = st.slider('Ancho figura', min_value=1.0, max_value=16.0, value=1.0, step=0.1) # Step is float
    height = st.slider('Alto figura', min_value=1.0, max_value=16.0, value=1.0, step=0.1) # Step is float

    if st.button('Crear el Grafo'):
        G = funcion_prueba(peso, color_especial_arista, color_normal_arista, tamaño_letra, (width, height))
        buffer = io.BytesIO()
        nx.write_graphml(G, buffer)
        buffer.seek(0)
        b64 = base64.b64encode(buffer.read()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="graph.graphml">Descargar el Grafo en un archivo</a>'
        st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
