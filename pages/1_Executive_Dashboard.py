# pages/1_Executive_Dashboard.py

import streamlit as st
import pandas as pd

from src.preprocessing import load_data
from src.analytics import *
from src.visualizations import *
from src.insights import *


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# LOAD DATA
# ==========================================

@st.cache_data
def get_data():
    return load_data(
        "data/corporate_ai_adoption_dataset.csv"
    )


df = get_data()


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.image(
    "assets/logo.png",
    width=180
)

st.sidebar.title("Dashboard Filters")

industry_filter = st.sidebar.multiselect(
    "Select Industry",
    options=sorted(df["industry"].unique())
)

country_filter = st.sidebar.multiselect(
    "Select Country",
    options=sorted(df["country"].unique())
)

year_filter = st.sidebar.multiselect(
    "Select Year",
    options=sorted(df["year"].unique())
)

if industry_filter:
    df = df[df["industry"].isin(industry_filter)]

if country_filter:
    df = df[df["country"].isin(country_filter)]

if year_filter:
    df = df[df["year"].isin(year_filter)]


# ==========================================
# HEADER
# ==========================================

st.title("🚀 Executive AI Analytics Dashboard")

st.markdown("""
Monitor AI adoption, investments, productivity,
revenue impact, and organizational maturity.
""")


# ==========================================
# KPI SECTION
# ==========================================

metrics = executive_metrics(df)

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric(
        "Companies",
        f"{metrics['Total Companies']:,}"
    )

with c2:
    st.metric(
        "AI Adoption %",
        f"{metrics['Average AI Adoption']}%"
    )

with c3:
    st.metric(
        "Investment",
        f"${metrics['Total AI Investment']/1e9:.2f}B"
    )

with c4:
    st.metric(
        "Revenue Impact",
        f"${metrics['Total Revenue Impact']/1e9:.2f}B"
    )

with c5:
    st.metric(
        "Deployments",
        f"{metrics['Total Deployments']:,}"
    )


st.divider()


# ==========================================
# SECOND KPI ROW
# ==========================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Cost Savings",
        f"${metrics['Total Cost Savings']/1e9:.2f}B"
    )

with c2:
    st.metric(
        "Automation Rate",
        f"{metrics['Average Automation Rate']}%"
    )

with c3:
    st.metric(
        "Productivity Gain",
        f"{metrics['Average Productivity Gain']}%"
    )

with c4:
    st.metric(
        "AI Maturity",
        f"{metrics['Average Maturity Score']}"
    )


# ==========================================
# CHARTS ROW 1
# ==========================================

st.subheader("📈 AI Adoption & Revenue Trends")

year_df = yearly_trends(df)

col1, col2 = st.columns(2)

with col1:

    fig = yearly_adoption_trend(year_df)

    st.plotly_chart(
        apply_theme(fig),
        use_container_width=True
    )

with col2:

    fig = revenue_trend(year_df)

    st.plotly_chart(
        apply_theme(fig),
        use_container_width=True
    )


# ==========================================
# CHARTS ROW 2
# ==========================================

st.subheader("🏭 Industry Analytics")

industry_df = industry_performance(df)

col1, col2 = st.columns(2)

with col1:

    fig = adoption_by_industry(
        industry_df
    )

    st.plotly_chart(
        apply_theme(fig),
        use_container_width=True
    )

with col2:

    fig = revenue_by_industry(
        industry_df
    )

    st.plotly_chart(
        apply_theme(fig),
        use_container_width=True
    )


# ==========================================
# CHARTS ROW 3
# ==========================================

st.subheader("🌍 Global Performance")

country_df = country_performance(df)

fig = country_heatmap(country_df)

st.plotly_chart(
    apply_theme(fig),
    use_container_width=True
)


# ==========================================
# CHARTS ROW 4
# ==========================================

st.subheader(
    "💰 Investment vs Revenue Impact"
)

sample_df = df.sample(
    min(5000, len(df)),
    random_state=42
)

fig = investment_vs_revenue(
    sample_df
)

st.plotly_chart(
    apply_theme(fig),
    use_container_width=True
)


# ==========================================
# AI MATURITY GAUGE
# ==========================================

st.subheader("🤖 AI Maturity Score")

avg_score = round(
    df["ai_maturity_score"].mean(),
    2
)

fig = ai_maturity_gauge(
    avg_score
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ==========================================
# CORRELATION HEATMAP
# ==========================================

st.subheader(
    "🔍 Correlation Analysis"
)

corr = correlation_matrix(df)

fig = correlation_heatmap(corr)

st.plotly_chart(
    apply_theme(fig),
    use_container_width=True
)


# ==========================================
# TOP PERFORMERS
# ==========================================

st.subheader(
    "🏆 Top Performing Organizations"
)

top_df = top_performers(df)

st.dataframe(
    top_df,
    use_container_width=True
)


# ==========================================
# AI INSIGHTS
# ==========================================

st.subheader(
    "🧠 AI Generated Insights"
)

insights = generate_all_insights(df)

for item in insights:
    st.success(item)


# ==========================================
# RECOMMENDATIONS
# ==========================================

st.subheader(
    "📌 Strategic Recommendations"
)

for rec in recommendations(df):

    st.info(rec)


# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Corporate AI Adoption Analytics Dashboard | Streamlit + Plotly + Python"
)
