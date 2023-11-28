import streamlit as st
import requests
from utils.titulo_principal import show_title

st.set_page_config(
    page_title="ACS - Historial",
    page_icon=":book:"
)

show_title()

st.markdown("### :star: Marcadores")

def display_info_card(info):
    col1, col2, col3 = st.columns([1, 4, .5])

    with col1:
        st.image(info["foto_perfil"], width=96)

    with col2:
        st.markdown(f'''###### {info["nombre"]}''')
        st.markdown(f'''LinkedIn: {info['linkedin']}''')

    with col3:
        st.checkbox(":x:", key=info["linkedin"])

def delete_selected_profiles(talleristas):
    perfiles_seleccionados = [
        tallerista["linkedin"] for tallerista in talleristas if st.session_state.get(tallerista["linkedin"])
    ]

    if perfiles_seleccionados:
        response = requests.delete('http://localhost:8000/talleristas/', json=perfiles_seleccionados)
        if response.status_code == 200:
            st.sidebar.success('Talleristas eliminados con éxito.')
            st.rerun()
        else:
            st.sidebar.error('Hubo un problema al eliminar los talleristas.')

def show_saved_bookmarks():
    with st.spinner("Cargando marcadores..."):
        response = requests.get('http://localhost:8000/talleristas/')
        if response.status_code == 200:
            if response.json().__len__() == 0:
                st.success("No hay marcadores guardados.")
            else:
                with st.form("Marcadores"):
                    saved_talleristas = response.json()
                    for tallerista in saved_talleristas:
                        display_info_card(tallerista)
                    _, col2, _ = st.columns([0.75, 1, 0.75])
                    with col2:
                        submitted = st.form_submit_button("Eliminar talleristas seleccionados")
                    if submitted:
                        delete_selected_profiles(saved_talleristas)
        else:
            st.error("Error al cargar los marcadores.")

show_saved_bookmarks()