import streamlit as st
from utils.titulo_principal import main_cfg
from utils.openai_api import description_filter
from utils.google_api import google_custom_search
from time import sleep
import requests

st.set_page_config(
    page_title="Búsqueda de Talleristas", 
    page_icon=":artist:"
)

main_cfg()

st.markdown("### :female-artist: Búsqueda de Talleristas")

descripcion_taller = st.text_input("Introduce una descripción del taller que deseas realizar:")

def on_save():
    s = st.sidebar.success("Guardando perfiles...")
    d = st.sidebar.empty()
    for i in range(100, 0, -1):
        d.progress(i)
        sleep(0.05)
    if i < 2:
        sleep(.5)
        s.empty()
        d.empty()

def display_info_card(info):
    col1, col2, col3 = st.columns([1, 4, .5])

    with col1:
        st.image(info["foto_perfil"], width=96)

    with col2:
        st.markdown(f'''###### {info["titulo"]}''')
        st.markdown(f'''LinkedIn: {info['enlace']}''')

    with col3:
        st.checkbox(":star:", key=info["enlace"])

def save_selected_profiles(talleristas):
    perfiles_seleccionados = [
        {
            "nombre": tallerista["titulo"],  # Asumiendo que "titulo" contiene el nombre del tallerista
            "linkedin": tallerista["enlace"],  # Asumiendo que "enlace" contiene la URL de LinkedIn
            "foto_perfil": tallerista["foto_perfil"]  # El nombre de este campo ya es correcto
        }
        for tallerista in talleristas if st.session_state.get(tallerista["enlace"])
    ]
    if perfiles_seleccionados:
        response = requests.post('http://localhost:8000/talleristas/', json=perfiles_seleccionados)
        if response.status_code == 200:
            st.success('Talleristas guardados con éxito')
        elif response.status_code == 409:
            st.warning('Algunos talleristas ya estaban guardados.')
        else:
            st.error('Hubo un problema al guardar los talleristas.')
        on_save()

if descripcion_taller:
    success = True
    with st.spinner("Filtrando la descripción..."):
        descripcion_filtrada = description_filter(descripcion_taller)
        if "[error]" in descripcion_filtrada[:7].lower():
            st.error(descripcion_filtrada[7:])
            success = False
    if success:
        with st.spinner("Buscando talleristas..."):
            sleep(1)
            talleristas = google_custom_search(descripcion_filtrada)
            with st.form(key="form_talleristas"):
                for tallerista in talleristas:
                    display_info_card(tallerista)
                col1, col2, col3 = st.columns([0.75, 1, 0.75])
                with col2:
                    submitted = st.form_submit_button("Guardar talleristas seleccionados")
                if submitted:
                    save_selected_profiles(talleristas)
