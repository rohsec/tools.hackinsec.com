import streamlit as st

def app():
    st.snow()
    st.image("https://dorks.hackinsec.com/HACKINSEC-11-16-2023.gif",)
    # st.header("",divider=True)
    st.write("Hello there 👋 , Welcome to tools.hackinsec.com - A Bug Bounty Tool Kit for Hackers by Hackers <3")
    st.write("""Unlock the full potential of your bug hunting journey with our comprehensive suite of utility tools designed for hackers and bug bounty hunters.
          This tool kit is under continous development and new tools are being added every other day. Currently, the tool kit offers the following set of utility tools:""")
    st.markdown("""
>Google Dorker
            
> Crt.sh Subdomian Extractor       
                 
>Parameter Extractor
            
>Endpoint Extractor    
            
>Bulk URL Open
            
>Word Replacer""")
    st.divider()
    st.write("Tool Created By: 𝝘𝝝𝝜𝗦𝝨𝗖 (https://twitter.com/rohsec)")
    st.write("If you appreciate the work I do, consider supporting my work! Your small contribution can help me continue my work for the community 🙌")
    st.link_button("☕ Buy me a Coffee",url="https://buymeacoffee.com/rohsec",type="primary")