import streamlit as st
from rembg import remove
from PIL import Image
import numpy as np

def backgroundremove():
    main_image = Image.open('app2/static/main_banner.png')

    upload_path = "app3/images/"
    download_path = "app3/results/"

    st.image(main_image,use_column_width='auto')
    st.title(" Background Remover ")


    col1, col2 = st.columns(2)

    uploaded_file = st.file_uploader("Load Image", accept_multiple_files =True)
    
    if uploaded_file:
        for image in uploaded_file:
            with Image.open(image) as img:
                col1.header("Original Image")
                col1.image(img)

                output = remove(img)
                col2.header("Output Image")
                col2.image(output)
