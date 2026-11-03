import streamlit as st
import webbrowser
st.title("BCAS Login System")
adminpass=st.text_input("password")
st.write(adminpass)
if adminpass=="bc123":
    webbrowser.open_new_tab("https://smart-class.streamlit.app/")
if adminpass==None:
    st.write("Please enter your password.")
else:
    st.error("Please enter a valid password.")