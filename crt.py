import streamlit as st
import requests
import json

BASE_URL = "https://crt.sh/?q={}&output=json"
subdomains = set()
wildcardsubdomains = set()

def crtsh(domain):
    try:
        subdomains.clear()
        wildcardsubdomains.clear()
        response = requests.get(BASE_URL.format(domain), timeout=25)
        if response.ok:
            content = response.content.decode('UTF-8')
            jsondata = json.loads(content)
            for i in range(len(jsondata)):
                name_value = jsondata[i]['name_value']
                if name_value.find('\n'):
                    subname_value = name_value.split('\n')
                    for subname_value in subname_value:
                        if subname_value.find('*'):
                            if subname_value not in subdomains:
                                subdomains.add(subname_value)
                        else:
                            if subname_value not in wildcardsubdomains:
                                wildcardsubdomains.add(subname_value)
    except:
        st.error("Opps!! Techincial error occured.")

def app():
    st.title("Extract Subdomains from Crt.sh 🧾")
    inp=st.text_input("Target Domain",placeholder="Enter a domain here...")
    if st.button("Find Subdomains"):
        if(inp!=""):
            with st.spinner(text="Fetching subdomains..."):
                crtsh(inp)
                col1,col2=st.columns([1,1])
                col1.text_area("Fetched Subdomains", '\n'.join(sorted(subdomains)),key="crt",height=250)
                col2.text_area("WildCard Subdomains", '\n'.join(sorted(wildcardsubdomains)),key="crtW",height=250)

                    
                
        else:
            st.error("Please valdiate your input !!")