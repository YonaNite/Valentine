import streamlit as st
import random

# List of cheesy pickup lines
pickup_lines = [
    "Are you French? Cuz Eiffel for you!",
    "Do you have a Band-Aid? Cuz I just scraped my knee falling for you!",
    "Are you a magician? Cuz whenever I look at you, everyone else disappears!",
    "Are you a parking ticket? Cuz you've got 'FINE' written all over you!",
    "Do you have a map? I keep getting lost in your eyes!",
    "If you were a vegetable, you'd be a cute-cumber!",
    "Are you a campfire? Cuz you're hot and I want s'more!",
    "If beauty were a crime, you'd be serving a life sentence!",
    "Are you a Wi-Fi signal? Cuz I'm feeling a connection!",
    "Are you a loan? Cuz you've got my interest",
]

# Set the page title and background color
st.set_page_config(page_title="Valentine's Day Card", page_icon="💖", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #FFB0E1;
            text-align: center;
        }
        .big-text {
            font-size: 36px;
            font-family: 'Brush Script MT', cursive;
            font-weight: bold;
            color: #BFE8FF;
            text-align: center;
        }
        .heart-button {
            background-color: #D5C2FF;
            color: white;
            border-radius: 50px;
            padding: 15px;
            font-size: 20px;
            cursor: pointer;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Valentine Message
st.markdown('<p class="big-text">💖 Be My Valentine 💖</p>', unsafe_allow_html=True)

# Button to display a pickup line
if st.button("💘 Click for a Cute Message 💘"):
    st.success(random.choice(pickup_lines))

# Cute heart icons for decoration
st.markdown('<p class="big-text">💖💖💖</p>', unsafe_allow_html=True)