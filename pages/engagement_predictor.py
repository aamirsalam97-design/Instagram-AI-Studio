import streamlit as st
from PIL import Image

from utils.gemini_api import predict_engagement


def engagement_predictor():

    st.title("📈 AI Engagement Predictor")

    uploaded_file = st.file_uploader(
        "Upload Instagram Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(image, use_container_width=True)

        if st.button("🚀 Predict Engagement"):

            with st.spinner("Analyzing..."):

                description = "Instagram image uploaded by user"

                result = predict_engagement(description)

                st.success("Prediction Complete!")

                st.markdown(result)