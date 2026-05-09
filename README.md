# Data Mining Final Project

## Project Title

Customer Segmentation in Online Retail

---

## Domain

Online Retail

---

## Dataset

Online Retail II Dataset from UCI Machine Learning Repository

The dataset contains transactional data for an online retail company, including customer purchases, quantities, invoices, prices, and countries.

---

## Project Overview

This project focuses on analyzing customer purchasing behavior in an online retail business using Data Mining techniques.

The main objective is to understand customer behavior patterns, segment customers into different groups, and generate business insights that can support marketing strategies and decision-making.

The project follows the CRISP-DM methodology and includes data preprocessing, clustering, classification, regression, visualization, and dashboard deployment.

---

# Phase 1 — Understanding & Planning

This phase focused on understanding the project requirements and planning the complete workflow.

The following tasks were completed:

* Understanding the business problem and project objectives
* Exploring the dataset and identifying data quality issues
* Analyzing dataset size, features, and data types
* Identifying missing values, duplicates, and cancelled transactions
* Planning the project workflow using the CRISP-DM methodology
* Selecting suitable Data Mining techniques for customer segmentation

---

# CRISP-DM Methodology

## 1. Business Understanding

The goal is to analyze customer purchasing behavior and segment customers into groups based on spending patterns.

This helps businesses:

* Improve marketing strategies
* Identify high-value customers
* Personalize customer targeting
* Support business decision-making

---

## 2. Data Understanding

The dataset was explored to understand:

* Number of records and features
* Data types
* Missing values
* Duplicates
* Outliers
* Customer purchasing patterns

Visualizations and statistical summaries were used to better understand the data.

---

## 3. Data Preparation

The following preprocessing steps were applied:

* Removing missing values
* Removing duplicate rows
* Removing cancelled transactions
* Creating a new feature called `TotalPrice`
* Aggregating customer-level features
* Scaling numerical features using `StandardScaler`

---

## 4. Modeling

Several Data Mining techniques were applied:

### Clustering

* K-Means Clustering
* Elbow Method for selecting the optimal number of clusters
* PCA for dimensionality reduction and visualization

### Classification

* Decision Tree Classifier

### Regression

* Linear Regression

### Evaluation

* Silhouette Score
* Accuracy Score
* Classification Report

---

## 5. Evaluation

The models were evaluated using:

* Silhouette Score for clustering quality
* Accuracy Score for classification
* Visual analysis using charts and plots

The results showed clear customer segmentation and meaningful purchasing patterns.

---

## 6. Deployment

An interactive dashboard was built using Streamlit to visualize:

* Customer distribution across clusters
* Average spending per cluster
* Customer metrics and KPIs
* Business insights
* Interactive filters

The dashboard acts as the deployment layer of the project.

---

# Phase 2 — Full Implementation

This phase includes the complete technical implementation of the project.

Implemented tasks include:

* Data cleaning and preprocessing
* Feature engineering
* Customer aggregation
* Data scaling
* K-Means clustering
* PCA visualization
* Elbow Method visualization
* Correlation Heatmap
* Outlier detection using Boxplot
* Cluster evaluation using Silhouette Score
* Decision Tree classification
* Linear Regression
* Interactive dashboard development

---

# Dashboard Features

The Streamlit dashboard includes:

* Cluster filtering
* Spending range filtering
* Customer distribution visualization
* Average spending analysis
* Key performance metrics
* Business insights panel
* Interactive charts and graphs

---

# Tools & Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit
* Jupyter Notebook

---

# Setup Instructions

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

# How to Run the Dashboard

```bash
streamlit run dashboard/app.py
```

---

# Key Business Insights

* Most customers belong to low-spending segments.
* A small group of customers generates a large portion of revenue.
* Customer segmentation helps businesses target customers more effectively.
* Different customer groups show different purchasing behaviors.

---

# Future Work

Possible future improvements include:

* Applying advanced clustering techniques such as DBSCAN and Hierarchical Clustering
* Hyperparameter tuning for better model performance
* Adding more interactive dashboard features
* Deploying the dashboard online using Streamlit Cloud or Render
* Expanding the analysis with additional business features

---

# Repository Structure

```text
project/
│
├── data/
├── notebook/
├── dashboard/
│   └── app.py
├── requirements.txt
├── README.md
└── customers_clustered.csv
```

---

# Author

Malak Houssin
