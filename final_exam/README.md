# QMB6315: Python for Business Analytics
## Spring 2025

# Final Examination

 Save your scripts and materials in a folder called ```final_exam``` in your GitHub respository.

## Recommended model

Enter the summary statistics from your recommended model in the code block below.


```

#       SELECT *
    FROM Applications
            
         app_id          ssn  zip_code    income  purchases  credit_limit
count    500.00       500.00    500.00    500.00     500.00        500.00
mean  560031.30 550528735.66  57925.57  59546.00   11080.20      20801.20
std   262395.22 266293457.37  25879.95  24376.06    8323.58      10374.40
min   102227.00 100091104.00  10654.00      0.00     300.00        300.00
25%   331219.50 314443704.50  35886.75  43000.00    4536.39      12400.00
50%   567079.50 559834767.50  59040.00  59500.00    8883.66      19400.00
75%   788718.50 777102393.25  80699.25  78000.00   14890.65      29750.00
max   998685.00 999092731.00  99977.00 123000.00   39841.47      41300.00
Index(['app_id', 'ssn', 'zip_code', 'income', 'homeownership', 'purchases',
       'credit_limit'],
      dtype='object')
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              purchases   R-squared:                       0.361
Model:                            OLS   Adj. R-squared:                  0.357
Method:                 Least Squares   F-statistic:                     93.44
Date:                Sun, 11 May 2025   Prob (F-statistic):           6.03e-48
Time:                        08:57:21   Log-Likelihood:                -5110.4
No. Observations:                 500   AIC:                         1.023e+04
Df Residuals:                     496   BIC:                         1.025e+04
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
Intercept                   1.1e+04   1103.160      9.972      0.000    8833.124    1.32e+04
C(homeownership)[T.Rent] -5732.2381    649.333     -8.828      0.000   -7008.020   -4456.456
income                      -0.0622      0.012     -5.071      0.000      -0.086      -0.038
credit_limit                 0.3736      0.029     12.963      0.000       0.317       0.430
==============================================================================
Omnibus:                       19.685   Durbin-Watson:                   1.909
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               21.384
Skew:                           0.505   Prob(JB):                     2.27e-05
Kurtosis:                       2.931   Cond. No.                     2.60e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.6e+05. This might indicate that there are
strong multicollinearity or other numerical problems.

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

         income  purchases  credit_limit   fico  num_late  past_def  \
count    500.00     500.00        500.00 500.00    500.00    500.00   
mean   59546.00   11080.20      20801.20 688.78      0.86      0.16   
std    24376.06    8323.58      10374.40 124.60      1.20      0.48   
min        0.00     300.00        300.00 307.00      0.00      0.00   
25%    43000.00    4536.39      12400.00 602.00      0.00      0.00   
50%    59500.00    8883.66      19400.00 690.00      0.00      0.00   
75%    78000.00   14890.65      29750.00 795.50      1.00      0.00   
max   123000.00   39841.47      41300.00 893.00      5.00      4.00   

       num_bankruptcy  
count          500.00  
mean             0.17  
std              0.50  
min              0.00  
25%              0.00  
50%              0.00  
75%              0.00  
max              3.00  
Index(['income', 'homeownership', 'purchases', 'credit_limit', 'fico',
       'num_late', 'past_def', 'num_bankruptcy'],
      dtype='object')
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              purchases   R-squared:                       0.528
Model:                            OLS   Adj. R-squared:                  0.522
Method:                 Least Squares   F-statistic:                     78.78
Date:                Sun, 11 May 2025   Prob (F-statistic):           2.84e-76
Time:                        08:57:21   Log-Likelihood:                -5034.4
No. Observations:                 500   AIC:                         1.008e+04
Df Residuals:                     492   BIC:                         1.012e+04
Df Model:                           7                                         
Covariance Type:            nonrobust                                         
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
Intercept                 -3.52e+04   6876.198     -5.120      0.000   -4.87e+04   -2.17e+04
C(homeownership)[T.Rent] -6098.7865    560.883    -10.874      0.000   -7200.809   -4996.764
income                      -0.0644      0.011     -6.075      0.000      -0.085      -0.044
credit_limit                -0.5763      0.162     -3.568      0.000      -0.894      -0.259
fico                        92.2193     14.575      6.327      0.000      63.582     120.856
num_late                  2666.8459    227.587     11.718      0.000    2219.684    3114.008
past_def                   820.6749    875.244      0.938      0.349    -899.003    2540.352
num_bankruptcy            2452.6395   1000.539      2.451      0.015     486.784    4418.495
==============================================================================
Omnibus:                       39.698   Durbin-Watson:                   1.998
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               47.812
Skew:                           0.687   Prob(JB):                     4.15e-11
Kurtosis:                       3.639   Cond. No.                     1.80e+06
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.8e+06. This might indicate that there are
strong multicollinearity or other numerical problems.

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

         income  purchases  credit_limit   fico  num_late  past_def  \
count    500.00     500.00        500.00 500.00    500.00    500.00   
mean   59546.00   11080.20      20801.20 688.78      0.86      0.16   
std    24376.06    8323.58      10374.40 124.60      1.20      0.48   
min        0.00     300.00        300.00 307.00      0.00      0.00   
25%    43000.00    4536.39      12400.00 602.00      0.00      0.00   
50%    59500.00    8883.66      19400.00 690.00      0.00      0.00   
75%    78000.00   14890.65      29750.00 795.50      1.00      0.00   
max   123000.00   39841.47      41300.00 893.00      5.00      4.00   

       num_bankruptcy  avg_income  density  
count          500.00      500.00   500.00  
mean             0.17    60280.67   338.55  
std              0.50    14305.81   545.32  
min              0.00    11674.63     0.01  
25%              0.00    51539.59    31.32  
50%              0.00    60348.68   143.87  
75%              0.00    69892.91   389.65  
max              3.00    99560.27  3826.97  
Index(['income', 'homeownership', 'purchases', 'credit_limit', 'fico',
       'num_late', 'past_def', 'num_bankruptcy', 'avg_income', 'density'],
      dtype='object')
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              purchases   R-squared:                       0.583
Model:                            OLS   Adj. R-squared:                  0.576
Method:                 Least Squares   F-statistic:                     76.26
Date:                Sun, 11 May 2025   Prob (F-statistic):           2.07e-87
Time:                        08:57:21   Log-Likelihood:                -5003.5
No. Observations:                 500   AIC:                         1.003e+04
Df Residuals:                     490   BIC:                         1.007e+04
Df Model:                           9                                         
Covariance Type:            nonrobust                                         
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
Intercept                -3.286e+04   6549.112     -5.017      0.000   -4.57e+04      -2e+04
C(homeownership)[T.Rent] -6526.8141    530.983    -12.292      0.000   -7570.099   -5483.529
income                      -0.0496      0.012     -3.966      0.000      -0.074      -0.025
credit_limit                -0.5489      0.152     -3.606      0.000      -0.848      -0.250
fico                        89.0137     13.734      6.481      0.000      62.028     115.999
num_late                  2646.4521    214.530     12.336      0.000    2224.941    3067.963
past_def                  1242.8911    826.098      1.505      0.133    -380.241    2866.023
num_bankruptcy            2122.7518    944.217      2.248      0.025     267.537    3977.966
avg_income                  -0.0414      0.021     -1.944      0.052      -0.083       0.000
density                      3.5650      0.450      7.921      0.000       2.681       4.449
==============================================================================
Omnibus:                       46.505   Durbin-Watson:                   1.955
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               59.946
Skew:                           0.728   Prob(JB):                     9.61e-14
Kurtosis:                       3.871   Cond. No.                     2.45e+06
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.45e+06. This might indicate that there are
strong multicollinearity or other numerical problems.
count   500.00
mean      0.59
std       0.33
min       0.04
25%       0.28
50%       0.60
75%       0.94
max       1.00
Name: utilization, dtype: float64
                            OLS Regression Results                            
==============================================================================
Dep. Variable:            utilization   R-squared:                       0.619
Model:                            OLS   Adj. R-squared:                  0.613
Method:                 Least Squares   F-statistic:                     99.79
Date:                Sun, 11 May 2025   Prob (F-statistic):           7.06e-98
Time:                        08:57:21   Log-Likelihood:                 87.597
No. Observations:                 500   AIC:                            -157.2
Df Residuals:                     491   BIC:                            -119.3
Df Model:                           8                                         
Covariance Type:            nonrobust                                         
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
Intercept                    1.0838      0.078     13.855      0.000       0.930       1.237
C(homeownership)[T.Rent]    -0.2847      0.020    -14.192      0.000      -0.324      -0.245
income                    -2.09e-06   4.72e-07     -4.428      0.000   -3.02e-06   -1.16e-06
fico                        -0.0004   9.05e-05     -4.630      0.000      -0.001      -0.000
num_late                     0.1249      0.008     15.415      0.000       0.109       0.141
past_def                     0.1198      0.031      3.837      0.000       0.058       0.181
num_bankruptcy               0.0503      0.031      1.629      0.104      -0.010       0.111
avg_income               -1.104e-06   8.06e-07     -1.370      0.171   -2.69e-06    4.79e-07
density                      0.0001    1.7e-05      8.606      0.000       0.000       0.000
==============================================================================
Omnibus:                       45.091   Durbin-Watson:                   1.889
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               55.470
Skew:                           0.813   Prob(JB):                     9.01e-13
Kurtosis:                       3.148   Cond. No.                     7.60e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 7.6e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
                            OLS Regression Results                            
==============================================================================
Dep. Variable:          log_odds_util   R-squared:                       0.843
Model:                            OLS   Adj. R-squared:                  0.841
Method:                 Least Squares   F-statistic:                     329.8
Date:                Sun, 11 May 2025   Prob (F-statistic):          5.14e-192
Time:                        08:57:21   Log-Likelihood:                -894.93
No. Observations:                 500   AIC:                             1808.
Df Residuals:                     491   BIC:                             1846.
Df Model:                           8                                         
Covariance Type:            nonrobust                                         
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
Intercept                    4.1002      0.558      7.346      0.000       3.004       5.197
C(homeownership)[T.Rent]    -2.0981      0.143    -14.655      0.000      -2.379      -1.817
income                   -2.356e-05   3.37e-06     -6.996      0.000   -3.02e-05   -1.69e-05
fico                        -0.0029      0.001     -4.500      0.000      -0.004      -0.002
num_late                     1.0320      0.058     17.852      0.000       0.918       1.146
past_def                     1.7965      0.223      8.062      0.000       1.359       2.234
num_bankruptcy               3.2794      0.220     14.902      0.000       2.847       3.712
avg_income                 2.18e-06   5.75e-06      0.379      0.705   -9.12e-06    1.35e-05
density                      0.0012      0.000     10.207      0.000       0.001       0.001
==============================================================================
Omnibus:                      288.870   Durbin-Watson:                   1.987
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             2461.365
Skew:                           2.423   Prob(JB):                         0.00
Kurtosis:                      12.729   Cond. No.                     7.60e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 7.6e+05. This might indicate that there are
strong multicollinearity or other numerical problems.

```