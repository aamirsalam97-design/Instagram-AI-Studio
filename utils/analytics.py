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
        "Motivational": 0,
    }

    for style, _ in rows:
        if style in counts:
            counts[style] += 1

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Total Captions", total)

    with c2:
        st.metric("Styles Used", len(counts))

    with c3:
        st.metric("Database Entries", total)

    st.divider()

    df = pd.DataFrame({
        "Style": list(counts.keys()),
        "Count": list(counts.values())
    })

    st.subheader("📊 Caption Style Analytics")

    bar = px.bar(
        df,
        x="Style",
        y="Count",
        text="Count",
        title="Caption Styles Used"
    )

    st.plotly_chart(bar, use_container_width=True)

    pie = px.pie(
        df,
        names="Style",
        values="Count",
        title="Caption Distribution"
    )

    st.plotly_chart(pie, use_container_width=True)

    st.divider()

    st.subheader("📋 Statistics")

    for style, count in counts.items():
        st.write(f"{style}: {count}")