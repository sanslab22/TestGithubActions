import streamlit as st


# Set the title of the app
st.title("My First Streamlit App")

# Add a text input
name = st.text_input("Enter your name", "Guest")

# Display a welcome message
st.write(f"Hello, {name}! Welcome to Streamlit!")
