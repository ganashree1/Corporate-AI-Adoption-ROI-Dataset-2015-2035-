import streamlit as st
import pandas as pd

from src.preprocessing import load_data
from src.analytics import executive_metrics
from src.visualizations import apply_theme, yearly_adoption_trend, revenue_trend
from src.insights import generate_all_insights


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Corporate AI Analytics",
    page_icon="🚀",
    layout="wide"
)


# ==========================================
# LOAD DATA
# ==========================================

@st.cache_data
def get_data():

    df = load_data("data/corporate_ai_adoption_dataset.csv")

    return df


df = get_data()


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

st.sidebar.image("assets/logo.png", width=180)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home Dashboard",
        "📊 Executive Dashboard",
        "🏭 Industry Analysis",
        "🌍 Country Analysis",
        "🤖 AI Maturity",
        "📈 Predictive Analytics"
    ]
)


# ==========================================
# HOME PAGE
# ==========================================

if page == "🏠 Home Dashboard":

    st.title("🚀 Corporate AI Adoption Analytics Platform")

    st.markdown(
        """
        A powerful AI-driven analytics system to analyze:

        - AI adoption trends  
        - Industry performance  
        - Country-wise intelligence  
        - ROI & revenue impact  
        - AI maturity & automation levels  
        """
    )

    st.divider()


    # KPI METRICS

    metrics = executive_metrics(df)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Total Companies",
            f"{metrics['Total Companies']:,}"
        )

    with c2:
        st.metric(
            "AI Adoption",
            f"{metrics['Average AI Adoption']}%"
        )

    with c3:
        st.metric(
            "Revenue Impact",
            f"${metrics['Total Revenue Impact']/1e9:.2f}B"
        )

    with c4:
        st.metric(
            "Investment",
            f"${metrics['Total AI Investment']/1e9:.2f}B"
        )


    st.divider()


    # TREND CHARTS

    st.subheader("📈 AI Adoption & Revenue Trends")

    trend_df = df.groupby("year").mean(numeric_only=True).reset_index()

    col1, col2 = st.columns(2)

    with col1:

        fig1 = yearly_adoption_trend(trend_df)

        st.plotly_chart(apply_theme(fig1), use_container_width=True)

    with col2:

        fig2 = revenue_trend(trend_df)

        st.plotly_chart(apply_theme(fig2), use_container_width=True)


    # INSIGHTS

    st.subheader("🧠 Key Insights")

    for insight in generate_all_insights(df):

        st.success(insight)


# ==========================================
# EXECUTIVE DASHBOARD PAGE
# ==========================================

elif page == "📊 Executive Dashboard":

    st.switch_page("pages/1_Executive_Dashboard.py")


# ==========================================
# INDUSTRY ANALYSIS PAGE
# ==========================================

elif page == "🏭 Industry Analysis":

    st.switch_page("pages/2_Industry_Analysis.py")


# ==========================================
# COUNTRY ANALYSIS PAGE
# ==========================================

elif page == "🌍 Country Analysis":

    st.info("Run pages/3_Country_Analysis.py (to be added)")


# ==========================================
# AI MATURITY PAGE
# ==========================================

elif page == "🤖 AI Maturity":

    st.info("Run pages/4_AI_Maturity.py (to be added)")


# ==========================================
# PREDICTIVE ANALYTICS PAGE
# ==========================================

elif page == "📈 Predictive Analytics":

    st.info("Run pages/5_Predictive_Analytics.py (to be added)")


# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Corporate AI Adoption Analytics | Built with Streamlit + Python + Plotly"
)
