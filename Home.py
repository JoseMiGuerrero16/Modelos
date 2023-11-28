import streamlit as st
from streamlit.logger import get_logger
from utils.titulo_principal import show_title

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Apprende Custom Search",
        page_icon=":rocket:"
    )

    st.sidebar.write("Navegación")

    show_title()

    st.write(
        '''
    ### :rocket: Cómo usar la aplicación

    Para comenzar dirígete a la barra lateral izquierda y selecciona la opción de **Talleristas** o **Insumos**.
    En el apartado de **Talleristas** podrás buscar tallerista describiendo el tipo de taller que desees realizar
    y en el apartado de **Insumos** podrás buscar productos señalando su nombre.

    Finalmente, en el apartado de **Historial** aparecerán aquellos talleristas que hayas marcado con el símbolo :star: 
    y podrás eliminarlos con el símbolo :x:.
    '''
    )

if __name__ == "__main__":
    run()
