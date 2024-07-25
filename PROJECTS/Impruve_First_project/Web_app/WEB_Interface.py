import streamlit as st
from Functions import get_dat_n, put_dat

st.title("CRUD WEB Application")
st.write("Data lists.")
st.write("Data from text file")

get_data = get_dat_n()
for dat in get_data:
    st.checkbox(dat)

st.text_input(label="", placeholder="Enter new data")
st.button(label="ADD")