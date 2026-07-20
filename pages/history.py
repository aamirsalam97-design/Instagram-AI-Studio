import streamlit as st

from utils.database import (
    get_captions,
    delete_history
)


def history():

    st.title("📜 Caption History")

    username = st.session_state["username"]

    if st.button("🗑 Delete My History"):

        delete_history(username)

        st.success("History Deleted Successfully")

        st.rerun()

    rows = get_captions(username)

    if len(rows) == 0:

        st.info("No captions generated yet.")

        return

    for style, caption in rows:

        with st.expander(f"🎨 {style}"):

            st.markdown(caption)