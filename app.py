import streamlit as st # webapp library
import pandas as pd # analysing files
from modules.eda import run_eda
from modules.visualizer import run_visualizer

st.set_page_config(page_title="AI Data Insight Generator", layout="wide") # browser page title

st.title("📊 AI Data Insight Generator")
st.markdown("Upload your dataset and get instant analysis + visual insights.")

uploded_file = st.file_uploader("Upload Your file", type=["csv"])

if(uploded_file):
    df = pd.read_csv(uploded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())

    st.sidebar.title("Navigation")
    option = st.sidebar.radio("Choose Section:", ("EDA", "Visualizations"))

    if option == "EDA":
        run_eda(df)
    elif option == "Visualizations":
        run_visualizer(df)
else:
    st.info("Please upload a CSV file to begin.")
