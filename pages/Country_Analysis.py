import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Country Analysis Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Country Analysis Dashboard")
st.markdown("Deep insights into country-wise data performance and trends.")

# =========================
# DATA LOADING
# =========================
@st.cache_data
def load_data():
    # Change this path based on your project
    df = pd.read_csv("data/cleaned_data.csv")
    return df

df = load_data()

# =========================
# COLUMN CHECK
# =========================
required_columns = ["country"]

if "country" not in df.columns:
    st.error("Dataset must contain a 'country' column.")
    st.stop()

# =========================
# SIDEBAR FILTERS
# =========================
st.sidebar.header("🔎 Filters")

countries = df["country"].dropna().unique().tolist()
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=countries,
    default=countries[:10] if len(countries) > 10 else countries
)

filtered_df = df[df["country"].isin(selected_countries)]

# =========================
# KPIs
# =========================
st.subheader("📊 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(filtered_df))
col2.metric("Countries Selected", filtered_df["country"].nunique())
col3.metric("Missing Values", filtered_df.isnull().sum().sum())

st.divider()

# =========================
# TOP COUNTRIES BY FREQUENCY
# =========================
st.subheader("🏆 Top Countries by Records")

country_counts = (
    filtered_df["country"]
    .value_counts()
    .reset_index()
)
country_counts.columns = ["country", "count"]

fig1 = px.bar(
    country_counts.head(15),
    x="country",
    y="count",
    text="count",
    title="Top 15 Countries"
)

st.plotly_chart(fig1, use_container_width=True)

# =========================
# PIE CHART
# =========================
st.subheader("🥧 Country Distribution")

fig2 = px.pie(
    country_counts.head(10),
    names="country",
    values="count",
    title="Top 10 Country Share"
)

st.plotly_chart(fig2, use_container_width=True)

# =========================
# OPTIONAL NUMERIC ANALYSIS
# =========================
numeric_cols = filtered_df.select_dtypes(include=["int64", "float64"]).columns.tolist()

if len(numeric_cols) > 0:
    st.subheader("📈 Numeric Analysis by Country")

    selected_metric = st.selectbox("Select Metric", numeric_cols)

    country_metric = filtered_df.groupby("country")[selected_metric].mean().reset_index()

    fig3 = px.bar(
        country_metric.sort_values(by=selected_metric, ascending=False).head(15),
        x="country",
        y=selected_metric,
        title=f"Average {selected_metric} by Country"
    )

    st.plotly_chart(fig3, use_container_width=True)

# =========================
# HEATMAP (OPTIONAL CORRELATION)
# =========================
if len(numeric_cols) > 1:
    st.subheader("🔥 Correlation Heatmap")

    corr = filtered_df[numeric_cols].corr()

    fig4 = px.imshow(
        corr,
        text_auto=True,
        title="Feature Correlation Heatmap"
    )

    st.plotly_chart(fig4, use_container_width=True)

# =========================
# INSIGHTS SECTION
# =========================
st.subheader("🧠 Automated Insights")

top_country = country_counts.iloc[0]["country"] if not country_counts.empty else "N/A"
total_countries = filtered_df["country"].nunique()

st.markdown(f"""
- 🌍 Most dominant country in dataset: **{top_country}**
- 📊 Total unique countries analyzed: **{total_countries}**
- 📉 Data distribution shows concentration across top countries
- 📌 Consider balancing dataset if used for ML modeling
""")

# =========================
# DOWNLOAD OPTION
# =========================
st.subheader("⬇️ Export Data")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="country_analysis_data.csv",
    mime="text/csv"
)
