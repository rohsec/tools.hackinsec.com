import streamlit as st

def app():
    st.title("Replace a Word 🔄")
    inp=st.text_area(label="Enter URLs (one per line):",height=200,placeholder="Enter your domains here...")
    orgi=st.text_input("Source",placeholder="Word to Replace...",)
    rep=st.text_input("Target",placeholder="Word to be Replaced...")
    if st.button("Replace"):
        if(inp!="" and orgi!="" and rep!=""):
            print("yes")
            out=inp.replace(orgi,rep)
            st.text_area("Result:",value=out,height=200)
        else:
            st.error("Please check all the required fields are filled properly !")