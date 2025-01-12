import streamlit as st
from datetime import datetime

# Title and Intro
st.title("Salon Booking App")
st.subheader("Effortlessly book salon services in Kerala!")

# Registration/Login Section
st.sidebar.header("Welcome")
choice = st.sidebar.radio("Login or Register:", ["Login", "Register"])
if choice == "Register":
    st.sidebar.text_input("Enter your name")
    st.sidebar.text_input("Enter your email")
    st.sidebar.text_input("Set a password", type="password")
    if st.sidebar.button("Register"):
        st.success("Registration successful!")
elif choice == "Login":
    st.sidebar.text_input("Enter email")
    st.sidebar.text_input("Enter password", type="password")
    if st.sidebar.button("Login"):
        st.success("Login successful!")

# Appointment Booking Section
st.header("Book Your Appointment")
services = ["Haircut", "Shaving", "Facial", "Manicure", "Pedicure"]
selected_service = st.selectbox("Choose a Service", services)
date = st.date_input("Select a Date")
time = st.time_input("Select a Time")
if st.button("Confirm Booking"):
    st.success(f"Booking Confirmed: {selected_service} on {date} at {time}")

# Admin Section (For Salon Owners)
st.sidebar.header("Salon Dashboard")
if st.sidebar.checkbox("Show Appointments"):
    st.sidebar.write("Here, salon owners can view/manage appointments.")

