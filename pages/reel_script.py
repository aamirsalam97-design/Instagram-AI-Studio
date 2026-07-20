import streamlit as st

from utils.gemini_api import generate_reel_script
from utils.pdf_generator import create_pdf


def reel_script():

    st.title("🎬 AI Reel Script Generator")

    topic = st.text_input("Reel Topic")

    duration = st.selectbox(
        "Duration",
        ["30", "60", "90"]
    )

    tone = st.selectbox(
        "Tone",
        [
            "Professional",
            "Funny",
            "Luxury",
            "Motivational"
        ]
    )

    if st.button("🚀 Generate Reel Script"):

        if topic.strip() == "":
            st.warning("Enter a topic.")
            return

        with st.spinner("Generating Script..."):

            result = generate_reel_script(
                topic,
                duration,
                tone
            )

        st.success("✅ Script Generated")

        st.markdown(result)

        st.download_button(
            "📥 Download TXT",
            result,
            "reel_script.txt",
            "text/plain"
        )

        create_pdf(
            "Reel_Script.pdf",
            "Instagram Reel Script",
            result
        )

        with open("Reel_Script.pdf", "rb") as pdf:

            st.download_button(
                "📄 Download PDF",
                pdf.read(),
                "Reel_Script.pdf",
                "application/pdf"
            )