import streamlit as st

# Streamlit App
st.title("MVP Application")
st.subheader("A Simple App with Login and Landing Page")

# Session State for Login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Login Page
if not st.session_state["logged_in"]:
    st.header("Login")
    phone_number = st.text_input("Enter your phone number", max_chars=10)
    if st.button("Login"):
        if phone_number:
            st.session_state["logged_in"] = True
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Please enter a valid phone number")
else:
    # Landing Page
    st.header("Landing Page")
    st.write("Welcome to the landing page!")

    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.experimental_rerun()
