import streamlit as st
from streamlit_option_menu import option_menu
import Grader_V1, Grader_V2, Grader_V3, Selector

# Set page configuration
st.set_page_config(page_title="CompApp")

# Store login state in session
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login(username, password):
    """Check login credentials."""
    valid_users = {
        "bariban": "0v6260",
        "gunaydin": "0v6260",
    }
    if username in valid_users and password == valid_users[username]:
        st.session_state.logged_in = True
        return True
    return False

# Authentication
if not st.session_state.logged_in:
    st.sidebar.header("🔒 Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    
    if st.sidebar.button("Login"):
        if login(username, password):
            st.sidebar.success("✅ Login successful")
            st.experimental_rerun()  # Refresh to load menu after login
        else:
            st.sidebar.error("❌ Invalid username or password")

else:
    # Sidebar menu
    with st.sidebar:
        st.sidebar.header("📌 Navigation")
        app = option_menu(
            menu_title="CompApp",
            options=["Grader V1", "Grader V2", "Grader V3", "Selector"],
            icons=["house-fill", "trophy-fill", "chat-fill", "info-circle-fill"],
            menu_icon="chat-text-fill",
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": "black"},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {
                    "color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                    "--hover-color": "blue"
                },
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )

    # Load selected app
    if app == "Grader V1":
        Grader_V1.app()
    elif app == "Grader V2":
        Grader_V2.app()
    elif app == "Grader V3":
        Grader_V3.app()
    elif app == "Selector":
        Selector.app()

    # Logout button
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()  # Refresh to return to login screen
