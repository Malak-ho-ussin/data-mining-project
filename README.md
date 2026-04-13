# Data Mining Final Project

## Domain

Online Retail

## Dataset

Online Retail II dataset from UCI

## About the Project

This project focuses on analyzing customer purchase data to better understand customer behavior.

First, the dataset was cleaned and missing values were handled. Then, a new feature called **TotalPrice** was created to represent the total cost of each transaction.

After that, **K-Means clustering** was applied to segment customers into different groups based on their purchasing behavior. A classification model was also built to predict the customer segment.

Finally, a simple interactive dashboard was created using Streamlit to visualize the results.

## Dashboard

A simple dashboard was built using Streamlit to explore customer segmentation.

It includes:

* Customer distribution across clusters
* Average spending per cluster
* Key metrics such as total customers and spending

To run the dashboard locally:

```bash
streamlit run dashboard/app.py
```

## Tools Used

* Python
* Pandas
* Scikit-learn
* Streamlit

## Conclusion

The project shows how data mining techniques can help in understanding customer behavior and supporting business decisions.

## Author

Malak Houssin
