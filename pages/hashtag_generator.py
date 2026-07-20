import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def hashtag_generator():

    st.title("#️⃣ AI Hashtag Generator")

    topic = st.text_input("Enter your post topic")

    if st.button("Generate Hashtags"):

        with st.spinner("Generating hashtags..."):

            prompt = f"""
Generate 30 trending Instagram hashtags for:

Topic: {topic}

Return only hashtags.
"""

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            hashtags = response.choices[0].message.content

            st.success("Generated Successfully!")

            st.markdown(hashtags)

            st.download_button(
                "📥 Download",
                hashtags,
                "hashtags.txt"
            )