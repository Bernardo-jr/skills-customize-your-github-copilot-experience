# 📘 Assignment: File I/O and Automation with Python

## 🎯 Objective

Learn how to read and write files in Python and automate a simple workflow by processing data from a CSV file and generating a text report.

## 📝 Tasks

### 🛠️ Load and summarize sales data

#### Description
Read sales records from a CSV file and compute summary statistics for the dataset.

#### Requirements
Completed program should:

- Load the file `sales-data.csv` using Python file I/O.
- Parse each row into sales records with fields for date, product, quantity, and price.
- Calculate total sales, total quantity sold, and the number of records processed.
- Return or print a summary in a readable format.

### 🛠️ Generate an automated sales report

#### Description
Write the sales summary to a report file and include a short recommendation based on the data.

#### Requirements
Completed program should:

- Create or overwrite a file named `sales-report.txt`.
- Write the summary statistics and a recommendation sentence to the file.
- The recommendation should mention whether sales were strong or if the data suggests reviewing low-performing items.
- Example output in `sales-report.txt`:
  ```text
  Total records: 5
  Total quantity sold: 27
  Total sales: $459.95
  Recommendation: Sales look strong across the product line.
  ```
