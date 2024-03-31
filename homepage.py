# homepage.py
import streamlit as st
import json
from streamlit_lottie import st_lottie


def show_homepage():
    st.write("Welcome to the homepage!")

    #Animation
    # Load Lottie animation
    def load_lottiefile(filepath:str):
        with open(filepath,"r") as f:
            return json.load(f)
        
    lottie_logo = load_lottiefile("C:\\Rithu\\xray\\final\\webpage\\templates\\home_anim.json")

    # Display Lottie animation (logo) 
    st.markdown(
        """
        <style>
        .logo-container {
            position: absolute;
            top: 10px;
            right: 10px;
            width: 100px; /* Adjust the width as needed */
            height: 100px; /* Adjust the height as needed */
        }
        </style>
        """
    , unsafe_allow_html=True)

    # Add a container div with the logo-container class
    st.markdown("<div class='logo-container'></div>", unsafe_allow_html=True)
    
    # Display the Lottie animation inside the container
    st_lottie(lottie_logo, quality="high", width=100, height=100)

    #Contents
    st.title("Glimpse: What You Need to Know")
    st.markdown("*Empowering You to Champion Alzheimer's with Confidence*", unsafe_allow_html=True)
    st.write("Are you ready to turn the tide against Alzheimer's disease? At AlzAware, we're your partners in the fight, offering a groundbreaking approach to tackling Alzheimer's head-on. Get ready to take control of your journey with our innovative tools and unwavering support.")

    st.subheader("Unraveling the Mystery of Alzheimer's")
    st.write("Alzheimer's disease can feel like a puzzle with no solution, but we're here to change that narrative. Our cutting-edge technology dives deep into MRI scan images to decode the likelihood and severity of Alzheimer's, giving you the power of foresight to plan ahead.")

    st.subheader("Why Choose AlzAware?")
    st.write("Glad you asked! Here's what makes us stand out:")
    st.markdown(
        """
        1. **Predictive Precision**: Our AI-driven algorithms don't just analyze scans; they predict the future. With early detection as our secret weapon, we're arming you with knowledge to face Alzheimer's head-on.
        2. **Armor Up with Knowledge**: Knowledge is power, and we're here to arm you with the strategies you need to shield against Alzheimer's. From lifestyle hacks to nutritional nuggets, we've got your back every step of the way.
        3. **Navigate with Confidence**: When it comes to Alzheimer's, you shouldn't have to wander alone. Our Seek feature connects you with top-tier specialists and hospitals, ensuring you have the support you need right at your fingertips.
        """,
        unsafe_allow_html=True
    )

    st.subheader("Ready to Rewrite Your Story?")
    st.write("Alzheimer's might be a formidable opponent, but together, we're unstoppable. Join the AlzAware revolution and take the reins of your destiny. Your journey toward empowerment starts now.")
    st.button("Let's Get Started")
