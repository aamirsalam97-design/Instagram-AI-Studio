import streamlit as st
from PIL import Image

from utils.gemini_api import (
    generate_caption,
    analyze_content_quality,
    translate_caption
)

from utils.database import save_caption
from utils.pdf_generator import create_pdf


def caption_generator():

    st.title("🤖 AI Caption Generator")

    uploaded_file = st.file_uploader(
        "Upload Instagram Image",
        type=["jpg", "jpeg", "png"]
    )

    style = st.selectbox(
        "Caption Style",
        [
            "Professional",
            "Funny",
            "Luxury",
            "Travel",
            "Fitness",
            "Motivational"
        ]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(image, use_container_width=True)

        if st.button("✨ Generate Caption"):

            with st.spinner("Generating AI Caption..."):

                try:

                    # Generate Caption
                    result = generate_caption(image, style)

                    # Save History
                    save_caption(
                        st.session_state["username"],
                        style,
                        result
                    )

                    # Analyze
                    quality = analyze_content_quality(result)

                    st.success("✅ Caption Generated Successfully!")

                    st.subheader("✨ AI Generated Caption")

                    st.markdown(result)

                    # Download TXT
                    st.download_button(
                        "📥 Download Caption (.txt)",
                        result,
                        "instagram_caption.txt",
                        "text/plain"
                    )

                    # PDF
                    create_pdf(
                        "AI_Report.pdf",
                        "Instagram AI Report",
                        result
                    )

                    with open("AI_Report.pdf", "rb") as pdf:

                        st.download_button(
                            "📄 Download PDF Report",
                            pdf.read(),
                            "Instagram_AI_Report.pdf",
                            "application/pdf"
                        )

                    st.divider()

                    # -------------------------
                    # Translator
                    # -------------------------

                    st.subheader("🌍 AI Caption Translator")

                    language = st.selectbox(
                        "Translate To",
                        [
                            "Hindi",
                            "Urdu",
                            "English",
                            "Spanish",
                            "French",
                            "German",
                            "Italian",
                            "Portuguese",
                            "Japanese",
                            "Korean",
                            "Chinese",
                            "Arabic",
                            "Russian"
                        ]
                    )

                    if st.button("🌍 Translate Caption"):

                        with st.spinner("Translating..."):

                            translated = translate_caption(
                                result,
                                language
                            )

                        st.success("✅ Translation Complete")

                        st.markdown(translated)

                        st.download_button(
                            "📥 Download Translation",
                            translated,
                            f"caption_{language}.txt",
                            "text/plain"
                        )

                    st.divider()

                    st.subheader("📊 AI Content Quality Report")

                    st.markdown(quality)

                except Exception as e:

                    st.exception(e)