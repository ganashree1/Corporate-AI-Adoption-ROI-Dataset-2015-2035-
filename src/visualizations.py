# visualizations.py

import plotly.express as px
import plotly.graph_objects as go


# ==========================================
# AI ADOPTION BY INDUSTRY
# ==========================================

def adoption_by_industry(df):

    fig = px.bar(
        df,
        x="industry",
        y="ai_adoption_level",
        color="ai_adoption_level",
        title="AI Adoption by Industry"
    )

    fig.update_layout(
        xaxis_title="Industry",
        yaxis_title="AI Adoption Level",
        height=500
    )

    return fig


# ==========================================
# YEARLY AI ADOPTION TREND
# ==========================================

def yearly_adoption_trend(df):

    fig = px.line(
        df,
        x="year",
        y="ai_adoption_level",
        markers=True,
        title="Yearly AI Adoption Trend"
    )

    fig.update_layout(height=500)

    return fig


# ==========================================
# REVENUE IMPACT BY INDUSTRY
# ==========================================

def revenue_by_industry(df):

    fig = px.bar(
        df,
        x="industry",
        y="revenue_impact",
        color="revenue_impact",
        title="Revenue Impact by Industry"
    )

    fig.update_layout(height=500)

    return fig


# ==========================================
# COST SAVINGS BY INDUSTRY
# ==========================================

def cost_savings_chart(df):

    fig = px.bar(
        df,
        x="industry",
        y="cost_savings",
        color="cost_savings",
        title="Cost Savings by Industry"
    )

    return fig


# ==========================================
# INVESTMENT VS REVENUE
# ==========================================

def investment_vs_revenue(df):

    fig = px.scatter(
        df,
        x="ai_investment_usd",
        y="revenue_impact",
        color="industry",
        size="deployment_count",
        hover_name="industry",
        title="Investment vs Revenue Impact"
    )

    fig.update_layout(height=600)

    return fig


# ==========================================
# COUNTRY HEATMAP
# ==========================================

def country_heatmap(df):

    fig = px.choropleth(
        df,
        locations="country",
        locationmode="country names",
        color="ai_adoption_level",
        hover_name="country",
        title="Global AI Adoption Heatmap"
    )

    return fig


# ==========================================
# AI MATURITY DISTRIBUTION
# ==========================================

def maturity_distribution(df):

    fig = px.pie(
        df,
        names="maturity_level",
        values="count",
        title="AI Maturity Distribution"
    )

    return fig


# ==========================================
# ROI DISTRIBUTION
# ==========================================

def roi_histogram(df):

    fig = px.histogram(
        df,
        x="roi",
        nbins=30,
        title="ROI Distribution"
    )

    return fig


# ==========================================
# CORRELATION HEATMAP
# ==========================================

def correlation_heatmap(corr_matrix):

    fig = px.imshow(
        corr_matrix,
        text_auto=True,
        title="Correlation Matrix"
    )

    return fig


# ==========================================
# PRODUCTIVITY ANALYSIS
# ==========================================

def productivity_chart(df):

    fig = px.bar(
        df,
        x="industry",
        y="productivity_gain",
        color="productivity_gain",
        title="Productivity Gain by Industry"
    )

    return fig


# ==========================================
# AUTOMATION RATE ANALYSIS
# ==========================================

def automation_chart(df):

    fig = px.bar(
        df,
        x="industry",
        y="automation_rate",
        color="automation_rate",
        title="Automation Rate by Industry"
    )

    return fig


# ==========================================
# TRAINING HOURS ANALYSIS
# ==========================================

def training_hours_chart(df):

    fig = px.bar(
        df,
        x="industry",
        y="employee_ai_training_hours",
        color="employee_ai_training_hours",
        title="Average AI Training Hours"
    )

    return fig


# ==========================================
# TOP COUNTRIES
# ==========================================

def top_countries_chart(df):

    fig = px.bar(
        df,
        x="country",
        y="revenue_impact",
        color="revenue_impact",
        title="Top Countries by Revenue Impact"
    )

    return fig


# ==========================================
# TOP INDUSTRIES
# ==========================================

def top_industries_chart(df):

    fig = px.bar(
        df,
        x="industry",
        y="revenue_impact",
        color="revenue_impact",
        title="Top Industries by Revenue Impact"
    )

    return fig


# ==========================================
# SUNBURST CHART
# ==========================================

def sunburst_chart(df):

    fig = px.sunburst(
        df,
        path=["country", "industry"],
        values="revenue_impact",
        title="Country → Industry Revenue Distribution"
    )

    return fig


# ==========================================
# TREEMAP
# ==========================================

def treemap_chart(df):

    fig = px.treemap(
        df,
        path=["industry"],
        values="revenue_impact",
        title="Industry Revenue Treemap"
    )

    return fig


# ==========================================
# BOXPLOT OF INVESTMENT
# ==========================================

def investment_boxplot(df):

    fig = px.box(
        df,
        x="industry",
        y="ai_investment_usd",
        title="Investment Distribution"
    )

    return fig


# ==========================================
# DEPLOYMENT ANALYSIS
# ==========================================

def deployment_chart(df):

    fig = px.bar(
        df,
        x="industry",
        y="deployment_count",
        color="deployment_count",
        title="AI Deployments by Industry"
    )

    return fig


# ==========================================
# KPI GAUGE
# ==========================================

def ai_maturity_gauge(score):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=score,

            title={
                "text":"Average AI Maturity Score"
            },

            gauge={
                "axis":{
                    "range":[0,100]
                }
            }
        )
    )

    fig.update_layout(height=400)

    return fig


# ==========================================
# REVENUE TREND
# ==========================================

def revenue_trend(df):

    fig = px.line(
        df,
        x="year",
        y="revenue_impact",
        markers=True,
        title="Revenue Impact Trend"
    )

    return fig


# ==========================================
# INVESTMENT TREND
# ==========================================

def investment_trend(df):

    fig = px.line(
        df,
        x="year",
        y="ai_investment_usd",
        markers=True,
        title="Investment Trend"
    )

    return fig


# ==========================================
# COST SAVINGS TREND
# ==========================================

def savings_trend(df):

    fig = px.line(
        df,
        x="year",
        y="cost_savings",
        markers=True,
        title="Cost Savings Trend"
    )

    return fig


# ==========================================
# DASHBOARD THEME
# ==========================================

def apply_theme(fig):

    fig.update_layout(

        template="plotly_dark",

        title_x=0.5,

        font=dict(size=14),

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    return fig
