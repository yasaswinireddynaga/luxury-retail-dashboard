import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_extras.metric_cards import style_metric_cards
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Luxury Retail Dashboard",
    layout="wide",
    page_icon="👛",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main, .stApp {
        background-color: #1a1a1a;
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    .block-container {
        padding: 2rem 2rem;
    }
    h1, h2, h3, h4 {
        color: #e0e0e0;
    }
    .stDataFrame {
        background-color: #2c2f33;
    }
    </style>
""", unsafe_allow_html=True)

# Dummy Data
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
st.sidebar.title("🧰 Campaign Settings")
channel = st.sidebar.selectbox("🎯 Choose Channel", ['Email', 'Social Media', 'SMS'])
subject_length = st.sidebar.slider("📝 Subject Length (characters)", 10, 100, 50)
personalized = st.sidebar.checkbox("💡 Personalization Enabled")

# Title section
st.markdown("""
# 👛 Luxury Retail AI Dashboard  
*Machine Learning-Driven Insights for Campaign Optimization*
""")

# Tabs
tabs = st.tabs(["📊 Feature Importance", "🔗 Association Rules", "🧠 Campaign Simulator"])

# Tab 1: Feature Importance
with tabs[0]:
    st.subheader("📌 Feature Importance (RandomForest Model)")
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    sns.barplot(data=feature_importance, y='Feature', x='Importance', ax=ax1, palette="coolwarm")
    ax1.set_title("Key Drivers of Campaign Performance", fontsize=14)
    st.pyplot(fig1)
    st.info("📈 Subject length and email channel are key to successful engagement.")

# Tab 2: Association Rules
with tabs[1]:
    st.subheader("🔍 Top 10 Demographic-Based Association Rules")
    st.dataframe(association_rules, use_container_width=True)
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.barplot(data=association_rules, y='Rule', x='Confidence', ax=ax2, palette="magma")
    ax2.set_xlim(0.7, 1.0)
    ax2.set_title("Confidence Levels for Association Patterns", fontsize=14)
    st.pyplot(fig2)
    st.warning("💡 Use these patterns to fine-tune targeting by region and customer profile.")

# Tab 3: Campaign Simulator
with tabs[2]:
    st.subheader("🧪 Predict Campaign Effectiveness")
    effectiveness_score = 0.5
    effectiveness_score += 0.1 if channel == 'Email' else -0.05
    effectiveness_score += 0.1 if personalized else 0
    effectiveness_score += 0.01 * (subject_length / 100)
    effectiveness_score = round(min(1.0, effectiveness_score), 2)

    if effectiveness_score >= 0.75:
        level = "🟢 High"
        msg = "✨ Excellent! This campaign setup has high predicted effectiveness."
    elif effectiveness_score >= 0.5:
        level = "🟡 Moderate"
        msg = "📊 Moderate engagement expected. Consider testing variations."
    else:
        level = "🔴 Low"
        msg = "⚠️ Low predicted performance. Optimize message or channel."

    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("Predicted Effectiveness", f"{effectiveness_score*100:.0f}%", level)
    with col2:
        if effectiveness_score >= 0.75:
        st.success(msg)
    else:
        st.warning(msg)

    st.markdown("---")
    st.markdown("🔁 *Lower scores for SMS and social campaigns suggest these channels need creative content or segmentation redesign. Future research should explore channel synergy without compromising brand exclusivity.*")

# Footer
st.markdown("---")
st.caption("🚀 Built by Yasaswini Reddy Naga | Independent Researcher| SLU Alumni")
