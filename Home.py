import streamlit as st
from streamlit_option_menu import option_menu
import os

#for webpage title
st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)
st.title("BrightSpot")

#for sidebar
with st.sidebar:
    selected = option_menu(
        menu_title= "Main Menu",
        options = ["Home" , "Object Detection" , "Low Light Enhancer" , "Background Remover", "SAM"],
        icons = ["house", "back", "lightbulb-fill", "magic" , "stars"],
        menu_icon = "cast",
        default_index= 0,
    )

#running the objectdetection web app
def run_app1():
    with st.spinner('Loading App 1...'):
        from app1.objectdetection import objectdetection
        objectdetection()


#running the lowlightenhancer web app
def run_app2():
    with st.spinner('Loading App 2...'):
        from app2.lowlightenhancer import lowlightenhancer
        lowlightenhancer()

##running the backgroundremove web app
def run_app3():
    with st.spinner('Loading App 3...'):
        from app3.backgroundremove import backgroundremove
        backgroundremove()

def run_app4():
    with st.spinner('Loading App 4...'):
        from app4.SAM import SAM
        SAM()

if selected == "Home":
    #st.title(f"{selected}")
    pass
if selected == "Object Detection":
    run_app1()
if selected == "Low Light Enhancer":
    run_app2()
if selected == "Background Remover":
    run_app3()
if selected == "SAM":
    run_app4()
# Link to app2.py
#link = '[ObjectDetection](http://localhost:8501/?app=Zero-shot-object-detection-Streamlit/objectdetection.py)'
#st.markdown(link, unsafe_allow_html=True)







