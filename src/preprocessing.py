# preprocessing.py

import pandas as pd
import numpy as np


def load_data(file_path):
    """
    Load dataset and perform preprocessing
    """

    df = pd.read_csv(file_path)

    return preprocess_data(df)


def preprocess_data(df):
    """
    Complete preprocessing pipeline
    """

    # -----------------------------
    # Remove duplicate records
    # -----------------------------
    df.drop_duplicates(inplace=True)

    # -----------------------------
    # Standardize column names
    # -----------------------------
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # -----------------------------
    # Numeric Columns
    # -----------------------------
    numeric_cols = [
        "ai_adoption_level",
        "ai_investment_usd",
        "automation_rate",
        "cost_savings",
        "revenue_impact",
        "productivity_gain",
        "employee_ai_training_hours",
        "ai_maturity_score",
        "deployment_count"
    ]

    for col in numeric_cols:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    # -----------------------------
    # Fill Missing Numeric Values
    # -----------------------------
    for col in numeric_cols:

        if col in df.columns:

            df[col].fillna(
                df[col].median(),
                inplace=True
            )

    # -----------------------------
    # Fill Missing Categorical Values
    # -----------------------------
    categorical_cols = df.select_dtypes(
        include="object"
    ).columns

    for col in categorical_cols:

        df[col].fillna(
            df[col].mode()[0],
            inplace=True
        )

    # -----------------------------
    # Convert Year Column
    # -----------------------------
    if "year" in df.columns:

        df["year"] = pd.to_numeric(
            df["year"],
            errors="coerce"
        )

        df["year"].fillna(
            df["year"].median(),
            inplace=True
        )

        df["year"] = df["year"].astype(int)

    # -----------------------------
    # Feature Engineering
    # -----------------------------

    # ROI Percentage
    if (
        "revenue_impact" in df.columns
        and "ai_investment_usd" in df.columns
    ):

        df["roi_percentage"] = (
            (
                df["revenue_impact"]
                - df["ai_investment_usd"]
            )
            / df["ai_investment_usd"]
        ) * 100

    # Investment Category
    if "ai_investment_usd" in df.columns:

        df["investment_category"] = pd.qcut(
            df["ai_investment_usd"],
            q=4,
            labels=[
                "Low",
                "Medium",
                "High",
                "Very High"
            ]
        )

    # Maturity Category
    if "ai_maturity_score" in df.columns:

        df["maturity_level"] = pd.cut(
            df["ai_maturity_score"],
            bins=[0, 25, 50, 75, 100],
            labels=[
                "Beginner",
                "Intermediate",
                "Advanced",
                "Leader"
            ]
        )

    # Adoption Category
    if "ai_adoption_level" in df.columns:

        df["adoption_category"] = pd.cut(
            df["ai_adoption_level"],
            bins=[0, 0.25, 0.50, 0.75, 1.0],
            labels=[
                "Low",
                "Moderate",
                "High",
                "Very High"
            ]
        )

    # -----------------------------
    # Outlier Treatment
    # -----------------------------
    for col in numeric_cols:

        if col in df.columns:

            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            df[col] = np.where(
                df[col] < lower,
                lower,
                np.where(
                    df[col] > upper,
                    upper,
                    df[col]
                )
            )

    return df


def get_dataset_summary(df):
    """
    Dataset summary for dashboard
    """

    summary = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum(),
        "Duplicate Rows": df.duplicated().sum(),
        "Memory Usage (MB)": round(
            df.memory_usage(deep=True).sum()
            / 1024**2,
            2
        )
    }

    return summary


def get_numeric_summary(df):
    """
    Numerical statistics
    """

    return df.describe().T


def get_categorical_summary(df):
    """
    Categorical statistics
    """

    cat_cols = df.select_dtypes(
        include="object"
    ).columns

    result = {}

    for col in cat_cols:

        result[col] = {
            "Unique Values": df[col].nunique(),
            "Top Value": df[col].mode()[0]
        }

    return pd.DataFrame(result).T


if __name__ == "__main__":

    FILE_PATH = "data/corporate_ai_adoption_dataset.csv"

    df = load_data(FILE_PATH)

    print("Dataset Loaded Successfully")
    print(get_dataset_summary(df))
