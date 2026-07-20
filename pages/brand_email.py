import streamlit as st
from utils.gemini_api import generate_brand_email


def brand_email():

    st.title("📧 Brand Collaboration Email Generator")

    creator = st.text_input("Creator Name")

    brand = st.text_input("Brand Name")

    niche = st.text_input("Your Niche")

    followers = st.text_input("Followers")

    tone = st.selectbox(
        "Email Tone",
        [
            "Professional",
            "Friendly",
            "Luxury",
            "Confident"
        ]
    )

    if st.button("🚀 Generate Email"):

        if not creator or not brand or not niche or not followers:
            st.warning("Please fill all fields.")
            return

        with st.spinner("Generating Email..."):

            email = generate_brand_email(
                creator,
                brand,
                niche,
                followers,
                tone
            )

        st.success("✅ Email Generated")

        st.markdown(email)