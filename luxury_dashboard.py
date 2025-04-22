import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_extras.metric_cards import style_metric_cards
from datetime import datetime
import time

# Page config
st.set_page_config(
    page_title="Luxury Retail Dashboard",
    layout="wide",
    page_icon="👛"
)

# Style
st.markdown("""
<style>
body {
    font-family: 'Segoe UI', sans-serif;
}
[data-testid="metric-container"] {
    background-color: #20242c;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #444;
    color: white;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    transition: all 0.3s ease-in-out;
}
[data-testid="stMetric"] div {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Data
feature_importance = pd.DataFrame({
    'Feature': ['subject_length', 'channel_email', 'subject_with_emoji', 'campaign_type_bulk', 'subject_with_discount'],
    'Importance': [0.35, 0.30, 0.15, 0.10, 0.10]
})
association_rules = pd.DataFrame({
    'Rule': [
        'Female & Bangalore => Fashion', 'Male & Delhi => Electronics',
        'Age 25-34 => Leather Goods', 'Urban => OTT Subscription',
        'High Income => Jewelry', 'Female & Mumbai => Handbags',
        'Student => Casual Wear', 'Male & Chennai => Shoes',
        'Age 35-44 => Watches', 'Retired => Home Decor'
    ],
    'Confidence': [0.91, 0.89, 0.88, 0.86, 0.85, 0.84, 0.82, 0.80, 0.79, 0.77]
})

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3523/3523063.png", width=150)
st.sidebar.title("Campaign Settings")
channel = st.sidebar.selectbox("Choose Channel", ['Email', 'Social Media', 'SMS'])
subject_length = st.sidebar.slider("Subject Length (characters)", 10, 100, 50)
personalized = st.sidebar.checkbox("Enable Personalization")

# Header
st.markdown("""
# Luxury Retail Campaign Optimizer
**Data-Driven Strategy & Real-Time Effectiveness Tracker**
---
""")

# Timestamp to simulate live updates
col_time = st.columns([1, 5])[0]
with col_time:
    now = datetime.now().strftime("%H:%M:%S")
    st.info(f"Last Updated: {now}")

# Tabs
tabs = st.tabs(["Feature Impact", "Associative Rules", "Campaign Simulator"])

# Tab 1
with tabs[0]:
    st.subheader("Top Predictive Features (RandomForest Model)")
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    sns.barplot(data=feature_importance, y='Feature', x='Importance', palette='coolwarm', ax=ax1)
    ax1.set_title("Feature Importance")
    st.pyplot(fig1)

# Tab 2
with tabs[1]:
    st.subheader("Top Association Rules")
    st.dataframe(association_rules, use_container_width=True)
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.barplot(data=association_rules, y='Rule', x='Confidence', ax=ax2, palette='magma')
    ax2.set_xlim(0.7, 1.0)
    ax2.set_title("Confidence Levels of Association Patterns")
    st.pyplot(fig2)

# Tab 3
with tabs[2]:
    st.subheader("Campaign Performance Simulator")
    effectiveness_score = 0.5
    effectiveness_score += 0.1 if channel == 'Email' else -0.05
    effectiveness_score += 0.1 if personalized else 0
    effectiveness_score += 0.01 * (subject_length / 100)
    effectiveness_score = round(min(1.0, effectiveness_score), 2)

    colA, colB = st.columns(2)
    with colA:
        st.metric("Predicted Effectiveness", f"{effectiveness_score*100:.0f}%", delta_color="normal")
    with colB:
        if effectiveness_score >= 0.75:
            st.success("Excellent! High effectiveness expected.")
        elif effectiveness_score >= 0.5:
            st.info("You're on the right track. With a few creative tweaks, this campaign can shine.")
        else:
            st.error("Low performance predicted. Rethink targeting or copy.")

    st.caption("This simulation updates in real time with your input.")

# Footer
st.markdown("---")
st.caption("Built by Yasaswini Reddy Naga | Independent Researcher | SLU Alumna")
