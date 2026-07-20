import streamlit as st
from utils.gemini_api import analyze_competitor
from utils.pdf_generator import create_pdf


def competitor_analyzer():

    st.title("📈 AI Competitor Analyzer")

    username = st.text_input(
        "Instagram Username / Brand"
    )

    if st.button("🚀 Analyze"):

        if username.strip() == "":
            st.warning("Please enter a username.")
            return

        with st.spinner("Analyzing..."):

            result = analyze_competitor(username)

        st.success("✅ Analysis Complete")

        st.markdown(result)

        st.download_button(
            "📥 Download TXT",
            result,
            "competitor_analysis.txt",
            "text/plain"
        )

        create_pdf(
            "Competitor_Report.pdf",
            "Competitor Analysis",
            result
        )

        with open("Competitor_Report.pdf", "rb") as pdf:

            st.download_button(
                "📄 Download PDF",
                pdf.read(),
                "Competitor_Report.pdf",
                "application/pdf"
            )