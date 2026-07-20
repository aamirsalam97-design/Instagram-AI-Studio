import streamlit as st

from utils.gemini_api import improve_caption
from utils.pdf_generator import create_pdf


def caption_improver():

    st.title("✨ AI Caption Improver")

    caption = st.text_area(
        "Paste Your Instagram Caption",
        height=200
    )

    if st.button("✨ Improve Caption"):

        if caption.strip() == "":
            st.warning("Please enter a caption.")
            return

        with st.spinner("Improving Caption..."):

            result = improve_caption(caption)

        st.success("✅ Caption Improved")

        st.subheader("🚀 Improved Caption")

        st.markdown(result)

        st.download_button(
            "📥 Download TXT",
            result,
            "improved_caption.txt",
            "text/plain"
        )

        create_pdf(
            "Improved_Caption.pdf",
            "Improved Instagram Caption",
            result
        )

        with open("Improved_Caption.pdf", "rb") as pdf:

            st.download_button(
                "📄 Download PDF",
                pdf.read(),
                "Improved_Caption.pdf",
                "application/pdf"
            )