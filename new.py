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
    "Are you a camera? Cuz all I can do is smile when I see you",
    "Are you a parking ticket? Cuz you've got 'FINE' written all over you!",
    "Are you a time traveler? Cuz I can see you in my future!",
    "Is your name Google? Cuz you have everything I've been searching for! ",
    "Are you made of copper and tellurium? Because you're Cu-Te!",
    "Did the sun come out, or did you just smile at me?",
    "I'd give up my morning cereal to spoon you instead.",
    "I love my bed, but I'd rather be in yours.",
    "It's a good thing I have my library card, because I am totally checking you out.",
    "If I could rearrange the alphabet, I'd put U and I together.",
    "Anyone who says Disneyland is the happiest place on earth has clearly never stood next to you.",
    "If you were words on a page you'd be the fine print.",
    "You know those gaps between your fingers? I think they were made for mine.",
    "Want to grab coffee? I like you a latte."
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
            font-size: 48px; /* Increased font size */
            font-family: 'Brush Script MT', cursive;
            font-weight: bold;
            color: #BFE8FF;
            text-align: center;
        }
        .heart-button {
            background: linear-gradient(to right, #FF7F7F, #FFB0E1); /* Gradient background */
            color: white;
            border-radius: 50px;
            padding: 20px 40px; /* Larger padding for a bigger button */
            font-size: 28px; /* Larger font size */
            cursor: pointer;
            border: none;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Shadow effect */
            transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth transition for hover effect */
        }
        .heart-button:hover {
            transform: scale(1.1); /* Slightly enlarge the button on hover */
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Enhanced shadow on hover */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<p style="font-size: 64px; font-family: Brush Script MT, cursive; font-weight: bold; color: #BFE8FF; text-align: center;">💖 Be My Valentine 💖</p>',
    unsafe_allow_html=True
)

# Button to display a pickup line
if st.button("💘 Click to Open 💘"):
    st.success(random.choice(pickup_lines))

# Cute heart icons for decoration
st.markdown('<p class="big-text">💖💖💖</p>', unsafe_allow_html=True)