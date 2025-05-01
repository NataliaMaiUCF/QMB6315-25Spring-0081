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
import sqlite3
import pandas as pd
import statsmodels.api as sm
import os







##################################################
# Set up Workspace
##################################################

os.chdir(r'C:\Users\Natalia Mai\Documents\GitHub\QMB6315S25\QMB6315-25Spring-0081\Natalias Repository\final_exam')





##################################################
# Question 1: Connect to a Database
#     and Obtain Applications Data
##################################################


#--------------------------------------------------
# a. Connect to the database called customers.db
#     and obtain a cursor object.
#--------------------------------------------------


con = sqlite3.connect(r'C:\Users\Natalia Mai\Documents\GitHub\QMB6315S25\QMB6315-25Spring-0081\Natalias Repository\final_exam\customers.db')

cur = con.cursor()


#--------------------------------------------------
# b. Submit a query to the database that obtains
#    the sales data.
#--------------------------------------------------

query_1 = """
            Select *
            FROM Applications
            """
print(query_1)
cur.execute(query_1)

#--------------------------------------------------
# c. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------

purchase_app = pd.read_sql(query_1, con)

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
           SELECT a.*, 
                  b.fico, 
                  b.num_past_late, 
                  b.num_default, 
                  b.bankruptcy
           FROM Applications a
           JOIN CreditBureau b ON a.app = b.app
            """
print(query_2)
cur.execute(query_2)




#--------------------------------------------------
# b. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------



# Code goes here
purchase_app_bureau = pd.read_sql(query_2, con)

# Could use a loop with a pd.concat() command.



# Describe the contents of the dataframe to check the result.
print("\nDataFrame Description:")
print(purchase_app_bureau.describe())
print("\nDataFrame Columns:")
print(purchase_app_bureau.columns)




#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_app_bureau = sm.ols(formula = 
                           "model formula goes here", 
                           data = purchase_app_bureau).fit()


# Display a summary table of regression results.
print(reg_model_app_bureau.summary())
print("\nRegression Results:")



##################################################
# Question 3: Obtain Demographic Data
##################################################



#--------------------------------------------------
# a. Submit a query to the database that obtains
#    the Application data joined with CreditBureau data.
#    and then joined with the Demographic data.
#--------------------------------------------------

query_3 = """
           SELECT a.*, 
                   b.fico, 
                   b.num_past_late, 
                   b.num_default, 
                   b.bankruptcy,
                   d.avg_income,
                   d.density
            FROM Applications a
            JOIN CreditBureau b ON a.app = b.app
            JOIN Demographic d ON a.zip_code = d.zip_code
            """
print(query_3)
cur.execute(query_3)




#--------------------------------------------------
# b. Create a data frame and load the query.
#--------------------------------------------------



# Code goes here
purchase_full = pd.read_sql(query_3,con)

# Could use a loop with a pd.concat() command.



# Check to see the columns in the result.
print (purchase_full.describe())
print("\nDataFrame Summary Statistics:")
print (purchase_full.columns)
print("\nDataFrame Columns:")

#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_full = sm.ols(formula = 
                           "purchases ~ income + C(homeownership) + credit_limit + "
                           "fico + num_past_late + num_default + bankruptcy + "
                           "avg_income + density", 
                           data = purchase_full).fit()


# Display a summary table of regression results.
print(reg_model_full.summary())
print("\nFull Regression Model Results:")


##################################################
# Question 4: Advanced Regression Modeling
##################################################

#--------------------------------------------------
# Parts a-c with utilization.
#--------------------------------------------------
import numpy as np


# Create a variable for credit utilization.
purchase_full['utilization'] = purchase_full['purchases'] / purchase_full['credit_limit']

print("\nCredit Utilization Variable Description:")
print(purchase_full['utilization'].describe())

#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------


reg_model_util = sm.ols(
    formula="utilization ~ income + C(homeownership) + fico + num_past_late + num_default + bankruptcy + avg_income + density",
    data=purchase_full
).fit()

print("\nRegression Results for Utilization Model:")
print(reg_model_util.summary())

#--------------------------------------------------
# Parts a-c with log_odds_util.
#--------------------------------------------------


# Create a variable for credit utilization.


purchase_full['utilization_adj'] = purchase_full['utilization'].clip(0.001, 0.999)
purchase_full['log_odds_util'] = np.log(purchase_full['utilization_adj'] / (1 - purchase_full['utilization_adj'])
)
print("\nLog-Odds Utilization Variable Description:")
print(purchase_full['log_odds_util'].describe())

#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------


reg_model_log_odds = sm.ols(
    formula="log_odds_util ~ income + C(homeownership) + fico + num_past_late + num_default + bankruptcy + avg_income + density",
    data=purchase_full
).fit()

print("\nRegression Results for Log-Odds Utilization Model:")
print(reg_model_log_odds.summary())









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
