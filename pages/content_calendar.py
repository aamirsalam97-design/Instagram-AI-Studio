import streamlit as st

from utils.gemini_api import generate_content_calendar
from utils.pdf_generator import create_pdf


def content_calendar():

    st.title("📅 AI Content Calendar")

    topic = st.text_input(
        "Enter Instagram Niche"
    )

    days = st.selectbox(
        "Number of Days",
        [7, 15, 30]
    )

    if st.button("🚀 Generate Calendar"):

        if topic.strip() == "":
            st.warning("Enter a topic.")
            return

        with st.spinner("Generating Calendar..."):

            result = generate_content_calendar(
                topic,
                days
            )

        st.success("✅ Calendar Generated")

        st.markdown(result)

        st.download_button(
            "📥 Download TXT",
            result,
            "content_calendar.txt",
            "text/plain"
        )

        create_pdf(
            "Content_Calendar.pdf",
            "Instagram Content Calendar",
            result
        )

        with open("Content_Calendar.pdf", "rb") as pdf:

            st.download_button(
                "📄 Download PDF",
                pdf.read(),
                "Content_Calendar.pdf",
                "application/pdf"
            )