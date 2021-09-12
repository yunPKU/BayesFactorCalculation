# BayesFactorCalculation
This repository contains an implementation of the bayesian hypothesis testing to determine if the calculated sampling date of a particalar viral sequence is different from its recorded sampling date.
The main outcome is a bayes factor with greater value indicates the calculated date is much more differ from the recorded date.
A example data (B11_29_gis_big_smpSize=7_before1130_iter=0_env.log.tar.gz) is uploaded as well. 

parameter	| meaning	| type    |
--------- |---------|  ------- | 
logPath	  | the fold where the log file is stored    | string | ~
logfileName| the name of the log file |  string | 'B11_29_gis_big_smpSize=7_before1130_iter=0_env.log'
span      | the span of the prior distribution of the sampling date | float | 0.9151
vlinePos  | the recorded date of all the tested squences | list | [2020.4411,2020.4438,2020.4438,2020.4466,2020.4466,2020.4521,2020.4438,2020.463] + [2020.4438]*5




