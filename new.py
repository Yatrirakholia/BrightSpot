'''# Function to import and run App 2
def run_app2():
    with st.spinner('Loading App 2...'):
        from  import app2
        app2()

# Function to import and run App 3
def run_app3():
    with st.spinner('Loading App 3...'):
        from app3.app3 import app3
        app3()

# Sidebar navigation
st.sidebar.title('Navigation')
selected_app = st.sidebar.selectbox(
    'Select App',
    ('App 1', 'App 2', 'App 3')
)

st.markdown(
        "<br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=GroundingDINO WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a> with the help of [GroundingDINO](https://github.com/IDEA-Research/GroundingDINO) built by [IDEA-Research](https://github.com/IDEA-Research)✨</center><hr>",
        unsafe_allow_html=True,
        )
        
# Run the selected app
if selected_app == 'App 1':
    run_app1()
elif selected_app == 'App 2':
    run_app2()
elif selected_app == 'App 3':
    run_app3()'''