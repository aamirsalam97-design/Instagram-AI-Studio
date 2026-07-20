import streamlit as st

from utils.gemini_api import profile_audit
from utils.pdf_generator import create_pdf


def profile_auditor():

    st.title("📈 AI Instagram Profile Auditor")

    name = st.text_input("Profile Name")

    niche = st.text_input("Niche")

    bio = st.text_area("Instagram Bio")

    if st.button("🚀 Audit Profile"):

        if name == "" or niche == "" or bio == "":
            st.warning("Please fill all fields.")
            return

        with st.spinner("Auditing Profile..."):

            result = profile_audit(
                name,
                niche,
                bio
            )

        st.success("✅ Audit Complete")

        st.markdown(result)

        st.download_button(
            "📥 Download TXT",
            result,
            "profile_audit.txt",
            "text/plain"
        )

        create_pdf(
            "Profile_Audit.pdf",
            "Instagram Profile Audit",
            result
        )

        with open("Profile_Audit.pdf", "rb") as pdf:

            st.download_button(
                "📄 Download PDF",
                pdf.read(),
                "Profile_Audit.pdf",
                "application/pdf"
            )