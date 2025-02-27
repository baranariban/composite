import streamlit as st
from streamlit_option_menu import option_menu

import Grader_V1, Grader_V2, Grader_V3, Selector

st.set_page_config(
    page_title="CompApp",
)

class MultiApp:
    def __init__(self):
        self.apps = []
        self.logged_in = False

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def login(self, username, password):
        valid_users = {
            "bariban": "0v6260",
            "gunaydin": "0v6260",
        }
        if username in valid_users and password == valid_users[username]:
            self.logged_in = True
            return True
        else:
            return False

    def run(self):
        if not self.logged_in:
            username = st.sidebar.text_input("Username")
            password = st.sidebar.text_input("Password", type="password")
            if st.sidebar.button("Login"):
                if self.login(username, password):
                    st.sidebar.success("Login successful")
                else:
                    st.sidebar.error("Invalid username or password")

        if self.logged_in:
            with st.sidebar:
                app = option_menu(
                    menu_title='CompApp',
                    options=['Grader V1', 'Grader V2', 'Grader V3', 'Selector'],
                    icons=['house-fill', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                    menu_icon='chat-text-fill',
                    default_index=0,
                    styles={
                        "container": {"padding": "5!important", "background-color": 'black'},
                        "icon": {"color": "white", "font-size": "23px"},
                        "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                     "--hover-color": "blue"},
                        "nav-link-selected": {"background-color": "#02ab21"},
                    }
                )

                if app == "Grader V1":
                    Grader_V1.app()
                if app == "Grader V2":
                    Grader_V2.app()
                if app == "Grader V3":
                    Grader_V3.app()
                if app == "Selector":
                    Selector.app()

multi_app = MultiApp()

multi_app.add_app("Grader V1", Grader_V1.app)
multi_app.add_app("Grader V2", Grader_V2.app)
multi_app.add_app("Grader V3", Grader_V3.app)
multi_app.add_app("Selector", Selector.app)

multi_app.run()
