import streamlit as st
from PIL import Image

with st.expander("start camera"):
    # START THE CAMERA
    cam_info = st.camera_input("webcan")

if cam_info:
    # CREATE POLLOW IMAGE INSTANCE
    img = Image.open(cam_info)
    # CONVERT THE IMAGE
    gray_img = img.convert("L")

    st.image(gray_img)