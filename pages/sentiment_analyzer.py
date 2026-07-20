import streamlit as st
from utils.gemini_api import analyze_sentiment


def sentiment_analyzer():

    st.title("😊 AI Sentiment Analyzer")

    comment = st.text_area(
        "Paste Instagram Comment"
    )

    if st.button("Analyze Sentiment"):

        if comment.strip() == "":
            st.warning("Please enter a comment.")
            return

        with st.spinner("Analyzing..."):

            result = analyze_sentiment(comment)

            st.success("Analysis Complete!")

            st.markdown(result)