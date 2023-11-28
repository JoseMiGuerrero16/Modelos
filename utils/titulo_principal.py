import streamlit as st

def show_title():
    st.markdown(
        """
        <style>
        #main-title {
            font-size: 3em;
            font-weight: 700;
            background-image: linear-gradient(to right, #FF69B4, #FFFF00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        strong {
            color: #FFA073;
        }
        """,
        unsafe_allow_html=True
    )

    st.write('<p id="main-title">Apprende Custom Search.</p>', unsafe_allow_html=True)
