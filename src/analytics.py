# analytics.py

import pandas as pd
import numpy as np


# ==========================================
# EXECUTIVE KPI METRICS
# ==========================================

def executive_metrics(df):

    metrics = {

        "Total Companies":
            len(df),

        "Total AI Investment":
            round(df["ai_investment_usd"].sum(), 2),

        "Total Revenue Impact":
            round(df["revenue_impact"].sum(), 2),

        "Total Cost Savings":
            round(df["cost_savings"].sum(), 2),

        "Average AI Adoption":
            round(df["ai_adoption_level"].mean() * 100, 2),

        "Average Productivity Gain":
            round(df["productivity_gain"].mean() * 100, 2),

        "Average Automation Rate":
            round(df["automation_rate"].mean() * 100, 2),

        "Average Maturity Score":
            round(df["ai_maturity_score"].mean(), 2),

        "Average Training Hours":
            round(
                df["employee_ai_training_hours"].mean(),
                2
            ),

        "Total Deployments":
            int(df["deployment_count"].sum())
    }

    return metrics


# ==========================================
# INDUSTRY ANALYSIS
# ==========================================

def industry_performance(df):

    result = df.groupby("industry").agg({

        "ai_adoption_level": "mean",
        "ai_investment_usd": "sum",
        "revenue_impact": "sum",
        "cost_savings": "sum",
        "productivity_gain": "mean",
        "automation_rate": "mean",
        "ai_maturity_score": "mean",
        "deployment_count": "sum"

    }).reset_index()

    return result.sort_values(
        by="revenue_impact",
        ascending=False
    )


# ==========================================
# COUNTRY ANALYSIS
# ==========================================

def country_performance(df):

    result = df.groupby("country").agg({

        "ai_adoption_level": "mean",
        "ai_investment_usd": "sum",
        "revenue_impact": "sum",
        "cost_savings": "sum",
        "ai_maturity_score": "mean"

    }).reset_index()

    return result.sort_values(
        by="revenue_impact",
        ascending=False
    )


# ==========================================
# YEARLY TREND ANALYSIS
# ==========================================

def yearly_trends(df):

    result = df.groupby("year").agg({

        "ai_adoption_level": "mean",
        "ai_investment_usd": "sum",
        "revenue_impact": "sum",
        "cost_savings": "sum",
        "deployment_count": "sum"

    }).reset_index()

    return result


# ==========================================
# ROI ANALYSIS
# ==========================================

def roi_analysis(df):

    df_roi = df.copy()

    df_roi["roi"] = (

        (
            df_roi["revenue_impact"]
            -
            df_roi["ai_investment_usd"]
        )
        /
        df_roi["ai_investment_usd"]

    ) * 100

    return df_roi


# ==========================================
# TOP INDUSTRIES
# ==========================================

def top_industries(df, n=10):

    return (

        df.groupby("industry")
        ["revenue_impact"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()

    )


# ==========================================
# TOP COUNTRIES
# ==========================================

def top_countries(df, n=10):

    return (

        df.groupby("country")
        ["revenue_impact"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()

    )


# ==========================================
# AI MATURITY ANALYSIS
# ==========================================

def maturity_distribution(df):

    return (

        df.groupby("maturity_level")
        .size()
        .reset_index(name="count")

    )


# ==========================================
# INVESTMENT CATEGORY ANALYSIS
# ==========================================

def investment_category_analysis(df):

    return (

        df.groupby("investment_category")
        .agg({

            "revenue_impact": "mean",
            "cost_savings": "mean",
            "ai_adoption_level": "mean"

        })

        .reset_index()

    )


# ==========================================
# CORRELATION MATRIX
# ==========================================

def correlation_matrix(df):

    numeric_df = df.select_dtypes(
        include=np.number
    )

    return numeric_df.corr()


# ==========================================
# COMPANY RANKING
# ==========================================

def company_ranking(df):

    ranking = df.sort_values(

        by="revenue_impact",
        ascending=False

    )

    return ranking.head(20)


# ==========================================
# DEPLOYMENT ANALYSIS
# ==========================================

def deployment_analysis(df):

    result = df.groupby("industry").agg({

        "deployment_count": "sum"

    }).reset_index()

    return result.sort_values(

        by="deployment_count",
        ascending=False

    )


# ==========================================
# PRODUCTIVITY ANALYSIS
# ==========================================

def productivity_analysis(df):

    result = df.groupby("industry").agg({

        "productivity_gain": "mean"

    }).reset_index()

    return result.sort_values(

        by="productivity_gain",
        ascending=False

    )


# ==========================================
# AUTOMATION ANALYSIS
# ==========================================

def automation_analysis(df):

    result = df.groupby("industry").agg({

        "automation_rate": "mean"

    }).reset_index()

    return result.sort_values(

        by="automation_rate",
        ascending=False

    )


# ==========================================
# TRAINING ANALYSIS
# ==========================================

def training_analysis(df):

    result = df.groupby("industry").agg({

        "employee_ai_training_hours":
        "mean"

    }).reset_index()

    return result.sort_values(

        by="employee_ai_training_hours",
        ascending=False

    )


# ==========================================
# INSIGHTS GENERATOR
# ==========================================

def generate_business_insights(df):

    insights = []

    top_industry = (

        df.groupby("industry")
        ["revenue_impact"]
        .sum()
        .idxmax()

    )

    insights.append(
        f"🏆 Highest revenue impact industry: {top_industry}"
    )

    top_country = (

        df.groupby("country")
        ["revenue_impact"]
        .sum()
        .idxmax()

    )

    insights.append(
        f"🌍 Top performing country: {top_country}"
    )

    adoption = round(

        df["ai_adoption_level"].mean()
        * 100,

        2

    )

    insights.append(
        f"🤖 Average AI adoption rate is {adoption}%"
    )

    maturity = round(

        df["ai_maturity_score"].mean(),
        2

    )

    insights.append(
        f"📈 Average AI maturity score is {maturity}"
    )

    roi = round(

        (
            df["revenue_impact"].sum()
            -
            df["ai_investment_usd"].sum()
        )
        /
        df["ai_investment_usd"].sum()

        * 100,

        2

    )

    insights.append(
        f"💰 Overall AI ROI is {roi}%"
    )

    return insights
