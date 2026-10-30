\# Customer Churn Analysis



\## Project Overview

This project analyzes customer churn for a telecommunications company using Python, MySQL, and Power BI. The objective is to identify customer segments with higher churn rates and develop insights that can help improve customer retention.



\## Tools and Technologies

\- Python

\- Pandas

\- Matplotlib

\- MySQL

\- Power BI

\- Git and GitHub



\## Dataset

The dataset contains telecommunications customer information, including:

\- Customer demographics

\- Contract types

\- Internet and phone services

\- Payment methods

\- Monthly and total charges

\- Customer tenure

\- Churn status



The original dataset contains 7,043 records. After cleaning missing values in `TotalCharges`, 7,032 records remain for analysis.



\## Project Structure



```text

customer-churn-analysis/

├── data/

│   ├── raw/

│   │   └── Telco-Customer-Churn.csv

│   └── processed/

│       └── customer\_churn\_cleaned.csv

├── powerbi/

│   └── Customer\_Churn\_Analysis.pbix

├── python/

│   ├── churn\_analysis.py

│   └── import\_to\_mysql.py

├── reports/

│   ├── churn\_by\_contract.png

│   ├── churn\_by\_payment\_method.png

│   ├── churn\_by\_tenure.png

│   └── monthly\_charges\_by\_churn.png

├── sql/

└── README.md

```



\## Key Findings

\- The overall customer churn rate is approximately 26.58%.

\- Customers on month-to-month contracts show higher churn than customers on longer-term contracts.

\- Customer tenure is an important factor to examine when identifying churn patterns.

\- Payment method is another useful dimension for exploring customer churn.



These findings are based on the cleaned dataset and dashboard analysis.



\## How to Run

1\. Clone or download the repository.

2\. Install Python and the required libraries.

3\. Run the Python analysis script:

&#x20;  `python python/churn\_analysis.py`

4\. Review the generated charts in the `reports/` folder.

5\. Open `powerbi/Customer\_Churn\_Analysis.pbix` in Power BI Desktop to explore the dashboard.



The MySQL import script can be used to load the cleaned dataset into a MySQL database after configuring your local database connection.



\## Business Objective

The goal is to identify customer groups with elevated churn and provide data-driven insights that support customer retention strategies.



\## Future Improvements

\- Add SQL queries for customer segmentation and churn analysis.

\- Develop additional customer retention metrics.

\- Explore predictive modeling to identify customers at risk of churn.

\- Enhance the Power BI dashboard with interactive filters and additional KPIs.

