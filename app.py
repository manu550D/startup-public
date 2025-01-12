import streamlit as st
from PIL import Image
import tempfile
import re

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
        # Validate phone number
        if re.fullmatch(r"\d{10}", phone_number):
            st.session_state["logged_in"] = True
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Please enter a valid 10-digit phone number")
else:
    # Landing Page
    st.header("Landing Page")
    st.write("Welcome to the landing page!")

    # Add a Plus Button
    if st.button("+ Add Bill"):
        st.write("Choose an option:")
        action = st.radio("Select an action:", ("Upload from Gallery", "Take a Photo"))

        if action == "Upload from Gallery":
            uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Bill", use_column_width=True)
        elif action == "Take a Photo":
            st.write("Taking a photo feature is not available in this MVP version.")

    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.experimental_rerun()
