# BayesFactorCalculation
This repository contains an implementation of the bayesian hypothesis testing to determine if the calculated sampling date of a particalar viral sequence is different from its recorded sampling date.
The main outcome is a bayes factor where greater value indicate the calculated date is much differ from the recorded date.

parameter	| meaning	| type
--------- |---------|  -------  
logPath	  | the fold where the log file is stored    | string
logfileName| the name of the log file |  string
span      | the span of the prior distribution of the sampling date | float
vlinePos  | the recorded date of all the tested squences | list




