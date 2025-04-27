# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6315: Python for Business Analytics
#
# Name:Natalia Barnett
#
# Date:4/20/2025
#
##################################################
#
# Sample Script for Assignment 4:
# Obtaining Data from a Database
#
##################################################
"""

##################################################
# Import Required Modules
##################################################

import pandas as pd
import os

# To pass SQL queries to a database
# you would import some kind of API 
# to interact with the database
# We will continue using sqlite3
import sqlite3 as dbapi

# Import a module for estimating regression models.
import statsmodels.formula.api as sm # Another way to estimate linear regression
# This is a "light duty" modeling package designed to mimic the interface in R.


##################################################
# Set up Workspace
##################################################


# Find out the current directory.
os.getcwd()

# Get the path where you saved this script.
# This only works when you run the entire script (with the green "Play" button or F5 key).
print(os.path.dirname(os.path.realpath(__file__)))
# It might be comverted to lower case, but it gives you an idea of the text of the path. 
# You could copy it directly or type it yourself, using your spelling conventions. 

# Change to a new directory.

# You could set it directly from the location of this file
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Check that the change was successful.
os.getcwd()
# I got lower case output, even though my folders have some upper case letters.
# But anyway, it works.



##################################################
# Question 1: Connect to a Database
#     and Obtain Sales Data
##################################################


#--------------------------------------------------
# a. Connect to the database called airplanes.db
#     and obtain a cursor object.
#--------------------------------------------------


con =  dbapi.connect('airplanes.db')

cur = con.cursor()


# Check the connection and cursor
print("Connection:", con)
print("Cursor:", cur)

#--------------------------------------------------
# b. Submit a query to the database that obtains
#    the sales data.
#--------------------------------------------------

query_1 = """
            SELECT *
            FROM Sales
            """
print(query_1)
cur.execute(query_1)

#--------------------------------------------------
# c. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------

results = cur.fetchall()

# Define column names
column_names = [desc[0] for desc in cur.description]


# Create an empty DataFrame with the specified column names
airplane_sales = pd.DataFrame(results, columns=column_names)


# Describe the contents of the dataframe to check the result.
print(airplane_sales.describe())
print(airplane_sales.columns)




#--------------------------------------------------
# Fit a regression model to check progress.
#--------------------------------------------------

reg_model_sales = sm.ols(formula = 
                           "price ~ age", 
                           data = airplane_sales).fit()


# Display a summary table of regression results.
print(reg_model_sales.summary())




##################################################
# Question 2: Obtain Specification Data
##################################################




#--------------------------------------------------
# a. Submit a query to the database that obtains
#    the sales data joined with specification data.
#--------------------------------------------------

query_2 = """
           SELECT Sales.*, Specs.*
           FROM Sales
           JOIN Specs ON Sales.sale_id = Specs.sale_id
            """
print(query_2)
cur.execute(query_2)
# Correction: From
# JOIN Specs ON Sales.spec_id = Specs.spec_id
# to 
# JOIN Specs ON Sales.sales_id = Specs.sales_id
# Need the correct name of the column that contains the key.

#--------------------------------------------------
# b. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------

# Fetch the results from the executed query
results = cur.fetchall()

# Define column names based on cursor description
column_names = [desc[0] for desc in cur.description]

# Create a DataFrame and load the query results into it
airplane_sales_specs = pd.DataFrame(results, columns=column_names)

# Describe the contents of the dataframe to check the result.
print(airplane_sales_specs.describe())
print(airplane_sales_specs.columns)




#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_sales_specs = sm.ols(formula = 
                           "price ~ age + passengers + wtop + fixgear + tdrag", 
                           data = airplane_sales_specs).fit()


# Display a summary table of regression results.
print(reg_model_sales_specs.summary())




##################################################
# Question 3: Obtain Performance Data
##################################################



#--------------------------------------------------
# a. Submit a query to the database that obtains
#    the sales data joined with specification data
#    and then joined with the performance data.
#--------------------------------------------------

# query_3 = """
#             SELECT Sales.*, Specs.*, Perf.*
#             FROM Sales
#             JOIN Specs ON Sales.sale_id = Specs.sale_id
#             JOIN Perf ON Sales.sale_id = Perf.sale_id
#             """
            
# I'm not sure what went wrong here, either.
# I just copied and pasted your same text without the spaces.
query_3 = """
SELECT Sales.*, Specs.*, Perf.*
FROM Sales
JOIN Specs ON Sales.sale_id = Specs.sale_id
JOIN Perf ON Sales.sale_id = Perf.sale_id
"""

print(query_3)
cur.execute(query_3)
# Correction: From
# JOIN Specs ON Sales.spec_id = Specs.spec_id
# JOIN Perf ON Sales.perf_id = Perf.perf_id
# to 
# JOIN Specs ON Sales.sales_id = Specs.sales_id
# JOIN Perf ON Sales.sales_id = Perf.sales_id


#--------------------------------------------------
# b. Create a data frame and load the query.
#--------------------------------------------------

# Fetch the results from the executed query
results = cur.fetchall()

# Define column names based on cursor description
column_names = [desc[0] for desc in cur.description]

# Code goes here
airplane_full = pd.DataFrame(results, columns=column_names)


# Check to see the columns in the result.
print(airplane_full.describe())
print(airplane_full.columns)



#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_full = sm.ols(formula = 
                           """price ~ age + passengers
                           + wtop + fixgear + tdrag + 
                           horse + fuel + ceiling + cruise""", 
                           data = airplane_full).fit()


# Display a summary table of regression results.
print(reg_model_full.summary())



##################################################
# Commit changes and close the connection
##################################################


# The commit method saves the changes. 
# con.commit()
# No changes were necessary -- only reading.

# Close the connection when finished. 
con.close()

# Then we can continue with this file when you have time
# to work on it later.



##################################################
# Extra code snippets
##################################################

# In case things go wrong, you can always drop the table
# and start over:
# cur.execute('DROP TABLE Sales')
# cur.execute('DROP TABLE Specs')
# cur.execute('DROP TABLE Perf')

# This can get the schema of the table,
# cur.execute("PRAGMA table_info('Sales')").fetchall()
# cur.execute("PRAGMA table_info('Specs')").fetchall()
# cur.execute("PRAGMA table_info('Perf')").fetchall()
# which states the names of the variables and the data types.



##################################################
# End
##################################################
