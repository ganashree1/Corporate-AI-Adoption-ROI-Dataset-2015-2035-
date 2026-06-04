# pages/2_Industry_Analysis.py

import streamlit as st

from src.preprocessing import load_data
from src.analytics import *
from src.visualizations import *
from src.insights import *


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Industry Analysis",
    page_icon="🏭",
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
# HEADER
# ==========================================

st.title("🏭 Industry Wise AI Analytics")

st.markdown(
    """
    Deep dive into how different industries are adopting AI,
    generating revenue, saving costs, and improving productivity.
    """
)

st.divider()


# ==========================================
# INDUSTRY FILTER (OPTIONAL)
# ==========================================

industries = st.sidebar.multiselect(
    "Filter Industry",
    df["industry"].unique()
)

if industries:
    df = df[df["industry"].isin(industries)]


# ==========================================
# INDUSTRY DATA
# ==========================================

industry_df = industry_performance(df)


# ==========================================
# KPI SECTION
# ==========================================

st.subheader("📊 Industry Performance Overview")

top_industry = industry_df.iloc[0]["industry"]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Top Industry",
        top_industry
    )

with col2:
    st.metric(
        "Avg Adoption",
        f"{industry_df['ai_adoption_level'].mean()*100:.2f}%"
    )

with col3:
    st.metric(
        "Total Revenue",
        f"${industry_df['revenue_impact'].sum()/1e9:.2f}B"
    )

with col4:
    st.metric(
        "Total Deployments",
        f"{industry_df['deployment_count'].sum():,}"
    )


st.divider()


# ==========================================
# CHART 1: AI ADOPTION BY INDUSTRY
# ==========================================

st.subheader("🤖 AI Adoption by Industry")

fig1 = adoption_by_industry(industry_df)

st.plotly_chart(
    apply_theme(fig1),
    use_container_width=True
)


# ==========================================
# CHART 2: REVENUE IMPACT
# ==========================================

st.subheader("💰 Revenue Impact by Industry")

fig2 = revenue_by_industry(industry_df)

st.plotly_chart(
    apply_theme(fig2),
    use_container_width=True
)


# ==========================================
# CHART 3: COST SAVINGS
# ==========================================

st.subheader("💸 Cost Savings by Industry")

fig3 = cost_savings_chart(industry_df)

st.plotly_chart(
    apply_theme(fig3),
    use_container_width=True
)


# ==========================================
# CHART 4: PRODUCTIVITY GAIN
# ==========================================

st.subheader("📈 Productivity Gain by Industry")

fig4 = productivity_chart(industry_df)

st.plotly_chart(
    apply_theme(fig4),
    use_container_width=True
)


# ==========================================
# CHART 5: AUTOMATION RATE
# ==========================================

st.subheader("⚙ Automation Rate by Industry")

fig5 = automation_chart(industry_df)

st.plotly_chart(
    apply_theme(fig5),
    use_container_width=True
)


# ==========================================
# CHART 6: TRAINING HOURS
# ==========================================

st.subheader("🎓 AI Training Hours by Industry")

fig6 = training_hours_chart(industry_df)

st.plotly_chart(
    apply_theme(fig6),
    use_container_width=True
)


# ==========================================
# TREEMAP ANALYSIS
# ==========================================

st.subheader("🌳 Revenue Contribution Treemap")

fig7 = treemap_chart(industry_df)

st.plotly_chart(
    apply_theme(fig7),
    use_container_width=True
)


# ==========================================
# SUNBURST VIEW
# ==========================================

st.subheader("🌍 Industry Revenue Distribution")

fig8 = sunburst_chart(industry_df)

st.plotly_chart(
    apply_theme(fig8),
    use_container_width=True
)


# ==========================================
# TOP INDUSTRIES TABLE
# ==========================================

st.subheader("🏆 Top Industries by Revenue Impact")

top_df = top_industries(industry_df)

st.dataframe(
    top_df,
    use_container_width=True
)


# ==========================================
# INSIGHTS SECTION
# ==========================================

st.subheader("🧠 Industry Insights")

insights = industry_insights(industry_df)

for i in insights:
    st.success(i)


# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Industry Analysis | Corporate AI Adoption Dashboard"
)
