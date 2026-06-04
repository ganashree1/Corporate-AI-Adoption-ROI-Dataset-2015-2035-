# insights.py

import pandas as pd


# ==========================================
# EXECUTIVE INSIGHTS
# ==========================================

def executive_insights(df):

    insights = []

    total_companies = len(df)

    avg_adoption = round(
        df["ai_adoption_level"].mean() * 100,
        2
    )

    total_investment = round(
        df["ai_investment_usd"].sum() / 1_000_000,
        2
    )

    total_revenue = round(
        df["revenue_impact"].sum() / 1_000_000,
        2
    )

    insights.append(
        f"📊 Dataset contains {total_companies:,} companies."
    )

    insights.append(
        f"🤖 Average AI Adoption Rate is {avg_adoption}%."
    )

    insights.append(
        f"💰 Total AI Investment is ${total_investment} Million."
    )

    insights.append(
        f"📈 Total Revenue Impact generated is ${total_revenue} Million."
    )

    return insights


# ==========================================
# INDUSTRY INSIGHTS
# ==========================================

def industry_insights(df):

    insights = []

    industry_revenue = (
        df.groupby("industry")
        ["revenue_impact"]
        .sum()
    )

    industry_adoption = (
        df.groupby("industry")
        ["ai_adoption_level"]
        .mean()
    )

    best_revenue_industry = industry_revenue.idxmax()

    best_adoption_industry = industry_adoption.idxmax()

    insights.append(
        f"🏆 Highest Revenue Industry: {best_revenue_industry}"
    )

    insights.append(
        f"🚀 Highest AI Adoption Industry: {best_adoption_industry}"
    )

    return insights


# ==========================================
# COUNTRY INSIGHTS
# ==========================================

def country_insights(df):

    insights = []

    country_revenue = (
        df.groupby("country")
        ["revenue_impact"]
        .sum()
    )

    country_adoption = (
        df.groupby("country")
        ["ai_adoption_level"]
        .mean()
    )

    top_country = country_revenue.idxmax()

    top_adoption_country = country_adoption.idxmax()

    insights.append(
        f"🌍 Top Revenue Generating Country: {top_country}"
    )

    insights.append(
        f"📈 Highest Adoption Country: {top_adoption_country}"
    )

    return insights


# ==========================================
# ROI INSIGHTS
# ==========================================

def roi_insights(df):

    insights = []

    roi = (

        (
            df["revenue_impact"].sum()
            -
            df["ai_investment_usd"].sum()
        )
        /
        df["ai_investment_usd"].sum()

    ) * 100

    roi = round(roi, 2)

    insights.append(
        f"💵 Overall ROI achieved is {roi}%."
    )

    if roi > 100:

        insights.append(
            "✅ AI investments are generating strong returns."
        )

    elif roi > 50:

        insights.append(
            "⚡ AI investments show healthy growth."
        )

    else:

        insights.append(
            "⚠ AI investments require optimization."
        )

    return insights


# ==========================================
# AI MATURITY INSIGHTS
# ==========================================

def maturity_insights(df):

    insights = []

    avg_score = round(
        df["ai_maturity_score"].mean(),
        2
    )

    insights.append(
        f"📊 Average AI Maturity Score: {avg_score}"
    )

    if avg_score >= 75:

        insights.append(
            "🏆 Organizations are AI Leaders."
        )

    elif avg_score >= 50:

        insights.append(
            "🚀 Organizations are AI Advanced."
        )

    else:

        insights.append(
            "📚 Organizations are still developing AI capabilities."
        )

    return insights


# ==========================================
# TRAINING INSIGHTS
# ==========================================

def training_insights(df):

    insights = []

    avg_hours = round(
        df["employee_ai_training_hours"].mean(),
        2
    )

    insights.append(
        f"🎓 Average AI Training Hours: {avg_hours}"
    )

    if avg_hours > 50:

        insights.append(
            "✅ Strong employee AI upskilling initiatives."
        )

    else:

        insights.append(
            "⚠ Additional employee AI training recommended."
        )

    return insights


# ==========================================
# AUTOMATION INSIGHTS
# ==========================================

def automation_insights(df):

    insights = []

    avg_rate = round(
        df["automation_rate"].mean() * 100,
        2
    )

    insights.append(
        f"⚙ Average Automation Rate: {avg_rate}%"
    )

    return insights


# ==========================================
# PRODUCTIVITY INSIGHTS
# ==========================================

def productivity_insights(df):

    insights = []

    avg_gain = round(
        df["productivity_gain"].mean() * 100,
        2
    )

    insights.append(
        f"📈 Average Productivity Gain: {avg_gain}%"
    )

    return insights


# ==========================================
# TOP PERFORMERS TABLE
# ==========================================

def top_performers(df):

    top_df = (

        df.sort_values(
            by="revenue_impact",
            ascending=False
        )

        .head(10)

        [[
            "industry",
            "country",
            "revenue_impact",
            "ai_investment_usd",
            "ai_maturity_score"
        ]]
    )

    return top_df


# ==========================================
# BUSINESS RECOMMENDATIONS
# ==========================================

def recommendations(df):

    recommendations = []

    avg_adoption = (
        df["ai_adoption_level"].mean()
        * 100
    )

    avg_maturity = (
        df["ai_maturity_score"].mean()
    )

    if avg_adoption < 60:

        recommendations.append(
            "Increase AI adoption across departments."
        )

    if avg_maturity < 70:

        recommendations.append(
            "Invest in AI governance and maturity frameworks."
        )

    if (
        df["employee_ai_training_hours"]
        .mean()
        < 50
    ):

        recommendations.append(
            "Expand employee AI training programs."
        )

    recommendations.append(
        "Focus on high ROI AI deployment opportunities."
    )

    recommendations.append(
        "Monitor industry leaders and benchmark performance."
    )

    return recommendations


# ==========================================
# MASTER INSIGHTS FUNCTION
# ==========================================

def generate_all_insights(df):

    insights = []

    insights.extend(
        executive_insights(df)
    )

    insights.extend(
        industry_insights(df)
    )

    insights.extend(
        country_insights(df)
    )

    insights.extend(
        roi_insights(df)
    )

    insights.extend(
        maturity_insights(df)
    )

    insights.extend(
        training_insights(df)
    )

    insights.extend(
        automation_insights(df)
    )

    insights.extend(
        productivity_insights(df)
    )

    return insights
