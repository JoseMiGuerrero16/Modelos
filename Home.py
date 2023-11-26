import streamlit as st
from streamlit.logger import get_logger
from utils.titulo_principal import main_cfg

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Apprende Custom Search",
        page_icon=":rocket:"
    )

    st.sidebar.write("Navegación")

    main_cfg()

    st.write(
    '''
    ### :rocket: Getting Started

    Para comenzar dirígete a la barra lateral izquierda y selecciona la opción de **Talleristas** o **Insumos**.
    En el apartado de **Talleristas** podrás buscar tallerista describiendo el tipo de taller que deseas realizar.
    En el apartado de **Insumos** podrás buscar insumos describiendo el tipo de producto que quieras adquirir.

    Finalmente, en el apartado de **Historial** aparecerán aquellos talleristas e insumos que hayas marcado con el símbolo :star:, y podrás eliminarlos con el símbolo :x:.
    '''
    )

if __name__ == "__main__":
    run()
