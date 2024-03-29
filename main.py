import streamlit as st
from streamlit_option_menu import option_menu
import home, replace,endpoints,about,param,crt,urls,index


class MultipApp:
    def __init__(self):
        self.apps = []
    
    def run():
        st.set_page_config(
        page_title="HackinSec",
        layout="wide",
        page_icon="https://dorks.hackinsec.com/HACKINSEC-11-16-2023.gif"
    )
        hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
                """
        st.markdown("""
        <style>
               .block-container {
                    padding-top: 0.4rem;
                }
        </style>
        """, unsafe_allow_html=True)

        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

        with st.sidebar:
            st.image(image="https://dorks.hackinsec.com/HACKINSEC-11-16-2023.gif")
            app = option_menu("HackinSec Tools", ["Home","Google Dorker", 'Crt.sh Extractor','Param Extractor', 'Endpoint Extractor', 'Replacer','Bulk URL Opener', 'About'], 
                icons=['house','rocket-takeoff', 'receipt-cutoff','scissors', 'box-arrow-up-right','arrow-counterclockwise','link-45deg','info-square'], menu_icon="cpu", default_index=0)
            st.text(">>>> Developed By: 𝝘𝝝𝝜𝗦𝝨𝗖 <<<<<")
            st.markdown("[![Buy me a Coffee](https://i.imgur.com/thJhzOO.png)](https://buymeacoffee.com/rohsec)")

        if app=="Home":
            index.app()    
        if app=="Google Dorker":
            home.app()
        if app=="Crt.sh Extractor":
            crt.app()
        if app=="Param Extractor":
            param.app()
        if app=="Replacer":
            replace.app()
        if app=="Endpoint Extractor":
            endpoints.app()
        if app=="Bulk URL Opener":
            urls.app()
        if app=="About":
            about.app()

    run()