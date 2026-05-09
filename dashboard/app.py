import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ================= Load Data =================
df = pd.read_csv('notebooks/customers_clustered.csv')

# ================= Sidebar Filters =================
st.sidebar.header("Filters")

# Cluster filter
selected_cluster = st.sidebar.selectbox(
    "Select Cluster",
    sorted(df['Cluster'].unique())
)

# Spending range filter
min_spend = int(df['TotalPrice'].min())
max_spend = int(df['TotalPrice'].max())

spend_range = st.sidebar.slider(
    "Select Spending Range",
    min_spend,
    max_spend,
    (min_spend, max_spend)
)

# Apply filters
filtered_df = df[
    (df['Cluster'] == selected_cluster) &
    (df['TotalPrice'] >= spend_range[0]) &
    (df['TotalPrice'] <= spend_range[1])
]

# ================= Title =================
st.title("Customer Segmentation Dashboard")
st.write("Interactive dashboard for analyzing customer behavior.")

st.write(f"Showing Cluster: {selected_cluster} | Spending Range: {spend_range}")

# ================= KPIs =================
st.subheader("Quick Info")

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(filtered_df))
col2.metric("Average Spending", round(filtered_df['TotalPrice'].mean(), 2))
col3.metric("Max Spending", round(filtered_df['TotalPrice'].max(), 2))

# ================= Cluster Distribution =================
st.subheader("Cluster Distribution")

counts = filtered_df['Cluster'].value_counts().sort_index()

fig1, ax1 = plt.subplots()
counts.plot(kind='bar', ax=ax1)

ax1.set_xlabel("Cluster")
ax1.set_ylabel("Number of Customers")
ax1.set_title("Customer Distribution")

st.pyplot(fig1)

# ================= Spending per Cluster =================
st.subheader("Spending by Cluster")

grouped = filtered_df.groupby('Cluster')[['Invoice', 'Quantity', 'TotalPrice']].mean()

fig2, ax2 = plt.subplots()
grouped['TotalPrice'].plot(kind='bar', ax=ax2)

ax2.set_xlabel("Cluster")
ax2.set_ylabel("Average Spending")
ax2.set_title("Average Spending per Cluster")

st.pyplot(fig2)

# ================= Spending Distribution =================
st.subheader("Spending Distribution")

fig3, ax3 = plt.subplots()
ax3.hist(filtered_df['TotalPrice'], bins=20)

ax3.set_xlabel("Total Price")
ax3.set_ylabel("Frequency")
ax3.set_title("Customer Spending Distribution")

st.pyplot(fig3)

# ================= Data Preview =================
st.subheader("Data Preview")
st.dataframe(filtered_df.head())

# ================= Summary =================
st.subheader("Cluster Summary")
st.dataframe(grouped)

# ================= Insights =================
st.subheader("Business Insights")

st.write("""
- Most customers fall into lower spending segments.
- High-value customers are fewer but contribute significantly.
- Filters allow deeper exploration of customer groups.
""")