# task7_intern
# Basic Sales Summary Using Python and SQLite
# Objective
This project demonstrates a simple Python program that interacts with a SQLite database to summarize product sales data and visualize total revenue using a bar chart.

# Tools & Technologies
Python 3.x
SQLite (sqlite3 module)
Pandas
Matplotlib

# Dataset Description
The script automatically creates a local SQLite database file named sales_data.db and populates it with a sample sales table containing the following fields:
Column Name	Data Type	Description
id	INTEGER	Unique identifier for each sale
product	TEXT	Name of the product (e.g., Laptop, Smartphone, Tablet)
quantity	INTEGER	Quantity of items sold
price	REAL	Price per unit
Sample data consists of multiple sales records for each product.

# Script Workflow
Connect to (or create) the SQLite database: sales_data.db.
Create the sales table with the specified schema if it doesn’t exist.
Insert sample sales records into the table.
Execute SQL Query to:
Calculate total quantity sold per product.
Calculate total revenue per product (quantity * price).
Load results into a Pandas DataFrame.
Display the sales summary in the console.
Plot a bar chart showing Total Revenue by Product.
Save the chart as sales_chart.png.
Close the database connection.
