import streamlit as st
import webbrowser

def open_urls_in_tabs(urls):
    for url in urls:
        webbrowser.open_new_tab(url)


def app():
    st.header(
        "🔗 Open URLs in New Tabs",
        divider=True
    )
    # st.title("Open URLs in New Tabs 🔗")
    urls = st.text_area("Enter URLs (one per line)", height=200,disabled=True)
    urls_list = [url.strip() for url in urls.split('\n') if url.strip()]

    if st.button("Open URLs in New Tabs",disabled=True):
        if urls_list:
            with st.spinner("Opening URLs..."):
                open_urls_in_tabs(urls_list)
            st.success("URLs opened successfully in new tabs!")
            st.snow()
        else:
            st.warning("Please enter at least one URL.")
    st.info("🚧 Work In Progress: This tool is coming soon...")