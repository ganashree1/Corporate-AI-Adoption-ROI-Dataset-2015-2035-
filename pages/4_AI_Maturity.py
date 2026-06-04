import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Maturity Analysis",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Maturity Analysis Dashboard")
st.markdown("Evaluate and visualize AI maturity levels across countries / industries / organizations.")

# =========================
# DATA LOADING
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_data.csv")
    return df

df = load_data()

# =========================
# COLUMN CHECK
# =========================
st.sidebar.header("⚙️ Settings")

entity_col = st.sidebar.selectbox(
    "Select Entity Column",
    options=df.columns,
    index=0
)

# Try to auto-detect numeric columns
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

if len(numeric_cols) == 0:
    st.error("No numeric columns found for AI maturity scoring.")
    st.stop()

selected_features = st.sidebar.multiselect(
    "Select Features for Maturity Score",
    options=numeric_cols,
    default=numeric_cols[:3] if len(numeric_cols) >= 3 else numeric_cols
)

if len(selected_features) == 0:
    st.warning("Select at least one feature.")
    st.stop()

# =========================
# DATA CLEANING
# =========================
df = df.dropna(subset=selected_features + [entity_col])

# =========================
# AI MATURITY SCORE (NORMALIZED INDEX)
# =========================
df["AI_Maturity_Score"] = df[selected_features].mean(axis=1)

# Normalize score to 0–100
df["AI_Maturity_Score"] = (
    (df["AI_Maturity_Score"] - df["AI_Maturity_Score"].min())
    / (df["AI_Maturity_Score"].max() - df["AI_Maturity_Score"].min())
) * 100

# =========================
# MATURITY LEVEL CLASSIFICATION
# =========================
def classify(score):
    if score < 25:
        return "Low"
    elif score < 50:
        return "Basic"
    elif score < 75:
        return "Advanced"
    else:
        return "Leading"

df["Maturity_Level"] = df["AI_Maturity_Score"].apply(classify)

# =========================
# KPIs
# =========================
st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Average AI Maturity", f"{df['AI_Maturity_Score'].mean():.2f}")
col2.metric("Highest Score", f"{df['AI_Maturity_Score'].max():.2f}")
col3.metric("Lowest Score", f"{df['AI_Maturity_Score'].min():.2f}")
col4.metric("Entities Analyzed", df[entity_col].nunique())

st.divider()

# =========================
# MATURITY DISTRIBUTION
# =========================
st.subheader("📈 AI Maturity Distribution")

fig1 = px.histogram(
    df,
    x="AI_Maturity_Score",
    nbins=20,
    title="Distribution of AI Maturity Scores",
    color_discrete_sequence=["#636EFA"]
)

st.plotly_chart(fig1, use_container_width=True)

# =========================
# MATURITY LEVEL BREAKDOWN
# =========================
st.subheader("🏷️ Maturity Level Breakdown")

level_counts = df["Maturity_Level"].value_counts().reset_index()
level_counts.columns = ["Maturity_Level", "Count"]

fig2 = px.pie(
    level_counts,
    names="Maturity_Level",
    values="Count",
    title="AI Maturity Segmentation"
)

st.plotly_chart(fig2, use_container_width=True)

# =========================
# TOP ENTITIES
# =========================
st.subheader(f"🏆 Top {entity_col} by AI Maturity")

top_df = df.sort_values(by="AI_Maturity_Score", ascending=False).head(15)

fig3 = px.bar(
    top_df,
    x=entity_col,
    y="AI_Maturity_Score",
    color="Maturity_Level",
    title="Top AI Mature Entities",
    text_auto=True
)

st.plotly_chart(fig3, use_container_width=True)

# =========================
# FEATURE CONTRIBUTION
# =========================
st.subheader("📊 Feature Contribution Analysis")

feature_means = df[selected_features].mean().reset_index()
feature_means.columns = ["Feature", "Average Value"]

fig4 = px.bar(
    feature_means,
    x="Feature",
    y="Average Value",
    title="Average Contribution of Selected Features"
)

st.plotly_chart(fig4, use_container_width=True)

# =========================
# CORRELATION HEATMAP
# =========================
st.subheader("🔥 Feature Correlation Heatmap")

corr = df[selected_features + ["AI_Maturity_Score"]].corr()

fig5 = px.imshow(
    corr,
    text_auto=True,
    title="Correlation Matrix"
)

st.plotly_chart(fig5, use_container_width=True)

# =========================
# INSIGHTS SECTION
# =========================
st.subheader("🧠 AI Maturity Insights")

top_entity = top_df.iloc[0][entity_col] if not top_df.empty else "N/A"
avg_score = df["AI_Maturity_Score"].mean()

st.markdown(f"""
- 🤖 Overall AI maturity average score is **{avg_score:.2f}**
- 🏆 Most advanced entity: **{top_entity}**
- 📊 Majority entities fall into mid-range maturity levels
- 📌 Feature selection strongly impacts maturity scoring accuracy
- 🚀 Organizations can improve maturity by investing in selected key features
""")

# =========================
# DOWNLOAD DATA
# =========================
st.subheader("⬇️ Download Results")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download AI Maturity Dataset",
    data=csv,
    file_name="ai_maturity_analysis.csv",
    mime="text/csv"
)
