import streamlit as st
from PIL import Image
import tempfile
import re
import os
import json

# Constants
USER_DATA_FILE = "user_data.json"

def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_user_data(data):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file)

# Load user data
user_data = load_user_data()

# Streamlit App
st.title("MVP Application")
st.subheader("A Simple App with Login and Landing Page")

# Session State for Login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "current_user" not in st.session_state:
    st.session_state["current_user"] = None

# Login Page
if not st.session_state["logged_in"]:
    st.header("Login or Register")
    phone_number = st.text_input("Enter your phone number", max_chars=10)
    if st.button("Register"):
        # Validate phone number for registration
        if re.fullmatch(r"\d{10}", phone_number):
            if phone_number in user_data:
                st.warning("This phone number is already registered.")
            else:
                user_data[phone_number] = {"bills": []}
                save_user_data(user_data)
                st.success("Registration successful! You can now log in.")
        else:
            st.error("Please enter a valid 10-digit phone number.")

    if st.button("Login"):
        # Validate phone number for login
        if re.fullmatch(r"\d{10}", phone_number):
            if phone_number in user_data:
                st.session_state["logged_in"] = True
                st.session_state["current_user"] = phone_number
                st.success("Login successful!")
                st.experimental_rerun()
            else:
                st.error("This phone number is not registered. Please register first.")
        else:
            st.error("Please enter a valid 10-digit phone number.")
else:
    # Landing Page
    st.header("Landing Page")
    st.write(f"Welcome, {st.session_state['current_user']}!")

    # Add a Plus Button
    if st.button("+ Add Bill"):
        st.write("Choose an option:")
        action = st.radio("Select an action:", ("Upload from Gallery", "Take a Photo"))

        if action == "Upload from Gallery":
            uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "pdf"])
            if uploaded_file is not None:
                file_type = uploaded_file.type
                if file_type.startswith("image"):
                    image = Image.open(uploaded_file)
                    st.image(image, caption="Uploaded Bill", use_column_width=True)
                    user_data[st.session_state["current_user"]]["bills"].append(uploaded_file.name)
                    save_user_data(user_data)
                    st.success("Bill uploaded and saved!")
                elif file_type == "application/pdf":
                    st.write("PDF Preview is not available in this version. File uploaded successfully.")
                    user_data[st.session_state["current_user"]]["bills"].append(uploaded_file.name)
                    save_user_data(user_data)
                else:
                    st.error("Unsupported file format. Please upload an image or PDF.")
        elif action == "Take a Photo":
            st.write("Taking a photo feature is not available in this MVP version.")

    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["current_user"] = None
        st.experimental_rerun()
