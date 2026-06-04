import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, accuracy_score, classification_report

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Predictive Analytics",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Predictive Analytics Dashboard")
st.markdown("Build ML models to predict outcomes from your dataset.")

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_data.csv")
    return df

df = load_data()

st.subheader("📂 Dataset Preview")
st.dataframe(df.head())

# =========================
# FEATURE SELECTION
# =========================
st.sidebar.header("⚙️ Model Settings")

all_columns = df.columns.tolist()

target_col = st.sidebar.selectbox(
    "Select Target Column (What to Predict)",
    options=all_columns
)

feature_cols = st.sidebar.multiselect(
    "Select Feature Columns",
    options=[col for col in all_columns if col != target_col],
    default=[col for col in all_columns if col != target_col][:5]
)

if len(feature_cols) == 0:
    st.warning("Please select at least one feature column.")
    st.stop()

# =========================
# CLEAN DATA
# =========================
model_df = df[feature_cols + [target_col]].dropna()

X = model_df[feature_cols]
y = model_df[target_col]

# =========================
# DETECT PROBLEM TYPE
# =========================
is_classification = y.dtype == "object" or y.nunique() < 10

st.info(f"Detected Problem Type: {'Classification' if is_classification else 'Regression'}")

# =========================
# TRAIN-TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# MODEL TRAINING
# =========================
if is_classification:
    model = RandomForestClassifier(n_estimators=100, random_state=42)
else:
    model = RandomForestRegressor(n_estimators=100, random_state=42)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# =========================
# METRICS
# =========================
st.subheader("📊 Model Performance")

col1, col2 = st.columns(2)

if is_classification:
    acc = accuracy_score(y_test, y_pred)
    col1.metric("Accuracy", f"{acc:.2f}")

    st.text("Classification Report:")
    st.text(classification_report(y_test, y_pred))

else:
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    col1.metric("MSE", f"{mse:.2f}")
    col2.metric("RMSE", f"{rmse:.2f}")

# =========================
# FEATURE IMPORTANCE
# =========================
st.subheader("📌 Feature Importance")

importance_df = pd.DataFrame({
    "Feature": feature_cols,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

fig1 = px.bar(
    importance_df,
    x="Feature",
    y="Importance",
    title="Feature Importance"
)

st.plotly_chart(fig1, use_container_width=True)

# =========================
# ACTUAL VS PREDICTED
# =========================
st.subheader("📈 Actual vs Predicted")

result_df = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})

fig2 = px.scatter(
    result_df,
    x="Actual",
    y="Predicted",
    title="Actual vs Predicted Values"
)

st.plotly_chart(fig2, use_container_width=True)

# =========================
# RESIDUALS (Regression only)
# =========================
if not is_classification:
    st.subheader("📉 Residual Analysis")

    result_df["Residual"] = result_df["Actual"] - result_df["Predicted"]

    fig3 = px.histogram(
        result_df,
        x="Residual",
        nbins=30,
        title="Residual Distribution"
    )

    st.plotly_chart(fig3, use_container_width=True)

# =========================
# PREDICTION SECTION
# =========================
st.subheader("🔮 Make a Prediction")

input_data = {}

for col in feature_cols:
    input_data[col] = st.number_input(f"Enter {col}", value=float(df[col].mean()))

input_df = pd.DataFrame([input_data])

if st.button("Predict"):
    prediction = model.predict(input_df)

    st.success(f"🎯 Prediction: {prediction[0]}")

# =========================
# INSIGHTS
# =========================
st.subheader("🧠 Insights")

top_feature = importance_df.iloc[0]["Feature"]

st.markdown(f"""
- 🔮 Model is trained using **{len(feature_cols)} features**
- 📌 Most important feature: **{top_feature}**
- 📊 {'Classification' if is_classification else 'Regression'} model applied automatically
- 🚀 Model can be improved with hyperparameter tuning and feature engineering
""")

# =========================
# DOWNLOAD RESULTS
# =========================
st.subheader("⬇️ Download Predictions")

download_df = result_df.copy()

csv = download_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Prediction Results",
    data=csv,
    file_name="predictive_results.csv",
    mime="text/csv"
)
