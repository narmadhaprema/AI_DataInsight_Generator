import streamlit as st
import pandas as pd

def run_eda(df): 

    st.title("Exploratory Data Analysis") 
    st.subheader("1️⃣ Basic Dataset Information")
    # Shape and Columns
    st.write(f"**Rows:**{df.shape[0]} | **Columns:**{df.shape[1]}")
    st.write("**Column Types:**")
    st.write(df.dtypes)

    # Missing Values
    st.write("**MIssing Values:**")
    st.write(df.isnull().sum())

    # Summary Statistics
    st.subheader("2️⃣ Summary Statistics")
    st.write(df.describe().T) # T -> Transposes rows and columns to show it clearer

    # Quick Insights
    st.markdown("---")
    st.subheader("Quick Insights")

    missing_count = df.isnull().sum().sum()

    if missing_count > 0:
        st.warning(f"⚠️ There are {missing_count} missing values in this dataset.")
    else:
        st.success("✅ No missing values detected.")

