import streamlit as st


def app():
    st.title("About ℹ️")
    st.text("Hi 👋! I am Rohit a.k.a rohsec. I am a full time BugBounty Hunter and HackerOne Ambassador.\nI like identifying vulnerabilities and helping organizations reinforce their defenses. \nI have ethically hacked and secured various big techs such as Sony, RedBull, BBC, Dutch Government etc.")
    st.image(image="https://i.postimg.cc/Jn2gYH24/rohsectemplatefont2.png")
    st.subheader("Socials")
    st.link_button("Twitter",type="secondary",url="https://twitter.com/rohsec")
    st.link_button("LinkedIn",type="secondary",url="https://linkedin.com/in/rohsec")
    st.subheader("Wall Of Fame")
    st.write("I have ethically hacked and secured various big techs such as Sony, RedBull, HackerOne, BBC, US-Dept. of Defense, Achmea, Dutch Government, SAP, Qiwi, Applovin etc.")
    st.image(image="https://i.postimg.cc/8P4FnBnZ/walloffame-WM.jpg")
    st.subheader("Support")
    st.write("If you appreciate the work I do, consider supporting my work! Your small contribution can help me continue my work for the community. Buy me a coffee 🙌")
    st.link_button("☕ Buy me a Coffee",url="https://buymeacoffee.com/rohsec",type="primary")