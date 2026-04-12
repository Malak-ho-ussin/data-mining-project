import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('notebooks/customers_clustered.csv')

st.title("Customer Segmentation Dashboard")

st.write("Dataset Preview")
st.write(df.head())

st.write("Cluster Distribution")
st.bar_chart(df['Cluster'].value_counts())

st.write("Average Values per Cluster")
cluster_analysis = df.groupby('Cluster').mean()
st.write(cluster_analysis)

fig, ax = plt.subplots()
cluster_analysis['TotalPrice'].plot(kind='bar', ax=ax)
st.pyplot(fig)