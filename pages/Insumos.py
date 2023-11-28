import streamlit as st
import requests
from utils.titulo_principal import show_title

def clear_text():
    st.session_state["desc"] = ""

def display_info_card(tallerista):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(tallerista["imagen"], width=128)
    with col2:
        st.markdown(f'''###### **{tallerista["nombre"]}**''')
        st.markdown(f'''Precio: {tallerista["precio"]:,} $''')
        st.markdown(f'''[enlace de compra]({tallerista["enlace"]})''')
    st.markdown('''---''')

st.set_page_config(
    page_title="ACS - Búsqueda de Insumos", 
    page_icon=":shopping_trolley:"
)

show_title()

st.markdown("### :shopping_trolley: Búsqueda de Insumos")

desc = st.text_input("Introduzca el nombre del producto que desee buscar:", key="desc")


if desc is not None and desc != '':
    with st.spinner("Buscando insumos..."):
        insumos = requests.get('http://localhost:8000/buscar/insumos/', params={"prompt": desc}).json()
        if insumos is None:
            st.error("No se encontraron insumos con ese nombre, intente con otro.")
        else:
            with st.expander(f"Mostrar {len(insumos)} productos."):
                for insumo in insumos:
                    display_info_card(insumo)
    _, col2, _ = st.columns([0.75, 1, 0.75])
    with col2:
        st.button("Limpiar búsqueda", on_click=clear_text)