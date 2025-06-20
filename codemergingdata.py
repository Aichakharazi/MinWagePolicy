# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:25:00 2024

@author: ak922
"""






import numpy as np
import pandas as pd

import addfips





import numpy 
import numpy as np
import pandas

import pandas as pd


import addfips
#%%

from linearmodels import PanelOLS
#%%
from linearmodels import RandomEffects

from linearmodels.panel import PooledOLS
#%%
import statsmodels
import statsmodels.api as sm
#%%
from linearmodels.panel import compare

#%%

import seaborn 
import seaborn as sns

#%%
import matplotlib
import matplotlib.pyplot as plt

#%%
import statsmodels.api
#%%
import statsmodels.api as sm
#%%
from statsmodels.compat.numpy import NP_LT_123
#%%
import statsmodels.formula.api as smf
#%%
from pandas import DataFrame
import statsmodels.formula.api as smf
#from statsmodels.iolib.summary2 import summary_col

import regex as re
#%%
import spacy
import csv

import seaborn as sns
#%%

from matplotlib import pyplot as plt



import matplotlib
import matplotlib.pyplot as plt

#%%
# PrCode	PROCESS_CODE  (processing code)
# SrHhd	H.H.SERIAL_NO  (household serial number)
# RespRel	RESP_SEX  (respondents sex)
# S04C05	SEC4_COL5  (sex of person)
# S04C09	SEC4_COL9  s4c9	(education level)
# S05C01	SEC5_COL1   ( did do any work for pay, profit or family gain during last week, at least for on)

#S05C07	SEC5_COL7  (what was employment status)
#S05C08	SEC5_COL8  (what was main occupation)
#S05C16	SEC5_COL16  (total hours)

#s5c251	total hours S05C25	SEC5_COL25  (conditional on being entrepreneur)
# S07C05	SEC7_COL53  (how much net money earned last year (total in rs.))
# S07C07  (how much net money did earn during last year from own business)


# formal sector (method 2): (Mustapha suggestion)  code: (5.10) in questionnaire 2020-2021
# what kind of  enterprise? 
#01. Federal Govt. (Skip to Col.5.14)
#02. Provincial Govt. (Skip to Col.5.14)
#03. Local body Govt. (Skip to Col.5.14)
#04. Public enterprise (Corporation by act of national or provincial assembly) (Skip to Col.5.14)
#05. Public limited company (Skip to Col.5.14)
#06. Private limited  company (Skip to Col.5.14)
#07. Cooperative society/UN agency/ Embassy (Skip to Col.5.14)
#08. Individual ownership
#09. Partnership
#10. Other (Specify )
    
    
    
#%%  	"processing_code","province","distric_with_label","region","serial_number_of_household"	




data2020_2021 = pd.read_csv('LFS2020-21.csv', sep=',')


# Function to convert earnings to annual
def convert_to_annual(row):
    if row['at_main_work_waht_is_the_periodicity_of_paymentk'] in [1, 2, 5, 6, 7]:
        return row['how_much_net_money_earned_last_week_total_in_rs_'] * 52
    elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] in [3, 4]:
        return row['how_much_net_money_earned_last_month_total_in_rs_'] * 12
  #  elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] == 'Annually':
  #      return row['Earnings']

# Apply conversion
data2020_2021['Annual_Earnings'] = data2020_2021.apply(convert_to_annual, axis=1)

#%%


# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['what_was_main_occupation'])
        
        if 1111 <= occupation_code <= 1439 or 2111 <= occupation_code <= 2659:
            return 1
        elif 3111 <= occupation_code <= 3522:
            return 2
        elif 4110 <= occupation_code <= 4419:
            return 3
        elif 5111 <= occupation_code <= 5419:
            return 4
        elif 6111 <= occupation_code <= 6340:
            return 5
        elif 7111 <= occupation_code <= 7549:
            return 6
        elif 8111 <= occupation_code <= 8350:
            return 7
        elif 9111 <= occupation_code <= 9629:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2020_2021['occupations_code_18'] = data2020_2021.apply(determine_occupation, axis=1)


# Labels for occupations
#occupation_labels = {
#    1: "Professionals",
#    2: "Technicians and Associate professionals",
#    3: "Administrative",
#    4: "Service and Sales",
#    5: "Agriculture",
#    6: "Skilled Craft and Trades",
#    7: "Production",
#    8: "Elementary"
#}
#%%  what_was_the_nature_of_work_done_by_the_establishment

def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['what_was_the_nature_of_work_done_by_the_establishment'])
        
        if 111 <= industry_code <= 322:
            return 1  # Agriculture, forestry and fishing
        elif 1010 <= industry_code <= 3320:
            return 2  # Manufacturing
        elif 4100 <= industry_code <= 4390:
            return 3  # Construction
        elif 4510 <= industry_code <= 6820:
            return 4  # Services
        elif (510 <= industry_code <= 990) or \
             (6910 <= industry_code <= 9900) or \
             (3510 <= industry_code <= 3600):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2020_2021['Industry'] = data2020_2021.apply(determine_industry, axis=1)




#%%
data2020_2021['TrainVar'] = 0
#%%
# Set 'TrainVar' to 1 where 'S04C11' is between 10 and 20 inclusive
data2020_2021.loc[data2020_2021['ever_completed_any_technical_vocational_training'].between(10, 20), 'TrainVar'] = 1

# Set 'TrainVar' to 2 where 'S04C11' is exactly 21
data2020_2021.loc[data2020_2021['ever_completed_any_technical_vocational_training'] == 21, 'TrainVar'] = 2
#%% replace 
data2020_2021['ever_completed_any_technical_vocational_training'] = data2020_2021['TrainVar']

#%% Earnings checked - accurate


columns_of_interest = [	"processing_code","household_number","respondents_sex",
"persons_relationship_to_head_of_the_household","sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
"province","distric_with_label","region","age_at_last_birthday",
"current_marital_status",
"literacy_1",
"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings",
"what_kind_of_enterprise",
"ever_completed_any_technical_vocational_training","occupations_code_18","Industry"]



data_clean2020_2021 = data2020_2021.loc[:, columns_of_interest]

#%% add year 
data_clean2020_2021['year'] = 2021

#%%
data2018_2019 = pd.read_csv('LFS2018-19.csv', sep=',')


#%%  Earnings checked - accurate
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['S07C02'] in [1, 2, 5, 6, 7]:
        return row['S07C03'] * 52
    elif row['S07C02'] in [3, 4]:
        return row['S07C04'] * 12
  #  elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] == 'Annually':
  #      return row['Earnings']

# Apply conversion
data2018_2019['Annual_Earnings'] = data2018_2019.apply(convert_to_annual, axis=1)


#%%
#%%


# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['S05C09'])
        
        if 1111 <= occupation_code <= 1439 or 2111 <= occupation_code <= 2659:
            return 1
        elif 3111 <= occupation_code <= 3522:
            return 2
        elif 4110 <= occupation_code <= 4419:
            return 3
        elif 5111 <= occupation_code <= 5419:
            return 4
        elif 6111 <= occupation_code <= 6340:
            return 5
        elif 7111 <= occupation_code <= 7549:
            return 6
        elif 8111 <= occupation_code <= 8350:
            return 7
        elif 9111 <= occupation_code <= 9629:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2018_2019['occupations_code_18'] = data2018_2019.apply(determine_occupation, axis=1)

#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['S05C10'])
        
        if 111 <= industry_code <= 322:
            return 1  # Agriculture, forestry and fishing
        elif 1010 <= industry_code <= 3320:
            return 2  # Manufacturing
        elif 4100 <= industry_code <= 4390:
            return 3  # Construction
        elif 4510 <= industry_code <= 6820:
            return 4  # Services
        elif (510 <= industry_code <= 990) or \
             (6910 <= industry_code <= 9900) or \
             (3510 <= industry_code <= 3600):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2018_2019['Industry'] = data2018_2019.apply(determine_industry, axis=1)
#%%

data2018_2019['TrainVar'] = 0
#%%
# Set 'TrainVar' to 1 where 'S04C11' is between 10 and 20 inclusive
data2018_2019.loc[data2018_2019['S04C11'].between(10, 20), 'TrainVar'] = 1

# Set 'TrainVar' to 2 where 'S04C11' is exactly 21
data2018_2019.loc[data2018_2019['S04C11'] == 21, 'TrainVar'] = 2


#%%
columns_of_interest = ["PrCode","SrHhd","RespSex","RespRel",
                       "S04C05","S04C06","S04C07","S04C08",
"S04C09",
"S04C15","S04C16","S04C17","S04C18",
"S05C08","S05C09",
"S05C171","Annual_Earnings","S05C11","TrainVar",'occupations_code_18',"Industry"]
#%%
data_clean2018_2019 = data2018_2019.loc[:, columns_of_interest]


#%% rename

columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1", #"literacy_2",
    "education_level", 
    "how_long_has_been_living_in_this_district", "previous_district_of_residence_before_moving_here",  "previous_residence_was_located_in_urban_rural", "main_reason_for_migration",
    "what_was_employment_status", "what_was_main_occupation", "total_hours",
    "Annual_Earnings",
    "what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    'occupations_code_18',"Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean2018_2019 = data_clean2018_2019.rename(columns=dict(zip(data_clean2018_2019.columns, columns_of_interest2)))

#%% add year 
data_clean2018_2019['year'] = 2019

#%% Earnings checked - accurate
data2017_2018 = pd.read_csv('LFS2017-18.csv', sep=',')
#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['S07C02'] in [1, 2, 5, 6, 7]:
        return row['S07C033'] * 52
    elif row['S07C02'] in [3, 4]:
        return row['S07C04'] * 12
  #  elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] == 'Annually':
  #      return row['Earnings']

# Apply conversion
data2017_2018['Annual_Earnings'] = data2017_2018.apply(convert_to_annual, axis=1)

#
#%%


# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['S05C09'])
        
        if 1111 <= occupation_code <= 1439 or 2111 <= occupation_code <= 2659:
            return 1
        elif 3111 <= occupation_code <= 3522:
            return 2
        elif 4110 <= occupation_code <= 4419:
            return 3
        elif 5111 <= occupation_code <= 5419:
            return 4
        elif 6111 <= occupation_code <= 6340:
            return 5
        elif 7111 <= occupation_code <= 7549:
            return 6
        elif 8111 <= occupation_code <= 8350:
            return 7
        elif 9111 <= occupation_code <= 9629:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2017_2018['occupations_code_18'] = data2017_2018.apply(determine_occupation, axis=1)


#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['S05C10'])
        
        if 111 <= industry_code <= 322:
            return 1  # Agriculture, forestry and fishing
        elif 1010 <= industry_code <= 3320:
            return 2  # Manufacturing
        elif 4100 <= industry_code <= 4390:
            return 3  # Construction
        elif 4510 <= industry_code <= 6820:
            return 4  # Services
        elif (510 <= industry_code <= 990) or \
             (6910 <= industry_code <= 9900) or \
             (3510 <= industry_code <= 3600):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2017_2018['Industry'] = data2017_2018.apply(determine_industry, axis=1)
#%%
#%%
data2017_2018['TrainVar'] = 0
#%%
# Set 'TrainVar' to 1 where 'S04C11' is between 10 and 20 inclusive
data2017_2018.loc[data2017_2018['S04C11'].between(10, 20), 'TrainVar'] = 1

# Set 'TrainVar' to 2 where 'S04C11' is exactly 21
data2017_2018.loc[data2017_2018['S04C11'] == 21, 'TrainVar'] = 2

#%%
columns_of_interest = ["PrCode","SrHhd","RespSex","RespRel",
                       "S04C05","S04C06","S04C07","S04C08",
"S04C09",
"S04C15","S04C16","S04C17","S04C18",
"S05C08","S05C09","S05C171","Annual_Earnings","S05C11","TrainVar",
"occupations_code_18","Industry"]
#%%
data_clean2017_2018 = data2017_2018.loc[:, columns_of_interest]

#%% rename 
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex","persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1", # "literacy_2",
    "education_level", 
    "how_long_has_been_living_in_this_district",
    "previous_district_of_residence_before_moving_here",
    "previous_residence_was_located_in_urban_rural",
    "main_reason_for_migration",
    "what_was_employment_status", "what_was_main_occupation", "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training","occupations_code_18",
    "Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean2017_2018 = data_clean2017_2018.rename(columns=dict(zip(data_clean2017_2018.columns, columns_of_interest2)))

#%% add year 
data_clean2017_2018['year'] = 2018


#%%  Earnings checked - accurate
data2014_2015 = pd.read_csv('LFS2014-15.csv', sep=',')


#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['SEC7_COL2'] in [1, 2, 5, 6, 7]:
        return row['SEC7_COL33'] * 52
    elif row['SEC7_COL2'] in [3, 4]:
        return row['SEC7_COL43'] * 12
  #  elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] == 'Annually':
  #      return row['Earnings']

# Apply conversion
data2014_2015['Annual_Earnings'] = data2014_2015.apply(convert_to_annual, axis=1)

#%%


# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['SEC5_COL9'])
        
        if 110 <= occupation_code <= 143 or 1111 <= occupation_code <= 1439 or 2111 <= occupation_code <= 2659:
            return 1
        elif 310 <= occupation_code <=352 or 3111 <= occupation_code <= 3522:
            return 2
        elif 4110 <= occupation_code <= 4419:
            return 3
        elif 5111 <= occupation_code <= 5419:
            return 4
        elif 6111 <= occupation_code <= 6340:
            return 5
        elif 7111 <= occupation_code <= 7549:
            return 6
        elif 8111 <= occupation_code <= 8350:
            return 7
        elif 9111 <= occupation_code <= 9629:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2014_2015['occupations_code_18'] = data2014_2015.apply(determine_occupation, axis=1)

#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['SEC5_COL10'])
        
        if 111 <= industry_code <= 322:
            return 1  # Agriculture, forestry and fishing
        elif 1010 <= industry_code <= 3320:
            return 2  # Manufacturing
        elif 4100 <= industry_code <= 4390:
            return 3  # Construction
        elif 4510 <= industry_code <= 6820:
            return 4  # Services
        elif (510 <= industry_code <= 990) or \
             (6910 <= industry_code <= 9900) or \
             (3510 <= industry_code <= 3600):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2014_2015['Industry'] = data2014_2015.apply(determine_industry, axis=1)

#%%
data2014_2015['TrainVar'] = 0
#%%
# Set 'TrainVar' to 1 where 'S04C11' is between 10 and 20 inclusive
data2014_2015.loc[data2014_2015['SEC4_COL11'].between(10, 20), 'TrainVar'] = 1

# Set 'TrainVar' to 2 where 'S04C11' is exactly 21
data2014_2015.loc[data2014_2015['SEC4_COL11'] == 21, 'TrainVar'] = 2

#%%

#%%
columns_of_interest = ["PROCESS_CODE","H.H.SERIAL_NO","RESP_SEX","RESP_RELATION",
                       "SEC4_COL5", "SEC4_COL6","SEC4_COL7","SEC4_COL8",
"SEC4_COL9",
"SEC4_COL15","SEC4_COL16","SEC4_COL17","SEC4_COL18",
"SEC5_COL8","SEC5_COL9","SEC5_COL17_1","Annual_Earnings","SEC5_COL11","TrainVar",
"occupations_code_18","Industry"]
#%%
data_clean2014_2015 = data2014_2015.loc[:, columns_of_interest]
#%% rename
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1", #"literacy_2",
    "education_level", 
    "how_long_has_been_living_in_this_district",
    "previous_district_of_residence_before_moving_here",
    "previous_residence_was_located_in_urban_rural",
    "main_reason_for_migration",
    "what_was_employment_status", "what_was_main_occupation", "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean2014_2015 = data_clean2014_2015.rename(columns=dict(zip(data_clean2014_2015.columns, columns_of_interest2)))

#%% add year 
data_clean2014_2015['year'] = 2015


#%%   Earnings checked - accurate
data2013_2014 = pd.read_csv('LFS2013-14.csv', sep=',')


#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['SEC7_COL2'] in [1, 2, 5, 6, 7]:
        return row['SEC7_COL33'] * 52
    elif row['SEC7_COL2'] in [3, 4]:
        return row['SEC7_COL43'] * 12
  #  elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] == 'Annually':
  #      return row['Earnings']

# Apply conversion
data2013_2014['Annual_Earnings'] = data2013_2014.apply(convert_to_annual, axis=1)

#%%


# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['SEC5_COL9'])
        
        if 1111 <= occupation_code <= 1439 or 2111 <= occupation_code <= 2659:
            return 1
        elif 3111 <= occupation_code <= 3522:
            return 2
        elif 4110 <= occupation_code <= 4419:
            return 3
        elif 5111 <= occupation_code <= 5419:
            return 4
        elif 6111 <= occupation_code <= 6340:
            return 5
        elif 7111 <= occupation_code <= 7549:
            return 6
        elif 8111 <= occupation_code <= 8350:
            return 7
        elif 9111 <= occupation_code <= 9629:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2013_2014['occupations_code_18'] = data2013_2014.apply(determine_occupation, axis=1)

#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['SEC5_COL10'])
        
        if 111 <= industry_code <= 322:
            return 1  # Agriculture, forestry and fishing
        elif 1010 <= industry_code <= 3320:
            return 2  # Manufacturing
        elif 4100 <= industry_code <= 4390:
            return 3  # Construction
        elif 4510 <= industry_code <= 6820:
            return 4  # Services
        elif (510 <= industry_code <= 990) or \
             (6910 <= industry_code <= 9900) or \
             (3510 <= industry_code <= 3600):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2013_2014['Industry'] = data2013_2014.apply(determine_industry, axis=1)

#%%
data2013_2014['TrainVar'] = 0
#%%
# Set 'TrainVar' to 1 where 'S04C11' is between 10 and 20 inclusive
data2013_2014.loc[data2013_2014['SEC4_COL11'].between(10, 20), 'TrainVar'] = 1

# Set 'TrainVar' to 2 where 'S04C11' is exactly 21
data2013_2014.loc[data2013_2014['SEC4_COL11'] == 21, 'TrainVar'] = 2



#%%
columns_of_interest = ["PROCESS_CODE","H.H.SERIAL_NO","RESP_SEX",
                       "RESP_RELATION",
                       "SEC4_COL5","SEC4_COL6","SEC4_COL7", "SEC4_COL8",
 "SEC4_COL9", 
 "SEC4_COL15","SEC4_COL16","SEC4_COL17","SEC4_COL18",
 "SEC5_COL8",
 "SEC5_COL9","SEC5_COL17_1","Annual_Earnings","SEC5_COL11","TrainVar",
 "occupations_code_18","Industry"]
#%%
data_clean2013_2014 = data2013_2014.loc[:, columns_of_interest]
#%% rename

columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1", #"literacy_2",
    "education_level", 
    "how_long_has_been_living_in_this_district",
    "previous_district_of_residence_before_moving_here",
    "previous_residence_was_located_in_urban_rural",
    "main_reason_for_migration",
    "what_was_employment_status", "what_was_main_occupation", "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean2013_2014 = data_clean2013_2014.rename(columns=dict(zip(data_clean2013_2014.columns, columns_of_interest2)))

#%% add year 
data_clean2013_2014['year'] = 2014


#%%   Earnings checked - accurate
data2012_2013 = pd.read_csv('LFS2012-13.csv', sep=',')

#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['s7_q2'] in [1, 2, 5, 6, 7]:
        return row['s7_q3'] * 52
    elif row['s7_q2'] in [3, 4]:
        return row['s7_q4'] * 12
  #  elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] == 'Annually':
  #      return row['Earnings']

# Apply conversion
data2012_2013['Annual_Earnings'] = data2012_2013.apply(convert_to_annual, axis=1)

#%%



# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['s5_q9'])
        
        if 1 <= occupation_code <= 2 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2012_2013['occupations_code_18'] = data2012_2013.apply(determine_occupation, axis=1)

#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['s5_q10'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2012_2013['Industry'] = data2012_2013.apply(determine_industry, axis=1)

#%%

data2012_2013['TrainVar'] = 0
#%%
# Set 'TrainVar' to 1 where 'S04C11' is between 10 and 20 inclusive
data2012_2013.loc[data2012_2013['s4_q11'].between(10, 20), 'TrainVar'] = 1

# Set 'TrainVar' to 2 where 'S04C11' is exactly 21
data2012_2013.loc[data2012_2013['s4_q11'] == 21, 'TrainVar'] = 2

#%%
columns_of_interest = ["Prcode","HHSno","RespSex","RespRel",
                       "s4_q5","s4_q6","s4_q7","s4_q8",
                       "s4_q9",  
                       "s4_q15", "s4_q16", "s4_q17", "s4_q18", 
                       "s5_q8","s5_q9","s5_q17_1","Annual_Earnings","s5_q11","TrainVar",
                       "occupations_code_18","Industry"]
#%%
data_clean2012_2013 = data2012_2013.loc[:, columns_of_interest]
#%% rename 

columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level", 
    "how_long_has_been_living_in_this_district",
    "previous_district_of_residence_before_moving_here",
    "previous_residence_was_located_in_urban_rural",
    "main_reason_for_migration",
    "what_was_employment_status", "what_was_main_occupation", "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean2012_2013 = data_clean2012_2013.rename(columns=dict(zip(data_clean2012_2013.columns, columns_of_interest2)))
#%% add year 
data_clean2012_2013['year'] = 2013


#%%
data2010_2011 = pd.read_csv('LFS2010-11.csv', sep=',')

#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['Sec7_7.2'] in [1, 2, 5, 6, 7]:
        return row['Sec7_7.3'] * 52
    elif row['Sec7_7.2'] in [3, 4]:
        return row['Sec7_7.4'] * 12
  #  elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] == 'Annually':
  #      return row['Earnings']

# Apply conversion
data2010_2011['Annual_Earnings'] = data2010_2011.apply(convert_to_annual, axis=1)

#%%
# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['Sec5_5.9'])
        
        if 1 <= occupation_code <= 2 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2010_2011['occupations_code_18'] = data2010_2011.apply(determine_occupation, axis=1)

#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['Sec5_5.10'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2010_2011['Industry'] = data2010_2011.apply(determine_industry, axis=1)

#%%

data2010_2011['TrainVar'] = 0
#%%
# Set 'TrainVar' to 1 where 'S04C11' is between 10 and 20 inclusive
data2010_2011.loc[data2010_2011['Sec4_4.11'].between(10, 20), 'TrainVar'] = 1

# Set 'TrainVar' to 2 where 'S04C11' is exactly 21
data2010_2011.loc[data2010_2011['Sec4_4.11'] == 21, 'TrainVar'] = 2


#%%
columns_of_interest = ["PrCode","HhSno","RespSex","RespRel",
                       "Sec4_4.5","Sec4_4.6","Sec4_4.7","Sec4_4.8",
                       "Sec4_4.9",  
                       "Sec4_4.15", "Sec4_4.16", "Sec4_4.17", "Sec4_4.18",
                       "Sec5_5.8","Sec5_5.9",
                       "Sec5_5.17.1","Annual_Earnings","Sec5_5.11","TrainVar",
                       "occupations_code_18","Industry"]
#%%
data_clean2010_2011 = data2010_2011.loc[:, columns_of_interest]

#%%
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level", 
    "how_long_has_been_living_in_this_district",
    "previous_district_of_residence_before_moving_here",
    "previous_residence_was_located_in_urban_rural",
    "main_reason_for_migration",
    "what_was_employment_status", "what_was_main_occupation", "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean2010_2011 = data_clean2010_2011.rename(columns=dict(zip(data_clean2010_2011.columns, columns_of_interest2)))
#%% add year 
data_clean2010_2011['year'] = 2011


#%%
data2009_2010 = pd.read_csv('LFS2009-10.csv', sep=',')

#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['Sec7_7.2'] in [1, 2, 5, 6, 7]:
        return row['Sec7_7.3'] * 52
    elif row['Sec7_7.2'] in [3, 4]:
        return row['Sec7_7.4'] * 12
  #  elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] == 'Annually':
  #      return row['Earnings']

# Apply conversion
data2009_2010['Annual_Earnings'] = data2009_2010.apply(convert_to_annual, axis=1)


#%%
# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['Sec5_5.9'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2009_2010['occupations_code_18'] = data2009_2010.apply(determine_occupation, axis=1)


#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['Sec5_5.10'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2009_2010['Industry'] = data2009_2010.apply(determine_industry, axis=1)
#%%

data2009_2010['TrainVar'] = 0
#%%
# Set 'TrainVar' to 1 where 'S04C11' is between 10 and 20 inclusive
data2009_2010.loc[data2009_2010['Sec4_4.11'].between(10, 20), 'TrainVar'] = 1

# Set 'TrainVar' to 2 where 'S04C11' is exactly 21
data2009_2010.loc[data2009_2010['Sec4_4.11'] == 21, 'TrainVar'] = 2

#%%
columns_of_interest = ["PrCode","HhSno","RespSex","RespRel",
                       "Sec4_4.5","Sec4_4.6","Sec4_4.7","Sec4_4.8",
                       "Sec4_4.9",  
                       "Sec4_4.15", "Sec4_4.16", "Sec4_4.17", "Sec4_4.18",
                       "Sec5_5.8","Sec5_5.9",
                       "Sec5_5.17.1","Annual_Earnings","Sec5_5.11","TrainVar","occupations_code_18",
                       "Industry"]
#%%
data_clean2009_2010 = data2009_2010.loc[:, columns_of_interest]
#%%  rename 
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level", 
    "how_long_has_been_living_in_this_district",
    "previous_district_of_residence_before_moving_here",
    "previous_residence_was_located_in_urban_rural",
    "main_reason_for_migration",
    "what_was_employment_status", "what_was_main_occupation", 
    "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training","occupations_code_18",
    "Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean2009_2010 = data_clean2009_2010.rename(columns=dict(zip(data_clean2009_2010.columns, columns_of_interest2)))

#%% add year 
data_clean2009_2010['year'] = 2010


#%%
data2008_2009 = pd.read_csv('LFS2008-09.csv', sep=',')


#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['Sec7_7.2'] in [1, 2, 5, 6, 7]:
        return row['Sec7_7.3'] * 52
    elif row['Sec7_7.2'] in [3, 4]:
        return row['Sec7_7.4'] * 12
  #  elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] == 'Annually':
  #      return row['Earnings']

# Apply conversion
data2008_2009['Annual_Earnings'] = data2008_2009.apply(convert_to_annual, axis=1)

#%%

# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['Sec5_5.9'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2008_2009['occupations_code_18'] = data2008_2009.apply(determine_occupation, axis=1)


#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['Sec5_5.10'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2008_2009['Industry'] = data2008_2009.apply(determine_industry, axis=1)
#%%

data2008_2009['TrainVar'] = 0
#%%
# Set 'TrainVar' to 1 where 'S04C11' is between 10 and 20 inclusive
data2008_2009.loc[data2008_2009['Sec4_4.11'].between(10, 20), 'TrainVar'] = 1

# Set 'TrainVar' to 2 where 'S04C11' is exactly 21
data2008_2009.loc[data2008_2009['Sec4_4.11'] == 21, 'TrainVar'] = 2

#%%
columns_of_interest =  ["PrCode","HhSno","RespSex","RespRel",
                        "Sec4_4.5","Sec4_4.6","Sec4_4.7","Sec4_4.8",
                        "Sec4_4.9",
                        "Sec4_4.15", "Sec4_4.16", "Sec4_4.17", "Sec4_4.18",
                       "Sec5_5.8","Sec5_5.9","Sec5_5.17.1","Annual_Earnings","Sec5_5.11","TrainVar",
                       "occupations_code_18","Industry"]
#%%
data_clean2008_2009 = data2008_2009.loc[:, columns_of_interest]
#%% rename 
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level", 
    "how_long_has_been_living_in_this_district",
    "previous_district_of_residence_before_moving_here",
    "previous_residence_was_located_in_urban_rural",
    "main_reason_for_migration",
    "what_was_employment_status", "what_was_main_occupation", "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean2008_2009 = data_clean2008_2009.rename(columns=dict(zip(data_clean2008_2009.columns, columns_of_interest2)))

#%% add year 
data_clean2008_2009['year'] = 2009




#%%
data2007_2008 = pd.read_csv('LFS2007-08.csv', sep=',')

#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['Sec7_7.2'] in [1, 2, 5, 6, 7]:
        return row['Sec7_7.3'] * 52
    elif row['Sec7_7.2'] in [3, 4]:
        return row['Sec7_7.4'] * 12
  #  elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] == 'Annually':
  #      return row['Earnings']

# Apply conversion
data2007_2008['Annual_Earnings'] = data2007_2008.apply(convert_to_annual, axis=1)

#%%

# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['Sec5_5.9'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2007_2008['occupations_code_18'] = data2007_2008.apply(determine_occupation, axis=1)

#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['Sec5_5.10'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2007_2008['Industry'] = data2007_2008.apply(determine_industry, axis=1)
#%%

#%%
data2007_2008['TrainVar'] = 0
#%%
# Set 'TrainVar' to 1 where 'S04C11' is between 10 and 20 inclusive
data2007_2008.loc[data2007_2008['Sec4_4.11'].between(10, 20), 'TrainVar'] = 1

# Set 'TrainVar' to 2 where 'S04C11' is exactly 21
data2007_2008.loc[data2007_2008['Sec4_4.11'] == 21, 'TrainVar'] = 2


#%%
columns_of_interest =  ["PrCode","HhSno","RespSex","RespRel",
                        "Sec4_4.5","Sec4_4.6","Sec4_4.7","Sec4_4.8",
                        "Sec4_4.9",  
                        "Sec4_4.15", "Sec4_4.16", "Sec4_4.17", "Sec4_4.18",
                       "Sec5_5.8","Sec5_5.9","Sec5_5.17.1","Annual_Earnings",
                       "Sec5_5.11","TrainVar",
                       "occupations_code_18","Industry"]
#%%
data_clean2007_2008 = data2007_2008.loc[:, columns_of_interest]
#%% rename 
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1", 
    "education_level", 
    "how_long_has_been_living_in_this_district",
    "previous_district_of_residence_before_moving_here",
    "previous_residence_was_located_in_urban_rural",
    "main_reason_for_migration",
    "what_was_employment_status", "what_was_main_occupation", "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean2007_2008 = data_clean2007_2008.rename(columns=dict(zip(data_clean2007_2008.columns, columns_of_interest2)))

#%% add year 
data_clean2007_2008['year'] = 2008



#%%
data2006_2007 = pd.read_csv('LFS2006-07.csv', sep=',')

#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['SECTION_7.7.1'] in [1, 2, 5, 6, 7]:
        return row['SECTION_7.7.2'] * 52
    elif row['SECTION_7.7.1'] in [3, 4]:
        return row['SECTION_7.7.3'] * 12
  #  elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] == 'Annually':
  #      return row['Earnings']

# Apply conversion
data2006_2007['Annual_Earnings'] = data2006_2007.apply(convert_to_annual, axis=1)


#%%

# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['SECTION_5.5.9'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2006_2007['occupations_code_18'] = data2006_2007.apply(determine_occupation, axis=1)

#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['SECTION_5.5.10'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2006_2007['Industry'] = data2006_2007.apply(determine_industry, axis=1)
#%%

#%%
data2006_2007['TrainVar'] = 0
#%%
# Set 'TrainVar' to 1 where 'S04C11' is between 10 and 20 inclusive
data2006_2007.loc[data2006_2007['SECTION_4.4.11']==1, 'TrainVar'] = 1

# Set 'TrainVar' to 2 where 'S04C11' is exactly 21
data2006_2007.loc[data2006_2007['SECTION_4.4.11'].between(3, 4), 'TrainVar'] = 2



#%%
columns_of_interest = ["PROCESS_CODE","HOUSEHOLD_SNO","RESPONDENT_SEX","RESPONDENT_REL",
                       "SECTION_4.4.5","SECTION_4.4.6","SECTION_4.4.7", "SECTION_4.4.8",
                       "SECTION_4.4.9", 
                       "SECTION_4.4.14", "SECTION_4.4.15", "SECTION_4.4.16","SECTION_4.4.17"
                       ,"SECTION_5.5.8","SECTION_5.5.9",
                       "SECTION_5.5.25.1","Annual_Earnings","SECTION_5.5.11","TrainVar",
                       "occupations_code_18","Industry"]
#%%
data_clean2006_2007 = data2006_2007.loc[:, columns_of_interest]
#%%
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level", 
    "how_long_has_been_living_in_this_district",
    "previous_district_of_residence_before_moving_here",
    "previous_residence_was_located_in_urban_rural",
    "main_reason_for_migration",
    "what_was_employment_status", "what_was_main_occupation", "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean2006_2007 = data_clean2006_2007.rename(columns=dict(zip(data_clean2006_2007.columns, columns_of_interest2)))


#%% add year 
data_clean2006_2007['year'] = 2007


#%%
data2005_2006 = pd.read_csv('LFS2005-06.csv', sep=',')


#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['SECTION_7.7.1'] in [1, 2, 5, 6, 7]:
        return row['SECTION_7.7.2'] * 52
    elif row['SECTION_7.7.1'] in [3, 4]:
        return row['SECTION_7.7.3'] * 12
  #  elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] == 'Annually':
  #      return row['Earnings']

# Apply conversion
data2005_2006['Annual_Earnings'] = data2005_2006.apply(convert_to_annual, axis=1)

#%%

# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['SECTION_5.5.9'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2005_2006['occupations_code_18'] = data2005_2006.apply(determine_occupation, axis=1)

#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['SECTION_5.5.10'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2005_2006['Industry'] = data2005_2006.apply(determine_industry, axis=1)
#%%

#%%
columns_of_interest = ["PROCESS_CODE","HOUSEHOLD_SNO","RESPONDENT_SEX","RESPONDENT_REL",
                       "SECTION_4.4.5","SECTION_4.4.6","SECTION_4.4.7","SECTION_4.4.8",
                       "SECTION_4.4.9", 
                       "SECTION_4.4.14", "SECTION_4.4.15", "SECTION_4.4.16", "SECTION_4.4.17", 
                       "SECTION_5.5.8","SECTION_5.5.9",
                       "SECTION_5.5.25.1","Annual_Earnings",
                       "SECTION_5.5.11","SECTION_4.4.11",
                       "occupations_code_18","Industry"]
#%%
data_clean2005_2006 = data2005_2006.loc[:, columns_of_interest]
#%% rename 
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level", 
    "how_long_has_been_living_in_this_district",
    "previous_district_of_residence_before_moving_here",
    "previous_residence_was_located_in_urban_rural",
    "main_reason_for_migration",
    "what_was_employment_status", "what_was_main_occupation", "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean2005_2006 = data_clean2005_2006.rename(columns=dict(zip(data_clean2005_2006.columns, columns_of_interest2)))


#%% add year 
data_clean2005_2006['year'] = 2006


#%%  LFS2003-04
data2003_2004 = pd.read_csv('LFS2003-04.csv', sep=',')

#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['Sec7Q23'] in [1, 2, 5, 6, 7]:
        return row['Sec7Q24'] * 52
    elif row['Sec7Q23'] in [3, 4]:
        return row['Sec7Q25'] * 12
  #  elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] == 'Annually':
  #      return row['Earnings']

# Apply conversion
data2003_2004['Annual_Earnings'] = data2003_2004.apply(convert_to_annual, axis=1)


#%%

# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['Sec5Q07'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2003_2004['occupations_code_18'] = data2003_2004.apply(determine_occupation, axis=1)

#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['Sec5Q08'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2003_2004['Industry'] = data2003_2004.apply(determine_industry, axis=1)
#%%

#%%
columns_of_interest = ["ProcessingCod","HHoldSrNo","RespondentSex","RespondentRelat",
                       "Sec4Q05","Sec4Q06","Sec4Q07","Sec4Q08",
                       "Sec4Q09",
                       "Sec4Q13","Sec4Q14", "Sec4Q15", "Sec4Q16",
                       "Sec5Q09", "Sec5Q07",   
                       "Sec5Q19Tot","Annual_Earnings","Sec5Q10","Sec4Q11",
                       "occupations_code_18","Industry"]

#%%
data_clean2003_2004 = data2003_2004.loc[:, columns_of_interest]


#%% rename 
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level", 
    "how_long_has_been_living_in_this_district",
    "previous_district_of_residence_before_moving_here",
    "previous_residence_was_located_in_urban_rural",
    "main_reason_for_migration",
    "what_was_employment_status" , "what_was_main_occupation",
    "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
data_clean2003_2004 = data_clean2003_2004.rename(columns=dict(zip(data_clean2003_2004.columns, columns_of_interest2)))

#%% add year 
data_clean2003_2004['year'] = 2004


#%%
data2001_2002 = pd.read_csv('LFS2001-02.csv', sep=',')

#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['Sec7Q23'] in [1, 2, 5, 6, 7]:
        return row['Sec7Q24'] * 52
    elif row['Sec7Q23'] in [3, 4]:
        return row['Sec7Q25'] * 12
  #  elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] == 'Annually':
  #      return row['Earnings']

# Apply conversion
data2001_2002['Annual_Earnings'] = data2001_2002.apply(convert_to_annual, axis=1)


#%%

# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['Sec5Q07'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2001_2002['occupations_code_18'] = data2001_2002.apply(determine_occupation, axis=1)


#%%

def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['Sec5Q08'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data2001_2002['Industry'] = data2001_2002.apply(determine_industry, axis=1)
#%%

#%%
columns_of_interest = ["ProcessingCod","HHoldSrNo","RespondentSex","RespondentRelat",
                       "Sec4Q05","Sec4Q06","Sec4Q07","Sec4Q08",
                       "Sec4Q09",
                       "Sec4Q13","Sec4Q14", "Sec4Q15", "Sec4Q16",
                       "Sec5Q09","Sec5Q07",
                       "Sec5Q19Tot","Annual_Earnings","Sec5Q10","Sec4Q11",
                       "occupations_code_18","Industry"]
#%%
data_clean2001_2002 = data2001_2002.loc[:, columns_of_interest]



#%%

columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level", 
    "how_long_has_been_living_in_this_district",
    "previous_district_of_residence_before_moving_here",
    "previous_residence_was_located_in_urban_rural",
    "main_reason_for_migration",
    "what_was_employment_status", "what_was_main_occupation",  
    "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean2001_2002 = data_clean2001_2002.rename(columns=dict(zip(data_clean2001_2002.columns, columns_of_interest2)))

#%% add year 
data_clean2001_2002['year'] = 2002


#%%
data1999_2000 = pd.read_csv('LFS1999-00.csv', sep=',')

#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['Sec07Q22'] in [1, 2, 5, 6, 7]:
        return row['Sec07Q23'] * 52
    elif row['Sec07Q22'] in [3, 4]:
        return row['Sec07Q24'] * 12
  #  elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] == 'Annually':
  #      return row['Earnings']

# Apply conversion
data1999_2000['Annual_Earnings'] = data1999_2000.apply(convert_to_annual, axis=1)


#%%

# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['Sec5Q07'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1999_2000['occupations_code_18'] = data1999_2000.apply(determine_occupation, axis=1)

#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['Sec5Q08'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1999_2000['Industry'] = data1999_2000.apply(determine_industry, axis=1)
#%%


#%%
columns_of_interest = ["ProcCode","HHoldSrNO","RespondSex","RespondRel",
                       "Sex", "Age","MaritalStat","Literacy",
                       "EducationLvl",
                       "Migration","PreviousDistt","PreviousResid","MainReason",
                       "Sec5Q09","Sec5Q07",
                       "Sec5Q18T","Annual_Earnings","Sec5Q10","TechTraining",
                       "occupations_code_18","Industry"]
#%%
data_clean1999_2000 = data1999_2000.loc[:, columns_of_interest]

#%%
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level", 
    "how_long_has_been_living_in_this_district",
    "previous_district_of_residence_before_moving_here",
    "previous_residence_was_located_in_urban_rural",
    "main_reason_for_migration",
    "what_was_employment_status","what_was_main_occupation",
    "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean1999_2000 = data_clean1999_2000.rename(columns=dict(zip(data_clean1999_2000.columns, columns_of_interest2)))



#%% add year 
data_clean1999_2000['year'] = 2000



#%%
data1997_1998 = pd.read_csv('LFS1997-98.csv', sep=',')

#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['Sec07Q22'] in [1, 2, 5, 6, 7]:
        return row['Sec07Q23'] * 52
    elif row['Sec07Q22'] in [3, 4]:
        return row['Sec07Q24'] * 12
  #  elif row['at_main_work_waht_is_the_periodicity_of_paymentk'] == 'Annually':
  #      return row['Earnings']

# Apply conversion
data1997_1998['Annual_Earnings'] = data1997_1998.apply(convert_to_annual, axis=1)


#%%

# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['Sec5Q07'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1997_1998['occupations_code_18'] = data1997_1998.apply(determine_occupation, axis=1)

#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['Sec5Q08'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1997_1998['Industry'] = data1997_1998.apply(determine_industry, axis=1)
#%%


#%%
columns_of_interest = ["ProcCode","HHoldSrNO","RespondSex","RespondRel",
                       "Sex", "Age","MaritalStat","Literacy",
                       "EducationLvl",
                       "Migration", "PreviousDistt","PreviousResid","MainReason",
                       "Sec5Q09","Sec5Q07",
                       "Sec5Q18T","Annual_Earnings","Sec5Q10",
                       "TechTraining","occupations_code_18","Industry"]
#%%
data_clean1997_1998 = data1997_1998.loc[:, columns_of_interest]

#%% rename
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level", 
    "how_long_has_been_living_in_this_district",
    "previous_district_of_residence_before_moving_here",
    "previous_residence_was_located_in_urban_rural",
    "main_reason_for_migration",
    "what_was_employment_status",  "what_was_main_occupation",
    "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean1997_1998 = data_clean1997_1998.rename(columns=dict(zip(data_clean1997_1998.columns, columns_of_interest2)))

#%% add year 
data_clean1997_1998['year'] = 1998


#%%
data1996_1997 = pd.read_csv('LFS1996-97.csv', sep=',')


#%%
# Function to convert earnings to annual
#def convert_to_annual(row):
#    if row['Sec07Q22'] in [1, 2, 5, 6, 7]:
#        return row['Sec07Q23'] * 52
#    elif row['Sec07Q22'] in [3, 4]:
#        return row['Sec07Q24'] * 12

def convert_to_annual(row):
    if row['Sec07Q22'] in [1, 2, 5, 6, 7]:
        return row['Sec07Q23'] * 52 
    elif row['Sec07Q22'] in [3, 4]:
        return row['Sec07Q24'] * 12 


# Apply conversion
data1996_1997['Annual_Earnings'] = data1996_1997.apply(convert_to_annual, axis=1)
#%%


#%%

# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['Sec5Q07'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1996_1997['occupations_code_18'] = data1996_1997.apply(determine_occupation, axis=1)
#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['Sec5Q08'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1996_1997['Industry'] = data1996_1997.apply(determine_industry, axis=1)
#%%

#%%
columns_of_interest = ["ProcCode","HHoldSrNO","RespondSex","RespondRel",
                       "Sex", "Age","MaritalStat","Literacy",
                       "EducationLvl",
                       "Migration", "PreviousDistt","PreviousResid","MainReason",
                       "Sec5Q09","Sec5Q07",
                       "Sec5Q18T","Annual_Earnings","Sec5Q10","TechTraining",
                       "occupations_code_18","Industry"]
#%%
data_clean1996_1997 = data1996_1997.loc[:, columns_of_interest]

#%% rename
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level", 
    "how_long_has_been_living_in_this_district",
    "previous_district_of_residence_before_moving_here",
    "previous_residence_was_located_in_urban_rural",
    "main_reason_for_migration",
    "what_was_employment_status", "what_was_main_occupation", 
    "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean1996_1997 = data_clean1996_1997.rename(columns=dict(zip(data_clean1996_1997.columns, columns_of_interest2)))


#%% add year 
data_clean1996_1997['year'] = 1997



#%%
#%% Survey 90 95 (similar var)


data1994_1995 = pd.read_csv('LFS1994-95.csv', sep=',')

#%% different here becasue we have a lot of missisng data when infdivdual repiort  
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['Sec07Q18'] in [0]:
        return row['Sec07Q19'] * 12
    elif row['Sec07Q19'] in [0]:
        return row['Sec07Q18'] * 52


# Apply conversion
data1994_1995['Annual_Earnings'] = data1994_1995.apply(convert_to_annual, axis=1)

#%%

#%%   occupation check (again), an industry code

# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['Sec5Q08'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1994_1995['occupations_code_18'] = data1994_1995.apply(determine_occupation, axis=1)

#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['Sec5Q09'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1994_1995['Industry'] = data1994_1995.apply(determine_industry, axis=1)
#%%



#%%
columns_of_interest = ["ProcCode","HHSerialNo","RespondSex","RespondRel",
                       "Sex","Age","MaritalStat","Literacy",
                       "EducationLvl",
                       "Sec5Q10","Sec5Q08","Sec06Q13","Annual_Earnings","Sec5Q11","TechTraining",
                       "occupations_code_18","Industry"]
#%%
data_clean1994_1995 = data1994_1995.loc[:, columns_of_interest]

#%% rename
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level", 
    "what_was_employment_status", "what_was_main_occupation", "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean1994_1995 = data_clean1994_1995.rename(columns=dict(zip(data_clean1994_1995.columns, columns_of_interest2)))

#%% add year 
data_clean1994_1995['year'] = 1995


#%%
data1993_1994 = pd.read_csv('LFS1993-94.csv', sep=',')

#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['Sec07Q18'] in [0]:
        return row['Sec07Q19'] * 12
    elif row['Sec07Q19'] in [0]:
        return row['Sec07Q18'] * 52
    if row['Sec07Q18'] == 0 and row['Sec07Q19'] == 0:
        return row['Sec07Q20'] 

# Apply conversion
data1993_1994['Annual_Earnings'] = data1993_1994.apply(convert_to_annual, axis=1)


#%%
#%%   occupation check (again), an industry code

# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['Sec5Q08'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1993_1994['occupations_code_18'] = data1993_1994.apply(determine_occupation, axis=1)
#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['Sec5Q09'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1993_1994['Industry'] = data1993_1994.apply(determine_industry, axis=1)
#%%

#%%
columns_of_interest = ["ProcCode","HHSerialNo","RespondSex","RespondRel",
                       "Sex","Age","MaritalStat","Literacy",
                       "EducationLvl",
                       "Sec5Q10","Sec5Q08","Sec06Q13","Annual_Earnings","Sec5Q11","TechTraining",
                       "occupations_code_18","Industry"]
#%%
data_clean1993_1994 = data1993_1994.loc[:, columns_of_interest]

#%% rename
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level", 
    "what_was_employment_status", "what_was_main_occupation", "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean1993_1994 = data_clean1993_1994.rename(columns=dict(zip(data_clean1993_1994.columns, columns_of_interest2)))

#%% add year 
data_clean1993_1994['year'] = 1994


#%%
data1992_1993 = pd.read_csv('LFS1992-93.csv', sep=',')

#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['Sec07Q18'] in [0]:
        return row['Sec07Q19'] * 12
    elif row['Sec07Q19'] in [0]:
        return row['Sec07Q18'] * 52
    if row['Sec07Q18'] == 0 and row['Sec07Q19'] == 0:
        return row['Sec07Q20'] 

# Apply conversion
data1992_1993['Annual_Earnings'] = data1992_1993.apply(convert_to_annual, axis=1)

#%%


# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['Sec5Q08'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1992_1993['occupations_code_18'] = data1992_1993.apply(determine_occupation, axis=1)
#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['Sec5Q09'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1992_1993['Industry'] = data1992_1993.apply(determine_industry, axis=1)
#%%

#%%
columns_of_interest = ["ProcCode","HHSerialNo","RespondSex","RespondRel",
                       "Sex","Age","MaritalStat","Literacy",
                       "EducationLvl",
                       "Sec5Q10","Sec5Q08",
                       "Sec06Q13","Annual_Earnings","Sec5Q11","TechTraining",
                       "occupations_code_18","Industry"]
#%%
data_clean1992_1993 = data1992_1993.loc[:, columns_of_interest]
#%% rename
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level", 
    "what_was_employment_status", "what_was_main_occupation", "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean1992_1993 = data_clean1992_1993.rename(columns=dict(zip(data_clean1992_1993.columns, columns_of_interest2)))


#%% add year 
data_clean1992_1993['year'] = 1993


#%%
data1991_1992 = pd.read_csv('LFS1991-92.csv', sep=',')



#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['Sec07Q18'] in [0]:
        return row['Sec07Q19'] * 12
    elif row['Sec07Q19'] in [0]:
        return row['Sec07Q18'] * 52
    if row['Sec07Q18'] == 0 and row['Sec07Q19'] == 0:
        return row['Sec07Q20'] 

# Apply conversion
data1991_1992['Annual_Earnings'] = data1991_1992.apply(convert_to_annual, axis=1)

#%%


# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['Sec5Q08'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1991_1992['occupations_code_18'] = data1991_1992.apply(determine_occupation, axis=1)
#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['Sec5Q09'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1991_1992['Industry'] = data1991_1992.apply(determine_industry, axis=1)
#%%

#%%
columns_of_interest = ["ProcCode","HHSerialNo","RespondSex","RespondRel",
                       "Sex","Age","MaritalStat","Literacy",
                       "EducationLvl",
                       "Sec5Q10","Sec5Q08",
                       "Sec06Q13","Annual_Earnings","Sec5Q11","TechTraining",
                       "occupations_code_18","Industry"]
#%%
data_clean1991_1992 = data1991_1992.loc[:, columns_of_interest]
#%% rename
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level", 
    "what_was_employment_status", "what_was_main_occupation", "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean1991_1992 = data_clean1991_1992.rename(columns=dict(zip(data_clean1991_1992.columns, columns_of_interest2)))

#%% add year 
data_clean1991_1992['year'] = 1992


#%%
data1990_1991 = pd.read_csv('LFS1990-91.csv', sep=',')

#%%
# Function to convert earnings to annual
def convert_to_annual(row):
    if row['Sec07Q18'] in [0]:
        return row['Sec07Q19'] * 12
    elif row['Sec07Q19'] in [0]:
        return row['Sec07Q18'] * 52
    if row['Sec07Q18'] == 0 and row['Sec07Q19'] == 0:
        return row['Sec07Q20'] 

# Apply conversion
data1990_1991['Annual_Earnings'] = data1990_1991.apply(convert_to_annual, axis=1)

#%%

# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['Sec5Q08'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1990_1991['occupations_code_18'] = data1990_1991.apply(determine_occupation, axis=1)

#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['Sec5Q09'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1990_1991['Industry'] = data1990_1991.apply(determine_industry, axis=1)
#%%

#%%
columns_of_interest = ["ProcCode","HHSerialNo","RespondSex","RespondRel",
                       "Sex","Age","MaritalStat","Literacy",
                       "EducationLvl",
                       "Sec5Q10","Sec5Q08",
                       "Sec06Q13","Annual_Earnings","Sec5Q11","TechTraining",
                       "occupations_code_18","Industry"]
#%%
data_clean1990_1991 = data1990_1991.loc[:, columns_of_interest]

#%% rename
columns_of_interest2 = [
    "processing_code", "household_number", "respondents_sex",
    "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level", 
    "what_was_employment_status", "what_was_main_occupation", 
    "total_hours",
    "Annual_Earnings","what_kind_of_enterprise",
    "ever_completed_any_technical_vocational_training",
    "occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean1990_1991 = data_clean1990_1991.rename(columns=dict(zip(data_clean1990_1991.columns, columns_of_interest2)))


#%% add year 
data_clean1990_1991['year'] = 1991



#%% Survey 80s (similar var)  - not comparabe to early waves
#%%


data1987_1988 = pd.read_csv('LFS1987-88.csv', sep=',')


#%%


data1987_1988['Annual_Earnings']  = data1987_1988['WorkIncome']



#%%

# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['NatuOccup'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1987_1988['occupations_code_18'] = data1987_1988.apply(determine_occupation, axis=1)

#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['NatuIndus'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1987_1988['Industry'] = data1987_1988.apply(determine_industry, axis=1)
#%%


#%%
columns_of_interest = ["PrCode","PersonNo","PsStatus",
                       "Sex","Age","MaritalStat","Literacy",
                       "EduLevel",
                       "Occupation","EmpStatus","TotHourWrk","Annual_Earnings","Agriculture",
                       "occupations_code_18","Industry"]
#%%
data_clean1987_1988 = data1987_1988.loc[:, columns_of_interest]

#%% rename
columns_of_interest2 = ["processing_code", "household_number",
                        "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level",  
    "what_was_main_occupation", "what_was_employment_status", 
    "total_hours",
    "Annual_Earnings","what_kind_of_enterprise","occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean1987_1988 = data_clean1987_1988.rename(columns=dict(zip(data_clean1987_1988.columns, columns_of_interest2)))

#%% add year 
data_clean1987_1988['year'] = 1988

#%%
data1986_1987 = pd.read_csv('LFS1986-87.csv', sep=',')

data1986_1987['Annual_Earnings']  = data1986_1987['WorkIncome']


#%%

# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['NatuOccup'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1986_1987['occupations_code_18'] = data1986_1987.apply(determine_occupation, axis=1)


#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['NatuIndus'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1986_1987['Industry'] = data1986_1987.apply(determine_industry, axis=1)
#%%

#%%
columns_of_interest = ["PrCode","PersonNo","PsStatus",
                       "Sex","Age","MaritalStat","Literacy","EduLevel",
                       "Occupation","EmpStatus","TotHourWrk","Annual_Earnings","Agriculture",
                       "occupations_code_18","Industry"]
#%%
data_clean1986_1987 = data1986_1987.loc[:, columns_of_interest]
#%% rename
columns_of_interest2 = ["processing_code",  "household_number", 
                        "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level",  "what_was_main_occupation", "what_was_employment_status", 
    "total_hours",
    "Annual_Earnings","what_kind_of_enterprise","occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean1986_1987 = data_clean1986_1987.rename(columns=dict(zip(data_clean1986_1987.columns, columns_of_interest2)))

#%% add year 
data_clean1986_1987['year'] = 1987


#%%
data1985_1986 = pd.read_csv('LFS1985-86.csv', sep=',')

data1985_1986['Annual_Earnings']  = data1985_1986['WorkIncome']


#%%

# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['NatuOccup'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1985_1986['occupations_code_18'] = data1985_1986.apply(determine_occupation, axis=1)


#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['NatuIndus'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1985_1986['Industry'] = data1985_1986.apply(determine_industry, axis=1)

#%%
columns_of_interest = ["PrCode","PersonNo","PsStatus",
                       "Sex","Age","MaritalStat","Literacy","EduLevel",
                       "Occupation","EmpStatus","TotHourWrk","Annual_Earnings","Agriculture",
                       "occupations_code_18","Industry"]
#%%
data_clean1985_1986 = data1985_1986.loc[:, columns_of_interest]

#%% rename
columns_of_interest2 = ["processing_code", "household_number",
                        "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level",  "what_was_main_occupation", "what_was_employment_status", 
    "total_hours",
    "Annual_Earnings","what_kind_of_enterprise","occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean1985_1986 = data_clean1985_1986.rename(columns=dict(zip(data_clean1985_1986.columns, columns_of_interest2)))

#%% add year 
data_clean1985_1986['year'] = 1986


#%%
data1984_1985 = pd.read_csv('LFS1984-85.csv', sep=',')

data1984_1985['Annual_Earnings']  = data1984_1985['WorkIncome']


#%%

# Function to determine the occupation category based on S5C8 value
def determine_occupation(row):
    try:
        # Convert the value to an integer
        occupation_code = int(row['NatuOccup'])
        
        if 1 <= occupation_code <= 10 or 11 <= occupation_code <= 14 or 21 <= occupation_code <= 26:
            return 1
        elif 31 <= occupation_code <= 35:
            return 2
        elif 41 <= occupation_code <= 44:
            return 3
        elif 51 <= occupation_code <= 54:
            return 4
        elif 61 <= occupation_code <= 63:
            return 5
        elif 71 <= occupation_code <= 75:
            return 6
        elif 81 <= occupation_code <= 83:
            return 7
        elif 91 <= occupation_code <= 96:
            return 8
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1984_1985['occupations_code_18'] = data1984_1985.apply(determine_occupation, axis=1)


#%%
def determine_industry(row):
    try:
        # Convert the value to an integer
        industry_code = int(row['NatuIndus'])
        
        if 1 <= industry_code <= 3:
            return 1  # Agriculture, forestry and fishing
        elif 10 <= industry_code <= 33:
            return 2  # Manufacturing
        elif 41 <= industry_code <= 43:
            return 3  # Construction
        elif 45 <= industry_code <= 68:
            return 4  # Services
        elif (5 <= industry_code <= 9) or \
             (69 <= industry_code <= 99) or \
             (35 <= industry_code <= 39):
            return 5  # Others (including Mining and quarrying)
        else:
            return np.nan  # Return NaN if the value does not match any range
    except ValueError:
        return np.nan  # Return NaN if the conversion to integer fails

# Apply the function to the DataFrame
data1984_1985['Industry'] = data1984_1985.apply(determine_industry, axis=1)
#%%
columns_of_interest = ["PrCode","PersonNo","PsStatus",
                       "Sex","Age","MaritalStat","Literacy","EduLevel",
                       "Occupation","EmpStatus","TotHourWrk","Annual_Earnings","Agriculture",
                       "occupations_code_18","Industry"]
#%%
data_clean1984_1985 = data1984_1985.loc[:, columns_of_interest]

#%% rename
columns_of_interest2 = ["processing_code",
            "household_number",  "persons_relationship_to_head_of_the_household",
     "sex_of_person","age_at_last_birthday","current_marital_status", "literacy_1",
    "education_level",  "what_was_main_occupation", "what_was_employment_status", 
    "total_hours",
    "Annual_Earnings","what_kind_of_enterprise","occupations_code_18","Industry"
    #"province", "distric_with_label", "region", 
    ]
#%%
# Rename columns for data_clean2018_2019
data_clean1984_1985 = data_clean1984_1985.rename(columns=dict(zip(data_clean1984_1985.columns, columns_of_interest2)))
#%% add year 
data_clean1984_1985['year'] = 1985

#%%  merging data


# Define mapping dictionary
sex_mapping = {"Male": 1, "Female": 2}

# Replace values in the 'sex_of_person' column
data_clean2020_2021['sex_of_person'] = data_clean2020_2021['sex_of_person'].replace(sex_mapping)
data_clean2020_2021['sex_of_person'] = data_clean2020_2021['sex_of_person'].replace(sex_mapping)

# Replace values in the 'sex_of_person' column
data_clean2017_2018['sex_of_person'] = data_clean2017_2018['sex_of_person'].replace(sex_mapping)
data_clean2017_2018['sex_of_person'] = data_clean2017_2018['sex_of_person'].replace(sex_mapping)


# Replace values in the 'sex_of_person' column
data_clean2005_2006['sex_of_person'] = data_clean2005_2006['sex_of_person'].replace(sex_mapping)
data_clean2005_2006['sex_of_person'] = data_clean2005_2006['sex_of_person'].replace(sex_mapping)

#%%
data_clean2020_2021['what_was_main_occupation'] = data_clean2020_2021['what_was_main_occupation'].str.strip()

data_clean2020_2021['what_was_main_occupation'] = data_clean2020_2021['what_was_main_occupation'].replace('', np.nan)
#%%
#data_clean2020_2021['occupations_code_18'] = data_clean2020_2021['occupations_code_18'].str.strip()

#data_clean2020_2021['occupations_code_18'] = data_clean2020_2021['occupations_code_18'].replace('', np.nan)

#%%
data_clean2020_2021['what_was_main_occupation'] = data_clean2020_2021['what_was_main_occupation'].astype(float)
data_clean2020_2021['occupations_code_18'] = data_clean2020_2021['occupations_code_18'].astype(float)

#%%
data_clean2020_2021['previous_district_of_residence_before_moving_here'] = data_clean2020_2021['previous_district_of_residence_before_moving_here'].replace(' ', np.nan)

data_clean2020_2021['previous_district_of_residence_before_moving_here'] = data_clean2020_2021['previous_district_of_residence_before_moving_here'].astype(float)

#%%


# Replace values in the respondents_sex column
data_clean2005_2006['respondents_sex'] = data_clean2005_2006['respondents_sex'].replace(sex_mapping)
data_clean2005_2006['respondents_sex'] = data_clean2005_2006['respondents_sex'].replace(sex_mapping)
#%%
# Define mapping dictionary
edu_mapping = {"No formal education": 1, "Nursery but below K.G":2, "K.G but below primary" :3, "Primary but below middle":4,
               "Middle but below metric":5,
"Matric but below inter":6, "Inter but below degree":7, "Degree in engineering":8, "Degree in medicine":9,
"Degree in computer":10, "Degree in agriculture":11, "Degree in other subject":12,
"M/A M.Sc":13, "M.Phil/Ph.D":14}

# Replace values in the 'sex_of_person' column
data_clean2005_2006['education_level'] = data_clean2005_2006['education_level'].replace(edu_mapping)
data_clean2005_2006['education_level'] = data_clean2005_2006['education_level'].replace(edu_mapping)
#%%




merged_data1 = pd.merge(data_clean2018_2019, data_clean2020_2021, how='outer', on=[
"processing_code","household_number",
"respondents_sex",
"persons_relationship_to_head_of_the_household",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])


#13. Respondent’s Sex 1=Male 
# 2=Female

#%%



merged_data2 = pd.merge(data_clean2017_2018, merged_data1, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])


#%%





merged_data3 = pd.merge(data_clean2014_2015, merged_data2, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"])




#%%



merged_data4 = pd.merge(data_clean2013_2014, merged_data3, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])


#%%


merged_data5 = pd.merge(data_clean2012_2013, merged_data4, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])


#%%



merged_data6 = pd.merge(data_clean2010_2011, merged_data5, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])

#%%


#%%



merged_data7 = pd.merge(data_clean2009_2010, merged_data6, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])

#%%

#%%



merged_data8 = pd.merge(data_clean2008_2009, merged_data7, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])



#%%



merged_data9 = pd.merge(data_clean2007_2008, merged_data8, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])



#%%



merged_data10 = pd.merge(data_clean2006_2007, merged_data9, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])


#%%



merged_data11 = pd.merge(data_clean2005_2006, merged_data10, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])


#%%






merged_data12 = pd.merge(data_clean2003_2004, merged_data11, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])



#%%



#%%






merged_data13 = pd.merge(data_clean2001_2002, merged_data12, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])

#%%



#%%






merged_data14 = pd.merge(data_clean1999_2000, merged_data13, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])



#%%



#%%






merged_data15 = pd.merge(data_clean1997_1998, merged_data14, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])



#%%


#%%






merged_data16 = pd.merge(data_clean1996_1997, merged_data15, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
"how_long_has_been_living_in_this_district",
"previous_district_of_residence_before_moving_here",
"previous_residence_was_located_in_urban_rural",
"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])

#%%


#%%






merged_data17 = pd.merge(data_clean1994_1995, merged_data16, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
#"how_long_has_been_living_in_this_district",
#"previous_district_of_residence_before_moving_here",
#"previous_residence_was_located_in_urban_rural",
#"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])


#%%




merged_data18 = pd.merge(data_clean1993_1994, merged_data17, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
#"how_long_has_been_living_in_this_district",
#"previous_district_of_residence_before_moving_here",
#"previous_residence_was_located_in_urban_rural",
#"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])

#%%





merged_data19 = pd.merge(data_clean1992_1993, merged_data18, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
#"how_long_has_been_living_in_this_district",
#"previous_district_of_residence_before_moving_here",
#"previous_residence_was_located_in_urban_rural",
#"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])


#%%




merged_data20 = pd.merge(data_clean1991_1992, merged_data19, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
#"how_long_has_been_living_in_this_district",
#"previous_district_of_residence_before_moving_here",
#"previous_residence_was_located_in_urban_rural",
#"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])




#%%



merged_data21 = pd.merge(data_clean1990_1991, merged_data20, how='outer', on=[
"processing_code","household_number",
"persons_relationship_to_head_of_the_household",
"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
#"how_long_has_been_living_in_this_district",
#"previous_district_of_residence_before_moving_here",
#"previous_residence_was_located_in_urban_rural",
#"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise","ever_completed_any_technical_vocational_training",
"occupations_code_18","Industry"
])


#%%


#%%



merged_data22 = pd.merge(data_clean1987_1988, merged_data21, how='outer', on=[
"processing_code",
"household_number",
"persons_relationship_to_head_of_the_household",
#"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
#"how_long_has_been_living_in_this_district",
#previous_district_of_residence_before_moving_here",
#"previous_residence_was_located_in_urban_rural",
#"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise",
#,"ever_completed_any_technical_vocational_training"
"occupations_code_18","Industry"
])



#%%




merged_data23 = pd.merge(data_clean1986_1987, merged_data21, how='outer', on=[
"processing_code",
"household_number",
"persons_relationship_to_head_of_the_household",
#"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
#"how_long_has_been_living_in_this_district",
#"previous_district_of_residence_before_moving_here",
#"previous_residence_was_located_in_urban_rural",
#"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise",
#,"ever_completed_any_technical_vocational_training"
"occupations_code_18","Industry"
])


#%%




merged_data24 = pd.merge(data_clean1986_1987, merged_data21, how='outer', on=[
"processing_code",
"household_number",
"persons_relationship_to_head_of_the_household",
#"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
#"how_long_has_been_living_in_this_district",
#"previous_district_of_residence_before_moving_here",
#"previous_residence_was_located_in_urban_rural",
#"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise",
#,"ever_completed_any_technical_vocational_training"
"occupations_code_18","Industry"
])


#%%



merged_data25 = pd.merge(data_clean1985_1986, merged_data24, how='outer', on=[
"processing_code",
"household_number",
"persons_relationship_to_head_of_the_household",
#"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
#"how_long_has_been_living_in_this_district",
#"previous_district_of_residence_before_moving_here",
#"previous_residence_was_located_in_urban_rural",
#"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise",
#,"ever_completed_any_technical_vocational_training"
"occupations_code_18","Industry"
])


#%%




merged_data26 = pd.merge(data_clean1984_1985, merged_data25, how='outer', on=[
"processing_code",
"household_number",
"persons_relationship_to_head_of_the_household",
#"respondents_sex",
"sex_of_person",	
"education_level","what_was_employment_status","what_was_main_occupation","total_hours",
#"province","distric_with_label","region",
"age_at_last_birthday",
"current_marital_status",
"literacy_1",
#"literacy_2",
#"how_long_has_been_living_in_this_district",
#"previous_district_of_residence_before_moving_here",
#"previous_residence_was_located_in_urban_rural",
#"main_reason_for_migration",
"Annual_Earnings","year","what_kind_of_enterprise",
#,"ever_completed_any_technical_vocational_training"
"occupations_code_18","Industry"
])


#%% need to fix the education level (conatins some wrong enteres for the years 2011, 2013, 2008)
# specifically 92, 61, 34

# Define the values to drop
values_to_drop = [92, 61, 34]

# Drop rows with specified values in the "education_level" column
merged_data26 = merged_data26[~merged_data26['education_level'].isin(values_to_drop)]


#%%  DROP MISSING DATA (in education, literacy, and age category)
# remove nana and zeros from r education literacy and age   column

values_to_drop = [0]

# Drop rows with specified values in the "education_level" column
merged_data26 = merged_data26[~merged_data26['education_level'].isin(values_to_drop)]
merged_data26 = merged_data26[~merged_data26['literacy_1'].isin(values_to_drop)]
merged_data26 = merged_data26[~merged_data26['age_at_last_birthday'].isin(values_to_drop)]
#%%


merged_data26.dropna(subset=["age_at_last_birthday","literacy_1","education_level"],inplace=True)

#%% Education level  grouping

# Create a new column 'edu' with initial value as 0  (0 here means missing data or no response)
merged_data26['edu'] = 0

# Set values based on conditions
merged_data26.loc[merged_data26['education_level'] == 1, 'edu'] = 1  # no  Education
merged_data26.loc[merged_data26['education_level'].isin([2, 3, 4]), 'edu'] = 2  # Primary Education - grade 1,2,3,4
merged_data26.loc[merged_data26['education_level'].isin([5, 6]), 'edu'] = 3  # Secondary Education - 5,6,7,8,9,10,11,12
merged_data26.loc[merged_data26['education_level'] >= 7, 'edu'] = 4  # Tertiary education - more than 12

#%% given eductaion categories I want to crear 4 dummies:
dummy_vars = pd.get_dummies(merged_data26['edu'], prefix='edu').astype(int)
#%% add thes new variables  (edu_0, edu_1  etc)
merged_data26 = pd.concat([merged_data26, dummy_vars], axis=1)
# note that edu_0 are just missing data with nan or no reposne  so it might be useful to drop themm duing the emp. analysis
#%% create a variable - indicator for low level of education or no eduaction 
merged_data26['Lowedu'] = 0

# Set values based on conditions
merged_data26.loc[merged_data26['education_level'].isin([1,2, 3, 4]), 'Lowedu'] = 1  # no  Education and Primary Education - grade 1,2,3,4
merged_data26.loc[merged_data26['education_level'] >= 5, 'Lowedu'] = 2  # Secondary and tertiary Education - 5, 6,7,8,9,10,11,12

#%% given eductaion categories I want to crear 4 dummies:
dummy_vars = pd.get_dummies(merged_data26['Lowedu'], prefix='Lowedu').astype(int)
#%% add thes new variables  (lowedu_0, lowedu_1   etc)
merged_data26 = pd.concat([merged_data26, dummy_vars], axis=1)

#%% age grouping
# Create new variables with initial value as 0
merged_data26['age_category'] = 0

# Set values based on conditions
merged_data26.loc[(merged_data26['age_at_last_birthday'] >= 1) & (merged_data26['age_at_last_birthday'] <= 14), 'age_category'] = 1  # Child
merged_data26.loc[(merged_data26['age_at_last_birthday'] >= 15) & (merged_data26['age_at_last_birthday'] <= 65), 'age_category'] = 2  # Adult
merged_data26.loc[merged_data26['age_at_last_birthday'] >= 66, 'age_category'] = 3  # Elder

#%% creat dummy varibles
# Create dummy variables for 'age_category' and convert to integers
age_category_dummies = pd.get_dummies(merged_data26['age_category'], prefix='age_category').astype(int)
#%% add it tyo the main dataframe
merged_data26 = pd.concat([merged_data26, age_category_dummies], axis=1)
# note that age_category_0 are just missing data or a reposne with 0 so it might be useful to drop themm duing the emp. analysis
#%%  sex grouping

# Set values based on conditions
gender_category_dummies = pd.get_dummies(merged_data26['sex_of_person'], prefix='sex_of_person').astype(int)

merged_data26 = pd.concat([merged_data26, gender_category_dummies], axis=1)
#%% marital status grouing 
marital_category_dummies = pd.get_dummies(merged_data26['current_marital_status'], prefix='current_marital_status').astype(int)

merged_data26 = pd.concat([merged_data26, marital_category_dummies], axis=1)

#%% literacy grouping 

literacy_category_dummies = pd.get_dummies(merged_data26['literacy_1'], prefix='literacy_1').astype(int)

merged_data26 = pd.concat([merged_data26, literacy_category_dummies], axis=1)

#%%  to fix this errors; DtypeWarning: Columns (19,20,21) have mixed types. Specify dtype option on import or set low_memory=False.

# Convert specific columns to float
merged_data26.iloc[:, 19]  = pd.to_numeric(merged_data26.iloc[:, 19], errors='coerce').astype(float)
merged_data26.iloc[:, 20]  = pd.to_numeric(merged_data26.iloc[:, 20], errors='coerce').astype(float)
merged_data26.iloc[:, 21]  = pd.to_numeric(merged_data26.iloc[:, 21], errors='coerce').astype(float)
#%%


#%% Processing code regional
# posistion I is province code

#Province Code
#Khyber Pakhtunkhaw 1
#Punjab 2
#Sindh 3
#Balochistan 4
#ISLAMABAD 6
#Gilgit-Baltistian 7
#AJ & Kashmir 8

# posistion II is the division 
#DIVISION
#KALAT  
#MEKRAN  
#NASIRABAD
#QUETTA
#RAKHSHAN
#SIBI
#ZHOB
#ISLAMABAD
#BANNU
#DERA ISMAIL KHAN
#HAZARA
#KOHAT
#MALAKAND
#MARDAN
#PESHAWAR
#BAHAWALPUR
#DERA GHAZI KHAN
#FAISALABAD
#GUJRANWALA
#LAHORE
#MULTAN
#RAWALPINDI
#SAHIWAL
#SARGODHA
#HYDERABAD
#KARACHI
#LARKANA
#MIRPUR KHAS
#SHAHEED BENAZIRABA
#SUKKUR




#%%

# 
#and III is district 
#DISTRICT	I	II-III
		
#AWARAN	4	54
#KALAT	4	51
#KHUZDAR	4	53
#LASBELA	4	55
#MASTUNG	4	52
#SHAHEED SIKANDAR	4	56
#GWADAR	4	62
#KECH	4	61
#PANJGUR	4	63
#JAFFARABAD	4	42
#JHAL MAGSI	4	44
#KACHHI	4	41
#NASIRABAD	4	43
#SOHBATPUR	4	45
#KILLA ABDULLAH	4	13
#PISHIN	4	12
#QUETTA	4	11
#CHAGAI	4	71
#KHARAN	4	72
#NUSHKI	4	73
#WASHUK	4	74
#DERA BUGTI	4	35
#HARNAI	4	32
#KOHLU	4	34
#SIBI	4	31
#ZIARAT	4	33
#BARKHAN	4	22
#DUKI	4	27
#KILLA SAIFULLAH	4	24
#LORALAI	4	21
#MUSAKHEL	4	23
#SHERANI	4	26
#ZHOB	4	25		
#ISLAMABAD	6	11		
#BANNU	1	61
#LAKKI MARWAT	1	62
#NORTH WAZIRISTAN	1	63
#DERA ISMAIL KHAN	1	71
#SOUTH WAZIRISTAN	1	73
#TANK	1	72
#ABBOTTABAD	1	24
#BATAGRAM	1	23
#HARIPUR	1	25
#KOHISTAN	1	21
#MANSEHRA	1	22
#TORGHAR	1	26
#HANGU	1	52
#KARAK	1	53
#KOHAT	1	51
#KURRAM	1	54
#ORAKZAI	1	55
#BAJAUR	1	18
#BUNER	1	16
#CHITRAL	1	11
#LOWER DIR	1	13
#MALAKAND	1	17
#SHANGLA	1	15
#SWAT	1	14
#UPPER DIR	1	12
#MARDAN	1	31
#SWABI	1	32
#CHARSADDA	1	41
#KHYBER	1	44
#MOHMAND	1	45
#NOWSHERA	1	43
#PESHAWAR	1	42		
#BAHAWALNAGAR	2	92
#BAHAWALPUR	2	91
#RAHIM YAR KHAN	2	93
#DERA GHAZI KHAN	2	81
#LAYYAH	2	83
#MUZAFFARGARH	2	84
#RAJANPUR	2	82
#CHINIOT	2	32
#FAISALABAD	2	31
#JHANG	2	33
#TOBA TEK SINGH	2	34
#GUJRANWALA	2	41
#GUJRAT	2	43
#HAFIZABAD	2	42
#MANDI BAHAUDDIN	2	44
#NAROWAL	2	46
#SIALKOT	2	45
#KASUR	2	52
#LAHORE	2	51
#NANKANA SAHIB	2	54
#SHEIKHUPURA	2	53
#KHANEWAL	2	74
#LODHRAN	2	73
#MULTAN	2	72
#VEHARI	2	71
#ATTOCK	2	11
#CHAKWAL	2	14
#JHELUM	2	13
#RAWALPINDI	2	12
#OKARA	2	61
#PAKPATTAN	2	63
#SAHIWAL	2	62
#BHAKKAR	2	22
#KHUSHAB	2	23
#MIANWALI	2	24
#SARGODHA	2	21		
#BADIN	3	37
#DADU	3	31
#HYDERABAD	3	33
#JAMSHORO	3	32
#MATIARI	3	36
#SUJAWAL	3	39
#TANDO ALLAHYAR	3	34
#TANDO MUHAMMAD	3	35
#THATTA	3	38
#KARACHI CENTRAL	3	55
#KARACHI EAST	3	54
#KARACHI SOUTH	3	53
#KARACHI WEST	3	51
#KORANGI	3	56
#MALIR	3	52
#JACOBABAD	3	11
#KAMBAR SHAHDAD K	3	15
#KASHMORE	3	12
#LARKANA	3	14
#SHIKARPUR	3	13
#MIRPUR KHAS	3	41
#THARPARKAR	3	43
#UMER KOT	3	42
#NAUSHAHRO FEROZE	3	61
#SANGHAR	3	63
#SHAHEED BENAZIRAB	3	62
#GHOTKI	3	22
#KHAIRPUR	3	23
#SUKKUR	3	21
		
		
		
#%%
merged_data26['processing_code_orginal'] = merged_data26['processing_code'].astype(str)
#%%
merged_data26['processing_code'] = merged_data26['processing_code'].astype(str)

#%%

# Extract the first digit  - province 
merged_data26['first_digit'] = merged_data26['processing_code'].str[0]

# Extract the first two digits  - division
merged_data26['first_two_digits'] = merged_data26['processing_code'].str[:2]

# Extract the first three digits   district
merged_data26['first_three_digits'] = merged_data26['processing_code'].str[:3]
# if = 1 rural, if = 2 urban
merged_data26['fourty_digit'] = merged_data26['processing_code'].str[3]



#%%  

#What was ……  employment status? (Read all the options to the respondent)
#01. Regular paid employee with fixed wage
#02. Casual paid employee
#03. Paid worker by piece rate or work performed
#04. Paid non-family apprentice
#05. Employer
#06. Own account worker (Agriculture)
#07. Own account worker  (Non-agriculture)
#08. Owner cultivator
#09. Share cropper
#10. Contract cultivator
#11. Contributing family worker (Agriculture)
#12. Contributing family worker (NonAgriculture)
#13. Member of a producer’s cooperative
#14. Other (Spe


#   1 to 4 are fomral 
#   5 to 14 are informal 
merged_data26['Formal'] = 0
merged_data26['Informal'] = 0



merged_data26.loc[merged_data26['what_was_employment_status'].isin([1, 2, 3, 4]), 'Formal'] = 1  # 
#%%
merged_data26.loc[merged_data26['what_was_employment_status'].isin([5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), 'Informal'] = 1  # 

#%%
dummy_vars = pd.get_dummies(merged_data26['Formal'], prefix='Formal').astype(int)
#%%
merged_data26 = pd.concat([merged_data26, dummy_vars], axis=1)



#%% method 22  formal sector

merged_data26['Method2_Formal'] = 0
#merged_data26['Method2_Informal'] = 0
#%%
# formal
merged_data26.loc[merged_data26['what_kind_of_enterprise'].isin([1, 2, 3, 4, 5, 6, 7]), 'Method2_Formal'] = 1  # 
# informal (all full time working age workers with an actcity not under the categories 1 to 7 ), the rest must be workers in the infomral sectors
# otherwise =2
merged_data26.loc[~merged_data26['what_kind_of_enterprise'].isin([1, 2, 3, 4, 5, 6, 7]), 'Method2_Formal'] = 2

#%%
dummy_vars = pd.get_dummies(merged_data26['Method2_Formal'], prefix='Method2_Formal').astype(int)
#%%
merged_data26 = pd.concat([merged_data26, dummy_vars], axis=1)


#%%  from weekly to annual 

merged_data26['total_hours_annual']  = merged_data26['total_hours']   * 52  
#%% from weekly to monthly
merged_data26['total_hours_monthly']  = merged_data26['total_hours']   * 4  


#%%
merged_data26["yeardclust"] = merged_data26['year'] 

#%% add minimum wage variables




merged_data26.loc[merged_data26['yeardclust'] == 1985, 'minimum_wage'] = 140

merged_data26.loc[merged_data26['yeardclust'] == 1986, 'minimum_wage'] = 140
merged_data26.loc[merged_data26['yeardclust'] == 1987, 'minimum_wage'] = 140
merged_data26.loc[merged_data26['yeardclust'] == 1988, 'minimum_wage'] = 140
merged_data26.loc[merged_data26['yeardclust'] == 1989, 'minimum_wage'] = 140
merged_data26.loc[merged_data26['yeardclust'] == 1990, 'minimum_wage'] = 140
merged_data26.loc[merged_data26['yeardclust'] == 1991, 'minimum_wage'] = 140

merged_data26.loc[merged_data26['yeardclust'] == 1992, 'minimum_wage'] = 150
merged_data26.loc[merged_data26['yeardclust'] == 1993, 'minimum_wage'] = 150
merged_data26.loc[merged_data26['yeardclust'] == 1994, 'minimum_wage'] = 150
merged_data26.loc[merged_data26['yeardclust'] == 1995, 'minimum_wage'] = 150

merged_data26.loc[merged_data26['yeardclust'] == 1996, 'minimum_wage'] = 1750
merged_data26.loc[merged_data26['yeardclust'] == 1997, 'minimum_wage'] = 1750

merged_data26.loc[merged_data26['yeardclust'] == 1998, 'minimum_wage'] = 2050
merged_data26.loc[merged_data26['yeardclust'] == 1999, 'minimum_wage'] = 2050
merged_data26.loc[merged_data26['yeardclust'] == 2000, 'minimum_wage'] = 2050


merged_data26.loc[merged_data26['yeardclust'] == 2001, 'minimum_wage'] = 2500
merged_data26.loc[merged_data26['yeardclust'] == 2002, 'minimum_wage'] = 2500
merged_data26.loc[merged_data26['yeardclust'] == 2003, 'minimum_wage'] = 2500
merged_data26.loc[merged_data26['yeardclust'] == 2004, 'minimum_wage'] = 2500

merged_data26.loc[merged_data26['yeardclust'] == 2005, 'minimum_wage'] = 3000

merged_data26.loc[merged_data26['yeardclust'] == 2006, 'minimum_wage'] = 4000

merged_data26.loc[merged_data26['yeardclust'] == 2007, 'minimum_wage'] = 4600

merged_data26.loc[merged_data26['yeardclust'] == 2008, 'minimum_wage'] = 6000
merged_data26.loc[merged_data26['yeardclust'] == 2009, 'minimum_wage'] = 6000

merged_data26.loc[merged_data26['yeardclust'] == 2010, 'minimum_wage'] = 7000
merged_data26.loc[merged_data26['yeardclust'] == 2011, 'minimum_wage'] = 7000

merged_data26.loc[merged_data26['yeardclust'] == 2012, 'minimum_wage'] = 8000


merged_data26.loc[merged_data26['yeardclust'] == 2013, 'minimum_wage'] = 10000

merged_data26.loc[merged_data26['yeardclust'] == 2014, 'minimum_wage'] = 12000

merged_data26.loc[merged_data26['yeardclust'] == 2015, 'minimum_wage'] = 13000

merged_data26.loc[merged_data26['yeardclust'] == 2016, 'minimum_wage'] = 14000

merged_data26.loc[merged_data26['yeardclust'] == 2017, 'minimum_wage'] = 15000

merged_data26.loc[merged_data26['yeardclust'] == 2018, 'minimum_wage'] = 16200

merged_data26.loc[merged_data26['yeardclust'] == 2019, 'minimum_wage'] = 17500
merged_data26.loc[merged_data26['yeardclust'] == 2020, 'minimum_wage'] = 17500

merged_data26.loc[merged_data26['yeardclust'] == 2021, 'minimum_wage'] = 20000

#%%  convert to annual 

merged_data26['minimum_wage_annual']  = merged_data26['minimum_wage']   * 12  

merged_data26['minimum_wage_monthly']  = merged_data26['minimum_wage']  


#%%


#%% regional data from 2010


#Province Code
#Khyber Pakhtunkhaw 1
#Punjab 2
#Sindh 3
#Balochistan 4
#ISLAMABAD 6
#Gilgit-Baltistian 7
#AJ & Kashmir 8



merged_data26.loc[merged_data26['yeardclust'] == 1985, 'minimum_wageRegional'] = 140

merged_data26.loc[merged_data26['yeardclust'] == 1986 , 'minimum_wageRegional'] = 140
merged_data26.loc[merged_data26['yeardclust'] == 1987, 'minimum_wageRegional'] = 140
merged_data26.loc[merged_data26['yeardclust'] == 1988, 'minimum_wageRegional'] = 140
merged_data26.loc[merged_data26['yeardclust'] == 1989, 'minimum_wageRegional'] = 140
merged_data26.loc[merged_data26['yeardclust'] == 1990, 'minimum_wageRegional'] = 140
merged_data26.loc[merged_data26['yeardclust'] == 1991, 'minimum_wageRegional'] = 140

merged_data26.loc[merged_data26['yeardclust'] == 1992, 'minimum_wageRegional'] = 150
merged_data26.loc[merged_data26['yeardclust'] == 1993, 'minimum_wageRegional'] = 150
merged_data26.loc[merged_data26['yeardclust'] == 1994, 'minimum_wageRegional'] = 150
merged_data26.loc[merged_data26['yeardclust'] == 1995, 'minimum_wageRegional'] = 150

merged_data26.loc[merged_data26['yeardclust'] == 1996, 'minimum_wageRegional'] = 1750
merged_data26.loc[merged_data26['yeardclust'] == 1997, 'minimum_wageRegional'] = 1750

merged_data26.loc[merged_data26['yeardclust'] == 1998, 'minimum_wageRegional'] = 2050
merged_data26.loc[merged_data26['yeardclust'] == 1999, 'minimum_wageRegional'] = 2050
merged_data26.loc[merged_data26['yeardclust'] == 2000, 'minimum_wageRegional'] = 2050


merged_data26.loc[merged_data26['yeardclust'] == 2001, 'minimum_wageRegional'] = 2500
merged_data26.loc[merged_data26['yeardclust'] == 2002, 'minimum_wageRegional'] = 2500
merged_data26.loc[merged_data26['yeardclust'] == 2003, 'minimum_wageRegional'] = 2500
merged_data26.loc[merged_data26['yeardclust'] == 2004, 'minimum_wageRegional'] = 2500

merged_data26.loc[merged_data26['yeardclust'] == 2005, 'minimum_wageRegional'] = 3000

merged_data26.loc[merged_data26['yeardclust'] == 2006, 'minimum_wageRegional'] = 4000

merged_data26.loc[merged_data26['yeardclust'] == 2007, 'minimum_wageRegional'] = 4600

merged_data26.loc[merged_data26['yeardclust'] == 2008, 'minimum_wageRegional'] = 6000
merged_data26.loc[merged_data26['yeardclust'] == 2009, 'minimum_wageRegional'] = 6000



merged_data26.loc[merged_data26['yeardclust'] == 2010 , 'minimum_wageRegional'] = 7000
merged_data26.loc[(merged_data26['yeardclust'] == 2010) &  (merged_data26['first_digit'] == 2 ), 'minimum_wageRegional'] = 8000




merged_data26.loc[merged_data26['yeardclust'] == 2011, 'minimum_wageRegional'] = 7000

merged_data26.loc[merged_data26['yeardclust'] == 2012, 'minimum_wageRegional'] = 8000
merged_data26.loc[(merged_data26['yeardclust'] == 2012) &  (merged_data26['first_digit'] == 2 ), 'minimum_wageRegional'] = 9000


merged_data26.loc[merged_data26['yeardclust'] == 2013, 'minimum_wageRegional'] = 10000

merged_data26.loc[merged_data26['yeardclust'] == 2014, 'minimum_wageRegional'] = 12000

merged_data26.loc[merged_data26['yeardclust'] == 2015, 'minimum_wageRegional'] = 13000

merged_data26.loc[merged_data26['yeardclust'] == 2016, 'minimum_wageRegional'] = 14000

merged_data26.loc[merged_data26['yeardclust'] == 2017, 'minimum_wageRegional'] = 15000

merged_data26.loc[merged_data26['yeardclust'] == 2018, 'minimum_wageRegional'] = 16200

merged_data26.loc[merged_data26['yeardclust'] == 2019, 'minimum_wageRegional'] = 17500
merged_data26.loc[merged_data26['yeardclust'] == 2020, 'minimum_wageRegional'] = 17500

merged_data26.loc[merged_data26['yeardclust'] == 2021, 'minimum_wageRegional'] = 20000
merged_data26.loc[(merged_data26['yeardclust'] == 2021) &  (merged_data26['first_digit'] == 3 ), 'minimum_wageRegional'] = 25000


#%%
merged_data26['minimum_wageRegional_annual']  = merged_data26['minimum_wageRegional']   * 12  

merged_data26['minimum_wageRegional_monthly']  = merged_data26['minimum_wageRegional']  





#%% add cpi variable and reproduce real wage


#	Pakistan#
#	CPI (2010=100)
#1978	7.582706258
#1979	8.209572147
#1980	9.189649827
#1981	10.28137229
#1982	10.88833606
#1983	11.58105565
#1984	12.28601381
#1985	12.97585373
#1986	13.43084092
#1987	14.05956793
#1988	15.30214369
#1989	16.50248435
#1990	17.99631095
#1991	20.11830462
#1992	22.03136255
#1993	24.22869679
#1994	27.22534911
#1995	30.58593146
#1996	33.75885744
#1997	37.59909387
#1998	39.940767
#1999	41.59536806
#2000	43.41169823
#2001	44.77841199
#2002	46.25177611
#2003	47.59961517
#2004	51.14322787
#2005	55.77850604
#2006	60.19676858
#2007	64.77093105
#2008	77.91044056
#2009	88.54347445
#2010	100
#2011	111.9160927
#2012	122.7522026
#2013	132.1944937
#2014	141.6984635
#2015	145.2824826
#2016	150.7525412
#2017	156.9113459
#2018	164.8793939
#2019	182.3209327
#2020	200.078979
#2021	219.0789001
#2022	262.618334
#2023	343.4210793



merged_data26.loc[merged_data26['yeardclust'] == 1985, 'cpi'] = 	12.97585373
merged_data26.loc[merged_data26['yeardclust'] == 1986, 'cpi'] = 	13.43084092
merged_data26.loc[merged_data26['yeardclust'] == 1987, 'cpi'] = 	14.05956793
merged_data26.loc[merged_data26['yeardclust'] == 1988, 'cpi'] = 	15.30214369
merged_data26.loc[merged_data26['yeardclust'] == 1989, 'cpi'] = 	16.50248435
merged_data26.loc[merged_data26['yeardclust'] == 1990, 'cpi'] = 	17.99631095
merged_data26.loc[merged_data26['yeardclust'] == 1991, 'cpi'] = 	20.11830462
merged_data26.loc[merged_data26['yeardclust'] == 1992, 'cpi'] = 	22.03136255
merged_data26.loc[merged_data26['yeardclust'] == 1993, 'cpi'] = 	24.22869679
merged_data26.loc[merged_data26['yeardclust'] == 1994, 'cpi'] = 	27.22534911
merged_data26.loc[merged_data26['yeardclust'] == 1995, 'cpi'] = 	30.58593146
merged_data26.loc[merged_data26['yeardclust'] == 1996, 'cpi'] = 	33.75885744
merged_data26.loc[merged_data26['yeardclust'] == 1997, 'cpi'] = 	37.59909387
merged_data26.loc[merged_data26['yeardclust'] == 1998, 'cpi'] = 	39.940767
merged_data26.loc[merged_data26['yeardclust'] == 1999, 'cpi'] = 	41.59536806
merged_data26.loc[merged_data26['yeardclust'] == 2000, 'cpi'] = 	43.41169823
merged_data26.loc[merged_data26['yeardclust'] == 2001, 'cpi'] = 	44.77841199
merged_data26.loc[merged_data26['yeardclust'] == 2002, 'cpi'] = 	46.25177611
merged_data26.loc[merged_data26['yeardclust'] == 2003, 'cpi'] = 	47.59961517
merged_data26.loc[merged_data26['yeardclust'] == 2004, 'cpi'] = 	51.14322787
merged_data26.loc[merged_data26['yeardclust'] == 2005, 'cpi'] = 	55.77850604
merged_data26.loc[merged_data26['yeardclust'] == 2006, 'cpi'] = 	60.19676858
merged_data26.loc[merged_data26['yeardclust'] == 2007, 'cpi'] = 	64.77093105
merged_data26.loc[merged_data26['yeardclust'] == 2008, 'cpi'] = 	77.91044056
merged_data26.loc[merged_data26['yeardclust'] == 2009, 'cpi'] = 	88.54347445
merged_data26.loc[merged_data26['yeardclust'] == 2010, 'cpi'] = 	100
merged_data26.loc[merged_data26['yeardclust'] == 2011, 'cpi'] = 	111.9160927
merged_data26.loc[merged_data26['yeardclust'] == 2012, 'cpi'] = 	122.7522026
merged_data26.loc[merged_data26['yeardclust'] == 2013, 'cpi'] = 	132.1944937
merged_data26.loc[merged_data26['yeardclust'] == 2014, 'cpi'] = 	141.6984635
merged_data26.loc[merged_data26['yeardclust'] == 2015, 'cpi'] = 	145.2824826
merged_data26.loc[merged_data26['yeardclust'] == 2016, 'cpi'] = 	150.7525412
merged_data26.loc[merged_data26['yeardclust'] == 2017, 'cpi'] = 	156.9113459
merged_data26.loc[merged_data26['yeardclust'] == 2018, 'cpi'] = 	164.8793939
merged_data26.loc[merged_data26['yeardclust'] == 2019, 'cpi'] = 	182.3209327
merged_data26.loc[merged_data26['yeardclust'] == 2020, 'cpi'] = 	200.078979
merged_data26.loc[merged_data26['yeardclust'] == 2021, 'cpi'] = 	219.0789001
merged_data26.loc[merged_data26['yeardclust'] == 2022, 'cpi'] = 	262.618334
merged_data26.loc[merged_data26['yeardclust'] == 2023, 'cpi'] = 	343.4210793

#%% real wages


merged_data26['Annual_Earnings_real']  = merged_data26['Annual_Earnings'] /(merged_data26['cpi']/100) 

#%%  real wages monthly 

merged_data26['monthly_Earnings_real']  = merged_data26['Annual_Earnings_real'] /12


#%% minimum wage real 



merged_data26['minimum_wageRegional_annual_real']  = (merged_data26['minimum_wageRegional'] * 12 )   /(merged_data26['cpi']/100)  
#%%
merged_data26['minimum_wageRegional_monthly_real'] = merged_data26['minimum_wageRegional_annual_real'] / 12
#%%
merged_data26['minimum_wage_annual_real']  = ( merged_data26['minimum_wage'] * 12   )/(merged_data26['cpi']/100)   
#%%
merged_data26['minimum_wage_monthly_real']  = merged_data26['minimum_wage_annual_real']/ 12


#%%  create work type varibles from employemnet status columns


#%%
# Create new variables with initial value as 0
merged_data26['Workers_Paid_Employees'] = 0

merged_data26['Self_employed'] = 0
#%%
# Set values based on conditions
merged_data26.loc[(merged_data26['what_was_employment_status'] >= 1) & (merged_data26['what_was_employment_status'] <= 4), 'Workers_Paid_Employees'] = 1  # 

merged_data26.loc[(merged_data26['what_was_employment_status'] > 4) & (merged_data26['what_was_employment_status'] <= 14), 'Self_employed'] = 1  # 

#%%

merged_data26['PUBLIC'] = 0
merged_data26['PRIVATE'] = 0

merged_data26.loc[(merged_data26['what_kind_of_enterprise'] >= 1) & (merged_data26['what_kind_of_enterprise'] <= 5), 'PUBLIC'] = 1
merged_data26.loc[merged_data26['what_kind_of_enterprise'] == 7, 'PUBLIC'] = 1
merged_data26.loc[(merged_data26['what_kind_of_enterprise'] == 6) | ((merged_data26['what_kind_of_enterprise'] >= 8) & (merged_data26['what_kind_of_enterprise'] <= 10)), 'PRIVATE'] = 1

#%%  part time of full time or non participant

# Create a categorical variable 'work_status' initialized with NaN
merged_data26['work_status'] = 0

# Identify full-time workers (35 hours or more)
merged_data26.loc[merged_data26['total_hours'] >= 35, 'work_status'] = 1

# Identify part-time workers (less than 35 hours)
merged_data26.loc[(merged_data26['total_hours'] > 0) & (merged_data26['total_hours'] < 35), 'work_status'] = 2

# Identify non-participants (0 hours)
merged_data26.loc[merged_data26['total_hours'] == 0, 'work_status'] = 3

# Define labels for the 'work_status' categories
#work_status_labels = {1: "Full-time", 2: "Part-time", 3: "Non-participant"}





#%% 

merged_data26.to_csv('LFSFullSample.csv', index =False)



#%%


readfile_final = pd.read_csv('LFSFullSample.csv', sep=',')


#%% to stata file  dta



# Step 1: Load the CSV file into a DataFrame
df = pd.read_csv('LFSFullSample.csv')

# Step 2: Convert and save the DataFrame to a Stata .dta file
df.to_stata('LFSFullSample.dta', write_index=False)


#%%
#%%

# List the names of the variables (columns)
variable_names = df.columns.tolist()

# Print the list of variable names
print(variable_names)


#%%

#%% drop those not in the labor force: old >65
#or our empirical analysis, we restrict attention to workers between the ages  of 15 and 65.
    

merged_data26 = merged_data26.drop(merged_data26[merged_data26.age_at_last_birthday > 65].index)
#%%  less than 15

merged_data26 = merged_data26.drop(merged_data26[(merged_data26.age_at_last_birthday < 15)].index)


#%% 


#%%

merged_data26.to_csv('Onlyworkingage_LFS_Sample.csv', index =False)
#%%
# Step 1: Load the CSV file into a DataFrame
df2 = pd.read_csv('Onlyworkingage_LFS_Sample.csv')

# Step 2: Convert and save the DataFrame to a Stata .dta file
df2.to_stata('Onlyworkingage_LFS_Sample.dta', write_index=False)


#%%

# List the names of the variables (columns)
variable_names = df2.columns.tolist()

# Print the list of variable names
print(variable_names)