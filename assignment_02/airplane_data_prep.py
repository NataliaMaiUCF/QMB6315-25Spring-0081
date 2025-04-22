# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6315: Python for Business Analytics
#
# Name: Natalia Barnett
#
# Date: 4/20/25
#
##################################################
#
# Sample Script for Assignment 2:
# Manipulating Data
#
##################################################
"""

##################################################
# Import Required Modules
##################################################

import os # To set working directory
import pandas as pd # To read and inspect data
import statsmodels.formula.api as sm

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
# Part a) Read Spreadsheet and Sales Data
##################################################

airplane_xlsx = pd.ExcelFile('airplane_data.xlsx')

airplane_sales = pd.read_excel(airplane_xlsx,  'airplane_sales')


# Describe the contents of that file.
airplane_sales.describe()


#--------------------------------------------------
# Fit a regression model.
#--------------------------------------------------

reg_model_sales = sm.ols(formula = 
                           "price ~ age ", 
                           data = airplane_sales).fit()


# Display a summary table of regression results.
print(reg_model_sales.summary())


##################################################
# Part b) Read Specification Data
##################################################


airplane_specs = pd.read_excel(airplane_xlsx,  'airplane_specs')


airplane_specs.describe()

#--------------------------------------------------
# Join the two datasets together.
#--------------------------------------------------

airplane_sales_specs = pd.concat([airplane_sales, airplane_specs], axis = 1)

airplane_sales_specs.describe()

airplane_sales_specs.columns



#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------


reg_model_sales_specs = sm.ols(formula = 
                           "price ~ age + passengers + wtop \
                                  + fixgear + tdrag", 
                           data = airplane_sales_specs).fit()


# Display a summary table of regression results.
print(reg_model_sales_specs.summary())



##################################################
# Part c) Read Performance Data
##################################################


airplane_perf = pd.read_excel(airplane_xlsx,  'airplane_perf')


# Describe the contents of that file.
airplane_perf.describe()

#--------------------------------------------------
# Join the third dataset to the first two.
#--------------------------------------------------

airplane_full = pd.concat([airplane_sales_specs, airplane_perf], axis = 1)

# Check to see the columns in the result.
airplane_full.describe()

airplane_full.columns



#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------
reg_model_full = sm.ols(formula = 
                           "price ~ age + passengers + wtop \
                               + fixgear + tdrag + horse \
                                   + fuel + ceiling + cruise", 
                           data = airplane_full).fit()


# Display a summary table of regression results.
print(reg_model_full.summary())


##################################################
# End
##################################################
