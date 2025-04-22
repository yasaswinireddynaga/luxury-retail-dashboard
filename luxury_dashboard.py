import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Sidebar Filters
st.sidebar.title("🔧 Campaign Inputs")
channel = st.sidebar.selectbox("Channel", ['Email', 'Social Media', 'SMS'])
subject_length = st.sidebar.slider("Subject Length (characters)", 10, 100, 50)
personalized = st.sidebar.checkbox("Include Personalization")

# Main Title
st.title("💼 Luxury Retail Strategy Dashboard")
st.markdown("Interactive dashboard showcasing machine learning insights and market targeting strategies for luxury fashion brands.")

# Tab Layout
tabs = st.tabs(["📊 Feature Importance", "🔗 Association Rules", "🧠 Campaign Simulator"])

# Tab 1: Feature Importance
with tabs[0]:
    st.subheader("RandomForest Feature Importance")
    fig1, ax1 = plt.subplots()
    sns.barplot(data=feature_importance, y='Feature', x='Importance', ax=ax1)
    ax1.set_title("Importance of Features Influencing Campaign Performance")
    st.pyplot(fig1)
    st.markdown("🛈 *subject_length* and *channel_email* are the top predictors.")

# Tab 2: Association Rules
with tabs[1]:
    st.subheader("Top 10 Demographic-Based Association Rules")
    st.dataframe(association_rules, use_container_width=True)
    fig2, ax2 = plt.subplots()
    sns.barplot(data=association_rules, y='Rule', x='Confidence', ax=ax2)
    ax2.set_xlim(0.7, 1.0)
    ax2.set_title("Confidence Levels for Rule Predictions")
    st.pyplot(fig2)
    st.markdown("🛈 Higher confidence means more reliable targeting patterns.")

# Tab 3: Campaign Simulator
with tabs[2]:
    st.subheader("Predict Campaign Effectiveness")
    effectiveness_score = 0.5
    effectiveness_score += 0.1 if channel == 'Email' else -0.05
    effectiveness_score += 0.1 if personalized else 0
    effectiveness_score += 0.01 * (subject_length / 100)
    effectiveness_score = round(min(1.0, effectiveness_score), 2)

    # Color-coded display
    if effectiveness_score >= 0.75:
        color = "🟢 High"
    elif effectiveness_score >= 0.5:
        color = "🟡 Moderate"
    else:
        color = "🔴 Low"

    st.metric("Predicted Effectiveness Score", f"{effectiveness_score*100:.0f}%", color)
    st.markdown("🛈 This score is a simulation based on model insights.")
    
    if effectiveness_score > 0.8:
        st.success("✨ Excellent! This campaign setup has high predicted effectiveness.")
    elif effectiveness_score < 0.5:
        st.warning("⚠️ Consider improving personalization or subject clarity.")

# Footer
st.markdown("---")
st.caption("Created by Yasaswini Reddy Naga | Master’s Research | Saint Louis University")
