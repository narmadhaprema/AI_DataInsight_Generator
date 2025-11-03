import streamlit as st
import matplotlib.pyplot as plt ## basic plotting
import seaborn as sns ## show advanced statistical visualization

def run_visualizer(df):
    st.header("📈 Data Visualizations")

    ## Add Data Type Filtering
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    # categorical_cols = df.select_dtypes(include=['object']).columns

    ## Correlation Heat
    if st.checkbox("Show Correlation Heatmap (Numeric Features Only)"):
        if len(numeric_cols) > 1:
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)
        else:
            st.warning("Not enough numeric columns for correlation heatmap.")

    ## Histogram
    if st.checkbox("Show Histograms"):
        column = st.selectbox("Select a column to plot histogram", numeric_cols)
        fig, ax = plt.subplots()
        sns.histplot(df[column], bins=20, kde=True, ax=ax)
        st.pyplot(fig)

    ## Boxplot
    if st.checkbox("Show Boxplots"):
        column = st.selectbox("Select a column to plot Boxplot", numeric_cols, key='boxplot')
        fig, ax = plt.subplots()
        sns.boxplot(x=df[column], ax=ax)
        st.pyplot(fig)
     
