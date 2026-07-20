import streamlit as st
from utils.auth import signup, login, create_users_table

create_users_table()


def login_page():

    st.title("🔐 Login / Signup")

    tab1, tab2 = st.tabs(["Login", "Signup"])

    # ---------------- Login ----------------
    with tab1:

        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):

            if login(username, password):

                st.session_state["logged_in"] = True
                st.session_state["username"] = username

                st.success("✅ Login Successful")
                st.rerun()

            else:
                st.error("❌ Invalid Username or Password")

    # ---------------- Signup ----------------
    with tab2:

        username = st.text_input("Choose Username", key="signup_user")
        password = st.text_input("Choose Password", type="password", key="signup_pass")

        if st.button("Create Account"):

            if signup(username, password):

                st.success("✅ Account Created Successfully")

            else:

                st.error("Username already exists.")