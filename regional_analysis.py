#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
import numpy as np
import math
    

def import_csv_to_df(location, filename):
    """
    Imports a csv file into a Pandas dataframe
    :params: an xls file and a sheetname from that file
    :return: a df
    """
    
    return pd.read_csv(location + filename + '.csv')


def export_to_csv(df, location, filename, index_write):
    """
    Exports a df to a csv file
    :params: a df and a location in which to save it
    :return: nothing, saves a csv
    """

    return df.to_csv(location + filename + '.csv', index=index_write)


def main():

    df = import_csv_to_df('./', 'cleaned_data')


    # Get rid of the private sector and unknown categories
    df = df[df['currentEmp1. What type of organisation do you work for?']!='Private company']
    df = df[df['currentEmp1. What type of organisation do you work for?']!='Other']

    # Combine the columns with the detail about the organisation into one column
    df['organisations'] = df['currentEmp2. Which university?'].fillna('') + df['currentEmp4. Which organisation do you work for?'].fillna('')
    
    # Get rid of commans in the salary
    df['socio4. Please select the range of your salary'] = df['socio4. Please select the range of your salary'].str.replace(',','')
    # Get the first part of the salary range
    df['first_salary'] = df['socio4. Please select the range of your salary'].str.extract('(\d+)', expand=False)
    # Extract the second part of the salary range, then convert it into an integer
    df['second_salary'] = df['socio4. Please select the range of your salary'].str.split('and', expand=False).str[1]
    df['second_salary'] = df['second_salary'].str.extract('(\d+)', expand=False)

    # Get rid of results where the person did not record their salary
    df.dropna(subset = ['first_salary', 'second_salary'], inplace=True) 

    # Find the mid-point between the two salaries
    df['mid_salary'] = df['first_salary'].astype(int) + (df['second_salary'].astype(int) - df['first_salary'].astype(int))/2

    # Get a list of the unique organisation names
    organisation_list = df['organisations'].unique().tolist()
    # Remove the blank organisation and the 'Other'
    organisation_list.remove('')
    organisation_list.remove('Other')
    # Sort
    organisation_list.sort()

    # Initialise
    results_df = pd.DataFrame(index=organisation_list)

    # Go through each organisation, find the average salary, then save it into a dataframe
    for curr_org in organisation_list:
        temp_df = df[df['organisations']==curr_org]
        average_salary = temp_df['mid_salary'].mean()
        results_df.loc[curr_org, 'mean salary'] = round(average_salary,0)
        results_df.loc[curr_org, 'number of results used to calculate mean'] = len(temp_df)
    
    export_to_csv(results_df, './', 'results', True)

if __name__ == '__main__':
    main()