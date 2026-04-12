import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# read data
df = pd.read_csv('notebooks/customers_clustered.csv')

# title
st.title("Customer Segmentation Dashboard")

st.write("Simple dashboard to explore customer groups based on their purchases.")

# basic info
st.subheader("Quick Info")

col1, col2, col3 = st.columns(3)

col1.write("Total Customers")
col1.write(len(df))

col2.write("Avg Spending")
col2.write(round(df['TotalPrice'].mean(), 2))

col3.write("Max Spending")
col3.write(round(df['TotalPrice'].max(), 2))

# preview
st.subheader("Data Preview")
st.write(df.head())

# cluster distribution
st.subheader("Clusters Distribution")

counts = df['Cluster'].value_counts().sort_index()
st.bar_chart(counts)

# grouping
st.subheader("Cluster Summary")

grouped = df.groupby('Cluster')[['Invoice', 'Quantity', 'TotalPrice']].mean()
st.write(grouped)

# plot
st.subheader("Spending by Cluster")

fig, ax = plt.subplots()
grouped['TotalPrice'].plot(kind='bar', ax=ax)

ax.set_xlabel("Cluster")
ax.set_ylabel("Total Price")

st.pyplot(fig)

# notes
st.subheader("Notes")

st.write("""
- Most customers are in the low spending group.
- Few customers spend much more than others.
- This can help in targeting customers differently.
""")