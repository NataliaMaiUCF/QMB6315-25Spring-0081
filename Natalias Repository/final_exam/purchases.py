# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6315: Python for Business Analytics
#
# Name:Natalia Barnett
#
# Date:5/1/25
#
##################################################
#
# Sample Script for Final Examination:
# Obtaining Data from a Database
# and Building Predictive Models
#
##################################################
"""

##################################################
# Import Required Modules
##################################################
import pandas as pd
import sqlite3
import statsmodels.formula.api as sm





##################################################
# Set up Workspace
##################################################

pd.set_option('display.max_columns', None)  # Show all columns in output
pd.set_option('display.float_format', '{:.2f}'.format)  # Format floats nicely






##################################################
# Question 1: Connect to a Database
#     and Obtain Applications Data
##################################################


#--------------------------------------------------
# a. Connect to the database called customers.db
#     and obtain a cursor object.
#--------------------------------------------------


con = sqlite3.connect("customers.db")

cur = con.cursor()



#--------------------------------------------------
# b. Submit a query to the database that obtains
#    the sales data.
#--------------------------------------------------

query_1 = """
            SELECT *
    FROM Applications
            """
print(query_1)
cur.execute(query_1)

#--------------------------------------------------
# c. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------

# Code goes here
purchase_app = pd.read_sql_query(query_1, con)

# Could use a loop with a pd.concat() command.


# Describe the contents of the dataframe to check the result.
print(purchase_app.describe())
print(purchase_app.columns)




#--------------------------------------------------
# Fit a regression model to check progress.
#--------------------------------------------------

reg_model_app = sm.ols(formula = 
    "purchases ~ income + C(homeownership) + credit_limit", 
    data = purchase_app).fit()



# Display a summary table of regression results.
print(reg_model_app.summary())




##################################################
# Question 2: Obtain CreditBureau Data
##################################################




#--------------------------------------------------
# a. Submit a query to the database that obtains
#    the Application data joined with CreditBureau data.
#--------------------------------------------------

query_2 = """
    SELECT 
        a.income,
        a.homeownership,
        a.purchases,
        a.credit_limit,
        b.fico,
        b.num_late,
        b.past_def,
        b.num_bankruptcy
    FROM Applications AS a
    JOIN CreditBureau AS b
        ON a.ssn = b.ssn
"""
print(query_2)
cur.execute(query_2)



#--------------------------------------------------
# b. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------



# Code goes here
purchase_app_bureau = pd.read_sql_query(query_2, con) 

# Could use a loop with a pd.concat() command.



# Describe the contents of the dataframe to check the result.
print(purchase_app_bureau.describe())
print(purchase_app_bureau.columns)



#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_app_bureau = sm.ols(formula = 
                           "purchases ~ income + C(homeownership) + credit_limit + fico + num_late + past_def + num_bankruptcy", 
                           data = purchase_app_bureau).fit()


# Display a summary table of regression results.
print(reg_model_app_bureau.summary())




##################################################
# Question 3: Obtain Demographic Data
##################################################



#--------------------------------------------------
# a. Submit a query to the database that obtains
#    the Application data joined with CreditBureau data.
#    and then joined with the Demographic data.
#--------------------------------------------------

query_3 = """
    SELECT 
        a.income,
        a.homeownership,
        a.purchases,
        a.credit_limit,
        b.fico,
        b.num_late,
        b.past_def,
        b.num_bankruptcy,
        d.avg_income,
        d.density
    FROM Applications AS a
    JOIN CreditBureau AS b
        ON a.ssn = b.ssn
    JOIN Demographic AS d
        ON a.zip_code = d.zip_code
"""
print(query_3)
cur.execute(query_3)




#--------------------------------------------------
# b. Create a data frame and load the query.
#--------------------------------------------------



# Code goes here
purchase_full = pd.read_sql_query(query_3, con)

# Could use a loop with a pd.concat() command.



# Check to see the columns in the result.
print(purchase_full.describe())

print(purchase_full.columns)


#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_full = sm.ols(formula = 
                           "purchases ~ income + C(homeownership) + credit_limit + fico + num_late + past_def + num_bankruptcy + avg_income + density",
                           data = purchase_full).fit()


# Display a summary table of regression results.
print(reg_model_full.summary())



##################################################
# Question 4: Advanced Regression Modeling
##################################################

#--------------------------------------------------
# Parts a-c with utilization.
#--------------------------------------------------


# Create a variable for credit utilization.

purchase_full["utilization"] = purchase_full["purchases"] / purchase_full["credit_limit"]

# Describe the new variable

print(purchase_full["utilization"].describe())



#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_util = sm.ols(
    formula = "utilization ~ income + C(homeownership) + fico + num_late + past_def + num_bankruptcy + avg_income + density",
    data = purchase_full
).fit()

print(reg_model_util.summary())





#--------------------------------------------------
# Parts a-c with log_odds_util.
#--------------------------------------------------


# Create a variable for credit utilization.

import numpy as np  # Add to top of script if not already

# Filter out rows where utilization is 0 or 1
purchase_full = purchase_full[(purchase_full["utilization"] > 0) & (purchase_full["utilization"] < 1)]

# Then calculate log_odds_util
purchase_full["log_odds_util"] = np.log(
    purchase_full["utilization"] / (1 - purchase_full["utilization"])
)



#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------


reg_model_logodds = sm.ols(
    formula = "log_odds_util ~ income + C(homeownership) + fico + num_late + past_def + num_bankruptcy + avg_income + density",
    data = purchase_full
).fit()

print(reg_model_logodds.summary())










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
# cur.execute('DROP TABLE Applications')
# cur.execute('DROP TABLE CreditBureau')
# cur.execute('DROP TABLE Demographic')

# This can get the schema of the table,
# cur.execute("PRAGMA table_info('Applications')").fetchall()
# cur.execute("PRAGMA table_info('CreditBureau')").fetchall()
# cur.execute("PRAGMA table_info('Demographic')").fetchall()
# which states the names of the variables and the data types.


##################################################
# End
##################################################
