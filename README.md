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

#Chapter 2: Descriptive Statistics
## Mean and Average
* Mean (u) - summary statistics computed with as the sum of the values divided by the number of values
* Average - one of many summary statistics used to describe the typical value or the central tendency of a sample

## Variance
* Variance (d^2)- intended to describe the spread, calculated as the mean squared deviation (i.e. sum((xi - u)^2)/n ), units are squared which makes it hard to interpret on its own
* Standard deviation (d) - square root of the variance

##Distributions
* Distribution - describes how often each value appears
* Histogram - most common representation of a distribution, shows the frequency or probability of each value
* Frequency - number of time a value appears in a dataset
* Probability - frequency expressed as a fraction of the sample size (n)
* Normalization - used to get from frequencies to probabilities diving by the sample size (n)
* Probability Mass Function (PMF) - Function that maps from values to probabilities

###Histograms
Features that can be observed in a histogram include:
* Mode - most common value in a distribution, summary statistics that describes the typical value in a histogram, for pregnancies the mode is 39 weeks
* Shape - shape (symmetric or asymmetric) around the mode, for pregnancy length it drops off quickly to the right and more slowly to the left since babies are often born early but seldom later than 42 weeks
* Outliers - values far from the mode or central tendency, may be due to unusual cases (e.g. babies born at 30 weeks) or due to errors in reporting or recording data
Histograms are usually not useful for comparing two distributions. In the example of pregnancies, when comparing length of pregnancies for first babies to other babies, differences in histograms may be due to sample sizes. In this case, PMFs can provide a better representation. 

###Outliers
In order to eliminate potentially erratic values, data can be trimmed by discarding some fraction of the highest and lowest values. 
*Truncated mean - statistical measure of central tendency like mean and median, involves the calculation of the mean after discarding given parts of a probability distribution or sample at the high and low end
	* typically discards equal amounts at the high and low end
	* number of points to be discarded is usually given as a percentage of the total number of points, but can also be given as a fixed number of points
	* when the lowest 25% and the highest 25% are discarded (i.e. the 25% trimmed mean) it is known as the interquartile mean

### Relative Risk
* Bins - used to group data into ranges that define subsets of a population meeting a criteria of interest
* Relative risk - ratio of two probabilities
	* Example: Probability that a first baby is born early is 18.2%. For other babies it is 16.8%, so the relative risk is 1.08. That means that first babies are about 8% more likely to be early. 






