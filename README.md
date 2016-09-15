Think Stats: Probability and Statistics for Programmers  
Notes from reading and working through exercises in the second edition of Think Stats book by Allen B. Downey, published by Green Tea Press and O'Reilly Media.

* http://greenteapress.com/thinkstats2/
* https://github.com/AllenDowney/ThinkStats2

# Preface
Author's process to work with a dataset:

1. Importing and cleaning - read the data, clean and transform it, and check that everything made it through the translation process intact
2. Single variable explorations - examine one variable at a time to understand what it means, looking at distributions of the values, and choosing appropriate summary statistics. 
3. Pair-wise explorations - identify possible relationships between variables, looking at tables and scatter plots, compute correlations and linear fits
4. Multivariate analysis - apparent relationships between variables, multiple regression to add control variables and investigate more complex relationships
5. Estimation and hypothesis testing - answers three questions:
	1. How big is the effect?
	2. How much variability should we expect if we run the same measurement again?
	3. Is it possible that the apparent effect is due to chance?
6. Visualization - important tool for finding possible relationships and effects, if apparent effect holds up to scrutiny, visualization is effective way to communicate results

Sources of data used in the book:

1. National Survey of Family Growth (NSFG) - conducted by the U.S. Centers for Disease Control (CDC) to gather "information on family life, marriage and divorce, pregnancy, infertility, use of contraception, and men's and women's health. The results are used ... to plan health services and health education programs, and to do statistical studies of families, fertility, and health."
	* http://cdc.gov/nchs/nsfg.htm

2. Behavioral Risk Factor Surveillance System (BRFSS) - conducted by the National Center for Chronic Disease Prevention and Health Promotion to "track health conditions and risk behaviors in the United States."
	* http://cdc.gov/BRFSS/


# Chapter 1: Exploratory Data Analysis
Case study: do first babies tend to arrive late?

* anecdotal evidence - based on data that is unpublished and usually personal


Anectodal evidence usually fails because:

* small number of observations
* selection bias
* confirmation bias
* inaccuracy

Statistical approach:

* data collection - using data from large survey to generate statistically valid inferences about the population
* descriptive statistics - summarize the data concisely, evaluate ways to visualize the data
* exploratory data analysis - looking for patterns, differences, and other features that address the question of interest, also used to check for inconsistencies and check for limitations
* estimation - using data from a sample to estimate characteristics of the general population
* hypothesis testing - when apparent efffects are seen (like a difference between two groups), used to evaluate wether the effect might have happened by chance

## The National Survey of Family Growth
National Survey of Family Growth (NSFG) is conducted by the U.S. Centers for Disease Control (CDC) to gather "information on family life, marriage and divorce, pregnancy, infertility, use of contraception, and men's and women's health. The results are used ... to plan health services and health education programs, and to do statistical studies of families, fertility, and health". 

* cross-sectional study - captures a snapshot of a group at a point in time (e.g. NSFG), meant to be representative
* longitudinal study - observes a group repeatedly over a period of time
* cycle - each deployement or instance that a survey is conducted
* population - goal of survey is to draw conclusions about a population (e.g. for NSFG, people in the US aged 15-44), ideally surveys would collect data from every member of the population
* sample - subset of a population, surveys collect data for a sample and draw conclusions about a population
* respondents - people who participate in a survey
* representative - every member of the target population has an equal chance of participating
* oversampling - deliberately sampling groups at rates higher than their representation in a population, used to make sure that group is large enough to draw valid statistical inferences, drawback is that it is not as easy to draw conclusions about the general population
* codebook - documents the design of a study, the survey questions, and encoding in the responses

### NSFG Data
* record - each line in the file, contains information about one pregnancy
* Stata dictionary file - documents the format of the file, indicates the list of variable names, types, and indices that identify where in each line to find each variable

###Pandas
* Pandas - Python data and statistics package
* DataFrame - fundamental data structure provided by pandas
	* contains a row for each record and a column for each variable
	* contains variable names and their types
	* provides methods for accessing and modifying the data
* columns - attribute of a DataFrame, returns a sequence of column names as Unicode strings
* Index - columns attribute returns and Index, which is another pandas data structure and similar to a list
* Series - pandas data structure, the result of accesing a column from a DataFrame using the column name as key, similar to a Python list with additional features
	* last line of a Series includes the variable name, length, and data type
	* elements in a Series can be accessed using indices and slices
		* using index produces a value (e.g. int64)
		`pregordr[0]`
		* using slice produces another Series (e.g. list)
		`pregordr[2:5]` 

Tables and Records
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

* Truncated mean - statistical measure of central tendency like mean and median, involves the calculation of the mean after discarding given parts of a probability distribution or sample at the high and low end
	* typically discards equal amounts at the high and low end
	* number of points to be discarded is usually given as a percentage of the total number of points, but can also be given as a fixed number of points
	* when the lowest 25% and the highest 25% are discarded (i.e. the 25% trimmed mean) it is known as the interquartile mean

### Relative Risk
* Bins - used to group data into ranges that define subsets of a population meeting a criteria of interest
* Relative risk - ratio of two probabilities
	* Example: Probability that a first baby is born early is 18.2%. For other babies it is 16.8%, so the relative risk is 1.08. That means that first babies are about 8% more likely to be early. 






