import streamlit as st
from utils.gemini_api import generate_reply


def reply_generator():

    st.title("💬 AI Reply Generator")

    comment = st.text_area(
        "Paste Instagram Comment",
        height=150
    )

    if st.button("🚀 Generate Reply"):

        if not comment.strip():
            st.warning("Please enter a comment.")
            return

        with st.spinner("Generating AI Reply..."):

            try:

                reply = generate_reply(comment)

                st.success("✅ Reply Generated Successfully!")

                st.subheader("AI Reply")

                st.markdown(reply)

                st.download_button(
                    label="📥 Download Reply",
                    data=reply,
                    file_name="instagram_reply.txt",
                    mime="text/plain"
                )

            except Exception as e:

                st.exception(e)