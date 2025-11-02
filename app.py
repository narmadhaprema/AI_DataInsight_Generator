import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Data Insight Generator", page_icon="📊", layout="wide")

st.title("📊 AI Data Insight Generator")
st.markdown("Welcome! Upload you csv to get business insights.")

uploaded_file = st.file_uploader("Upload your CSV here", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Your File has been uploaded successfully!!")
    st.write("### Data preview:")
    st.dataframe(df.head())
else:
    st.info("Please upload your CSV file to proceed")