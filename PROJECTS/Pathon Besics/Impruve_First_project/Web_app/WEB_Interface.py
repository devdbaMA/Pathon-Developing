import streamlit as st
from Functions import get_dat_n, put_dat

get_data = get_dat_n()


def ins_data():
    new_data = st.session_state["new_data"] + "\n"
    get_data.append(new_data)
    put_dat(get_data)
    st.session_state["new_data"] = ""  # Clear the input field after adding


st.title("CRUD Web Application")
st.write("Data lists:")
st.write("Data from text file")

for index, dat in enumerate(get_data):
    checkbox = st.checkbox(dat, key=dat)
    if checkbox:
        get_data.pop(index)
        put_dat(get_data)
        del st.session_state[dat]  # Corrected line to delete the session state entry
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter new data", on_change=ins_data, key="new_data")
