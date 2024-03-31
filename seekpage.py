
# seek_page.py
import streamlit as st
import json
from streamlit_lottie import st_lottie

def show_seek_page():
    st.title("Seek Specialist Care: Discover Your Alzheimer's Ally")
    st.markdown("*Welcome to AlzAware's Seek page, where we unlock the door to the best Alzheimer's specialists in Chennai. Your path to peace of mind begins here.*", unsafe_allow_html=True)

    st.subheader("Why AlzAware Rocks!!!")

    #Animation
    # Load Lottie animation
    def load_lottiefile2(filepath:str):
        with open(filepath,"r") as f:
            return json.load(f)
        
    lottie_seek = load_lottiefile2("C:\\Rithu\\xray\\final\\webpage\\templates\\seek_anim.json")

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
    st_lottie(lottie_seek, quality="high", width=100, height=100)

    #
    #Contents
    st.write("At AlzAware, we're on a mission to connect you with the cream of the crop in Alzheimer's care. Say goodbye to uncertainty and hello to expert guidance, courtesy of our handpicked lineup of Chennai's top-notch doctors.")

    st.subheader("Meet City's Expert Doctors")
    st.markdown("""
        1. **Dr. Rajesh Kumar, MD**
           - Location: Apollo Hospitals, Greams Road
           - Experience: 15+ years 
           - Fees: INR 2000 per consultation

        2. **Dr. Priya Sharma, MBBS, DNB**
           - Location: Fortis Malar Hospital, Adyar
           - Experience: 12+ years 
           - Fees: INR 1800 per consultation

        3. **Dr. Arjun Singh, MD, DM**
           - Location: Global Hospital, Perumbakkam
           - Experience: 20+ years 
           - Fees: INR 2500 per consultation

        4. **Dr. Sneha Patel, MBBS, MRCP**
           - Location: MIOT International, Manapakkam
           - Experience: 10+ years 
           - Fees: INR 2200 per consultation

        5. **Dr. Ananya Gupta, MD, DM**
           - Location: Vijaya Hospital, Vadapalani
           - Experience: 8+ years 
           - Fees: INR 1900 per consultation

        6. **Dr. Vikram Singh, MD, DNB**
           - Location: Kauvery Hospital, Alwarpet
           - Experience: 18+ years 
           - Fees: INR 2300 per consultation
    """, unsafe_allow_html=True)

    st.subheader("Lock In Your Appointment!")
    st.write("Ready to kickstart your journey to wellness? Grab your phone and reach out to our superstar doctors now. Let's turn your worries into wins, one appointment at a time!")
