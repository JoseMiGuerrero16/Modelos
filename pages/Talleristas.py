import streamlit as st
import requests
from utils.titulo_principal import show_title

st.set_page_config(
    page_title="ACS - Búsqueda de Talleristas", 
    page_icon=":artist:"
)

show_title()

st.markdown("### :female-artist: Búsqueda de Talleristas")

descripcion_taller = st.text_input("Introduzca una descripción del taller que desea realizar:")

def display_info_card(info):
    col1, col2, col3 = st.columns([1, 4, .5])
    with col1:
        st.image(info["foto_perfil"], width=96)
    with col2:
        st.markdown(f'''###### {info["titulo"]}''')
        st.markdown(f'''LinkedIn: {info['enlace']}''')
    with col3:
        st.checkbox(":star:", key=info["enlace"])
    st.markdown('''---''')

def save_selected_profiles(talleristas):
    perfiles_seleccionados = [
        {
            "nombre": tallerista["titulo"],
            "linkedin": tallerista["enlace"],
            "foto_perfil": tallerista["foto_perfil"]
        }
        for tallerista in talleristas if st.session_state.get(tallerista["enlace"])
    ]
    if perfiles_seleccionados:
        response = requests.post('http://localhost:8000/talleristas/', json=perfiles_seleccionados)
        if response.status_code == 200:
            st.success('Talleristas guardados con éxito.')
        elif response.status_code == 409:
            st.warning('Algunos talleristas ya estaban guardados.')
        else:
            st.error('Hubo un problema al guardar los talleristas.')

if descripcion_taller:
    success = True
    with st.spinner("Filtrando la descripción..."):
        descripcion_filtrada = requests.get(f'http://localhost:8000/filtrar/?prompt={descripcion_taller}').json()
        if "[error]" in descripcion_filtrada[:7].lower():
            st.error(descripcion_filtrada[7:])
            success = False
    if success:
        with st.spinner("Buscando talleristas..."):
            talleristas = requests.get('http://localhost:8000/buscar/talleristas/', params={"prompt": descripcion_filtrada}).json()
            if talleristas.__len__() == 0:
                st.error("No se encontraron talleristas para la descripción dada.")
            else:
                with st.form(key="form_talleristas"):
                    for tallerista in talleristas:
                        display_info_card(tallerista)
                    col1, col2, col3 = st.columns([0.75, 1, 0.75])
                    with col2:
                        submitted = st.form_submit_button("Guardar talleristas seleccionados")
                    if submitted:
                        save_selected_profiles(talleristas)
