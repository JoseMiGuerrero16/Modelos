import streamlit as st
from utils.titulo_principal import main_cfg
from utils.jumbo_webscrap import search_supply

st.set_page_config(
    page_title="Búsqueda de Insumos", 
    page_icon=":shopping_trolley:"
)

main_cfg()

st.markdown("### :shopping_trolley: Búsqueda de Insumos")

descripcion_insumo = st.text_input("Introduce el nombre del producto que quieras buscar:")

def display_info_card(info):
    col1, col2 = st.columns([1, 4])

    with col1:
        st.image(info["imagen"], width=128)

    with col2:
        st.markdown(f'''###### **{info["nombre"]}**''')
        st.markdown(f'''Precio: {info['precio']:,} $''')
        st.markdown(f'''Enlace: {info['enlace']}''')

if descripcion_insumo:
    num_page = 1
    success = True
    with st.spinner("Buscando insumos..."):
        insumos = search_supply(descripcion_insumo, num_page)
        if insumos is None:
            st.error("No se encontraron insumos con ese nombre, inténtalo con otro.")
        else:
            for insumo in insumos:
                display_info_card(insumo)
