import streamlit as st
import pandas as pd
import plotly.express as px
from utils.database import get_captions


def analytics():

    st.title("📊 Analytics Dashboard")

    rows = get_captions()

    total = len(rows)

    counts = {
        "Professional": 0,
        "Funny": 0,
        "Luxury": 0,
        "Travel": 0,
        "Fitness": 0,
        "Motivational": 0
    }

    for style, _ in rows:
        if style in counts:
            counts[style] += 1

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Captions", total)

    with col2:
        st.metric("Styles Used", len(counts))

    with col3:
        st.metric("Database Entries", total)

    st.divider()

    df = pd.DataFrame({
        "Style": list(counts.keys()),
        "Count": list(counts.values())
    })

    st.subheader("📊 Caption Style Analytics")

    fig1 = px.bar(
        df,
        x="Style",
        y="Count",
        text="Count",
        title="Caption Styles Used"
    )

    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.pie(
        df,
        names="Style",
        values="Count",
        title="Caption Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    st.subheader("📋 Style Statistics")

    for style, count in counts.items():
        st.write(f"**{style}:** {count}")