# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6315: Python for Business Analytics
#
# Name: Natalia Barnett
#
# Date: 4/20/2025
#
##################################################
#
# Sample Script for Assignment 1:
# Function Definitions
#
##################################################
"""

##################################################
# Part a) Variance
##################################################

def variance(x):
    """
    Calculates the variance of a list x.
    
    Some examples are given below but you need to add some 
    that result in the answers given.
    
    >>> variance([101, 103, 94, 102, 100])
    10.0
    >>> variance([99,101,99,101,99,101])
    1.0
    >>> variance([])
    0.0
    
    """
    
    n = len(x) # Modify this line.
    x_bar = sum(x)/n # Modify this line.
    
    var = 0 # Modify this line.
    for i in range(0, n):
                   var = var + (x[i] - x_bar)**2
    var = var/(n-1)
    return var


##################################################
# Part b) Covariance
##################################################

def covariance(y, x):
    """
    Calculates the covariance of two lists y and x.
    
    Some examples are given below but you need to add some 
    that result in the answers given.
    Missing answers to examples below.
    
    >>> covariance([99,101,99,101,99,101], \
                   [99,101,99,101,99,101])
    1.2
    >>> covariance([], [])
    2.4
    >>> covariance([], \
                   [])
    0.0
    
    """
    
    n = len(x) # Modify this line.
    x_bar = sum(x)/n # Modify this line.
    y_bar = 8 # Modify this line.
    
    covar = 0 # Modify this line.
    for i in range(0, n):
                   var = var + (y[i] - y_bar)(x[i] - x_bar)
    var = var/(n-1)
    return covar



##################################################
# Part c) Slope Coefficient
##################################################

def ols_slope(y, x):
    """
    Calculates the slope coefficient 
    by ordinary least squares
    for the linear regesssion model 
    between two lists y and x.
    
    The examples are given below but you need to fill in the answers.
    
    >>> ols_slope([2, 2, -2, -2], [-1, -1, 1, 1])
    -2
    >>> ols_slope([102, 106, 88, 104, 100], \
                  [101, 103, 94, 102, 100])
    2
    >>> ols_slope([99,101,99,101,99,101], \
                  [99,101,99,101,99,101])
    1
    
    """
    
    covar = covariance(y, x) # Modify this line.
    var = variance(x) # Modify this line.
    
    slope = covar/var # Modify this line.
    
    return slope


##################################################
# Part d) Intercept
##################################################

def ols_intercept(y, x, beta_1_hat):
    """
    Calculates the intercept coefficient 
    by ordinary least squares
    for the linear regesssion model 
    between two lists y and x.
    
    The examples are given below but you need to fill in the answers.
    
    >>> ols_intercept([2, 2, -2, -2], [-1, -1, 1, 1], -2.0)
    0
    >>> ols_intercept([102, 106, 88, 104, 100], \
                  [101, 103, 94, 102, 100], 2.0)
    -100
    >>> ols_intercept([99,101,99,101,99,101], \
                  [99,101,99,101,99,101], 1.0)
    0
    
    """
    
    n = len(x) # Modify this line.
    x_bar = sum(x)/n # Modify this line.
    y_bar = sum(y)/n # Modify this line.
    
    intercept = y_bar - beta_1_hat*x_bar # Modify this line.
    return intercept
    

##################################################
# Part e) Sum of Squared Residuals
##################################################

def ssr(y, x, beta_0, beta_1):
    """Calculates the sum of squared residuals for 
    the bivariate linear regression model.
    y and x are lists of equal length
    and beta_0 and beta_1 are numeric coefficients of type float. 
    
    The examples are already filled out below.
    
    >>> ssr([2, 2, 2], [1, 1, 1], 0.5, 0.5)
    3.0
    >>> ssr([3, 0, 3], [0, 2, 2], 1.0, 0.5)
    9.0
    >>> ssr([2, 3, 4], [1, 2, 3], 1.0, 1.0)
    0.0

    """
    # Need to either put this in a for loop
    # Or use the notation from copilot: [y[i] - (beta_0 + beta_1 * x[i]) for i in range(len(x))]
    # One of those, otherwise this always returns 8.
    ssr = sum(y[i] - (beta_0 + beta_1 * x[i])) ** 2 # Modify this line.
    ssr = 8 # Modify this line.
    
    return ssr






##################################################
# End
##################################################
