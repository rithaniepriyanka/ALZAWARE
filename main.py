# main.py
import streamlit as st
from PIL import Image

#page icon
pg_icon=Image.open('Alzaware_logo.png')
st.set_page_config(page_title='AlzAware',page_icon=pg_icon)


# Import pages
from homepage import show_homepage
from predict_page import prediction
from shield_page import show_shield_page
from seekpage import show_seek_page

# App title with enhanced styling
#st.title("AlzAware: Scan, Shield, Seek")
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Victoria&display=swap');

    .title-text {
        font-family: 'Montserrat', sans-serif; /* Montserrat font */
        font-size: 48px; /* Increase font size */
        animation: rainbow 5s linear infinite; /* Rainbow animation */
        margin-bottom: 20px; /* Increase space below title */
        text-align: center; /* Center align text */
    }

    @keyframes rainbow {
        0% { color: #FFE4C4; } /* Bisque */
        20% { color: #4169E1; } /* Ocean Blue */
        40% { color: #87CEEB; } /* Sky Blue */
        60% { color: #DDA0DD; } /* Plum */
        80% { color: #FF69B4; } /* Hot Pink */
        100% { color: #8A2BE2; } /* Blue Violet */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<p class="title-text">AlzAware: Scan, Shield, Seek</p>', unsafe_allow_html=True)

#
# Display logo in the navigation bar
st.sidebar.image(pg_icon, use_column_width=True)

# Navigation
menu = ["Home", "🔍 Scan", "🤝 Shield", "🏥 Seek"]
choice = st.sidebar.selectbox("Menu", menu)

# Display the selected page
if choice == "Home":
    show_homepage()
elif choice == "🔍 Scan":
    prediction()
elif choice == "🤝 Shield":
    show_shield_page()
elif choice == "🏥 Seek":
    show_seek_page()

