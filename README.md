# 2017_UK_RSE_Survey_regional_analysis
A quick analysis of the 2017 UK RSE Survey for James Hetherington

I've run this in a virtual environment. The libraries are contained in the requirements.txt file.

# Notes 
* The results are in the results.csv file
* The original data from the survey is cleaned_data.csv
* It's BSD 3-clause licensed

# Assumptions
* We asked people to select their salary from within a range of salaries. To calculate the mean salary, I took the mid-point of the salary range the respondent selected.
* As you'll see from the results.csv, some means are calculated on a dataset containing one data point. That's all we've got.
* It's broken down on a per-organisation basis, because we didn't record regions
