import streamlit as st

st.write("hello! Kunle")

st.markdown("""
<style>
    .stTextInput > label {
        font-size:200px;
        font-weight:bold;
        color: white;
        background:linear-gradient(to bottom, #3399ff 0%,#00ffff 100%);
        border: 2px;
        border-radius: 3px;
    }

    [data-baseweb="base-input"]{
        background:linear-gradient(to bottom, #3399ff 0%,#00ffff 100%);
        border: 2px;
        border-radius: 3px;
    }

    input[class]{
        font-weight: bold;
        font-size:120%;
        color: black;
        bg-color: white;
    }
</style>
""", unsafe_allow_html=True)

firstname = st.text_input("name", value="", placeholder="John", key="firstname")
lastname = st.text_input("name", value="", placeholder="Doe", key="lastname")

st.write(firstname)
