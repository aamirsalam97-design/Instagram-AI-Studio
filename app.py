from pages.brand_email import brand_email
from pages.profile_auditor import profile_auditor
from pages.competitor_analyzer import competitor_analyzer
from pages.reel_script import reel_script
from pages.content_calendar import content_calendar
from pages.caption_improver import caption_improver

import streamlit as st

from pages.login import login_page
from pages.caption_generator import caption_generator
from pages.hashtag_generator import hashtag_generator
from pages.history import history
from pages.image_analyzer import image_analyzer
from pages.sentiment_analyzer import sentiment_analyzer
from pages.engagement_predictor import engagement_predictor
from pages.analytics import analytics
from pages.reply_generator import reply_generator


# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="Instagram AI Studio",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------
# Login Session
# -----------------------------------

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "username" not in st.session_state:
    st.session_state["username"] = ""

if not st.session_state["logged_in"]:
    login_page()
    st.stop()


# -----------------------------------
# CSS
# -----------------------------------

st.markdown("""
<style>

.main{
    background:#F8F9FA;
}

.title{
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:#E1306C;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:20px;
}

.footer{
    text-align:center;
    color:gray;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------------
# Sidebar
# -----------------------------------

st.sidebar.title("📸 Instagram AI Studio")

st.sidebar.success(f"👤 {st.session_state['username']}")

if st.sidebar.button("🚪 Logout"):
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.rerun()

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🤖 Caption Generator",
        "✨ Caption Improver",
        "📅 Content Calendar",
        "🎬 Reel Script",
        "📈 Competitor Analyzer",
        "📈 Profile Auditor",
        "📧 Brand Email",
        "#️⃣ Hashtag Generator",
        "📜 History",
        "🖼️ Image Analyzer",
        "😊 Sentiment Analyzer",
        "💬 Reply Generator",
        "📈 Engagement Predictor",
        "📊 Analytics",
        "⚙️ Settings"
    ]
)


# -----------------------------------
# Home
# -----------------------------------

if page == "🏠 Home":

    st.markdown(
        "<p class='title'>📸 Instagram AI Studio</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='subtitle'>AI Powered Instagram Content Creation Platform</p>",
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Captions", 0)

    with c2:
        st.metric("Hashtags", 0)

    with c3:
        st.metric("Images", 0)

    with c4:
        st.metric("Predictions", 0)

    st.divider()

    st.subheader("🚀 Features")

    left, right = st.columns(2)

    with left:
        st.success("🤖 AI Caption Generator")
        st.success("#️⃣ AI Hashtag Generator")
        st.success("🖼️ YOLO Image Analyzer")
        st.success("😊 Sentiment Analyzer")

    with right:
        st.success("💬 AI Reply Generator")
        st.success("📈 Engagement Predictor")
        st.success("📊 Analytics Dashboard")
        st.success("📜 Caption History")


# -----------------------------------
# Pages
# -----------------------------------

elif page == "🤖 Caption Generator":
    caption_generator()
    
elif page == "✨ Caption Improver":   
    caption_improver()  
    
elif page == "📅 Content Calendar":
    content_calendar()  
    
elif page == "🎬 Reel Script":
    reel_script()
    
elif page == "📈 Competitor Analyzer":
    competitor_analyzer()
    
elif page == "📈 Profile Auditor":
    profile_auditor()
    
elif page == "📧 Brand Email":
    brand_email()

elif page == "#️⃣ Hashtag Generator":
    hashtag_generator()

elif page == "📜 History":
    history()

elif page == "🖼️ Image Analyzer":
    image_analyzer()

elif page == "😊 Sentiment Analyzer":
    sentiment_analyzer()

elif page == "💬 Reply Generator":
    reply_generator()

elif page == "📈 Engagement Predictor":
    engagement_predictor()

elif page == "📊 Analytics":
    analytics()

elif page == "⚙️ Settings":
    st.title("⚙️ Settings")
    st.info("🚧 Coming Soon")


# -----------------------------------
# Footer
# -----------------------------------

st.markdown("---")

st.markdown(
    "<p class='footer'>Made with ❤️ using Python, Streamlit, Groq & YOLO</p>",
    unsafe_allow_html=True
)