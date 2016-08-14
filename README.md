# probable-eureka
Think Stats: Probability and Statistics for Programmers  
Notes from reading and working through exercises in Think Stats book by Allen B. Downey, published by O'Reilly Media.

* http://greenteapress.com/thinkstats/
* https://github.com/AllenDowney/ThinkStats2

# Definitions
1. probability - study of random events
2. statistics - discipline of using data samples to support claims about populations, most statistical analysis is based on probability

# Chapter 1: Statistical Thinking for Programmers
Anectodal evidence usually fails because:
* small number of observations
* selection bias
* confirmation bias
* inaccuracy

Statistical tools:
* data collection
* descriptive statistics
* exploratory data analysis
* hypothesis testing
* estimation - using data from a sample to estimate characteristics of the general population

## The National Survey of Family Growth
National Survey of Family Growth (NSFG) is conducted by the U.S. Centers for Disease Control (CDC) to gather "information on family life, marriage and divorce, pregnancy, infertility, use of contraception, and men's and women's health. The results are used ... to plan health services and health education programs, and to do statistical studies of families, fertility, and health". 
* cross-sectional study - captures a snapshot of a group at a point in time (e.g. NSFG), meant to be representative
* longitudinal study - observes a group repeatedly over a period of time
* cycle - each deployement or instance that a survey is conducted
* respondents - people who participate in a survey
* cohort - group of respondents
* representative - every member of the target population has an equal chance of participating
* oversampling - deliberately sampling groups at rates higher than their representation in a population, used to make sure that group is large enough to draw valid statistical inferences, drawback is that it is not as easy to draw conclusions about the general population

Tables and Records
* record - each line in the respondents file, contains information about one respondent
* fields - variables that make up a record
* table - collection of records

### NSFG Pregnancy Records
1. caseid - integer ID of the respondent
2. prglenth - duration of the pregnancy in weeks
3. outcome - integer code for the outcome of the pregnancy (1 indicates a live birth)
4. birthord - birth order of each live birth, the code for a first child is 1, field is blank for outcomes other than live birth
5. finalwgt - statistical weight associated with the respondent, floating-point value that indicates the number of people in the U.S. population that the respondent represents

These variables are recodes, which means that they do not come from raw data directly but instead are calculated using the raw data. 

