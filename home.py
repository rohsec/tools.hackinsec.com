import streamlit as st

def app():
    st.title("Google Dorker 🚀")
    inp=st.text_input(label="Domain",placeholder="Enter a daomin...")
    if st.button("Update Domain"):
        if(inp==""):
            st.error("Enter a valid domain...")
        else:
            with open("dorks1.txt","r") as f1:
                xx=f1.readlines()
            f1.close()
            print(xx)
            for i in xx:
                if(i.startswith("#")):
                    st.subheader(i[3:].strip())
                elif(i.startswith(">")):
                    st.markdown((f"`{i[1:].replace('example.com',inp)}`"))
                # cols[1].link_button("➤",url=f"https://google.com/search?q={i[1:].replace('example.com',inp)}")
                else:
                    pass