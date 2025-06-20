# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:28:50 2024

@author: ak922
"""

#  main code 



import patsy


import numpy 
import numpy as np
import pandas
import pandas as pd
import addfips
import seaborn 
import matplotlib
import matplotlib.pyplot as plt
from pandas import DataFrame
import seaborn 
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from pandas import DataFrame
import regex as re
import spacy
import csv
import statistics
import numpy as np
import pandas as pd
from linearmodels import PanelOLS
from linearmodels import RandomEffects
from linearmodels.panel import PooledOLS
import statsmodels
from statsmodels.sandbox.regression import gmm
import statsmodels.api as sm


import pandas as pd
import numpy as np
from scipy import stats
from matplotlib import style
import seaborn as sns
from matplotlib import pyplot as plt
import statsmodels.formula.api as smf

#%% use full sample (including those below 15 and over 65 )


readfile_final = pd.read_csv('LFSFullSample.csv', sep=',')

#%%
readfile_final['age_at_last_birthday2'] = readfile_final['age_at_last_birthday'] ** 2


#%%

# Step 1: Generate a household size variable and set it to 1 for each observation
readfile_final['Gen_househol_size'] = 1

#%%



# Create new variables with initial value as 0
readfile_final['children5'] = 0

readfile_final['children12'] = 0

# Set values based on conditions
readfile_final.loc[(readfile_final['age_at_last_birthday'] >= 0) & (readfile_final['age_at_last_birthday'] <= 5), 'children5'] = 1  # 

readfile_final.loc[(readfile_final['age_at_last_birthday'] > 5) & (readfile_final['age_at_last_birthday'] <= 12), 'children12'] = 1  # 



#%%

data_1985 = readfile_final.loc[readfile_final['year'] == 1985]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df1985 = data_1985.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

#%% rename 


collapsed_df1985.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df1985 = pd.merge(data_1985, collapsed_df1985, on=['processing_code','household_number'], how='left')

#%%


data_1986 = readfile_final.loc[readfile_final['year'] == 1986]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df1986 = data_1986.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df1986.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df1986 = pd.merge(data_1986, collapsed_df1986, on=['processing_code','household_number'], how='left')


#%%


data_1987 = readfile_final.loc[readfile_final['year'] == 1987]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df1987 = data_1987.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df1987.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df1987 = pd.merge(data_1987, collapsed_df1987, on=['processing_code','household_number'], how='left')


#%%


data_1988 = readfile_final.loc[readfile_final['year'] == 1988]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df1988 = data_1988.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df1988.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df1988 = pd.merge(data_1988, collapsed_df1988, on=['processing_code','household_number'], how='left')

#%%
data_1991 = readfile_final.loc[readfile_final['year'] == 1991]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df1991 = data_1991.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()


collapsed_df1991.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df1991 = pd.merge(data_1991, collapsed_df1991, on=['processing_code','household_number'], how='left')

#%%
data_1992 = readfile_final.loc[readfile_final['year'] == 1992]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df1992 = data_1992.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df1992.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df1992 = pd.merge(data_1992, collapsed_df1992, on=['processing_code','household_number'], how='left')



#%%
data_1993 = readfile_final.loc[readfile_final['year'] == 1993]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df1993 = data_1993.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df1993.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df1993 = pd.merge(data_1993, collapsed_df1993, on=['processing_code','household_number'], how='left')


#%%
data_1994 = readfile_final.loc[readfile_final['year'] == 1994]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df1994 = data_1994.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df1994.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df1994 = pd.merge(data_1994, collapsed_df1994, on=['processing_code','household_number'], how='left')


#%%
data_1995 = readfile_final.loc[readfile_final['year'] == 1995]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df1995 = data_1995.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df1995.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df1995 = pd.merge(data_1995, collapsed_df1995, on=['processing_code','household_number'], how='left')


#%%
data_1997 = readfile_final.loc[readfile_final['year'] == 1997]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df1997 = data_1997.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df1997.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df1997 = pd.merge(data_1997, collapsed_df1997, on=['processing_code','household_number'], how='left')


#%%
data_1998 = readfile_final.loc[readfile_final['year'] == 1998]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df1998 = data_1998.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df1998.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df1998 = pd.merge(data_1998, collapsed_df1998, on=['processing_code','household_number'], how='left')


#%%
data_2000 = readfile_final.loc[readfile_final['year'] == 2000]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df2000 = data_2000.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()


collapsed_df2000.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df2000 = pd.merge(data_2000, collapsed_df2000, on=['processing_code','household_number'], how='left')


#%%
data_2002 = readfile_final.loc[readfile_final['year'] == 2002]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df2002 = data_2002.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df2002.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df2002 = pd.merge(data_2002, collapsed_df2002, on=['processing_code','household_number'], how='left')


#%%
data_2004 = readfile_final.loc[readfile_final['year'] == 2004]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df2004 = data_2004.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()


collapsed_df2004.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df2004 = pd.merge(data_2004, collapsed_df2004, on=['processing_code','household_number'], how='left')


#%%
data_2006 = readfile_final.loc[readfile_final['year'] == 2006]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df2006 = data_2006.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df2006.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df2006 = pd.merge(data_2006, collapsed_df2006, on=['processing_code','household_number'], how='left')


#%%
data_2007 = readfile_final.loc[readfile_final['year'] == 2007]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df2007 = data_2007.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()


collapsed_df2007.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df2007 = pd.merge(data_2007, collapsed_df2007, on=['processing_code','household_number'], how='left')


#%%
data_2008 = readfile_final.loc[readfile_final['year'] == 2008]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df2008 = data_2008.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df2008.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df2008 = pd.merge(data_2008, collapsed_df2008, on=['processing_code','household_number'], how='left')


#%%
data_2009 = readfile_final.loc[readfile_final['year'] == 2009]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df2009 = data_2009.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df2009.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df2009 = pd.merge(data_2009, collapsed_df2009, on=['processing_code','household_number'], how='left')


#%%
data_2010 = readfile_final.loc[readfile_final['year'] == 2010]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df2010 = data_2010.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()


collapsed_df2010.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df2010 = pd.merge(data_2010, collapsed_df2010, on=['processing_code','household_number'], how='left')


#%%
data_2011 = readfile_final.loc[readfile_final['year'] == 2011]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df2011 = data_2011.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()


collapsed_df2011.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df2011 = pd.merge(data_2011, collapsed_df2011, on=['processing_code','household_number'], how='left')


#%%
data_2013 = readfile_final.loc[readfile_final['year'] == 2013]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df2013 = data_2013.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df2013.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df2013 = pd.merge(data_2013, collapsed_df2013, on=['processing_code','household_number'], how='left')




#%%
data_2014 = readfile_final.loc[readfile_final['year'] == 2014]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df2014 = data_2014.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df2014.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df2014 = pd.merge(data_2014, collapsed_df2014, on=['processing_code','household_number'], how='left')


#%%
data_2015 = readfile_final.loc[readfile_final['year'] == 2015]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df2015 = data_2015.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()


collapsed_df2015.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df2015 = pd.merge(data_2015, collapsed_df2015, on=['processing_code','household_number'], how='left')



#%%
data_2018 = readfile_final.loc[readfile_final['year'] == 2018]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df2018 = data_2018.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df2018.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df2018 = pd.merge(data_2018, collapsed_df2018, on=['processing_code','household_number'], how='left')



#%%
data_2019 = readfile_final.loc[readfile_final['year'] == 2019]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df2019 = data_2019.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()

collapsed_df2019.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df2019 = pd.merge(data_2019, collapsed_df2019, on=['processing_code','household_number'], how='left')



#%%
data_2021 = readfile_final.loc[readfile_final['year'] == 2021]
#%%
# Step 3: Collapse the dataset to calculate the sum of household sizes
collapsed_df2021 = data_2021.groupby(['processing_code','household_number']).agg({
    'Gen_househol_size': 'sum',
    'children5': 'sum',
    'children12': 'sum'
}).reset_index()


collapsed_df2021.rename(columns={
    'Gen_househol_size': 'Gen_househol_size_Ne',
    'children5': 'children5_Ne',
    'children12': 'children12_Ne'
}, inplace=True)

#%%
merged_df2021 = pd.merge(data_2021, collapsed_df2021, on=['processing_code','household_number'], how='left')



#%%



merged_df_combined = pd.concat([merged_df2019, merged_df2021], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df2018], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df2015], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df2014], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df2013], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df2011], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df2010], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df2009], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df2008], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df2007], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df2006], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df2004], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df2002], ignore_index=True)

merged_df_combined = pd.concat([merged_df_combined, merged_df2000], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df1998], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df1997], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df1995], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df1994], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df1993], ignore_index=True)
merged_df_combined = pd.concat([merged_df_combined, merged_df1992], ignore_index=True)

merged_df_combined = pd.concat([merged_df_combined, merged_df1991], ignore_index=True)

merged_df_combined = pd.concat([merged_df_combined, merged_df1988], ignore_index=True)

merged_df_combined = pd.concat([merged_df_combined, merged_df1987], ignore_index=True)

merged_df_combined = pd.concat([merged_df_combined, merged_df1986], ignore_index=True)

merged_df_combined = pd.concat([merged_df_combined, merged_df1985], ignore_index=True)

#%% final file


indust_category_dummies = pd.get_dummies(merged_df_combined['Industry'], prefix='Industry').astype(int)
#%% add it tyo the main dataframe
merged_df_combined  = pd.concat([merged_df_combined , indust_category_dummies], axis=1)

#%%


occupation_category_dummies = pd.get_dummies(merged_df_combined['occupations_code_18'], prefix='occupations_code_18').astype(int)
  #%% add it tyo the main dataframe
merged_df_combined  = pd.concat([merged_df_combined , occupation_category_dummies], axis=1)

#%%  "TrainVar"


TrainVar_category_dummies = pd.get_dummies(merged_df_combined['ever_completed_any_technical_vocational_training'], prefix='ever_completed_any_technical_vocational_training').astype(int)
  #%% add it tyo the main dataframe
merged_df_combined  = pd.concat([merged_df_combined, TrainVar_category_dummies], axis=1)


#%%

merged_df_combined.to_csv('merged_df_Analysis_Sample.csv', index =False)
#%%
# Step 1: Load the CSV file into a DataFrame
df2 = pd.read_csv('merged_df_Analysis_Sample.csv')
#%%
# Step 2: Convert and save the DataFrame to a Stata .dta file
df2.to_stata('merged_df_Analysis_Sample.dta', write_index=False)

#%% Start:    df2 = pd.read_csv('merged_df_Analysis_Sample.csv')
 

df2 = pd.read_csv('merged_df_Analysis_Sample.csv', sep=',')


#%% drop this years


df2 = df2[df2['year'] != 1985]
#%%
df2 = df2[df2['year'] != 1986]
#%%
df2 = df2[df2['year'] != 1987]
#%%
df2 = df2[df2['year'] != 1988]
#%%
df2 = df2[df2['year'] != 1989]
#%%
df2 = df2[df2['year'] != 1990]
#%%
df2 = df2[df2['year'] != 1991]


#%% Drop observations where both earnings variables are missing
#  drop if missing(wage_workers) & missing(wage_selfemployed_weekly)
#%  * Drop observations where  inductry S5C9 is missing
#drop if S5C9==.

# # Create a new column 'student' based on S4C10 value (1 -> Student, otherwise Non-Student)
# df['student'] = (df['S4C10'] != 1).astype(int)

nan_count_column = df2['Annual_Earnings'].isna().sum()
print(f"NaN count in annual earnings: {nan_count_column}")


#%%
# Dropping rows with NaN values in 'Annual_Earnings_real' column
df2 = df2.dropna(subset=['Annual_Earnings'])
#%%
# Checking NaN count again after dropping
nan_count_after_drop = df2['Annual_Earnings'].isna().sum()
print(f"NaN count after drop: {nan_count_after_drop}")

#%%
df2 = df2[df2['Annual_Earnings'] != 0]


#%%
df2['work_status_report'] = df2['work_status']
#%%   0 and 3 considered as non partcipants   
df2.loc[df2['work_status'] == 3 , 'work_status_report'] = 0

#%%
df2_d = df2.drop(df2[df2.age_at_last_birthday > 65].index)
#%%
df2_d = df2_d.drop(df2_d[(df2_d.age_at_last_birthday < 15)].index)

#%%




#%%
#Full-time wage employees 
#Part-time wage employees 
#Non-participantsa 

# Identify full-time workers (35 hours or more)   'total_hours'] >= 35, 'work_status'] = 1
# Identify part-time workers (less than 35 hours)=  > 0) & (merged_data26['total_hours'] < 35), 'work_status'] = 2
# Identify non-participants (0 hours) ['total_hours'] == 0, 'work_status'] = 3


# drop zero  0  missing data and sleect years 
df2_testing = df2_d.loc[(df2_d['yeardclust'].isin([1992, 2021]))]


#%%





# Initialize an empty string to store LaTeX code for the combined table
latex_combined_table = ""

# Loop through each year of interest
for year in [1992, 2021]:
    # Filter data for the specific year
    df_year = df2_testing[df2_testing['yeardclust'] == year]
    
    # Table 1: Tabulate work status
    tab_work_status = df_year['work_status_report'].value_counts()
    tab_work_status_female = df_year[df_year['sex_of_person_2.0'] == 1]['work_status_report'].value_counts()
    tab_work_status_male = df_year[df_year['sex_of_person_2.0'] == 0]['work_status_report'].value_counts()

    # Combine into DataFrame
    work_status_table = pd.DataFrame({
        'Total': tab_work_status,
        'Female': tab_work_status_female,
        'Male': tab_work_status_male
    }).fillna(0).astype(int)

     # Store data in dictionaries
    if year == 1992:
        data_1992 = work_status_table
    elif year == 2021:
        data_2021 = work_status_table

# Combine the data from both years into a single DataFrame
combined_table = pd.concat(
    [data_1992.rename(columns=lambda x: f'{x} (1992)'), 
     data_2021.rename(columns=lambda x: f'{x} (2021)')],
    axis=1
)

# Generate LaTeX code for the combined table
latex_combined_table = combined_table.to_latex(
    index=True,
    caption='Distribution of Work Status by Gender for 1992 and 2021',
    label='tab:work_status_combined',
    float_format="%.0f",
    bold_rows=True
)

# Open the .tex file to write the LaTeX document
output_file_path = 'participation2_waves.tex'
with open(output_file_path, 'w') as f:
    f.write('\\documentclass{article}\n')
    f.write('\\usepackage{booktabs}\n')  # For better looking tables
    f.write('\\begin{document}\n\n')
    
    # Write LaTeX table to file
    f.write('\\section*{Descriptive Statistics}\n')
    f.write(latex_combined_table)
    f.write('\n\n')

    # Close the LaTeX document
    f.write('\\end{document}')

print(f"LaTeX document saved to {output_file_path}")

#%%

#%%



#%%  Descritive stat
#steps:
#keep if age >= 15 & age <= 64
#drop if age < 15 | age > 65

#  We only use full time wage employees
# keep if work_status==1
# those who work >= 35, 'work_status'] = 1


# Keep only full-time wage employees
#df2 = df2[df2['work_status'] == 1]

#%% to do:

#***We exclude self-employed workers and other categories from our analysis******
#*** leaving only wage employees (full-time and part-time) in the dataset.*******
#drop if S5C7 > 3


# *DROP FULL TIME Students************************************************
#describe S4C10
#tab S4C10
#drop if S4C10==18


# Create a new column 'student' based on S4C10 value (1 -> Student, otherwise Non-Student)
#df['student'] = (df['S4C10'] != 1).astype(int)

#%%
df2_fulltime = df2_d[df2_d['work_status'] == 1]
#%%
df2_fulltime['hourly_wage'] = df2_fulltime['Annual_Earnings_real']/df2_fulltime['total_hours_annual']



# Optional: Check for and handle any potential division by zero or NaN values
# For instance, you might want to replace NaN values with 0 or another placeholder value
df2_fulltime['hourly_wage'].replace([np.inf, -np.inf], np.nan, inplace=True)  # Replace infinities with NaN
df2_fulltime['hourly_wage'].fillna(0, inplace=True)  # Replace NaN values with 0 (or use another method if appropriate)
#%%
df2_fulltime['loghourly_wage']= np.log1p(df2_fulltime['hourly_wage'])




#%%
from stargazer.stargazer import Stargazer


mean_logrwage_male = df2_fulltime[df2_fulltime['sex_of_person_1.0'] == 1]['loghourly_wage'].mean()

# Average log hourly wage for women
mean_logrwage_female = df2_fulltime[df2_fulltime['sex_of_person_1.0'] == 0]['loghourly_wage'].mean()

print("Mean log wage (male):", mean_logrwage_male)
print("Mean log wage (female):", mean_logrwage_female)

df2_fulltime['wagedifferential_male'] = df2_fulltime['loghourly_wage'] - mean_logrwage_male

df2_fulltime['wagedifferential_female'] = df2_fulltime['loghourly_wage'] - mean_logrwage_female



#%%    district fixed effcets instead of houshold fixed effcets first_three_digits
#df2_fulltime['FE_first_three_digits'] = df2_fulltime['first_three_digits']
df2_fulltime = df2_fulltime.set_index(['year','processing_code'])

#%%
df2_fulltime['sex_of_person_2.0current_marital_status_2.0'] = df2_fulltime['sex_of_person_2.0'] * df2_fulltime['current_marital_status_2.0']

#%%  married: 'current_marital_status_2.0'

# Define the dependent variables
dep_vars_list = ['loghourly_wage']

# Define the exogenous variables
exog_vars_list = [['sex_of_person_2.0'], 
                  ['sex_of_person_2.0','current_marital_status_2.0'], 
                  ['sex_of_person_2.0','current_marital_status_2.0','sex_of_person_2.0current_marital_status_2.0'],
                  ['sex_of_person_2.0','current_marital_status_2.0','sex_of_person_2.0current_marital_status_2.0','edu_2'],
                  ['sex_of_person_2.0','current_marital_status_2.0','sex_of_person_2.0current_marital_status_2.0','edu_2','edu_3'],
                  ['sex_of_person_2.0','current_marital_status_2.0','sex_of_person_2.0current_marital_status_2.0','edu_2','edu_3','edu_4'],
                  ['sex_of_person_2.0','current_marital_status_2.0','sex_of_person_2.0current_marital_status_2.0','edu_2','edu_3','edu_4','children5_Ne']]
# Ensure that we have the correct number of columns for Stargazer
num_models = len(dep_vars_list) * len(exog_vars_list)

# Store all the results in a list
results_list = []

# Loop through each dependent variable
for dep_var in dep_vars_list:
    y = df2_fulltime[dep_var]
    
    for exog_vars in exog_vars_list:
        # Define the exogenous variables and add a constant
        exog = sm.add_constant(df2_fulltime[exog_vars])
        
        # Run the regression
        model = PanelOLS(y, exog, entity_effects=False, time_effects=False)
        results = model.fit(cov_type="clustered", clusters=df2_fulltime['yeardclust'])
        
        # Store the results
        results_list.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer(results_list)

# Customize table appearance
stargazer.title("Regression Results")

# Create a list of column names that match the number of results
column_names = [f"Model {i+1}" for i in range(len(results_list))]

# Specify custom columns (ensure this list matches the number of models)
stargazer.custom_columns(column_names, [1] * len(results_list))

stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"

with open("modelsWagesfulltime.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)
#%%


    
    



#%% dummy variable for training var
# dummy var for industry var
# dummy var for occupation var



#%%
# 'Workers_Paid_Employees'
# Self_employed'  
#%%


#df2_d['hourly_wage'] = df2_d['Annual_Earnings_real']/df2_d['total_hours_annual']



# Optional: Check for and handle any potential division by zero or NaN values
# For instance, you might want to replace NaN values with 0 or another placeholder value
#df2_d['hourly_wage'].replace([np.inf, -np.inf], np.nan, inplace=True)  # Replace infinities with NaN
#df2_d['hourly_wage'].fillna(0, inplace=True)  # Replace NaN values with 0 (or use another method if appropriate)
#%%
#df2_d['loghourly_wage']= np.log1p(df2_d['hourly_wage'])


#%%

# Filter the DataFrame to include only the specified years
selected_years = [1992, 2021]
filtered_df = df2_fulltime[df2_fulltime['yeardclust'].isin(selected_years)]



#-

# Keep the grouping columns
grouping_cols = ['yeardclust', 'sex_of_person_2.0']

# Select only numeric columns but keep the grouping columns
numeric_cols = filtered_df.select_dtypes(include=[int, float]).columns.tolist()
needed_cols = grouping_cols + [col for col in numeric_cols if col not in grouping_cols]

# Subset the dataframe to only those columns
subset_df = filtered_df[needed_cols]

# Now group and compute means
means_df = subset_df.groupby(['yeardclust', 'sex_of_person_2.0']).mean().transpose()

total_means = subset_df.groupby(['yeardclust']).mean().transpose()

#---

#numeric_data = filtered_df.select_dtypes(include=[int, float])

# Calculate the mean for each variable by year
#means_df = numeric_data.groupby(['yeardclust', 'sex_of_person_2.0']).mean().transpose()    

# Add total row for means
#total_means = numeric_data.groupby(['yeardclust']).mean().transpose()
total_means['Total'] = total_means.mean(axis=1)

# Combine the year-specific means with the total
means_df = pd.concat([means_df, total_means], axis=1)

counts_df = filtered_df.groupby(['yeardclust', 'sex_of_person_2.0']).size().unstack()


# Add total row for counts
#total_counts = filtered_df.groupby(['yeardclust']).size().unstack(fill_value=0)

#counts_df = pd.concat([counts_df, total_counts], axis=1)


# Convert the reshaped DataFrame to LaTeX table format
latex_table = means_df.to_latex(header=True, 
                                index=True, 
                                bold_rows=True, 
                                float_format="{:0.2f}".format)


latex_counts_table = counts_df.to_latex(header=True, 
                                        index=True, 
                                        bold_rows=True)





# Open the .tex file to write the LaTeX document
with open('de_mSecond_waves.tex', 'w') as f:
    f.write('\\documentclass{article}\n')
    f.write('\\usepackage{booktabs}\n')  # For better looking tables
    f.write('\\begin{document}\n\n')
    
    # Write LaTeX table to file
    f.write('\\section*{Descriptive Statistics}\n')
    f.write(latex_table)
    f.write('\n\n')
    
    f.write('\\section*{Number of Observations}\n')
    f.write(latex_counts_table)
    f.write('\n\n')

    # Close the LaTeX document
    f.write('\\end{document}')
    

#%%




#%% quantile regression plus plot
 
# this ine:  xxxxx2.0  is not a valid syntax for referring  (so I modify it) 
df2_fulltime['sex_of_person_2FemaleQ']  = df2_fulltime['sex_of_person_2.0']
#%%


# Define the quantiles
quantiles = [0.1, 0.2, 0.3, 0.4,0.5,0.6,0.7, 0.8, 0.9]

# Initialize storage for results
results = []

# Loop over each quantile and store the coefficients
for q in quantiles:
    # Run quantile regression
    model = smf.quantreg('loghourly_wage ~ sex_of_person_2FemaleQ', df2_fulltime).fit(q=q)
    
    # Extract coefficients and standard errors
    b_female = model.params['sex_of_person_2FemaleQ']
    se_female = model.bse['sex_of_person_2FemaleQ']
    
    # Store the results
    results.append({'quantile': q, 'b_female': b_female, 'se_female': se_female})

# Convert the results to a DataFrame
results_df = pd.DataFrame(results)

# Calculate 95% confidence intervals
results_df['ci_lower'] = results_df['b_female'] - 1.96 * results_df['se_female']
results_df['ci_upper'] = results_df['b_female'] + 1.96 * results_df['se_female']

# Plot the gender wage gap across quantiles with 95% confidence intervals
plt.figure()
plt.plot(results_df['quantile'], results_df['b_female'], marker='o', color='#020F59', label='Female Coefficient')
plt.fill_between(results_df['quantile'], results_df['ci_lower'], results_df['ci_upper'], color='#020F59', alpha=0.2)
#plt.title("Gender Wage Gaps Across the Distribution",fontsize = 16)
plt.xlabel("Quantile",fontsize = 14)
plt.ylabel("(Log) hourly wage (real)",fontsize = 14)
plt.xticks(quantiles)
plt.grid(True)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.savefig("Fulltimewage_distribution_by_gender.pdf", format='pdf')
plt.close()
#plt.show()


#%%


df2_fulltime['logAnnual_Earnings']= np.log1p(df2_fulltime['Annual_Earnings'])

df2_fulltime['logAnnual_Earnings_real']= np.log1p(df2_fulltime['Annual_Earnings_real'])


# Define the quantiles
quantiles = [0.1, 0.2, 0.3, 0.4,0.5,0.6,0.7, 0.8, 0.9]

# Initialize storage for results
results = []

# Loop over each quantile and store the coefficients
for q in quantiles:
    # Run quantile regression
    model = smf.quantreg('logAnnual_Earnings_real ~ sex_of_person_2FemaleQ', df2_fulltime).fit(q=q)
    
    # Extract coefficients and standard errors
    b_female = model.params['sex_of_person_2FemaleQ']
    se_female = model.bse['sex_of_person_2FemaleQ']
    
    # Store the results
    results.append({'quantile': q, 'b_female': b_female, 'se_female': se_female})

# Convert the results to a DataFrame
results_df = pd.DataFrame(results)

# Calculate 95% confidence intervals
results_df['ci_lower'] = results_df['b_female'] - 1.96 * results_df['se_female']
results_df['ci_upper'] = results_df['b_female'] + 1.96 * results_df['se_female']

# Plot the gender wage gap across quantiles with 95% confidence intervals

plt.figure()
plt.plot(results_df['quantile'], results_df['b_female'], marker='o', color='#020F59', label='Female Coefficient')
plt.fill_between(results_df['quantile'], results_df['ci_lower'], results_df['ci_upper'], color='#020F59', alpha=0.2)
#plt.title("Gender Wage Gaps Across the Distribution",fontsize = 16)
plt.xlabel("Quantile",fontsize = 14)
plt.ylabel("(Log) annual wage (real)",fontsize = 14)
plt.xticks(quantiles)
plt.grid(True)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.savefig("Fulltimewage_distribution_by_genderDiffer.pdf", format='pdf')
plt.close()
#plt.show()



#%%
forplott_df2_fulltime = df2_fulltime
#%%

# Figure 2: Distribution of (log) real hourly wages, by year and gender
plt.figure()
# KDE plot for males
sns.kdeplot(df2_fulltime['loghourly_wage'][df2_fulltime['sex_of_person_2FemaleQ'] == 0], 
            color='#D92344', label='Male',  linewidth=2.5)

# KDE plot for females
sns.kdeplot(df2_fulltime['loghourly_wage'][df2_fulltime['sex_of_person_2FemaleQ'] == 1], 
            color='#020F59', linestyle='--', label='Female', linewidth=2.5)

# Add title and labels
#plt.title("Kernel Density Estimate",fontsize = 16)
plt.xlabel("(Log) hourly Wage (real)",fontsize = 14)
plt.ylabel("Density",fontsize = 14)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# Reorder the legend manually
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles=[handles[0], handles[1]], labels=[labels[0], labels[1]], fontsize=14)

# Save the plot as a PDF file
plt.savefig("Fulltimekernelplot.pdf", format='pdf')


#%%




# Figure 2: Distribution of (log) real hourly wages, by year and gender
plt.figure()
# KDE plot for males
sns.kdeplot(df2_fulltime['logAnnual_Earnings_real'][df2_fulltime['sex_of_person_2FemaleQ'] == 0], 
            color='#D92344', label='Male',  linewidth=2.5)

# KDE plot for females
sns.kdeplot(df2_fulltime['logAnnual_Earnings_real'][df2_fulltime['sex_of_person_2FemaleQ'] == 1], 
            color='#020F59', linestyle='--', label='Female', linewidth=2.5)

# Add title and labels
#plt.title("Kernel Density Estimate",fontsize = 14)
plt.xlabel("(Log) annual wages (real)",fontsize = 14)
plt.ylabel("Density",fontsize = 14)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# Reorder the legend manually
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles=[handles[0], handles[1]], labels=[labels[0], labels[1]], fontsize=14)

# Save the plot as a PDF file
plt.savefig("FulltimekernelplotDiffer.pdf", format='pdf')




#%% replication code




#%%   Oaxaca-Blinder  (decomposition)


df3 = df2_fulltime.dropna(subset=['loghourly_wage',
                                  #'age_at_last_birthday'
                                  #, 'age_at_last_birthday2',
                                  'PUBLIC',
          'ever_completed_any_technical_vocational_training',
          'literacy_1_1.0',
          'literacy_1_2.0',
          'current_marital_status_1.0',
          'current_marital_status_2.0',
          'current_marital_status_3.0',
          'current_marital_status_4.0',
          'edu_1',
          'edu_2',
          'edu_3',
          'edu_4',
          'first_digit',
          'first_two_digits',
          'first_three_digits',
          'fourty_digit',
          'Method2_Formal_1',
          'Method2_Formal_2',
          'Formal_0',
          'Formal_1',
          'PUBLIC',
          'PRIVATE',
          'children5_Ne',
          'children12_Ne',
          'Industry_1.0',
          'Industry_2.0',
          'Industry_3.0',
          'Industry_4.0',
          'Industry_5.0',
          'occupations_code_18_1.0',
          'occupations_code_18_2.0',
          'occupations_code_18_3.0',
          'occupations_code_18_4.0',
          'occupations_code_18_5.0',
          'occupations_code_18_6.0',
          'occupations_code_18_7.0',
          'occupations_code_18_8.0',
          'ever_completed_any_technical_vocational_training_0.0',
          'ever_completed_any_technical_vocational_training_1.0',
          'ever_completed_any_technical_vocational_training_2.0' ])


# Define the dependent and independent variables
X = df3[['age_at_last_birthday', 'age_at_last_birthday2','PUBLIC',
          'ever_completed_any_technical_vocational_training',
          'literacy_1_1.0',
          'literacy_1_2.0',
          'current_marital_status_1.0',
          'current_marital_status_2.0',
          'current_marital_status_3.0',
          'current_marital_status_4.0',
          'edu_1',
          'edu_2',
          'edu_3',
          'edu_4',
          'first_digit',
          'first_two_digits',
          'first_three_digits',
          'fourty_digit',
          'Method2_Formal_1',
          'Method2_Formal_2',
          'Formal_0',
          'Formal_1',
          'PUBLIC',
          'PRIVATE',
          'children5_Ne',
          'children12_Ne',
          'Industry_1.0',
          'Industry_2.0',
          'Industry_3.0',
          'Industry_4.0',
          'Industry_5.0',
          'occupations_code_18_1.0',
          'occupations_code_18_2.0',
          'occupations_code_18_3.0',
          'occupations_code_18_4.0',
          'occupations_code_18_5.0',
          'occupations_code_18_6.0',
          'occupations_code_18_7.0',
          'occupations_code_18_8.0',
          'ever_completed_any_technical_vocational_training_0.0',
          'ever_completed_any_technical_vocational_training_1.0',
          'ever_completed_any_technical_vocational_training_2.0'   
          ]]
X = sm.add_constant(X)  # Adds the intercept term
y = df3['loghourly_wage']

# Perform regressions for each group
model_A = sm.OLS(y[df3['sex_of_person_1.0'] == 1], X[df3['sex_of_person_1.0'] == 1]).fit()
model_B = sm.OLS(y[df3['sex_of_person_1.0'] == 0], X[df3['sex_of_person_1.0'] == 0]).fit()

# Get the coefficients
beta_A = model_A.params
beta_B = model_B.params

# Calculate the mean characteristics
X_mean_A = X[df3['sex_of_person_1.0'] == 1].mean()
X_mean_B = X[df3['sex_of_person_1.0'] == 0].mean()

# Decomposition
# 1. Differences in characteristics
diff_characteristics = (X_mean_B - X_mean_A).dot(beta_A)

# 2. Differences in coefficients
diff_coefficients = (beta_B - beta_A).dot(X_mean_A)

# 3. Unexplained part (Residual)
unexplained_part = (y[df3['sex_of_person_1.0'] == 0].mean() - y[df3['sex_of_person_1.0'] == 1].mean()) - diff_characteristics - diff_coefficients



print("Oaxaca-Blinder Decomposition Results:")
print(f"Difference due to characteristics: {diff_characteristics:.2f}")
print(f"Difference due to coefficients: {diff_coefficients:.2f}")
print(f"Unexplained part: {unexplained_part:.2f}")

# Output results
print("\nModel A Summary:")
print(model_A.summary())
print("\nModel B Summary:")
print(model_B.summary())


#%% replicate



import pandas as pd 
import numpy as np 
import statsmodels.api as sm
import warnings
try:
    import matplotlib.pyplot as plt
except ImportError:
    warnings.warn("Matplotlib failed to import", ImportWarning)

class Oaxaca:

    def __init__(self, data, by, endo, debug = True):
        
        self.data = data
        self.by = by
        self.df_type = ""
        self.f_df = ""
        self.s_df = ""
        self.endo = endo
        self.two_gap = 0
        self.three_gap = 0

        self.f_mean = 0
        self.s_mean = 0

        self.char_eff = 0
        self.coef_eff = 0
        self.int_eff = 0

        self.exp_eff = 0
        self.unexp_ex = 0

        self.t_x = 0
        self.t_y = 0

        self.explained = 0
        self.unexplained = 0

        self.char_eff_var = 0
        self.coef_eff_var = 0

        self.cotton_fix_model = 0

        #A bunch of error checking
        if type(self.data) != type(pd.DataFrame()) and type(self.data) != type(np.array(1)):
            raise ValueError('The data must be in a DataFrame or a numpy array')


        if type(self.data) == type(pd.DataFrame()):
            #By must be a string
            if type(self.by) != str:
                raise ValueError('The "by" variable must be a string if datatype is {}'.format(type(self.data)))

            if type(self.endo) != str:
                raise ValueError('The "endo" variable must be a string if datatype is {}'.format(type(self.data)))
            
            #The by is not in the columns
            if by not in self.data.columns.values:
                raise ValueError('The "by" variable must be in the DataFrame')

            if endo not in self.data.columns.values:
                raise ValueError('The "endo" variable must be in the DataFrame')

            self.df_type = 'df'

        if type(self.data) == type(np.array(1)):
            #By must be an integer to index the numpy array
            if type(self.by) != int:
                raise ValueError('The "by" variable must be a int if datatype is {}'.format(type(self.data)))

            if type(self.by) != int:
                raise ValueError('The "endo" variable must be a int')

            self.df_type = 'np'
        
        if debug == False and data.shape[0] < data.shape[1]:
            raise ValueError("You have more columns, {}, than rows, {}".format(data.shape[0], data.shape[1]))
    
        #Split the Dataframe by the 'By' value
        if self.df_type == 'np':
            self.data = pd.DataFrame(self.data)
            split = self.data.iloc[:,by].value_counts().index
            
            #We need binary differences for this value
            if len(split) != 2:
                print("These are the attempted split values: {}".format(split))
                raise KeyError('There are more than 2 unique values in the by columns')

            print("These are the attempted split values: {}".format(split))
            
            self.t_x = self.data.drop(self.data.columns[endo], axis = 1)
            self.t_y = self.data.iloc[:, endo]

            self.f_df = self.data[self.data.iloc[:, by] == split[0]]
            self.s_df = self.data[self.data.iloc[:, by] != split[0]]
           
            self.f_x = self.f_df.drop(self.f_df.columns[[by, endo]], axis = 1)
            self.f_y = self.f_df.iloc[:, endo]
        
            self.s_x = self.s_df.drop(self.s_df.columns[[by, endo]], axis = 1)
            self.s_y = self.s_df.iloc[:, endo]

            self.f_x = sm.add_constant(self.f_x)
            self.s_x = sm.add_constant(self.s_x)
            self.t_x = sm.add_constant(self.t_x)

        if self.df_type == 'df':
            split = self.data[by].value_counts().index
            
            if len(split) != 2:
                print("These are the attempted split values: {}".format(split))
                raise KeyError('There are more than 2 unique values in the by columns')

            print("These are the attempted split values: {}".format(split))
            
            self.t_x = self.data.drop([endo], axis = 1)
            self.t_y = self.data[endo]


            self.f_df = self.data[self.data[by] == split[0]]
            self.s_df = self.data[self.data[by] != split[0]]

            self.f_x = self.f_df.drop([by,endo], axis = 1)
            self.f_y = self.f_df[endo]

            self.s_x = self.s_df.drop([by,endo], axis = 1)
            self.s_y = self.s_df[endo]

            self.f_x = sm.add_constant(self.f_x)
            self.s_x = sm.add_constant(self.s_x)
            self.t_x = sm.add_constant(self.t_x)

        

    def fix(self):
        #There may be issues with the "first" dataframe not being the correct one
        #we remidy this by flipping the two if the gap is negative
        self.f_df, self.s_df = self.s_df, self.f_df
        self.f_x, self.s_x = self.s_x, self.f_x
        self.f_y, self.s_y = self.s_y, self.f_y
        self.f_mean, self.s_mean = self.s_mean, self.f_mean


    def three_fold(self, plot = False, round_val = 5):
        self.f_mean = self.f_y.mean()
        self.s_mean = self.s_y.mean()

        if round_val != False:
            try:
                round_val = int(round_val)
            except ValueError:
                raise ValueError("Your round value must either by an int or be able to be casted into one.")
        
        #The wrong first is first
        if self.f_mean - self.s_mean < 0:
            self.fix()
        
        self.f_model = sm.OLS(self.f_y, self.f_x).fit()
        self.s_model = sm.OLS(self.s_y, self.s_x).fit()

        #Characteristic Effect
        self.char_eff = (self.f_x.mean() - self.s_x.mean()) @ self.s_model.params

        #Coefficient Effect
        self.coef_eff = (self.s_x.mean()) @ (self.f_model.params - self.s_model.params)

        #Interaction Effect
        self.int_eff = (self.f_x.mean() - self.s_x.mean()) @ (self.f_model.params - self.s_model.params)
        
        self.three_gap = self.f_mean - self.s_mean
        
        if round_val != False:
            self.char_eff = round(self.char_eff, round_val)
            self.coef_eff = round(self.coef_eff, round_val)
            self.int_eff = round(self.int_eff, round_val)
            self.three_gap = round(self.three_gap, round_val)


        print("Characteristic Effect: {}".format(self.char_eff))
        print("Coefficent Effect: {}".format(self.coef_eff))
        print("Interaction Effect: {}".format(self.int_eff))
        print("Gap: {}".format(self.three_gap))
        
        if plot == True:
            self.plot(plt_type=3)

        return self.char_eff, self.coef_eff, self.int_eff, self.three_gap


    def two_fold(self, plot = False, round_val = 5):
        self.f_mean = self.f_y.mean()
        self.s_mean = self.s_y.mean()
        
        if round_val != False:
            try:
                round_val = int(round_val)
            except ValueError:
                raise ValueError("Your round value must either by an int or be able to be casted into one.")
        
        #The wrong first is first
        if self.f_mean - self.s_mean < 0:
            self.fix()

        self.t_model = sm.OLS(self.t_y, self.t_x).fit()
        self.t_params = self.t_model.params.drop(self.by)
        self.f_model = sm.OLS(self.f_y, self.f_x).fit()
        self.s_model = sm.OLS(self.s_y, self.s_x).fit()
            
        self.unexplained = (self.f_x.mean() @ (self.f_model.params - self.t_params)) + (self.s_x.mean() @ (self.t_params - self.s_model.params))

        self.explained = (self.f_x.mean() - self.s_x.mean()) @ self.t_params
        
        self.two_gap = self.f_mean - self.s_mean
        
        if round_val != False:
            self.unexplained = round(self.unexplained, round_val)
            self.explained = round(self.explained, round_val)
            self.two_gap = round(self.two_gap, round_val)
       
        print('Unexplained Effect: {}'.format(self.unexplained))
        print('Explained Effect: {}'.format(self.explained))
        print('Gap: {}'.format(self.two_gap))
        if plot == True:
            self.plot(plt_type = 2)

        return self.unexplained, self.explained, self.two_gap


    def var(self):
        #Calculates the variance of the model
        #This is an attempt to check to see if the models have not been fit
        if len(self.f_model.params) == 0 and len(self.s_model.params) == 0:
            raise ValueError("Please fit the model before you use this command")
        #I will use this value several times, so I will store it.
        
        f_x_mean = self.f_x.mean()
        s_x_mean = self.s_x.mean()

        #Calculate the f centered matrix, then use a estimator to calculate the variance of x
        f_cov = self.f_x - 1 * f_x_mean
        f_cov = (f_cov.T @ f_cov) / (len(f_cov) * (len(f_cov) - 1))
        
        #Same here for S
        s_cov = self.s_x - 1 * s_x_mean
        s_cov = (s_cov.T @ s_cov) / (len(s_cov) * (len(s_cov) -1))

        f_1 = (f_x_mean - s_x_mean) @ self.f_model.cov_params() @ (f_x_mean - s_x_mean)
        f_2 = self.f_model.params @ (f_cov + s_cov) @ self.f_model.params

        s_1 = s_x_mean @ (self.f_model.cov_params() + self.s_model.cov_params()) @ s_x_mean
        s_2 = (self.f_model.params - self.s_model.params) @ s_cov @ (self.f_model.params - self.s_model.params)   
        
        f_val = f_1 + f_2
        s_val = s_1 + s_2

        print("Characteristic Effect Variance: {}".format(f_val))
        print("Coefficient Effect Variance: {}".format(s_val))
        return (f_val), (s_val)


    def cotton_model(self, plot = True, round_val = 5):
        #This adjusts for over representation

        #This checks to see if the model has been fitted yet.
        if len(self.f_model.params) == 0 and len(self.s_model.params) == 0:
            raise ValueError("Please fit the model before using it")
        
        if round_val != False:
            try:
                round_val = int(round_val)
            except ValueError:
                raise ValueError("Your round value must either by an int or be able to be casted into one.")

        self.cotton_fix_model = (len(self.f_x) / (len(self.f_x) + len(self.s_x))) * self.f_model.params + ((len(self.s_x) / (len(self.f_x) + len(self.s_x))) * self.s_model.params)

        self.cotton_unexplained = (self.f_x.mean() @ (self.f_model.params - self.cotton_fix_model)) + (self.s_x.mean() @ (self.cotton_fix_model - self.s_model.params))

        self.cotton_explained = (self.f_x.mean() - self.s_x.mean()) @ self.cotton_fix_model
        
        if round_val != False:
            self.cotton_unexplained = round(self.cotton_unexplained, round_val)
            self.cotton_explained = round(self.cotton_explained, round_val)

        print('Unexplained Effect with Cotton Model: {}'.format(self.cotton_unexplained))
        print('Explained Effect with Cotton Model: {}'.format(self.cotton_explained))
        print('Gap: {}'.format(self.two_gap))
        if plot == True:
            self.plot(plt_type = 4)

        return self.cotton_unexplained, self.cotton_explained, self.two_gap


    def plot(self, plt_type = 3, fig_size = (6,10), xlabel = '', ylabel = 'Oaxaca Values', color1 = 'seagreen', color2 = 'darkturquoise', color3 = 'steelblue', color4 = 'navy'):
        
        #the plot types must either be able to made into an int or be an int
        try:
            plt_type = int(plt_type)
        except ValueError:
            raise ValueError('The plot type must be an integer.')

        #we only have two types of plots, 3 or 2, so it must be one of the two
        if plt_type != 3 and plt_type != 2 and plt_type != 4:
            raise ValueError("The plot types must be two, three, or four")

        #all the colors and labels must be strings
        if any(map((lambda value: type(value) != str), (xlabel, ylabel, color1, color2, color3, color4))):
            raise ValueError('All labels and colors must be strings.')
        
        #This sets the xlabel if default
        if xlabel == '':
            if plt_type == 3:
                xlabel = 'Three-Fold Oaxaca Plot'
            elif plt_type == 2:
                xlabel = 'Two-Fold Oaxaca Plot'
            elif plt_type == 4:
                xlabel = 'Cotton Model Oaxaca Plot'

        if plt_type == 2:
            if self.explained == 0 and self.unexplained == 0:
                raise ValueError("Please fit the values before attempting to plot")
                
        if plt_type == 3:
            if self.char_eff == 0 and self.coef_eff == 0:
                raise ValueError("Please fit the values before attempting to plot")
        
        if plt_type == 4:
            if self.cotton_explained == 0 and self.cotton_unexplained == 0:
                raise ValueError("Please fit the values before attempting to plot")
        
        #this is the three_fold plot
        if plt_type == 3:
            fig, ax = plt.subplots(figsize = fig_size)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.bar(x= 0, height = self.char_eff, width = .25, label = 'Character Effect', color = color1)
            plt.bar(x=0, height = self.coef_eff, bottom= self.char_eff, width = .25, label = 'Coefficent Effect', color = color2)
            plt.bar(x=0, height = -self.int_eff, width = .25, label = 'Interaction Effect', color = color3)
            plt.bar(x = .25, height = self.three_gap, width = .25, label = 'Total Gap', color = color4)
            plt.ylim(top = self.three_gap + .15)
            plt.xlim([-.2,.5])
            plt.axhline(y=0, color = 'k', linestyle = '--')
            ax.grid(zorder=0)
            plt.legend()

        #this is a two_fold plot
        if plt_type == 2:
            fig, ax = plt.subplots(figsize = fig_size)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.bar(x= 0, height = self.explained, width = .25, label = 'Explained', color = color1)
            plt.bar(x=0, height = self.unexplained, bottom= self.explained, width = .25, label = 'Unexplained', color = color2)
            plt.bar(x = .25, height = self.two_gap, width = .25, label = 'Total Gap', color = color3)
            plt.ylim(top = self.two_gap + .15)
            plt.xlim([-.2,.5])
            plt.axhline(y=0, color = 'k', linestyle = '--')
            ax.grid(zorder=0)
            plt.legend()
        
        #this is the cotton model plot
        if plt_type == 4:
            fig, ax = plt.subplots(figsize = fig_size)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.bar(x= 0, height = self.cotton_explained, width = .25, label = 'Cotton Model Explained', color = color1)
            plt.bar(x=0, height = self.cotton_unexplained, bottom= self.cotton_explained, width = .25, label = 'Cotton Model Unexplained', color = color2)
            plt.bar(x = .25, height = self.two_gap, width = .25, label = 'Total Gap', color = color3)
            plt.ylim(top = self.two_gap + .15)
            plt.xlim([-.2,.5])
            plt.axhline(y=0, color = 'k', linestyle = '--')
            ax.grid(zorder=0)
            plt.legend()


    def fit(self, two_fold = False, three_fold = False , plot = False, round_val = 5):
        if two_fold == True:
            self.two_fold(plot = plot, round_val = 5)
        if three_fold == True:
            self.three_fold(plot = plot, round_val = 5)



#%%





#%%

df_clean = df3.dropna(subset=['sex_of_person_2FemaleQ', 'loghourly_wage'])  # Clean missing data
df_clean = df_clean[df_clean['sex_of_person_2FemaleQ'].isin([0, 1])]        # Keep only 0 and 1 for the group variable

# Assign dependent and independent variables
y_test = df_clean['loghourly_wage']  # Outcome variable
X_test = df_clean[['age_at_last_birthday', 'age_at_last_birthday2', 'PUBLIC',  # Predictor variables
          'ever_completed_any_technical_vocational_training', 'literacy_1_1.0',
          'literacy_1_2.0', 'current_marital_status_1.0', 'current_marital_status_2.0',
          'current_marital_status_3.0', 'current_marital_status_4.0', 'edu_1',
          'edu_2', 'edu_3', 'edu_4', 'first_digit', 'first_two_digits',
          'first_three_digits', 'fourty_digit', 'Method2_Formal_1', 'Method2_Formal_2',
          'Formal_0', 'Formal_1', 'PUBLIC', 'PRIVATE', 'children5_Ne',
          'children12_Ne', 'Industry_1.0', 'Industry_2.0', 'Industry_3.0',
          'Industry_4.0', 'Industry_5.0', 'occupations_code_18_1.0',
          'occupations_code_18_2.0', 'occupations_code_18_3.0', 'occupations_code_18_4.0',
          'occupations_code_18_5.0', 'occupations_code_18_6.0', 'occupations_code_18_7.0',
          'occupations_code_18_8.0', 'ever_completed_any_technical_vocational_training_0.0',
          'ever_completed_any_technical_vocational_training_1.0', 'ever_completed_any_technical_vocational_training_2.0',
          'sex_of_person_2FemaleQ']]  # Group variable

group_test = df_clean['sex_of_person_2FemaleQ']  # Group for Oaxaca decomposition

# Fit the Oaxaca model
model = Oaxaca(df_clean, 'sex_of_person_2FemaleQ', 'loghourly_wage')
model.fit(two_fold=True, plot=True)

#%%  update ols regre table 5-10

f_datafull = df2_fulltime


f_datafull['loghourly_wage']= np.log1p(f_datafull['hourly_wage'])
f_datafull['logminimum_wage_annual_real']= np.log1p(f_datafull['minimum_wage_annual_real'])
#%
f_datafull['logAnnual_Earnings']= np.log1p(f_datafull['Annual_Earnings'])
f_datafull['logtotal_hours']= np.log1p(f_datafull['total_hours'])


f_datafull['logtotal_hours_annual']= np.log1p(f_datafull['total_hours_annual'])

f_datafull['sex_of_person_2.0Timeslogminimum_wage_annual_real'] = f_datafull['sex_of_person_2.0'] * f_datafull['logminimum_wage_annual_real']
f_datafull['sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real'] = f_datafull['sex_of_person_2.0'] * f_datafull['Lowedu_1'] * f_datafull['logminimum_wage_annual_real']

f_datafull['sex_of_person_2.0Times_Lowedu_1'] = f_datafull['sex_of_person_2.0'] * f_datafull['Lowedu_1'] 


f_datafull['Lowedu_1Timeslogminimum_wage_annual_real'] = f_datafull['Lowedu_1'] * f_datafull['logminimum_wage_annual_real']
f_datafull['current_marital_status_2.0Timeslogminimum_wage_annual_real'] = f_datafull['current_marital_status_2.0'] * f_datafull['logminimum_wage_annual_real']
f_datafull['sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real'] = f_datafull['sex_of_person_2.0'] *  f_datafull['current_marital_status_2.0'] * f_datafull['logminimum_wage_annual_real']

f_datafull['sex_of_person_2.0Timescurrent_marital_status_2.0'] = f_datafull['sex_of_person_2.0'] *  f_datafull['current_marital_status_2.0'] 

f_datafull['yeartimesfirst_digit'] = f_datafull['first_digit'] * f_datafull['yeardclust']


f_datafull['post1997'] = 0

# Set values based on conditions
f_datafull.loc[f_datafull['yeardclust'] >=1997, 'post1997'] = 1  # post1997
f_datafull.loc[f_datafull['yeardclust'] < 1997, 'post1997'] = 2  # before 1997

#%% given eductaion categories I want to crear 4 dummies:
dummy_vars = pd.get_dummies(f_datafull['post1997'], prefix='post1997').astype(int)
#%% add thes new variables  (lowedu_0, lowedu_1   etc)
f_datafull = pd.concat([f_datafull, dummy_vars], axis=1)
#%% add indicator post 1997
f_datafull['post1997logminimum_wage_annual_real']= np.log1p(f_datafull['minimum_wage_annual_real']) *  f_datafull['post1997_1']
f_datafull['post1997sex_of_person_2.0Timeslogminimum_wage_annual_real'] = f_datafull['sex_of_person_2.0'] * f_datafull['logminimum_wage_annual_real'] *  f_datafull['post1997_1']
f_datafull['post1997sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real'] = f_datafull['sex_of_person_2.0'] * f_datafull['Lowedu_1'] * f_datafull['logminimum_wage_annual_real']  *  f_datafull['post1997_1']
f_datafull['post1997sex_of_person_2.0Times_Lowedu_1'] = f_datafull['sex_of_person_2.0'] * f_datafull['Lowedu_1']  *  f_datafull['post1997_1']
f_datafull['post1997Lowedu_1Timeslogminimum_wage_annual_real'] = f_datafull['Lowedu_1'] * f_datafull['logminimum_wage_annual_real'] *  f_datafull['post1997_1']
f_datafull['post1997current_marital_status_2.0Timeslogminimum_wage_annual_real'] = f_datafull['current_marital_status_2.0'] * f_datafull['logminimum_wage_annual_real']   *  f_datafull['post1997_1']
f_datafull['post1997sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real'] = f_datafull['sex_of_person_2.0'] *  f_datafull['current_marital_status_2.0'] * f_datafull['logminimum_wage_annual_real']   *  f_datafull['post1997_1']

f_datafull['year22zz'] = f_datafull['yeardclust']

#%%
f_datafull['yeardclusttimeoccupations_code_18'] = f_datafull['year22zz'].astype(str) + f_datafull['occupations_code_18'].astype(str)
f_datafull['yeardclusttimeIndustry'] = f_datafull['year22zz'].astype(str)  + f_datafull['Industry'].astype(str)
f_datafull['yeardclusttimeIndustrytimeoccupations_code_18'] = f_datafull['year22zz'].astype(str)  + f_datafull['Industry'].astype(str) + f_datafull['occupations_code_18'].astype(str)

f_datafull['yeardclusttimeIndustrytimeoccupations_code_18timesfirst_digit']  = f_datafull['year22zz'].astype(str)  + f_datafull['Industry'].astype(str) + f_datafull['occupations_code_18'].astype(str)     + f_datafull['first_digit'].astype(str)

#%%


data_df2024 = df2_fulltime


#%%  group by district year 





columns_to_average = ['total_hours','Annual_Earnings',
'edu_1','edu_2','edu_3','edu_4', 'Lowedu_1',
'current_marital_status_1.0','current_marital_status_2.0',
'current_marital_status_3.0','current_marital_status_4.0',   
'literacy_1_1.0','literacy_1_2.0',
'Method2_Formal_1','Method2_Formal_2',
'total_hours_annual','total_hours_monthly',
'minimum_wage','minimum_wage_annual','minimum_wage_monthly',
'minimum_wageRegional','minimum_wageRegional_annual','minimum_wageRegional_monthly',
'cpi',
'Annual_Earnings_real','monthly_Earnings_real',
'minimum_wageRegional_annual_real','minimum_wageRegional_monthly_real',
'minimum_wage_annual_real','minimum_wage_monthly_real',
'PUBLIC',
'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
'occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
'occupations_code_18_7.0','occupations_code_18_8.0',
'hourly_wage','sex_of_person_2FemaleQ']








df_grouped_by_year = data_df2024.groupby(['yeardclust','first_three_digits'])[columns_to_average].mean().reset_index()


#%%
# save data to stata dta
df2_fulltime.to_stata('ToSend_MG_clean_fulltime.dta', write_index=False)
# Step 2: Convert and save the DataFrame to a Stata .dta file
df_grouped_by_year.to_stata('Aggregdata_District_year.dta', write_index=False)







#%%   regression district level data


# in logs 



df_grouped_by_year['loghourly_wage']= np.log1p(df_grouped_by_year['hourly_wage'])

df_grouped_by_year['logminimum_wage_annual_real']= np.log1p(df_grouped_by_year['minimum_wage_annual_real'])
#%%
df_grouped_by_year['logsex_of_person_2FemaleQ']= np.log1p(df_grouped_by_year['sex_of_person_2FemaleQ'])

df_grouped_by_year['logPUBLIC']= np.log1p(df_grouped_by_year['PUBLIC'])

df_grouped_by_year['logIndustry_1.0']= np.log1p(df_grouped_by_year['Industry_1.0'])
df_grouped_by_year['logIndustry_2.0']= np.log1p(df_grouped_by_year['Industry_2.0'])
df_grouped_by_year['logIndustry_3.0']= np.log1p(df_grouped_by_year['Industry_3.0'])
df_grouped_by_year['logIndustry_4.0']= np.log1p(df_grouped_by_year['Industry_4.0'])
df_grouped_by_year['logIndustry_5.0']= np.log1p(df_grouped_by_year['Industry_5.0'])

df_grouped_by_year['logoccupations_code_18_1.0']= np.log1p(df_grouped_by_year['occupations_code_18_1.0'])
df_grouped_by_year['logoccupations_code_18_2.0']= np.log1p(df_grouped_by_year['occupations_code_18_2.0'])
df_grouped_by_year['logoccupations_code_18_3.0']= np.log1p(df_grouped_by_year['occupations_code_18_3.0'])
df_grouped_by_year['logoccupations_code_18_4.0']= np.log1p(df_grouped_by_year['occupations_code_18_4.0'])
df_grouped_by_year['logoccupations_code_18_5.0']= np.log1p(df_grouped_by_year['occupations_code_18_5.0'])
df_grouped_by_year['logoccupations_code_18_6.0']= np.log1p(df_grouped_by_year['occupations_code_18_6.0'])
df_grouped_by_year['logoccupations_code_18_7.0']= np.log1p(df_grouped_by_year['occupations_code_18_7.0'])
df_grouped_by_year['logoccupations_code_18_8.0']= np.log1p(df_grouped_by_year['occupations_code_18_8.0'])

df_grouped_by_year['logMethod2_Formal_1']= np.log1p(df_grouped_by_year['Method2_Formal_1'])
df_grouped_by_year['logMethod2_Formal_2']= np.log1p(df_grouped_by_year['Method2_Formal_2'])

df_grouped_by_year['logAnnual_Earnings_real']= np.log1p(df_grouped_by_year['Annual_Earnings_real'])

#%%


df_grouped_by_year['yeardclust22'] = df_grouped_by_year['yeardclust']
#%%

df_grouped_by_year = df_grouped_by_year.set_index(['yeardclust', 'first_three_digits'])
#%%

# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real'],
                  ['logminimum_wage_annual_real','logPUBLIC'],                  
                  ['logminimum_wage_annual_real','logPUBLIC','logsex_of_person_2FemaleQ'],
                  ['logminimum_wage_annual_real','logPUBLIC','logsex_of_person_2FemaleQ','logMethod2_Formal_2'],                 
                  ['logminimum_wage_annual_real','logPUBLIC','logsex_of_person_2FemaleQ','logMethod2_Formal_2','logIndustry_1.0','logIndustry_2.0','logIndustry_3.0','logIndustry_4.0','logIndustry_5.0'],
                  ['logminimum_wage_annual_real','logPUBLIC','logsex_of_person_2FemaleQ','logMethod2_Formal_2', 'logoccupations_code_18_1.0','logoccupations_code_18_2.0','logoccupations_code_18_3.0',
                  'logoccupations_code_18_4.0','logoccupations_code_18_5.0','logoccupations_code_18_6.0',
                  'logoccupations_code_18_7.0','logoccupations_code_18_8.0']]


exog_list = [sm.add_constant(df_grouped_by_year[exog_vars]) for exog_vars in exog_vars_list]

# Store all the results in a list
results_list = []




for exog in exog_list:
    # Run the regression
    cons = PanelOLS(df_grouped_by_year.loghourly_wage, exog, entity_effects=False, time_effects=False,  check_rank=False)
    results = cons.fit( cov_type="clustered", clusters=df_grouped_by_year['yeardclust22'] ) #cov_type='robust')    #cov_type="clustered", clusters=df_grouped_by_year['yeardclust22'] 
    results_list.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list])

# Customize table appearance if needed
stargazer.title("Regression Results")
stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3','Model 4', 'Model 5', 'Model 6'], [1, 1, 1, 1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("District_miniwage.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)    
    
    
    
#%%




import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde


Femalesample = f_datafull.drop(f_datafull[(f_datafull['sex_of_person_2.0'] == 0 ) ].index)
Malesample = f_datafull.drop(f_datafull[(f_datafull['sex_of_person_2.0'] == 1 ) ].index)



#def drop_percent(data, low_percent=0.1, high_percent=0.9):
#    low_cutoff = np.percentile(data, low_percent*100)
#    high_cutoff = np.percentile(data, high_percent*100)
#    return data[(data >= low_cutoff) & (data <= high_cutoff)]


# Data points
data3 = Femalesample['loghourly_wage'].to_numpy()
data4 = Malesample['loghourly_wage'].to_numpy()

# Drop the bottom 10% and top 10% of data  _filtered
#data3 = drop_percent(data3)
#data4 = drop_percent(data4)


# Create a Kernel Density Estimate
kde3 = gaussian_kde(data3, bw_method=0.15)
kde4 = gaussian_kde(data4, bw_method=0.15)

xi3 = np.linspace(min(data3), max(data3), 100)
xi4 = np.linspace(min(data4), max(data4), 100)

f3 = kde3(xi3)
f4 = kde4(xi4)

# Plot the KDE
fig = plt.figure() 

plt.plot(xi3, f3, linewidth=2, color='#020F59', label='Female')
plt.plot(xi4, f4, linewidth=2, color='#D92344', label='Male')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)

plt.xlabel('log hourly earnings', fontsize=14)
plt.ylabel('Density', fontsize=14)
#plt.title('(B) H', fontsize=18)
plt.xlim(left=0)  # Force x-axis to start from 0



 
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=14) 
plt.tight_layout()

#ax = plt.gca()
#ax.yaxis.get_offset_text().set_size(8)
#ax.tick_params(axis='both', which='major', labelsize=8)

plt.show()
fig.savefig('NEWCFacts33N.pdf', bbox_inches='tight')



#%%


import numpy
from matplotlib import pyplot

y22 = Femalesample['loghourly_wage'].to_numpy()
y11 = Malesample['loghourly_wage'].to_numpy()
#%%  #8C1822
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)

fig = plt.figure() 


#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('earningsgend.pdf',format='pdf', dpi=300)
plt.show()


#%% 2018


y22 = Femalesample[Femalesample['yeardclust']== 2018]
y11 = Malesample[Malesample['yeardclust']== 2018]

y22 = y22['loghourly_wage'].to_numpy()
y11 = y11['loghourly_wage'].to_numpy()

#%% select 2021 only 

#y22 = y22[y22['yeardclust']== 2021]
#y11 = y11[y11['yeardclust']== 2021]

#%%  #8C1822
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)

fig = plt.figure() 


#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('2018earningsgend.pdf',format='pdf', dpi=300)
plt.show()


#%% 
y22 = Femalesample[Femalesample['yeardclust']==2015]
y11 = Malesample[Malesample['yeardclust']==2015]

y22 = y22['loghourly_wage'].to_numpy()
y11 = y11['loghourly_wage'].to_numpy()



#%%  #8C1822
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)

fig = plt.figure() 


#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('2015earningsgend.pdf',format='pdf', dpi=300)
plt.show()
#%%


#%% 
y22 = Femalesample[Femalesample['yeardclust']==2019]
y11 = Malesample[Malesample['yeardclust']==2019]

y22 = y22['loghourly_wage'].to_numpy()
y11 = y11['loghourly_wage'].to_numpy()



#%%  #8C1822
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)

fig = plt.figure() 


#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('2019earningsgend.pdf',format='pdf', dpi=300)
plt.show()



#%% industry   y22 = Femalesample[Femalesample['industry'] == 2]['loghourly_wage'].to_numpy()



y22 = Femalesample[Femalesample['Industry_1.0'] == 1]['loghourly_wage'].to_numpy()
y11 = Malesample[Malesample['Industry_1.0'] == 1]['loghourly_wage'].to_numpy()
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)
fig = plt.figure() 
#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('earningsgendINDU1.pdf',format='pdf', dpi=300)
plt.show()



y22 = Femalesample[Femalesample['Industry_2.0'] == 1]['loghourly_wage'].to_numpy()
y11 = Malesample[Malesample['Industry_2.0'] == 1]['loghourly_wage'].to_numpy()
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)
fig = plt.figure() 
#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('earningsgendINDU2.pdf',format='pdf', dpi=300)
plt.show()



y22 = Femalesample[Femalesample['Industry_3.0'] == 1]['loghourly_wage'].to_numpy()
y11 = Malesample[Malesample['Industry_3.0'] == 1]['loghourly_wage'].to_numpy()
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)
fig = plt.figure() 
#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('earningsgendINDU3.pdf',format='pdf', dpi=300)
plt.show()



y22 = Femalesample[Femalesample['Industry_4.0'] == 1]['loghourly_wage'].to_numpy()
y11 = Malesample[Malesample['Industry_4.0'] == 1]['loghourly_wage'].to_numpy()
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)
fig = plt.figure() 
#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('earningsgendINDU4.pdf',format='pdf', dpi=300)
plt.show()



y22 = Femalesample[Femalesample['Industry_5.0'] == 1]['loghourly_wage'].to_numpy()
y11 = Malesample[Malesample['Industry_5.0'] == 1]['loghourly_wage'].to_numpy()
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)
fig = plt.figure() 
#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('earningsgendINDU5.pdf',format='pdf', dpi=300)
plt.show()



#%%  occupations



#'logoccupations_code_18_1.0','logoccupations_code_18_2.0','logoccupations_code_18_3.0',
#'logoccupations_code_18_4.0','logoccupations_code_18_5.0','logoccupations_code_18_6.0',
#'logoccupations_code_18_7.0','logoccupations_code_18_8.0'


y22 = Femalesample[Femalesample['occupations_code_18_1.0'] == 1]['loghourly_wage'].to_numpy()
y11 = Malesample[Malesample['occupations_code_18_1.0'] == 1]['loghourly_wage'].to_numpy()
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)
fig = plt.figure() 
#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('earningsgendOCCUP1.pdf',format='pdf', dpi=300)
plt.show()



y22 = Femalesample[Femalesample['occupations_code_18_2.0'] == 1]['loghourly_wage'].to_numpy()
y11 = Malesample[Malesample['occupations_code_18_2.0'] == 1]['loghourly_wage'].to_numpy()
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)
fig = plt.figure() 
#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('earningsgendOCCUP2.pdf',format='pdf', dpi=300)
plt.show()




y22 = Femalesample[Femalesample['occupations_code_18_3.0'] == 1]['loghourly_wage'].to_numpy()
y11 = Malesample[Malesample['occupations_code_18_3.0'] == 1]['loghourly_wage'].to_numpy()
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)
fig = plt.figure() 
#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('earningsgendOCCUP3.pdf',format='pdf', dpi=300)
plt.show()




y22 = Femalesample[Femalesample['occupations_code_18_4.0'] == 1]['loghourly_wage'].to_numpy()
y11 = Malesample[Malesample['occupations_code_18_4.0'] == 1]['loghourly_wage'].to_numpy()
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)
fig = plt.figure() 
#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('earningsgendOCCUP4.pdf',format='pdf', dpi=300)
plt.show()




y22 = Femalesample[Femalesample['occupations_code_18_5.0'] == 1]['loghourly_wage'].to_numpy()
y11 = Malesample[Malesample['occupations_code_18_5.0'] == 1]['loghourly_wage'].to_numpy()
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)
fig = plt.figure() 
#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('earningsgendOCCUP5.pdf',format='pdf', dpi=300)
plt.show()



y22 = Femalesample[Femalesample['occupations_code_18_6.0'] == 1]['loghourly_wage'].to_numpy()
y11 = Malesample[Malesample['occupations_code_18_6.0'] == 1]['loghourly_wage'].to_numpy()
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)
fig = plt.figure() 
#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('earningsgendOCCUP6.pdf',format='pdf', dpi=300)
plt.show()






y22 = Femalesample[Femalesample['occupations_code_18_7.0'] == 1]['loghourly_wage'].to_numpy()
y11 = Malesample[Malesample['occupations_code_18_7.0'] == 1]['loghourly_wage'].to_numpy()
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)
fig = plt.figure() 
#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('earningsgendOCCUP7.pdf',format='pdf', dpi=300)
plt.show()






y22 = Femalesample[Femalesample['occupations_code_18_8.0'] == 1]['loghourly_wage'].to_numpy()
y11 = Malesample[Malesample['occupations_code_18_8.0'] == 1]['loghourly_wage'].to_numpy()
y22_log = y22  # log1p is used to handle log(0) by computing log(1 + x)
y11_log = y11  # log1p is used to handle log(0) by computing log(1 + x)
fig = plt.figure() 
#pyplot.hist(y22_log, bins=50, alpha=0.7, color = '#0F95D7',density = True)
pyplot.hist(y22_log, bins=65, alpha=0.9, color = '#020F59', label='Female', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=65, alpha=0.7, color = '#0F95D7', label='Male' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('earningsgendOCCUP8.pdf',format='pdf', dpi=300)
plt.show()





#%%

Femalesample = Femalesample[Femalesample['yeardclust'] != 2021]
#%%
Malesample = Malesample[Malesample['yeardclust'] != 2021]
#%%
f_datafullz = f_datafull[f_datafull['yeardclust'] != 2021]


#%%

bb1 = Femalesample.groupby('yeardclust')['loghourly_wage'].median()
#%%
bb2 = Malesample.groupby('yeardclust')['loghourly_wage'].median()
#%%
bb3 = f_datafullz.groupby('yeardclust')['loghourly_wage'].median()



fig = plt.figure() 

#ax.set(xlim = (0,2000000))  # 1400 Billion $
#xlabels = ['{:,.0f}'.format(x)  for x in ax.get_xticks()/1000]
#ax.set_xticklabels(xlabels)


#ax.set(ylim = (-400,430000))   # 4 Million $ after removing outliers
#ylabels = ['{:,.0f}'.format(y)  for y in ax.get_yticks()/100000]
#ax.set_yticklabels(ylabels)


plt.plot(bb1.index,bb1, color= '#A60303', linewidth=2, label='Female',  marker='D')
plt.plot(bb2.index,bb2, color='#022859', linewidth=2, linestyle='-',  label='Male' ,marker='o')
plt.plot(bb3.index,bb3, color='#035AA6', linewidth=2, label='Full sample',  marker='^')
plt.ticklabel_format(style='plain', axis='y')

#x =np.linspace(ax[0],ax[1]+0.01)
#plt.plot(x, model.params[0] + model.params[1] * x,'b',lw=2)
plt.grid(True)
plt.xlabel(r'years',fontsize = 16)
plt.ylabel(r'Earnings',fontsize = 16)
# Add annotations
#for stalp, (income, loans) in descriptx_datadf1456.groupby('stalp')[['perincome', 'drcon']].mean().iterrows():
#    plt.annotate(stalp, (income, loans), textcoords="offset points", xytext=(5,5), ha='center', fontsize=8)
    
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)

#plt.title('(B) H', fontsize=18)

 
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=14) 
plt.tight_layout()

plt.axis('tight')


    
plt.show()
fig.savefig('NEWFacts22N.pdf', bbox_inches='tight')
    
    
    
#%% try mean 




bb1 = Femalesample.groupby('yeardclust')['loghourly_wage'].mean()
#%%
bb2 = Malesample.groupby('yeardclust')['loghourly_wage'].mean()
#%%
bb3 = f_datafull.groupby('yeardclust')['loghourly_wage'].mean()



fig = plt.figure() 

#ax.set(xlim = (0,2000000))  # 1400 Billion $
#xlabels = ['{:,.0f}'.format(x)  for x in ax.get_xticks()/1000]
#ax.set_xticklabels(xlabels)


#ax.set(ylim = (-400,430000))   # 4 Million $ after removing outliers
#ylabels = ['{:,.0f}'.format(y)  for y in ax.get_yticks()/100000]
#ax.set_yticklabels(ylabels)


plt.plot(bb1.index,bb1, color= '#A60303', linewidth=2, label='Female',marker='D'  )
plt.plot(bb2.index,bb2, color='#022859', linewidth=2, linestyle='--',  label='Male',marker='o'  )
plt.plot(bb3.index,bb3, color='#035AA6', linewidth=2, label='Full sample,marker',marker='^')
plt.ticklabel_format(style='plain', axis='y')

#x =np.linspace(ax[0],ax[1]+0.01)
#plt.plot(x, model.params[0] + model.params[1] * x,'b',lw=2)
plt.grid(True)
plt.xlabel(r'years',fontsize = 16)
plt.ylabel(r'Earnings',fontsize = 16)
# Add annotations
#for stalp, (income, loans) in descriptx_datadf1456.groupby('stalp')[['perincome', 'drcon']].mean().iterrows():
#    plt.annotate(stalp, (income, loans), textcoords="offset points", xytext=(5,5), ha='center', fontsize=8)
    
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)

#plt.title('(B) H', fontsize=18)

 
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=14) 
plt.tight_layout()

plt.axis('tight')


    
plt.show()
fig.savefig('NEWFacts22NMEAN.pdf', bbox_inches='tight')
    
   #
#%% annual earnings   real 

#'total_hours_annual','total_hours_monthly',
#'minimum_wage','minimum_wage_annual','minimum_wage_monthly',
#'minimum_wageRegional','minimum_wageRegional_annual','minimum_wageRegional_monthly',
#'cpi',
#'Annual_Earnings_real','monthly_Earnings_real',
#'minimum_wageRegional_annual_real','minimum_wageRegional_monthly_real',
#'minimum_wage_annual_real'


Femalesample = Femalesample[Femalesample['yeardclust'] != 2021]
#%%
Malesample = Malesample[Malesample['yeardclust'] != 2021]
#%%
f_datafullz = f_datafull[f_datafull['yeardclust'] != 2021]


#%%

bb1 = Femalesample.groupby('yeardclust')['Annual_Earnings_real'].mean()
#%%
bb2 = Malesample.groupby('yeardclust')['Annual_Earnings_real'].mean()
#%%
bb3 = f_datafullz.groupby('yeardclust')['Annual_Earnings_real'].mean()
#%%
bb4 = f_datafullz.groupby('yeardclust')['minimum_wage_annual_real'].mean()



fig = plt.figure() 

#ax.set(xlim = (0,2000000))  # 1400 Billion $
#xlabels = ['{:,.0f}'.format(x)  for x in ax.get_xticks()/1000]
#ax.set_xticklabels(xlabels)


#ax.set(ylim = (-400,430000))   # 4 Million $ after removing outliers
#ylabels = ['{:,.0f}'.format(y)  for y in ax.get_yticks()/100000]
#ax.set_yticklabels(ylabels)


plt.plot(bb1.index,bb1/1000, color= '#A60303', linewidth=2, linestyle='-', label='Female',marker='D' )
plt.plot(bb2.index,bb2/1000, color='#035AA6', linewidth=2, linestyle='-',  label='Male',marker='o' )
plt.plot(bb3.index,bb3/1000, color='#022859', linewidth=2, linestyle='-',label='Full sample',marker='^')
plt.plot(bb4.index,bb4/1000, color='#022859', linewidth=2, linestyle='--', label='Minimum wage',marker='s')


plt.ticklabel_format(style='plain', axis='y')

#x =np.linspace(ax[0],ax[1]+0.01)
#plt.plot(x, model.params[0] + model.params[1] * x,'b',lw=2)
plt.grid(True)
plt.xlabel(r'Years',fontsize = 12)
plt.ylabel(r'real value (in 000 rs/annual)',fontsize = 12)
# Add annotations
#for stalp, (income, loans) in descriptx_datadf1456.groupby('stalp')[['perincome', 'drcon']].mean().iterrows():
#    plt.annotate(stalp, (income, loans), textcoords="offset points", xytext=(5,5), ha='center', fontsize=8)
    
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)

#plt.title('(B) H', fontsize=18)
plt.tight_layout()

plt.axis('tight')

 
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.legend()
plt.legend(fontsize=12) 

# Set tight axis limits
ax = plt.gca()  # Get the current axis

ax.set_xlim(1992,2019)  # Automatically adjust x limits based on the data
ax.set_ylim(auto=True)  # Automatically adjust y limits based on the data


    
plt.show()
fig.savefig('NEWFacts22Nannual_Earnings_real.pdf', bbox_inches='tight')

# report to excel

ZQ1 = pd.concat([bb1, bb2, bb4, bb3], axis=1)
ZQ1.to_csv('Figure1_data1.csv', index =False)

#%% plot mimimu wage real only 


fig = plt.figure() 

#ax.set(xlim = (0,2000000))  # 1400 Billion $
#xlabels = ['{:,.0f}'.format(x)  for x in ax.get_xticks()/1000]
#ax.set_xticklabels(xlabels)


#ax.set(ylim = (-400,430000))   # 4 Million $ after removing outliers
#ylabels = ['{:,.0f}'.format(y)  for y in ax.get_yticks()/100000]
#ax.set_yticklabels(ylabels)


#plt.plot(bb1.index,bb1/1000, color= '#A60303', linewidth=2, linestyle='-', label='Female',marker='D' )
#plt.plot(bb2.index,bb2/1000, color='#035AA6', linewidth=2, linestyle='-',  label='Male',marker='o' )
#plt.plot(bb3.index,bb3/1000, color='#022859', linewidth=2, linestyle='-',label='Full sample',marker='^')
plt.plot(bb4.index,bb4/1000, color='#022859', linewidth=2, linestyle='--',marker='s')


plt.ticklabel_format(style='plain', axis='y')

#x =np.linspace(ax[0],ax[1]+0.01)
#plt.plot(x, model.params[0] + model.params[1] * x,'b',lw=2)
plt.grid(True)
plt.xlabel(r'Years',fontsize = 12)
plt.ylabel(r'real value (in 000 rs/annual)',fontsize = 12)
# Add annotations
#for stalp, (income, loans) in descriptx_datadf1456.groupby('stalp')[['perincome', 'drcon']].mean().iterrows():
#    plt.annotate(stalp, (income, loans), textcoords="offset points", xytext=(5,5), ha='center', fontsize=8)
    
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)

#plt.title('(B) H', fontsize=18)
plt.tight_layout()

plt.axis('tight')

 
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.legend()
plt.legend(fontsize=12) 

# Set tight axis limits
ax = plt.gca()  # Get the current axis

ax.set_xlim(1992,2019)  # Automatically adjust x limits based on the data
ax.set_ylim(auto=True)  # Automatically adjust y limits based on the data


    
plt.show()
fig.savefig('Minwageannual_realonly.pdf', bbox_inches='tight')










#%%  female only 


f_datafull_Femalesample = f_datafull.drop(f_datafull[(f_datafull['sex_of_person_2.0'] == 0 ) ].index)
f_datafull_Malesample = f_datafull.drop(f_datafull[(f_datafull['sex_of_person_2.0'] == 1 ) ].index)

#%% 'first_digit','yeartimesfirst_digit',


# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real',
                   #'first_three_digits' ,
                   'first_digit',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                   'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                   'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                   'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                   ,'age_at_last_birthday2'
                   ],
                  ['logminimum_wage_annual_real',
                   #'first_three_digits' ,
                   'first_digit',
                   'Lowedu_1','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real',
                   #'first_three_digits' ,
                   'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],              
                  ['logminimum_wage_annual_real',
                   #'first_three_digits' ,
                   'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real', 
                   #'first_three_digits' ,
                   'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull_Femalesample, return_type='dataframe')
#fe_formula = 'yeartimesfirst_digit - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull_Femalesample, return_type='dataframe')

#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull_Femalesample, return_type='dataframe')


exog_list = [sm.add_constant(pd.concat([f_datafull_Femalesample[exog_vars]  ], axis=1))  for exog_vars in exog_vars_list]


# 'yeardclusttimeIndustry'   yeardclust

# Store all the results in a list
results_list2f = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull_Femalesample.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit(cov_type="clustered", clusters=f_datafull_Femalesample['yeardclusttimeIndustrytimeoccupations_code_18'] ) #  cov_type='robust')    #cov_type="clustered", clusters=f_datafull_Femalesample['yeardclust']
    results_list2f.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list2f])

# Customize table appearance if needed
stargazer.title("Female only Results log hourly wage cluster STD yea-induc-occup  ")
stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3','Model 4', 'Model 5'], [1, 1, 1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("R_Femalesample_Wagesminimuwagelog.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)    
    
#%%  yeardclust     'first_digit','yeartimesfirst_digit',

# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                   'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                   'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                   'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                   ,'age_at_last_birthday2'
                   ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Lowedu_1','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],              
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','post1997current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]


#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull_Femalesample, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull_Femalesample, return_type='dataframe')



exog_list = [sm.add_constant(pd.concat([f_datafull_Femalesample[exog_vars] ], axis=1))  for exog_vars in exog_vars_list]



# Store all the results in a list
results_list2 = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull_Femalesample.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit(cov_type="clustered", clusters=f_datafull_Femalesample['yeardclusttimeIndustrytimeoccupations_code_18']) #  cov_type='robust')    #cov_type="clustered", clusters=f_datafull_Femalesample['yeardclust']
    results_list2.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list2])

# Customize table appearance if needed
stargazer.title("Post 1997 Female only Results log hourly wage cluster STD yea-induc-occup ")
stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3','Model 4', 'Model 5'], [1, 1, 1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("POSTR_Femalesample_Wagesminimuwagelog.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)    
    
#%%

#%%



# Define the exogenous variables
# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real', 'first_three_digits' ,'first_digit',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                   'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                   'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                   'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                   ,'age_at_last_birthday2'
                   ],
                  ['logminimum_wage_annual_real', 'first_three_digits' ,'first_digit',
                   'Lowedu_1','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real', 'first_three_digits' ,'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],              
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'logtotal_hours_annual ~ {fe_formula}', data=f_datafull_Femalesample, return_type='dataframe')
#fe_formula = 'year22zz  - 1'
#y, X_fe1 = patsy.dmatrices(f'logtotal_hours_annual ~ {fe_formula}', data=f_datafull_Femalesample, return_type='dataframe')



exog_list = [sm.add_constant(pd.concat([f_datafull_Femalesample[exog_vars]   ], axis=1))  for exog_vars in exog_vars_list]


# Store all the results in a list
results_listfemale = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull_Femalesample.logtotal_hours_annual, exog, entity_effects=False, time_effects=False)
    results = cons.fit( cov_type='robust') #  cov_type="clustered", clusters=f_datafull_Femalesample['yeardclusttimeIndustrytimeoccupations_code_18'] )   #cov_type='robust')    # cov_type="clustered", clusters=f_datafull_Femalesample['yeardclust']
    results_listfemale.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_listfemale])

# Customize table appearance if needed
stargazer.title("Female only Results hours worked cluster STD yea-induc-occup ")
stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3','Model 4', 'Model 5'], [1, 1, 1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("R_Femalesample_total_hoursminimuwagelog.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex) 
    

#%%


# Define the exogenous variables
# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real', 'first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                   'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                   'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                   'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                   ,'age_at_last_birthday2'
                   ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Lowedu_1','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real', 'first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1', 
                   'Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],              
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','post1997current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'logtotal_hours_annual ~ {fe_formula}', data=f_datafull_Femalesample, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'logtotal_hours_annual ~ {fe_formula}', data=f_datafull_Femalesample, return_type='dataframe')



exog_list = [sm.add_constant(pd.concat([f_datafull_Femalesample[exog_vars]  ], axis=1))  for exog_vars in exog_vars_list]



# Store all the results in a list
results_list = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull_Femalesample.logtotal_hours_annual, exog, entity_effects=False, time_effects=False)
    results = cons.fit(  cov_type="clustered", clusters=f_datafull_Femalesample['yeardclusttimeIndustrytimeoccupations_code_18'] )   #cov_type='robust')    # cov_type="clustered", clusters=f_datafull_Femalesample['yeardclust']
    results_list.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list])

# Customize table appearance if needed
stargazer.title("Post 1997 Female only Results hours worked cluster STD yea-induc-occup ")
stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3','Model 4', 'Model 5'], [1, 1, 1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("POSTR_Femalesample_total_hoursminimuwagelog.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)   



#%%
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'text.usetex': True, 'font.family': 'serif'})
plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
    'axes.labelsize': 22,
    'xtick.labelsize': 18,
    'ytick.labelsize': 18,
    'legend.fontsize': 14
})

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "text.latex.preamble": r"\usepackage{amsmath}"
})

# Extract the coefficients for 'logminimum_wage_annual_real' and their confidence intervals from the results
coefficients = []
lower_bounds = []
upper_bounds = []

# Loop through the results and extract the relevant information
for results in results_listfemale:
    # Get the coefficient for logminimum_wage_annual_real
    coef = results.params['logminimum_wage_annual_real']
    
    # Get the confidence interval for the coefficient
    conf_int = results.conf_int().loc['logminimum_wage_annual_real']
    
    # Store the coefficient and confidence interval
    coefficients.append(coef)
    lower_bounds.append(conf_int[0])
    upper_bounds.append(conf_int[1])

# Create a list of model names
#model_names = [f'(${i+1}$)' for i in range(len(coefficients))]

custom_model_names = [
    '$MinWage$',
    '$+ I_{Low Skill}$',
    '$+ I_{Low Skill}$ x $MinWage$',
    '$+ I_{Married}$',
    '$+ I_{Married}$ x $MinWage$'
]

colors = ['#A60303','#022859','#035AA6','#73020C','#020F59']
          # '#F20505','#044BD9','#03258C','#032859']
#

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the coefficients with their confidence intervals
#ax.errorbar(model_names, coefficients, 
#            yerr=[np.array(coefficients) - np.array(lower_bounds), np.array(upper_bounds) - np.array(coefficients)],
#            fmt='o', capsize=10, color='#020F59', label='Coefficients', linewidth=2, markersize=8)

for i, (coef, lower, upper, model, color) in enumerate(zip(coefficients, lower_bounds, upper_bounds, custom_model_names , colors)):
    ax.errorbar(model, coef, 
                yerr=[[coef - lower], [upper - coef]],
                fmt='o', capsize=10, color=color, label=f'Model {model}', linewidth=3, markersize=8)



# Customize the plot
#ax.set_xlabel(r'Models',fontsize=14)
#ax.set_title('Coefficients of Minimum Wage from Different Models with Confidence Intervals')
ax.axhline(0, color='black', linewidth=0.7, linestyle='--')  # Horizontal line at 0 for reference
ax.grid(True, linestyle='--', alpha=0.7)

# Axes and styling
ax.axhline(0, color='black', linestyle='--', linewidth=1)
ax.set_xticks(np.arange(len(custom_model_names)))
ax.set_xticklabels(custom_model_names, rotation=45, ha='right')
ax.set_ylabel(r'Coefficient on $\log(\text{MinWage})$', fontsize=22)
ax.set_xlim(-0.5, len(custom_model_names) - 0.5)
ax.grid(axis='y', linestyle='--', alpha=0.5)  
plt.tight_layout()

plt.savefig("Femalecoefficients_hoursworkedMimimuwage_plot.pdf", format='pdf')
     
#%%  male only    'first_digit','yeartimesfirst_digit',



# Define the exogenous variables
# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real', 'first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                   'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                   'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                   'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                   ,'age_at_last_birthday2'
                   ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Lowedu_1','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],              
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','post1997current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull_Malesample, return_type='dataframe')
#fe_formula = 'yeartimesfirst_digit - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull_Malesample, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull_Malesample, return_type='dataframe')



exog_list = [sm.add_constant(pd.concat([f_datafull_Malesample[exog_vars] ], axis=1))  for exog_vars in exog_vars_list]


# Store all the results in a list
results_list1 = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull_Malesample.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit(cov_type="clustered", clusters=f_datafull_Malesample['yeardclusttimeIndustrytimeoccupations_code_18'] )   # cov_type="clustered", clusters=f_datafull_Malesample['yeardclust']
    results_list1.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list1])

# Customize table appearance if needed
stargazer.title("POST male only  Results hourly wage  cluster STD yea-induc-occup ")
stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3','Model 4', 'Model 5'], [1, 1, 1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("POSTR_Malesample_Wagesminimuwagelog.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)    
    



#%%  'first_digit','yeartimesfirst_digit',

# Define the exogenous variables
# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real', 'first_three_digits' ,'first_digit',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                   'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                   'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                   'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                   ,'age_at_last_birthday2'
                   ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'Lowedu_1','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],              
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull_Malesample, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull_Malesample, return_type='dataframe')



exog_list = [sm.add_constant(pd.concat([f_datafull_Malesample[exog_vars]   ], axis=1))  for exog_vars in exog_vars_list]


# Store all the results in a list
results_list1 = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull_Malesample.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit( cov_type="clustered", clusters=f_datafull_Malesample['yeardclusttimeIndustrytimeoccupations_code_18'] )   # cov_type="clustered", clusters=f_datafull_Malesample['yeardclust']
    results_list1.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list1])

# Customize table appearance if needed
stargazer.title("male only  Results hourly wage cluster STD yea-induc-occup ")
stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3','Model 4', 'Model 5'], [1, 1, 1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("R_Malesample_Wagesminimuwagelog.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)    
    

#%%  'first_digit','yeartimesfirst_digit',



# Define the exogenous variables
# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real', 'first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                   'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                   'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                   'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                   ,'age_at_last_birthday2'
                   ],
                  ['logminimum_wage_annual_real', 'first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Lowedu_1','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],              
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','post1997current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'logtotal_hours_annual ~ {fe_formula}', data=f_datafull_Malesample, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'logtotal_hours_annual ~ {fe_formula}', data=f_datafull_Malesample, return_type='dataframe')



exog_list = [sm.add_constant(pd.concat([f_datafull_Malesample[exog_vars]], axis=1))  for exog_vars in exog_vars_list]




# Store all the results in a list
results_list = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull_Malesample.logtotal_hours_annual, exog, entity_effects=False, time_effects=False)
    results = cons.fit(cov_type="clustered", clusters=f_datafull_Malesample['yeardclusttimeIndustrytimeoccupations_code_18']) #cov_type='robust')   #   cov_type="clustered", clusters=f_datafull_Malesample['yeardclust']
    results_list.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list])

# Customize table appearance if needed
stargazer.title("POST MALE Only Results hours worked cluster STD yea-induc-occup ")
stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3','Model 4', 'Model 5'], [1, 1, 1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("POSTR_Malesample_total_hoursminimuwagelog.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)        
   
   
   

#%% 'first_digit','yeartimesfirst_digit',

# Define the exogenous variables
# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real', 'first_three_digits' ,'first_digit',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                   'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                   'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                   'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                   ,'age_at_last_birthday2'
                   ],
                  ['logminimum_wage_annual_real', 'first_three_digits' ,'first_digit',
                   'Lowedu_1','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],              
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]


#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'logtotal_hours_annual ~ {fe_formula}', data=f_datafull_Malesample, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'logtotal_hours_annual ~ {fe_formula}', data=f_datafull_Malesample, return_type='dataframe')



exog_list = [sm.add_constant(pd.concat([f_datafull_Malesample[exog_vars]], axis=1))  for exog_vars in exog_vars_list]




# Store all the results in a list
results_list = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull_Malesample.logtotal_hours_annual, exog, entity_effects=False, time_effects=False)
    results = cons.fit( cov_type="clustered", clusters=f_datafull_Malesample['yeardclusttimeIndustrytimeoccupations_code_18'])    # 
 
        #cov_type='robust' )# cov_type="clustered", clusters=f_datafull_Malesample['yeardclusttimeIndustrytimeoccupations_code_18']) #cov_type='robust')   #   cov_type="clustered", clusters=f_datafull_Malesample['yeardclust']    

       # 
    
    results_list.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list])

# Customize table appearance if needed
stargazer.title("MALE Only Results hours worked cluster STD yea-induc-occup -district ")
stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3','Model 4', 'Model 5'], [1, 1, 1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("R_Malesample_total_hoursminimuwagelog.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)        
   
   
#%%
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'text.usetex': True, 'font.family': 'serif'})
# Set LaTeX-style font rendering
plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
    'axes.labelsize': 22,
    'xtick.labelsize': 18,
    'ytick.labelsize': 18,
    'legend.fontsize': 14
})

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "text.latex.preamble": r"\usepackage{amsmath}"
})

# Extract the coefficients for 'logminimum_wage_annual_real' and their confidence intervals from the results
coefficients = []
lower_bounds = []
upper_bounds = []

# Loop through the results and extract the relevant information
for results in results_list:
    # Get the coefficient for logminimum_wage_annual_real
    coef = results.params['logminimum_wage_annual_real']
    
    # Get the confidence interval for the coefficient
    conf_int = results.conf_int().loc['logminimum_wage_annual_real']
    
    # Store the coefficient and confidence interval
    coefficients.append(coef)
    lower_bounds.append(conf_int[0])
    upper_bounds.append(conf_int[1])

# Create a list of model names
#model_names = [f'(${i+1}$)' for i in range(len(coefficients))]


custom_model_names = [
    '$MinWage$',
    '$+ I_{Low Skill}$',
    '$+ I_{Low Skill}$ x $MinWage$',
    '$+ I_{Married}$',
    '$+ I_{Married}$ x $MinWage$'
]

colors = ['#A60303','#022859','#035AA6','#73020C','#020F59']
          # '#F20505','#044BD9','#03258C','#032859']

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the coefficients with their confidence intervals
#ax.errorbar(model_names, coefficients, 
#            yerr=[np.array(coefficients) - np.array(lower_bounds), np.array(upper_bounds) - np.array(coefficients)],
#            fmt='o', capsize=10, color='#020F59', label='Coefficients', linewidth=2, markersize=8)

for i, (coef, lower, upper, model, color) in enumerate(zip(coefficients, lower_bounds, upper_bounds, custom_model_names , colors)):
    ax.errorbar(model, coef, 
                yerr=[[coef - lower], [upper - coef]],
                fmt='o', capsize=10, color=color, label=f'Model {model}', linewidth=2, markersize=7)



# Customize the plot
#ax.set_xlabel(r'Models',fontsize=14)
#ax.set_title('Coefficients of Minimum Wage from Different Models with Confidence Intervals')
ax.axhline(0, color='black', linewidth=0.7, linestyle='--')  # Horizontal line at 0 for reference
ax.grid(True, linestyle='--', alpha=0.7)

# Axes and styling
ax.axhline(0, color='black', linestyle='--', linewidth=1)
ax.set_xticks(np.arange(len(custom_model_names)))
ax.set_xticklabels(custom_model_names, rotation=45, ha='right')
ax.set_ylabel(r'Coefficient on $\log(\text{MinWage})$', fontsize=22)
ax.set_xlim(-0.5, len(custom_model_names) - 0.5)
ax.grid(axis='y', linestyle='--', alpha=0.5)  
plt.tight_layout()

plt.savefig("Malecoefficients_hoursworkedMimimuwage_plot.pdf", format='pdf')
   




   
   
 #%% additional reuslt IV 
 
 
 #%%  merge data

re_l = pd.read_csv('timeseries_annual_1950-2014.csv', sep=',')
re_l['temp_index_orginNUMDAYS']= re_l['temp_index']

re_l['temp_index']= np.log1p(re_l['temp_index'])

 #%%

# Merge the datasets on 'year' and 'region'
final_df_merged = pd.merge(f_datafull, re_l, on=['year', 'first_digit'])

# Display the merged DataFrame
print(final_df_merged)


#%%    'first_digit','first_two_digits','first_three_digits','fourty_digit'
 #%%  'year','FE_first_three_digits'
import pandas as pd
from linearmodels.iv import IV2SLS

final_df_merged['first_three_digitstimesyear']=final_df_merged['first_three_digits']*final_df_merged['year']
# first_digit

# Define the dependent variable, endogenous regressor, exogenous regressors, and instruments
y           = final_df_merged['loghourly_wage']
x_endog     = final_df_merged['logminimum_wage_annual_real']
x_exog = final_df_merged[['sex_of_person_2.0',
                          #'first_three_digits' ,
                          'first_digit',
                          'sex_of_person_2.0Timeslogminimum_wage_annual_real',
                          'Lowedu_1',
                          'Lowedu_1Timeslogminimum_wage_annual_real',
                          'current_marital_status_2.0',
                          'current_marital_status_2.0Timeslogminimum_wage_annual_real',
                          'sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real',
                          'sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real']]

controls = final_df_merged[['Method2_Formal_2','PUBLIC'
                            ,'age_at_last_birthday'
                            ,'age_at_last_birthday2'
                            ]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')






x_exog = pd.concat([x_exog, controls], axis=1)


instrument  = final_df_merged[['temp_index']]





# Add a constant term to the exogenous variables
x_exog = x_exog.assign(constant=1)

 # Perform IV Regression using 2SLS (Two-Stage Least Squares)
iv_model = IV2SLS(dependent=y, exog=x_exog, endog=x_endog, instruments=instrument)
iv_results = iv_model.fit( cov_type="clustered", clusters=final_df_merged['yeardclusttimeIndustrytimeoccupations_code_18'] )#cov_type='robust')

# Display results
print(iv_results.summary)



controls = final_df_merged[['sex_of_person_2.0'
                            #,'first_three_digits' 
                            ,'first_digit',
                          'Lowedu_1',
                          'current_marital_status_2.0',
                          'Method2_Formal_2',
                          'PUBLIC'
                          ,'age_at_last_birthday'
                          ,'age_at_last_birthday2'
                          ]]
#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')



# First-stage regression to diagnose instruments
instrument_with_const = sm.add_constant(pd.concat([controls, instrument], axis=1))
first_stage_model = sm.OLS(x_endog, instrument_with_const)
first_stage_results = first_stage_model.fit() #  cov_type="cluster", cov_kwds={'groups': final_df_merged['yeardclusttimeIndustrytimeoccupations_code_18timesfirst_digit']} )   #cov_type='robust') #cov_type='HC0')
print(first_stage_results.summary())



    
print("F-statistic:", first_stage_results.fvalue)



    # Use Stargazer to generate the LaTeX table
stargazer = Stargazer([first_stage_results, iv_results])
stargazer.title("Regression Results")
stargazer.custom_columns(["First Stage", "Second Stage (2SLS)"], [1, 1])
stargazer.add_line("Dependent Variable", ["logminimum_wage_annual_real", "loghourly_wage"])
latex_table = stargazer.render_latex()

   
#%%  with more control  PUBLIC','logsex_of_person_2FemaleQ','logMethod2_Formal_2'
# Define the dependent variable, endogenous regressor, exogenous regressors, and instruments











#%%

y = final_df_merged['loghourly_wage']
x_endog = final_df_merged['logminimum_wage_annual_real']

# Define exogenous variables (excluding duplicates)
x_exog = final_df_merged[['sex_of_person_2.0', 
                          #'first_three_digits' ,
                          'first_digit',
                          'sex_of_person_2.0Timeslogminimum_wage_annual_real',
                          'Lowedu_1',
                          'Lowedu_1Timeslogminimum_wage_annual_real',
                          'current_marital_status_2.0',
                          'current_marital_status_2.0Timeslogminimum_wage_annual_real',
                          'sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real',
                          'sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real']]

# Include controls in exogenous variables
controls = final_df_merged[['Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                            'Method2_Formal_2','PUBLIC',
'occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
'occupations_code_18_7.0','occupations_code_18_8.0'
,'age_at_last_birthday'
,'age_at_last_birthday2'
#,'yeartimesfirst_digit' 
#,'first_three_digitstimesyear'
]]


#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')



x_exog = pd.concat([x_exog, controls], axis=1)

# Instruments should exclude columns already in x_exog
instrument = final_df_merged[['temp_index']]

# Add constant to exogenous variables but avoid duplicating constants in instruments
x_exog = sm.add_constant(x_exog)

# Perform IV Regression using 2SLS
iv_model = IV2SLS(dependent=y, exog=x_exog, endog=x_endog, instruments=instrument)
iv_results = iv_model.fit(cov_type="clustered", clusters=final_df_merged['yeardclusttimeIndustrytimeoccupations_code_18'])  
    #cov_type="clustered", clusters=final_df_merged['yeardclusttimeIndustry'])#cov_type='robust') #  cov_type="clustered", clusters=final_df_merged['yeardclusttimeIndustry'] )#cov_type='robust')) #cov_type='robust')
#yeardclust'
# Display results
print(iv_results.summary)



# Include controls in exogenous variables
controls = final_df_merged[['sex_of_person_2.0', 
                            #'first_three_digits' ,
                            'first_digit',
                          'Lowedu_1',
                          'current_marital_status_2.0',
                          'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                          'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
'occupations_code_18_7.0','occupations_code_18_8.0',
'age_at_last_birthday',
'age_at_last_birthday2', 
#'yeartimesfirst_digit'
#,'first_three_digitstimesyear',
]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')

# First-stage regression to diagnose instruments
instrument_with_const = sm.add_constant(pd.concat([controls, instrument], axis=1))
first_stage_model = sm.OLS(x_endog, instrument_with_const)
first_stage_results = first_stage_model.fit()  #cov_type="cluster", cov_kwds={"groups": final_df_merged['yeardclusttimeIndustrytimeoccupations_code_18']})
#    cov_type="cluster", cov_kwds={"groups": final_df_merged['yeardclust']} ) #cov_type='HC0') #cov_type="cluster", cov_kwds={"groups": final_df_merged['yeardclust']} )
                                            
#                                            clusters=final_df_merged['yeardclusttimeIndustry'] )    
#cov_type='robust') )   #cov_type='HC0')

print("\nFirst Stage Regression Results:")
print(first_stage_results.summary())
print("F-statistic:", first_stage_results.fvalue)

# Generate LaTeX table using Stargazer
stargazer = Stargazer([first_stage_results, iv_results])
stargazer.title("Regression Results cluster STD yea-induc-occup ")
stargazer.custom_columns(["First Stage", "Second Stage (2SLS)"], [1, 1])
stargazer.add_line("Dependent Variable", ["logminimum_wage_annual_real", "loghourly_wage"])
latex_table = stargazer.render_latex()

# Write LaTeX code to file
with open("IV_wageminimuwagelog.tex", 'w') as tex_file:
    tex_file.write("""
\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}
\\title{Instrumental Variables (IV) Regression Results}
\\author{Your Name}
\\date{\\today}
\\maketitle
\\section*{Summary of IV2SLS Regression Results}
""")
    tex_file.write(latex_table)
    tex_file.write("""
\\end{document}
""")




#%%
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

# Extract the residuals (epsilon)
residuals = iv_results.resids

# Extract the instrument
temp_index = final_df_merged['temp_index']





#%%
plt.figure(figsize=(12, 6))

# Scatter plot
plt.scatter(temp_index, residuals, alpha=0.2)

# Fit a linear regression line
slope, intercept = np.polyfit(temp_index, residuals, 1)
line = slope * np.array(temp_index) + intercept

# Plot the trend line
plt.plot(temp_index, line, color='#020F59', label='regression line')

# Labels and grid
plt.xlabel(r'Instrument : Heat Index', fontsize=18,fontname='Times New Roman')
plt.ylabel(r'Residuals ($\epsilon$)', fontsize=18,fontname='Times New Roman')
plt.grid(True, linestyle='--', alpha=0.6)
#plt.legend(loc='upper right')  # Example of setting legend location
plt.legend(loc='upper right', fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=15)  # Format labels
plt.yticks(fontsize=16,  fontname='Times New Roman')

plt.savefig('New_estimation_IV.png', format='png', dpi=72, bbox_inches='tight', transparent=False)

#plt.savefig('NewestimationIV.pdf',format='pdf', dpi=150, bbox_inches='tight')
#plt.show()
plt.close()



#%%  report Fonly M only and iV resylst

# report few results


exog_vars_list = [['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull_Malesample, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull_Malesample, return_type='dataframe')



exog_list = [sm.add_constant(pd.concat([f_datafull_Malesample[exog_vars]], axis=1))  for exog_vars in exog_vars_list]


# Store all the results in a list
results_list15 = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull_Malesample.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit(cov_type="clustered", clusters=f_datafull_Malesample['yeardclusttimeIndustrytimeoccupations_code_18'] )   # cov_type="clustered", clusters=f_datafull_Malesample['yeardclust']
    results_list15.append(results)



# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real',
                   'first_three_digits' ,'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull_Femalesample, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull_Femalesample, return_type='dataframe')



exog_list = [sm.add_constant(pd.concat([f_datafull_Femalesample[exog_vars]], axis=1))  for exog_vars in exog_vars_list]



# Store all the results in a list
results_list25 = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull_Femalesample.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit(cov_type="clustered", clusters=f_datafull_Femalesample['yeardclusttimeIndustrytimeoccupations_code_18']) #  cov_type='robust')    #cov_type="clustered", clusters=f_datafull_Femalesample['yeardclust']
    results_list25.append(results)
    
from stargazer.stargazer import Stargazer

# Define the beginning and ending parts of the LaTeX document
beginningtex = r"""
\documentclass{report}
\usepackage{booktabs}
\usepackage{geometry}
\geometry{a4paper, margin=1in}
\title{Consolidated Regression Results}
\author{Your Name}
\date{\today}
\begin{document}
\maketitle
"""

endtex = r"""
\end{document}
"""

# Consolidated LaTeX Table
all_results = results_list15 + results_list25 + [first_stage_results, iv_results]
stargazer = Stargazer(all_results)

# Custom titles for each block
stargazer.title("Consolidated Regression Results cluster STD yea-induc-occup ")
stargazer.custom_columns(
    ['Male Model 4', 'Male Model 5',
     'Female Model 4', 'Female Model 5',
     'IV First Stage', 'IV Second Stage (2SLS)'],
    [1, 1, 1, 1, 1, 1]
)
stargazer.add_line("Dependent Variable", ["Y"] * 4 + ["logminimum_wage_annual_real", "loghourly_wage"])

# Render the consolidated LaTeX table
consolidated_latex_table = stargazer.render_latex()

# Combine all content into one LaTeX file
with open("Consolidated_Regression_Results.tex", 'w') as f:
    f.write(beginningtex)
    f.write("\\section*{Consolidated Regression Results}\n")
    f.write(consolidated_latex_table)
    f.write(endtex)



#Correlation between ln(real hourly wage) error term and ln(heat index) 
residuals = iv_results.resids

correlation0resid = final_df_merged['temp_index'].corr(iv_results.resids)
print(f"The correlation between resid of hourly wage eq and heat index : {correlation0resid}")




#%%
y = final_df_merged['loghourly_wage']
x_endog = final_df_merged['logminimum_wage_annual_real']

# Define exogenous variables (excluding duplicates)
#x_exog = final_df_merged[['sex_of_person_2.0',
#                          'sex_of_person_2.0Timeslogminimum_wage_annual_real',
#                          'Lowedu_1',
#                          'Lowedu_1Timeslogminimum_wage_annual_real',
#                          'current_marital_status_2.0',
#                          'current_marital_status_2.0Timeslogminimum_wage_annual_real',
#                          'sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real',
#                          'sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real']]

# Include controls in exogenous variables
controls = final_df_merged[[#'first_three_digits' ,
                            'first_digit','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                            'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
'occupations_code_18_7.0','occupations_code_18_8.0','sex_of_person_2.0',
                          'sex_of_person_2.0Timeslogminimum_wage_annual_real',
                          'Lowedu_1',
                          'Lowedu_1Timeslogminimum_wage_annual_real',
                          'current_marital_status_2.0',
                          'current_marital_status_2.0Timeslogminimum_wage_annual_real',
                          'sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real',
                          'sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real'
                          ,'age_at_last_birthday'
                          ,'age_at_last_birthday2'
                          ]]


#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')


x_exog = pd.concat([controls], axis=1)

# Instruments should exclude columns already in x_exog
instrument = final_df_merged[['temp_index']]

# Add constant to exogenous variables but avoid duplicating constants in instruments
x_exog = sm.add_constant(x_exog)

# Perform IV Regression using 2SLS
iv_model2 = IV2SLS(dependent=y, exog=x_exog, endog=x_endog, instruments=instrument)
iv_results2 = iv_model2.fit(cov_type="clustered", clusters=final_df_merged['yeardclusttimeIndustrytimeoccupations_code_18'] )  #cov_type='robust') )   cov_type='robust')

# Display results
print(iv_results2.summary)
#%%

controls = final_df_merged[[#'first_three_digits' ,
                            'first_digit','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                            'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
'occupations_code_18_7.0','occupations_code_18_8.0','sex_of_person_2.0',
                          'Lowedu_1',
                          'current_marital_status_2.0'
                          ,'age_at_last_birthday'
                          ,'age_at_last_birthday2'
                          ]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')

# First-stage regression to diagnose instruments
instrument_with_const = sm.add_constant(pd.concat([controls, instrument ], axis=1))
first_stage_model2 = sm.OLS(x_endog, instrument_with_const)
first_stage_results2 = first_stage_model2.fit() # cov_type="cluster", cov_kwds={"groups": final_df_merged['yeardclusttimeIndustrytimeoccupations_code_18timesfirst_digit']})
print(first_stage_results2.summary())

# Define the beginning and ending parts of the LaTeX document
beginningtex = r"""
\documentclass{report}
\usepackage{booktabs}
\usepackage{geometry}
\geometry{a4paper, margin=1in}
\title{Consolidated Regression Results 2}
\author{Your Name}
\date{\today}
\begin{document}
\maketitle
"""

endtex = r"""
\end{document}
"""


# Consolidated LaTeX Table
all_results = results_list1[3:5] + results_list2f[3:5] + [first_stage_results2, iv_results2]
stargazer = Stargazer(all_results)


# Custom titles for each block
stargazer.title("Consolidated Regression Results cluster STD yea-induc-occup ")
stargazer.custom_columns(
    ['Male Model 4', 'Male Model 5',
     'Female Model 4', 'Female Model 5',
     'IV First Stage', 'IV Second Stage (2SLS)'],
    [ 1, 1, 1, 1, 1, 1]
)
stargazer.add_line("Dependent Variable", ["Y"] * 4 + ["logminimum_wage_annual_real", "loghourly_wage"])

# Render the consolidated LaTeX table
consolidated_latex_table = stargazer.render_latex()

# Combine all content into one LaTeX file
with open("IV_additionacontrolsminimuwagelog.tex", 'w') as f:
    f.write(beginningtex)
    f.write("\\section*{Consolidated Regression Results}\n")
    f.write(consolidated_latex_table)
    f.write(endtex)
    
    
 #Correlation between ln(real hourly wage) error term and ln(heat index) 
residuals = iv_results2.resids

correlation0resid = final_df_merged['temp_index'].corr(iv_results2.resids)
print(f"The correlation between resid of hourly wage eq and heat index : {correlation0resid}")

   

#%% testing
r_squared = first_stage_results2.rsquared

# Number of observations
n = len(x_endog)

# Compute Hansen's J-statistic
hansen_j_statistic = n * r_squared

# Print Hansen J-statistic
print(f"Hansen J-statistic: {hansen_j_statistic}")
degrees_of_freedom = len(instrument.columns) -  len(x_endog)  # Assuming 1 instrument
from scipy.stats import chi2

# Calculate p-value using Chi-squared distribution
p_value = 1 - chi2.cdf(hansen_j_statistic, degrees_of_freedom)
print(f"Hansen J-test p-value: {p_value}")


# since the model is exaclty identified  Hansen J-statistic is not relevant here,  we shouldn't worry too much about its high value
# Access the Kleibergen-Paap F-statistic for weak instruments
kleibergen_paap_f_statistic = first_stage_results2.fvalue

# Print the Kleibergen-Paap F-statistic
print(f"Kleibergen-Paap F-statistic: {kleibergen_paap_f_statistic}")
 # report to latex file 
 
 # Generate the LaTeX table code as a string
latex_table = f"""
\\documentclass{{article}}
\\usepackage{{amsmath}}
\\usepackage{{amsfonts}}
\\usepackage{{graphicx}}
\\usepackage{{float}}

\\begin{{document}}

\\title{{First-Stage Regression Analysis Results}}
\\author{{}}
\\date{{}}
\\maketitle

\\section*{{Results}}

The following table summarizes the key statistics from the first-stage regression and instrumental variable analysis:

\\begin{{table}}[H]
\\centering
\\begin{{tabular}}{{|l|l|}}
\\hline
\\textbf{{Statistic}} & \\textbf{{Value}} \\\\ \\hline
$R^2$ (First Stage) & {r_squared:.4f} \\\\ \\hline
Number of Observations ($n$) & {n} \\\\ \\hline
Hansen J-statistic & {hansen_j_statistic:.4f} \\\\ \\hline
Degrees of Freedom (df) & {degrees_of_freedom} \\\\ \\hline
Hansen J-test p-value & {p_value:.4f} \\\\ \\hline
Kleibergen-Paap F-statistic & {kleibergen_paap_f_statistic:.4f} \\\\ \\hline
\\end{{tabular}}
\\caption{{Summary of First-Stage Regression Results}}
\\end{{table}}

\\section*{{Interpretation}}

\\begin{{itemize}}
    \\item The $R^2$ from the first-stage regression captures the explanatory power of the instruments.
    \\item The Hansen J-statistic and its corresponding p-value are used for testing overidentifying restrictions. However, since the model is exactly identified, the Hansen J-statistic is not relevant in this case.
    \\item The Kleibergen-Paap F-statistic is used to assess the strength of the instruments. A high value suggests that the instruments are strong and not weak.
\\end{{itemize}}

\\end{{document}}
"""

# Save the LaTeX code to a .tex file
with open('TestingIVfirst_stage_results.tex', 'w') as f:
    f.write(latex_table)

print("LaTeX table saved to 'first_stage_results.tex'")
 


#%% iv on hours 


final_df_merged['yeartimesfirst_digit'] = final_df_merged['first_digit'] * final_df_merged['year']


y = final_df_merged['logtotal_hours_annual']
x_endog = final_df_merged['logminimum_wage_annual_real']

# Define exogenous variables (excluding duplicates)
x_exog = final_df_merged[[
                          'sex_of_person_2.0'
                          #,'first_three_digits' 
                          ,'first_digit',
                          'sex_of_person_2.0Timeslogminimum_wage_annual_real',
                          'Lowedu_1',
                          'Lowedu_1Timeslogminimum_wage_annual_real',
                          'current_marital_status_2.0',
                          'current_marital_status_2.0Timeslogminimum_wage_annual_real',
                          'sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real',
                          'sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real']]

# Include controls in exogenous variables
controls = final_df_merged[['Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                            'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
'occupations_code_18_7.0','occupations_code_18_8.0'
,'age_at_last_birthday'
,'age_at_last_birthday2'
]]

#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')

x_exog = pd.concat([x_exog, controls], axis=1)

# Instruments should exclude columns already in x_exog
instrument = final_df_merged[['temp_index']]

# Add constant to exogenous variables but avoid duplicating constants in instruments
x_exog = sm.add_constant(x_exog)

# Perform IV Regression using 2SLS
iv_model = IV2SLS(dependent=y, exog=x_exog, endog=x_endog, instruments=instrument)
iv_results = iv_model.fit( cov_type="clustered", clusters=final_df_merged['yeardclusttimeIndustrytimeoccupations_code_18'] )#cov_type='robust') ) cov_type='robust')

# Display results
print(iv_results.summary)


controls = final_df_merged[['sex_of_person_2.0'
                            #,'first_three_digits' 
                            ,'first_digit',
                          'Lowedu_1',
                          'current_marital_status_2.0',
    'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
    'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
'occupations_code_18_7.0','occupations_code_18_8.0'
,'age_at_last_birthday'
,'age_at_last_birthday2'
]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')

# First-stage regression to diagnose instruments
instrument_with_const = sm.add_constant(pd.concat([controls, instrument ], axis=1))
first_stage_model = sm.OLS(x_endog, instrument_with_const)
first_stage_results = first_stage_model.fit( ) #cov_type="cluster", cov_kwds={"groups": final_df_merged['yeardclusttimeIndustrytimeoccupations_code_18timesfirst_digit']} )    #cov_type='HC0')
print(first_stage_results.summary())


print("\nFirst Stage Regression Results:")
print(first_stage_results.summary())
print("F-statistic:", first_stage_results.fvalue)
#%%

#%%
# Generate LaTeX table using Stargazer
stargazer = Stargazer([first_stage_results, iv_results])
stargazer.title("Regression Results cluster STD yea-induc-occup ")
stargazer.custom_columns(["First Stage", "Second Stage (2SLS)"], [1, 1])
stargazer.add_line("Dependent Variable", ["logminimum_wage_annual_real", "logtotal_hours_annual"])
latex_table = stargazer.render_latex()

# Write LaTeX code to file
with open("IV_hoursworkminimuwagelog.tex", 'w') as tex_file:
    tex_file.write("""
\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}
\\title{Instrumental Variables (IV) Regression Results}
\\author{Your Name}
\\date{\\today}
\\maketitle
\\section*{Summary of IV2SLS Regression Results}
""")
    tex_file.write(latex_table)
    tex_file.write("""
\\end{document}
""")







#%%    'first_digit','first_two_digits','first_three_digits','fourty_digit'






#cov_type="clustered", clusters=final_df_merged['yeardclust']

# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                   'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                   'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                   'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                   ,'age_at_last_birthday2'
                   ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                  'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                  'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                  'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                  ,'age_at_last_birthday2'
                  ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                  'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                  'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                  'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                  ,'age_at_last_birthday2'
                  ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                  'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                  'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                  'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                  ,'age_at_last_birthday2'
                  ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                  'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                  'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                  'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                  ,'age_at_last_birthday2'
                  ],              
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                  'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                  'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                  'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                  ,'age_at_last_birthday2'
                  ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                  'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                  'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                  'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                  ,'age_at_last_birthday2'
                  ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real','sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                  'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                  'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                  'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                  ,'age_at_last_birthday2'
                  ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real','sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real','sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                  'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                  'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                  'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                  ,'age_at_last_birthday2'
                  ]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull, return_type='dataframe')



exog_list = [sm.add_constant(pd.concat([f_datafull[exog_vars]], axis=1))  for exog_vars in exog_vars_list]


# Store all the results in a list
results_list = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit(  cov_type="clustered", clusters=f_datafull['yeardclusttimeIndustry'] )   #cov_type='robust')
    results_list.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list])

# Customize table appearance if needed
stargazer.title("Regression Results cluster STD yea-indu")
stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3','Model 4', 'Model 5', 'Model 6','Model 7', 'Model 8','Model 9'], [1, 1, 1, 1, 1, 1, 1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("NoFixedEffects1_Wagesminimuwagelog.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)    
#%% 


# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real',
                   'first_three_digits' ,
                   'first_digit',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                   'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                   'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                   'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                   ,'age_at_last_birthday2'
                   ],
                  ['logminimum_wage_annual_real',
                   'first_three_digits' ,
                   'first_digit',
                   'sex_of_person_2.0','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                  'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                  'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                  'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                  ,'age_at_last_birthday2'
                  ],
                  ['logminimum_wage_annual_real',
                   'first_three_digits' ,
                   'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                  'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                  'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                  'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                  ,'age_at_last_birthday2'
                  ],
                  ['logminimum_wage_annual_real',
                   'first_three_digits' ,
                   'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                  'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                  'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                  'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                  ,'age_at_last_birthday2'
                  ],
                  ['logminimum_wage_annual_real',
                   'first_three_digits' ,
                   'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                  'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                  'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                  'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                  ,'age_at_last_birthday2'
                  ],              
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                  'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                  'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                  'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                  ,'age_at_last_birthday2'
                  ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                  'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                  'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                  'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                  ,'age_at_last_birthday2'
                  ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real','sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                  'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                  'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                  'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                  ,'age_at_last_birthday2'
                  ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real','sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real','sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                  'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                  'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                  'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                  ,'age_at_last_birthday2'
                  ]]

# controle for district instead of province
#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull, return_type='dataframe')
#fe_formula = 'yeartimesfirst_digit - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull, return_type='dataframe')



exog_list = [sm.add_constant(pd.concat([f_datafull[exog_vars]], axis=1))  for exog_vars in exog_vars_list]


# Store all the results in a list
results_list = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull.loghourly_wage, exog, entity_effects=False, time_effects=True)
    results = cons.fit(cov_type='robust')
    results_list.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list])

# Customize table appearance if needed
stargazer.title("Regression Results  year fe and cov_type= robust ")
stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3','Model 4', 'Model 5', 'Model 6','Model 7', 'Model 8','Model 9'], [1, 1, 1, 1, 1, 1, 1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("TimeixedEffects_Wagesminimuwagelog.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)    
    
    
 #%%  I moved these rehg here   (13/12/2024)




# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                   'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                   'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                   'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                   ,'age_at_last_birthday2'
                   ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'sex_of_person_2.0','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'sex_of_person_2.0','post1997sex_of_person_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'sex_of_person_2.0','post1997sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'sex_of_person_2.0','post1997sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],              
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'sex_of_person_2.0','post1997sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'sex_of_person_2.0','post1997sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','post1997current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'sex_of_person_2.0','post1997sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','post1997current_marital_status_2.0Timeslogminimum_wage_annual_real','post1997sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'sex_of_person_2.0','post1997sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','post1997current_marital_status_2.0Timeslogminimum_wage_annual_real','post1997sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real','post1997sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]


#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull, return_type='dataframe')



exog_list = [sm.add_constant(pd.concat([f_datafull[exog_vars]], axis=1))  for exog_vars in exog_vars_list]


# Store all the results in a list
results_list = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit( cov_type="clustered", clusters=f_datafull['yeardclusttimeIndustrytimeoccupations_code_18']  ) #cov_type='robust')  # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list])

# Customize table appearance if needed
stargazer.title("Post Regression Results hourly wage cluster STD yea-induc-occup ")
stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3','Model 4', 'Model 5', 'Model 6','Model 7', 'Model 8','Model 9'], [1, 1, 1, 1, 1, 1, 1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("POSTNEWlfpak_ols_modelsWagesminimuwagelog.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)    
 
    
#%%

# Define the exogenous variables
exog_vars_list = [
    #['logminimum_wage_annual_real',
    #               'first_digit','yeartimesfirst_digit','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
    #               'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
    #               'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
    #               'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday','age_at_last_birthday2'],
    #              ['logminimum_wage_annual_real',
    #               'sex_of_person_2.0','first_digit','yeartimesfirst_digit','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
    #                                 'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
    #                                 'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
    #                                 'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday','age_at_last_birthday2'],
    #              ['logminimum_wage_annual_real',
    #               'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','first_digit','yeartimesfirst_digit','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
    #                                 'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
    #                                 'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
    #                                 'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday','age_at_last_birthday2'],
    #              ['logminimum_wage_annual_real',
    #               'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','first_digit','yeartimesfirst_digit','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
    #                                 'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
    #                                 'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
    #                                 'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday','age_at_last_birthday2'],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],              
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real','sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real','sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real','sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull, return_type='dataframe')



exog_list = [sm.add_constant(pd.concat([f_datafull[exog_vars]], axis=1))  for exog_vars in exog_vars_list]



# Store all the results in a list
results_list = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit( cov_type="clustered", clusters=f_datafull['yeardclusttimeIndustrytimeoccupations_code_18']  ) #cov_type='robust')  # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list])

# 'Model 1', 'Model 2', 'Model 3','Model 4', 
# Customize table appearance if needed
stargazer.title("Regression Results hourly wage cluster STD yea-induc-occup  ")
stargazer.custom_columns(['Model 1', 'Model 2','Model 3', 'Model 4','Model 5'], [ 1, 1, 1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("NEWlfpak_ols_modelsWagesminimuwagelog.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)    
 
    



    
 
#%%
#exog_vars_list =  []

#exog_list = [sm.add_constant(f_datafull[exog_vars]) for exog_vars in exog_vars_list]

# Store all the results in a list
#results_list = []

#for exog in exog_list:
#    # Run the regression
#    cons = PanelOLS(f_datafull.loghourly_wage, exog, entity_effects=False, time_effects=False)
#    results = cons.fit(cov_type="clustered", clusters=f_datafull['yeartimesfirst_digit'])
#    results_list.append(results)

# Use Stargazer to create LaTeX table
#stargazer = Stargazer([results for results in results_list])

# Customize table appearance if needed
#stargazer.title("Regression Results")
#stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3','Model 4', 'Model 5'], [1, 1, 1, 1, 1])
#stargazer.show_model_numbers(False)

# Write to LaTeX file
#beginningtex = """\\documentclass{report}
#\\usepackage{booktabs}
#\\begin{document}"""
#endtex = "\\end{document}"


#with open("NEWlfpak_ols_modelsWagesminimuwage2tablog.tex", 'w') as dfoutput:
#    dfoutput.write(beginningtex)
#    dfoutput.write(stargazer.render_latex())
#    dfoutput.write(endtex)     
    
#%%



# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                   'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                   'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                   'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                   ,'age_at_last_birthday2'
                   ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],              
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real','sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real','sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real','sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull, return_type='dataframe')



exog_list = [sm.add_constant(pd.concat([f_datafull[exog_vars]], axis=1))  for exog_vars in exog_vars_list]

# Store all the results in a list
results_list = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull.logtotal_hours_annual, exog, entity_effects=False, time_effects=False)
    results = cons.fit(cov_type='robust') #  cov_type="clustered", clusters=f_datafull['yeardclusttimeIndustrytimeoccupations_code_18timesfirst_digit'] )   # cov_type='robust') # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list])

# Customize table appearance if needed
stargazer.title("Regression Results cluster  robust ")
stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3','Model 4', 'Model 5', 'Model 6','Model 7', 'Model 8','Model 9'], [1, 1, 1, 1, 1, 1, 1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("NEWlfpak_ols_modelstotal_hoursminimuwagelog.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)        
    



#%%  example plor

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'text.usetex': True, 'font.family': 'serif'})

plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
    'axes.labelsize': 22,
    'xtick.labelsize': 18,
    'ytick.labelsize': 18,
    'legend.fontsize': 14
})

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "text.latex.preamble": r"\usepackage{amsmath}"
})

# Extract the coefficients for 'logminimum_wage_annual_real' and their confidence intervals from the results
coefficients = []
lower_bounds = []
upper_bounds = []

# Loop through the results and extract the relevant information
for results in results_list:
    # Get the coefficient for logminimum_wage_annual_real
    coef = results.params['logminimum_wage_annual_real']
    
    # Get the confidence interval for the coefficient
    conf_int = results.conf_int().loc['logminimum_wage_annual_real']
    
    # Store the coefficient and confidence interval
    coefficients.append(coef)
    lower_bounds.append(conf_int[0])
    upper_bounds.append(conf_int[1])

# Create a list of model names
#model_names = [f'(${i+1}$)' for i in range(len(coefficients))]
custom_model_names = [
    '$MinWage$',
    '$+ I_{Female}$',
    '$+ I_{Female}$ x $MinWage  $',
    '$+ I_{Low Skill}$',
    '$+ I_{Low Skill}$ x $MinWage$',
    '$+ I_{Married}$',
    '$+ I_{Married}$ x $MinWage$',
    '$+ I_{Low Skill}$ x $I_{Female}$ x $MinWage$',
    '$+ I_{Married}$ x $I_{Female}$ x $MinWage$'
]

colors = ['#A60303','#022859','#035AA6','#73020C','#020F59','#F20505','#044BD9','#03258C','#032859']
# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the coefficients with their confidence intervals
#ax.errorbar(model_names, coefficients, 
#            yerr=[np.array(coefficients) - np.array(lower_bounds), np.array(upper_bounds) - np.array(coefficients)],
#            fmt='o', capsize=10, color='#020F59', label='Coefficients', linewidth=2, markersize=8)

# Plot the coefficients with their confidence intervals
for i, (coef, lower, upper, model, color) in enumerate(zip(coefficients, lower_bounds, upper_bounds, custom_model_names , colors)):
    ax.errorbar(model, coef, 
                yerr=[[coef - lower], [upper - coef]],
                fmt='o', capsize=10, color=color, label=f'Model {model}', linewidth=3, markersize=8)



# Customize the plot
#ax.set_xlabel(r'Models',fontsize=14)
#ax.set_title('Coefficients of Minimum Wage from Different Models with Confidence Intervals')
ax.axhline(0, color='black', linewidth=0.7, linestyle='--')  # Horizontal line at 0 for reference
ax.grid(True, linestyle='--', alpha=0.7)


#ax.legend(fontsize=14, loc='best')

# Axes and styling
ax.axhline(0, color='black', linestyle='--', linewidth=1)
ax.set_xticks(np.arange(len(custom_model_names)))
ax.set_xticklabels(custom_model_names, rotation=45, ha='right')
ax.set_ylabel(r'Coefficient on $\log(\text{MinWage})$', fontsize=22)
ax.set_xlim(-0.5, len(custom_model_names) - 0.5)
ax.grid(axis='y', linestyle='--', alpha=0.5)  
plt.tight_layout()

plt.savefig("coefficients_hoursworkedMimimuwage_plot.pdf", format='pdf')

#%%




# Define the exogenous variables
#exog_vars_list =  [['logminimum_wage_annual_real','current_marital_status_2.0'],
#                  ['logminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real'],
#                  ['logminimum_wage_annual_real','sex_of_person_2.0','current_marital_status_2.0','Lowedu_1'],
#                  ['logminimum_wage_annual_real','sex_of_person_2.0','Lowedu_1','sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real'],
#                  ['logminimum_wage_annual_real', 'sex_of_person_2.0','current_marital_status_2.0','Lowedu_1','sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real','current_marital_status_2.0Timeslogminimum_wage_annual_real','Lowedu_1Timeslogminimum_wage_annual_real','sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real']]


#exog_list = [sm.add_constant(f_datafull[exog_vars]) for exog_vars in exog_vars_list]

# Store all the results in a list
#results_list = []

#for exog in exog_list:
    # Run the regression
#    cons = PanelOLS(f_datafull.logtotal_hours_annual, exog, entity_effects=False, time_effects=False)
#    results = cons.fit(cov_type="clustered", clusters=f_datafull['yeardclust'])
#    results_list.append(results)

# Use Stargazer to create LaTeX table
#stargazer = Stargazer([results for results in results_list])

# Customize table appearance if needed
#stargazer.title("Regression Results")
#stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3','Model 4', 'Model 5'], [1, 1, 1, 1, 1])
#stargazer.show_model_numbers(False)

# Write to LaTeX file
#beginningtex = """\\documentclass{report}
#\\usepackage{booktabs}
#\\begin{document}"""
#endtex = "\\end{document}"


#with open("NEWlfpak_ols_modelstotal_hoursminimuwage2tablog.tex", 'w') as dfoutput:
#    dfoutput.write(beginningtex)
#    dfoutput.write(stargazer.render_latex())
#    dfoutput.write(endtex)        
    
    
    
#%% 



    


#%% dummy varible in logs 




# Define the exogenous variables
exog_vars_list = [['sex_of_person_2.0'], ['current_marital_status_2.0'], ['Lowedu_1']]
exog_list = [sm.add_constant(f_datafull[exog_vars]) for exog_vars in exog_vars_list]

# Store all the results in a list
results_list = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull.logtotal_hours_annual, exog, entity_effects=False, time_effects=False)
    results = cons.fit(   cov_type="clustered", clusters=f_datafull['yeardclusttimeIndustry'] ) #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list])

# Customize table appearance if needed
stargazer.title("Regression Results cluster STD yea-induc")
stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3'], [1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("NEWlfpak_dummyvar_modelsLOG.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)    
    
    


# Store all the results in a list
results_list = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit(   cov_type="clustered", clusters=f_datafull['yeardclusttimeIndustry'] )  # cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list])

# Customize table appearance if needed
stargazer.title("Regression Results cluster STD yea-indu ")
stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3'], [1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX filenny66j
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("NEWlfpak_dummyvar_modelsWagesLOG.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)    
    
#%%  'first_digit','yeartimesfirst_digit'
import patsy

examf_datafull = f_datafull.copy()
examf_datafull['income_percentile'] = f_datafull.groupby('yeardclust')['hourly_wage'].transform(lambda x: pd.qcut(x, 5, labels=False))



#low income 
percetile1_ = examf_datafull[examf_datafull['income_percentile'] == 0] 
percetile2_ = examf_datafull[examf_datafull['income_percentile'] == 1] 
percetile3_ = examf_datafull[examf_datafull['income_percentile'] == 2] 
#high income 
percetile4_ = examf_datafull[examf_datafull['income_percentile'] == 3] 
percetile5_ = examf_datafull[examf_datafull['income_percentile'] == 4] 



# Define the exogenous variables
exog_vars_list = [
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0',
                   #'sex_of_person_2.0Timeslogminimum_wage_annual_real',
                   'Lowedu_1',
                   #'Lowedu_1Timeslogminimum_wage_annual_real',
                   'current_marital_status_2.0',
                   #'current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   #'sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real',
                   #'sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     #'PUBLIC',
                                     'occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]









exog_list = [sm.add_constant(percetile1_[exog_vars]) for exog_vars in exog_vars_list]

# Store all the results in a list
results_list = []

for exog in exog_list:
    # Run the regression
    cons = sm.Logit(percetile1_.Method2_Formal_2, exog,maxiter=100, method='bfgs')
    results = cons.fit(  cov_type='HC1')   # cov_type="cluster" , cov_kwds={'groups': percetile1_['yeardclusttimeIndustrytimeoccupations_code_18']}) # , clusters=f_datafull['yeardclusttimeIndustry'] ) # cov_type='HC1')  # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results)
    
    
exog_list = [sm.add_constant(percetile2_[exog_vars]) for exog_vars in exog_vars_list]


for exog in exog_list:
    # Run the regression
    cons = sm.Logit(percetile2_.Method2_Formal_2, exog,maxiter=100, method='bfgs')
    results = cons.fit(  cov_type='HC1')   # cov_type="cluster" , cov_kwds={'groups': percetile2_['yeardclusttimeIndustrytimeoccupations_code_18']}) # , clusters=f_datafull['yeardclusttimeIndustry'] ) # cov_type='HC1')  # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results)


exog_list = [sm.add_constant(percetile3_[exog_vars]) for exog_vars in exog_vars_list]


for exog in exog_list:
    # Run the regression
    cons = sm.Logit(percetile3_.Method2_Formal_2, exog,maxiter=100, method='bfgs')
    results = cons.fit(   cov_type='HC1')   # cov_type="cluster" , cov_kwds={'groups': percetile3_['yeardclusttimeIndustrytimeoccupations_code_18']}) # , clusters=f_datafull['yeardclusttimeIndustry'] ) # cov_type='HC1')  # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results)


exog_list = [sm.add_constant(percetile4_[exog_vars]) for exog_vars in exog_vars_list]


for exog in exog_list:
    # Run the regression
    cons = sm.Logit(percetile4_.Method2_Formal_2, exog,maxiter=100, method='bfgs')
    results = cons.fit(  cov_type='HC1')   # cov_type="cluster" , cov_kwds={'groups': percetile4_['yeardclusttimeIndustrytimeoccupations_code_18']}) # , clusters=f_datafull['yeardclusttimeIndustry'] ) # cov_type='HC1')  # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results)
    
exog_list = [sm.add_constant(percetile5_[exog_vars]) for exog_vars in exog_vars_list]


for exog in exog_list:
    # Run the regression
    cons = sm.Logit(percetile5_.Method2_Formal_2, exog,maxiter=100, method='bfgs')
    results = cons.fit(  cov_type='HC1')   # cov_type="cluster" , cov_kwds={'groups': percetile5_['yeardclusttimeIndustrytimeoccupations_code_18']}) # , clusters=f_datafull['yeardclusttimeIndustry'] ) # cov_type='HC1')  # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results)
    

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list])
#'Model 1', 'Model 2', 'Model 3','Model 4',
# Customize table appearance if needed
stargazer.title("Regression Results LOGIT PROBIT INFORMAL SECTOR cluster STD yea-induc-occup  ")
stargazer.custom_columns(['Model 1', 'Model 2','Model 3', 'Model 4','Model 5'], [ 1, 1, 1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("Comments_Wagesminimuwagelog.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)    
 
    



#%%   
f_datafull['income_percentile'] = f_datafull.groupby('yeardclust')['hourly_wage'].transform(lambda x: pd.qcut(x, 5, labels=False))

all_exampl = f_datafull

#low income 
percetile1_ = f_datafull[f_datafull['income_percentile'] == 0] 
percetile2_ = f_datafull[f_datafull['income_percentile'] == 1] 
percetile3_ = f_datafull[f_datafull['income_percentile'] == 2] 
#high income 
percetile4_ = f_datafull[f_datafull['income_percentile'] == 3] 
percetile5_ = f_datafull[f_datafull['income_percentile'] == 4] 
#percetile6_ = f_datafull[f_datafull['income_percentile'] == 5] 

#%% plot wage percentile v (extreme of the distrbution ) with minmi wage polic line 




percetile1_1992 = percetile1_[percetile1_['yeardclust'] == 1992] 
percetile5_1992 = percetile5_[percetile5_['yeardclust'] == 1992] 
all_exampl_1992 = all_exampl[all_exampl['yeardclust'] == 1992]

percetile1_1997 = percetile1_[percetile1_['yeardclust'] == 1997] 
percetile5_1997 = percetile5_[percetile5_['yeardclust'] == 1997] 
all_exampl_1997 = all_exampl[all_exampl['yeardclust'] == 1997]


percetile1_2004 = percetile1_[percetile1_['yeardclust'] == 2004] 
percetile5_2004 = percetile5_[percetile5_['yeardclust'] == 2004] 
all_exampl_2004 = all_exampl[all_exampl['yeardclust'] == 2004]

percetile1_2010 = percetile1_[percetile1_['yeardclust'] == 2010] 
percetile5_2010 = percetile5_[percetile5_['yeardclust'] == 2010] 
all_exampl_2010 = all_exampl[all_exampl['yeardclust'] == 2010]



percetile1_2015 = percetile1_[percetile1_['yeardclust'] == 2015] 
percetile5_2015 = percetile5_[percetile5_['yeardclust'] == 2015] 
all_exampl_2015 = all_exampl[all_exampl['yeardclust'] == 2015]


percetile1_2021 = percetile1_[percetile1_['yeardclust'] == 2021] 
percetile5_2021 = percetile5_[percetile5_['yeardclust'] == 2021] 
all_exampl_2021 = all_exampl[all_exampl['yeardclust'] == 2021]




y22_log = percetile1_1992['logAnnual_Earnings_real']
y11_log = percetile5_1992['logAnnual_Earnings_real']

y33_log = percetile5_1992['logminimum_wage_annual_real']

fig = plt.figure() 

min_wage_value = y33_log.mean()  # or y33_log.iloc[0] if it's a single-value Series
pyplot.axvline(x=min_wage_value, color='red', linestyle='--', linewidth=2, label='Minimum Wage')

pyplot.hist(y22_log, bins=55, alpha=0.9, color = '#020F59', label='0-20 percentile', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=55, alpha=0.7, color = '#0F95D7', label='80-100 percentile' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Real Annual Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('Distribution1992.pdf',format='pdf', dpi=300)
plt.show()



y22_log = percetile1_2010['logAnnual_Earnings_real']
y11_log = percetile5_2010['logAnnual_Earnings_real']

y33_log = percetile5_2010['logminimum_wage_annual_real']

fig = plt.figure() 

min_wage_value = y33_log.mean()  # or y33_log.iloc[0] if it's a single-value Series
pyplot.axvline(x=min_wage_value, color='red', linestyle='--', linewidth=2, label='Minimum Wage')

pyplot.hist(y22_log, bins=55, alpha=0.9, color = '#020F59', label='0-20 percentile', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=55, alpha=0.7, color = '#0F95D7', label='80-100 percentile' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Real Annual Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('Distribution2010.pdf',format='pdf', dpi=300)
plt.show()


y22_log = percetile1_2015['logAnnual_Earnings_real']
y11_log = percetile5_2015['logAnnual_Earnings_real']

y33_log = percetile5_2015['logminimum_wage_annual_real']

fig = plt.figure() 

min_wage_value = y33_log.mean()  # or y33_log.iloc[0] if it's a single-value Series
pyplot.axvline(x=min_wage_value, color='red', linestyle='--', linewidth=2, label='Minimum Wage')

pyplot.hist(y22_log, bins=55, alpha=0.9, color = '#020F59', label='0-20 percentile', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=55, alpha=0.7, color = '#0F95D7', label='80-100 percentile' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Real Annual Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('Distribution2015.pdf',format='pdf', dpi=300)
plt.show()


y22_log = percetile1_2021['logAnnual_Earnings_real']
y11_log = percetile5_2021['logAnnual_Earnings_real']

y33_log = percetile5_2021['logminimum_wage_annual_real']

fig = plt.figure() 

min_wage_value = y33_log.mean()  # or y33_log.iloc[0] if it's a single-value Series
pyplot.axvline(x=min_wage_value, color='red', linestyle='--', linewidth=2, label='Minimum Wage')

pyplot.hist(y22_log, bins=55, alpha=0.9, color = '#020F59', label='0-20 percentile', rwidth=0.85, density = True)
pyplot.hist(y11_log, bins=55, alpha=0.7, color = '#0F95D7', label='80-100 percentile' , rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Real Annual Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('Distribution2021.pdf',format='pdf', dpi=300)
plt.show()

#%% all 


y22_log = all_exampl_1992['logAnnual_Earnings_real']

y33_log = all_exampl_1992['logminimum_wage_annual_real']

fig = plt.figure() 

min_wage_value = y33_log.mean()  # or y33_log.iloc[0] if it's a single-value Series
pyplot.axvline(x=min_wage_value, color='red', linestyle='--', linewidth=2, label='Minimum Wage')

pyplot.hist(y22_log, bins=55, alpha=0.9, color = '#020F59', rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Real Annual Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('allDistribution1992.pdf',format='pdf', dpi=300)
plt.show()




y22_log = all_exampl_1997['logAnnual_Earnings_real']

y33_log = all_exampl_1997['logminimum_wage_annual_real']

fig = plt.figure() 

min_wage_value = y33_log.mean()  # or y33_log.iloc[0] if it's a single-value Series
pyplot.axvline(x=min_wage_value, color='red', linestyle='--', linewidth=2, label='Minimum Wage')

pyplot.hist(y22_log, bins=55, alpha=0.9, color = '#020F59', rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Real Annual Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('allDistribution1997.pdf',format='pdf', dpi=300)
plt.show()





y22_log = all_exampl_2004['logAnnual_Earnings_real']

y33_log = all_exampl_2004['logminimum_wage_annual_real']

fig = plt.figure() 

min_wage_value = y33_log.mean()  # or y33_log.iloc[0] if it's a single-value Series
pyplot.axvline(x=min_wage_value, color='red', linestyle='--', linewidth=2, label='Minimum Wage')

pyplot.hist(y22_log, bins=55, alpha=0.9, color = '#020F59', rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Real Annual Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('allDistribution2004.pdf',format='pdf', dpi=300)
plt.show()


y22_log = all_exampl_2010['logAnnual_Earnings_real']

y33_log = all_exampl_2010['logminimum_wage_annual_real']

fig = plt.figure() 

min_wage_value = y33_log.mean()  # or y33_log.iloc[0] if it's a single-value Series
pyplot.axvline(x=min_wage_value, color='red', linestyle='--', linewidth=2, label='Minimum Wage')

pyplot.hist(y22_log, bins=55, alpha=0.9, color = '#020F59', rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Real Annual Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('allDistribution2010.pdf',format='pdf', dpi=300)
plt.show()


y22_log = all_exampl_2015['logAnnual_Earnings_real']

y33_log = all_exampl_2015['logminimum_wage_annual_real']

fig = plt.figure() 

min_wage_value = y33_log.mean()  # or y33_log.iloc[0] if it's a single-value Series
pyplot.axvline(x=min_wage_value, color='red', linestyle='--', linewidth=2, label='Minimum Wage')

pyplot.hist(y22_log, bins=55, alpha=0.9, color = '#020F59', rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Real Annual Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('allDistribution2015.pdf',format='pdf', dpi=300)
plt.show()


y22_log = all_exampl_2021['logAnnual_Earnings_real']

y33_log = all_exampl_2021['logminimum_wage_annual_real']

fig = plt.figure() 

min_wage_value = y33_log.mean()  # or y33_log.iloc[0] if it's a single-value Series
pyplot.axvline(x=min_wage_value, color='red', linestyle='--', linewidth=2, label='Minimum Wage')

pyplot.hist(y22_log, bins=55, alpha=0.9, color = '#020F59', rwidth=0.85, density = True)
pyplot.legend(loc='upper right')
plt.grid(True, axis='y' , linestyle='-', alpha=0.5)
pyplot.ylabel(r"Density",fontsize=14)

pyplot.xlabel(r"Real Annual Earnings (in log)",fontsize=14)
#pyplot.xlim(1,40)
pyplot.tight_layout()

 
pyplot.xticks(fontsize=14)
pyplot.yticks(fontsize=14)

plt.legend()
plt.legend(fontsize=12) 
plt.savefig('allDistribution2021.pdf',format='pdf', dpi=300)
plt.show()




#%% 'first_digit', 'yeartimesfirst_digit',,'first_three_digits'

import patsy

# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1',
                   'Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real','sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real',                 
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0',
                   'Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2','first_three_digits'
                                     ]]


#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=percetile1_, return_type='dataframe')
# Add the fixed effects design matrix columns to the exogenous variables list
#exog_vars_list[0].extend(X_fe.columns.tolist())
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=percetile1_, return_type='dataframe')
# Add the fixed effects design matrix columns to the exogenous variables list
#exog_vars_list[0].extend(X_fe1.columns.tolist())




exog_list = [sm.add_constant(percetile1_[exog_vars]) for exog_vars in exog_vars_list]

# Store all the results in a list
results_list = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(percetile1_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit( cov_type="clustered", clusters=percetile1_['yeardclusttimeIndustrytimeoccupations_code_18'] )  #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results) 
    
exog_list = [sm.add_constant(percetile2_[exog_vars]) for exog_vars in exog_vars_list]
    
for exog in exog_list:
    # Run the regression
    cons = PanelOLS(percetile2_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results2 = cons.fit( cov_type="clustered", clusters=percetile2_['yeardclusttimeIndustrytimeoccupations_code_18'] ) #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results2)   
exog_list = [sm.add_constant(percetile3_[exog_vars]) for exog_vars in exog_vars_list]

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(percetile3_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results3 = cons.fit(  cov_type="clustered", clusters=percetile3_['yeardclusttimeIndustrytimeoccupations_code_18'] ) #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results3)         
exog_list = [sm.add_constant(percetile4_[exog_vars]) for exog_vars in exog_vars_list]

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(percetile4_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results4 = cons.fit( cov_type="clustered", clusters=percetile4_['yeardclusttimeIndustrytimeoccupations_code_18'] ) # cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results4) 

exog_list = [sm.add_constant(percetile5_[exog_vars]) for exog_vars in exog_vars_list]

for exog in exog_list:
#    # Run the regression
    cons = PanelOLS(percetile5_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results5 = cons.fit( cov_type="clustered", clusters=percetile5_['yeardclusttimeIndustrytimeoccupations_code_18'] ) #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results5)         
    
#exog_list = sm.add_constant(percetile6_[exog_vars]) 
 #%% 
#exog_list = [sm.add_constant(percetile6_[exog_vars]) for exog_vars in exog_vars_list]

#for exog in exog_list:
#    # Run the regression
#    cons = PanelOLS(percetile6_.loghourly_wage, exog, entity_effects=False, time_effects=False,check_rank=True)
#    results6 = cons.fit(cov_type="clustered", clusters=percetile6_['yeardclust']  ) #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
#    results_list.append(results6)    

 #%%   
 
 
 
all_results = results_list
stargazer = Stargazer(all_results)


# Custom titles for each block
stargazer.title("Consolidated Regression Results wage distribution cluster STD yea-induc-occup ")
stargazer.custom_columns(
    ['Model 1', 'Model 2', 'Model 3', 'Model 4', 'Model 5'],
    [1, 1, 1, 1, 1]
)
stargazer.add_line("Dependent Variable", ["Y"] * 5 )

# Render the consolidated LaTeX table
consolidated_latex_table = stargazer.render_latex()

# Combine all content into one LaTeX file
with open("Comments2_Wagesminimuwagelog.tex", 'w') as f:
    f.write(beginningtex)
    f.write("\\section*{Consolidated Regression Results}\n")
    f.write(consolidated_latex_table)
    f.write(endtex) 
#%%  PLOTTING RESULTS WAGE DISTRIBUTION 



import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'text.usetex': True, 'font.family': 'serif'})


# Extract the coefficients for 'logminimum_wage_annual_real' and their confidence intervals from the results
coefficients = []
lower_bounds = []
upper_bounds = []

# Loop through the results and extract the relevant information
for results in results_list:
    # Get the coefficient for logminimum_wage_annual_real
    coef = results.params['logminimum_wage_annual_real']
    
    # Get the confidence interval for the coefficient
    conf_int = results.conf_int().loc['logminimum_wage_annual_real']
    
    # Store the coefficient and confidence interval
    coefficients.append(coef)
    lower_bounds.append(conf_int[0])
    upper_bounds.append(conf_int[1])

# Create a list of model names
#model_names = [f'(${i+1}$)' for i in range(len(coefficients))]
custom_model_names = [
    '0-20',
    '20-40 ',
    '40-60',
    '60-80',
    '80-100'
]

colors = ['#A60303','#022859','#035AA6','#73020C','#020F59','#F20505','#044BD9','#03258C','#032859']
# Create the plot
fig, ax = plt.subplots(figsize=(16, 10))

# Plot the coefficients with their confidence intervals
#ax.errorbar(model_names, coefficients, 
#            yerr=[np.array(coefficients) - np.array(lower_bounds), np.array(upper_bounds) - np.array(coefficients)],
#            fmt='o', capsize=10, color='#020F59', label='Coefficients', linewidth=2, markersize=8)

# Plot the coefficients with their confidence intervals
for i, (coef, lower, upper, model, color) in enumerate(zip(coefficients, lower_bounds, upper_bounds, custom_model_names , colors)):
    ax.errorbar(model, coef, 
                yerr=[[coef - lower], [upper - coef]],
                fmt='o', capsize=10, color=color, label=f'Model {model}', linewidth=3, markersize=8)



# Customize the plot
#ax.set_xlabel(r'Models',fontsize=14)
ax.set_ylabel(r'Coefficient of $\log$ MinWage',fontsize=24)
#ax.set_title('Coefficients of Minimum Wage from Different Models with Confidence Intervals')
ax.axhline(0, color='black', linewidth=0.7, linestyle='--')  # Horizontal line at 0 for reference
ax.grid(True, linestyle='--', alpha=0.7)


#ax.legend(fontsize=14, loc='best')

# Rotate model names for better readability
plt.xticks(rotation=45, ha='right')
plt.tick_params(axis='x', labelsize=34)  # Increase x-axis tick size
plt.tick_params(axis='y', labelsize=34)  # Increase y-axis tick size
# Show the plot
plt.tight_layout()
#plt.show()    

plt.savefig("coefficients_hourlyWAGEMimimuwage_plot.pdf", format='pdf')

#%%  check sensitivity of estimates of results (MW on wage across wage distribution 


f_datafull['income_percentile'] = f_datafull.groupby('yeardclust')['hourly_wage'].transform(lambda x: pd.qcut(x, 5, labels=False))



#low income 
percetile1_ = f_datafull[f_datafull['income_percentile'] == 0] 
percetile2_ = f_datafull[f_datafull['income_percentile'] == 1] 
percetile3_ = f_datafull[f_datafull['income_percentile'] == 2] 
#high income 
percetile4_ = f_datafull[f_datafull['income_percentile'] == 3] 
percetile5_ = f_datafull[f_datafull['income_percentile'] == 4] 
#percetile6_ = f_datafull[f_datafull['income_percentile'] == 5] 

 

#%% 'first_digit', 'yeartimesfirst_digit','first_three_digits' ,'

import patsy

# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real','first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1',
                   'Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real','sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real',                 
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0',
                   'Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2','first_three_digits'
                                     ]]


#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=percetile1_, return_type='dataframe')
# Add the fixed effects design matrix columns to the exogenous variables list
#exog_vars_list[0].extend(X_fe.columns.tolist())
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=percetile1_, return_type='dataframe')
# Add the fixed effects design matrix columns to the exogenous variables list
#exog_vars_list[0].extend(X_fe1.columns.tolist())




exog_list = [sm.add_constant(percetile1_[exog_vars]) for exog_vars in exog_vars_list]

# Store all the results in a list
results_list = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(percetile1_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit(cov_type='robust' )  #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results) 
    
exog_list = [sm.add_constant(percetile2_[exog_vars]) for exog_vars in exog_vars_list]
    
for exog in exog_list:
    # Run the regression
    cons = PanelOLS(percetile2_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results2 = cons.fit( cov_type='robust' ) #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results2)   
exog_list = [sm.add_constant(percetile3_[exog_vars]) for exog_vars in exog_vars_list]

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(percetile3_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results3 = cons.fit( cov_type='robust'  ) #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results3)         
exog_list = [sm.add_constant(percetile4_[exog_vars]) for exog_vars in exog_vars_list]

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(percetile4_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results4 = cons.fit( cov_type='robust'  ) # cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results4) 

exog_list = [sm.add_constant(percetile5_[exog_vars]) for exog_vars in exog_vars_list]

for exog in exog_list:
#    # Run the regression
    cons = PanelOLS(percetile5_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results5 = cons.fit(cov_type='robust'  ) #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results5)         
    
#exog_list = sm.add_constant(percetile6_[exog_vars]) 
 #%% 
#exog_list = [sm.add_constant(percetile6_[exog_vars]) for exog_vars in exog_vars_list]

#for exog in exog_list:
#    # Run the regression
#    cons = PanelOLS(percetile6_.loghourly_wage, exog, entity_effects=False, time_effects=False,check_rank=True)
#    results6 = cons.fit(cov_type="clustered", clusters=percetile6_['yeardclust']  ) #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
#    results_list.append(results6)    

 #%%   
 
 
 
all_results = results_list
stargazer = Stargazer(all_results)


# Custom titles for each block
stargazer.title("Consolidated Regression Results wage distribution robust ")
stargazer.custom_columns(
    ['Model 1', 'Model 2', 'Model 3', 'Model 4', 'Model 5'],
    [1, 1, 1, 1, 1]
)
stargazer.add_line("Dependent Variable", ["Y"] * 5 )

# Render the consolidated LaTeX table
consolidated_latex_table = stargazer.render_latex()

# Combine all content into one LaTeX file
with open("STDrobustComments2_Wagesminimuwagelog.tex", 'w') as f:
    f.write(beginningtex)
    f.write("\\section*{Consolidated Regression Results}\n")
    f.write(consolidated_latex_table)
    f.write(endtex) 
#%%  PLOTTING RESULTS WAGE DISTRIBUTION 



import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'text.usetex': True, 'font.family': 'serif'})


# Extract the coefficients for 'logminimum_wage_annual_real' and their confidence intervals from the results
coefficients = []
lower_bounds = []
upper_bounds = []

# Loop through the results and extract the relevant information
for results in results_list:
    # Get the coefficient for logminimum_wage_annual_real
    coef = results.params['logminimum_wage_annual_real']
    
    # Get the confidence interval for the coefficient
    conf_int = results.conf_int().loc['logminimum_wage_annual_real']
    
    # Store the coefficient and confidence interval
    coefficients.append(coef)
    lower_bounds.append(conf_int[0])
    upper_bounds.append(conf_int[1])

# Create a list of model names
#model_names = [f'(${i+1}$)' for i in range(len(coefficients))]
custom_model_names = [
    '0-20',
    '20-40 ',
    '40-60',
    '60-80',
    '80-100'
]

colors = ['#A60303','#022859','#035AA6','#73020C','#020F59','#F20505','#044BD9','#03258C','#032859']
# Create the plot
fig, ax = plt.subplots(figsize=(16, 10))

# Plot the coefficients with their confidence intervals
#ax.errorbar(model_names, coefficients, 
#            yerr=[np.array(coefficients) - np.array(lower_bounds), np.array(upper_bounds) - np.array(coefficients)],
#            fmt='o', capsize=10, color='#020F59', label='Coefficients', linewidth=2, markersize=8)

# Plot the coefficients with their confidence intervals
for i, (coef, lower, upper, model, color) in enumerate(zip(coefficients, lower_bounds, upper_bounds, custom_model_names , colors)):
    ax.errorbar(model, coef, 
                yerr=[[coef - lower], [upper - coef]],
                fmt='o', capsize=10, color=color, label=f'Model {model}', linewidth=3, markersize=8)



# Customize the plot
#ax.set_xlabel(r'Models',fontsize=14)
ax.set_ylabel(r'Coefficient of $\log$ MinWage',fontsize=24)
#ax.set_title('Coefficients of Minimum Wage from Different Models with Confidence Intervals')
ax.axhline(0, color='black', linewidth=0.7, linestyle='--')  # Horizontal line at 0 for reference
ax.grid(True, linestyle='--', alpha=0.7)


#ax.legend(fontsize=14, loc='best')

# Rotate model names for better readability
plt.xticks(rotation=45, ha='right')
plt.tick_params(axis='x', labelsize=34)  # Increase x-axis tick size
plt.tick_params(axis='y', labelsize=34)  # Increase y-axis tick size
# Show the plot
plt.tight_layout()
#plt.show()    

plt.savefig("STDROBUTScoefficients_hourlyWAGEMimimuwage_plot.pdf", format='pdf')



#%%  


#%%   if we use the specifucation pos1997 and clsuter by year-indu-occup

f_datafull['income_percentile'] = f_datafull.groupby('yeardclust')['hourly_wage'].transform(lambda x: pd.qcut(x, 5, labels=False))



#low income 
percetile1_ = f_datafull[f_datafull['income_percentile'] == 0] 
percetile2_ = f_datafull[f_datafull['income_percentile'] == 1] 
percetile3_ = f_datafull[f_datafull['income_percentile'] == 2] 
#high income 
percetile4_ = f_datafull[f_datafull['income_percentile'] == 3] 
percetile5_ = f_datafull[f_datafull['income_percentile'] == 4] 
#percetile6_ = f_datafull[f_datafull['income_percentile'] == 5] 

 

#%% 'first_digit', 'yeartimesfirst_digit','first_three_digits'

import patsy

# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real','first_digit',               
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'sex_of_person_2.0','post1997sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','post1997current_marital_status_2.0Timeslogminimum_wage_annual_real','post1997sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real','post1997sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real',              
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0',
                   'Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2','yeartimesfirst_digit'
                                     ]]


#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=percetile1_, return_type='dataframe')
# Add the fixed effects design matrix columns to the exogenous variables list
#exog_vars_list[0].extend(X_fe.columns.tolist())
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=percetile1_, return_type='dataframe')
# Add the fixed effects design matrix columns to the exogenous variables list
#exog_vars_list[0].extend(X_fe1.columns.tolist())





exog_list = [sm.add_constant(percetile1_[exog_vars]) for exog_vars in exog_vars_list]

# Store all the results in a list
results_list = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(percetile1_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit( cov_type='robust'  )  #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results) 
    
exog_list = [sm.add_constant(percetile2_[exog_vars]) for exog_vars in exog_vars_list]
    
for exog in exog_list:
    # Run the regression
    cons = PanelOLS(percetile2_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results2 = cons.fit(cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results2)   
exog_list = [sm.add_constant(percetile3_[exog_vars]) for exog_vars in exog_vars_list]

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(percetile3_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results3 = cons.fit( cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results3)         
exog_list = [sm.add_constant(percetile4_[exog_vars]) for exog_vars in exog_vars_list]

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(percetile4_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results4 = cons.fit( cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results4) 

exog_list = [sm.add_constant(percetile5_[exog_vars]) for exog_vars in exog_vars_list]

for exog in exog_list:
#    # Run the regression
    cons = PanelOLS(percetile5_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results5 = cons.fit( cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results5)         
    
#exog_list = sm.add_constant(percetile6_[exog_vars]) 
 #%% 
#exog_list = [sm.add_constant(percetile6_[exog_vars]) for exog_vars in exog_vars_list]

#for exog in exog_list:
#    # Run the regression
#    cons = PanelOLS(percetile6_.loghourly_wage, exog, entity_effects=False, time_effects=False,check_rank=True)
#    results6 = cons.fit(cov_type="clustered", clusters=percetile6_['yeardclust']  ) #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
#    results_list.append(results6)    

 #%%   
 
 
 
all_results = results_list
stargazer = Stargazer(all_results)


# Custom titles for each block
stargazer.title("Consolidated Regression Results wage distribution robust ")
stargazer.custom_columns(
    ['Model 1', 'Model 2', 'Model 3', 'Model 4', 'Model 5'],
    [1, 1, 1, 1, 1]
)
stargazer.add_line("Dependent Variable", ["Y"] * 5 )

# Render the consolidated LaTeX table
consolidated_latex_table = stargazer.render_latex()

# Combine all content into one LaTeX file
with open("STDSTDRobustPOSTComments2_Wagesminimuwagelog.tex", 'w') as f:
    f.write(beginningtex)
    f.write("\\section*{Consolidated Regression Results}\n")
    f.write(consolidated_latex_table)
    f.write(endtex) 
#%%  PLOTTING RESULTS WAGE DISTRIBUTION 



import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'text.usetex': True, 'font.family': 'serif'})


# Extract the coefficients for 'logminimum_wage_annual_real' and their confidence intervals from the results
coefficients = []
lower_bounds = []
upper_bounds = []

# Loop through the results and extract the relevant information
for results in results_list:
    # Get the coefficient for logminimum_wage_annual_real
    coef = results.params['logminimum_wage_annual_real']
    
    # Get the confidence interval for the coefficient
    conf_int = results.conf_int().loc['logminimum_wage_annual_real']
    
    # Store the coefficient and confidence interval
    coefficients.append(coef)
    lower_bounds.append(conf_int[0])
    upper_bounds.append(conf_int[1])

# Create a list of model names
#model_names = [f'(${i+1}$)' for i in range(len(coefficients))]
custom_model_names = [
    '0-20',
    '20-40 ',
    '40-60',
    '60-80',
    '80-100'
]

colors = ['#A60303','#022859','#035AA6','#73020C','#020F59','#F20505','#044BD9','#03258C','#032859']
# Create the plot
fig, ax = plt.subplots(figsize=(16, 10))

# Plot the coefficients with their confidence intervals
#ax.errorbar(model_names, coefficients, 
#            yerr=[np.array(coefficients) - np.array(lower_bounds), np.array(upper_bounds) - np.array(coefficients)],
#            fmt='o', capsize=10, color='#020F59', label='Coefficients', linewidth=2, markersize=8)

# Plot the coefficients with their confidence intervals
for i, (coef, lower, upper, model, color) in enumerate(zip(coefficients, lower_bounds, upper_bounds, custom_model_names , colors)):
    ax.errorbar(model, coef, 
                yerr=[[coef - lower], [upper - coef]],
                fmt='o', capsize=10, color=color, label=f'Model {model}', linewidth=3, markersize=8)



# Customize the plot
#ax.set_xlabel(r'Models',fontsize=14)
ax.set_ylabel(r'Coefficient of $\log$ MinWage',fontsize=24)
#ax.set_title('Coefficients of Minimum Wage from Different Models with Confidence Intervals')
ax.axhline(0, color='black', linewidth=0.7, linestyle='--')  # Horizontal line at 0 for reference
ax.grid(True, linestyle='--', alpha=0.7)


#ax.legend(fontsize=14, loc='best')

# Rotate model names for better readability
plt.xticks(rotation=45, ha='right')
plt.tick_params(axis='x', labelsize=34)  # Increase x-axis tick size
plt.tick_params(axis='y', labelsize=34)  # Increase y-axis tick size
# Show the plot
plt.tight_layout()
#plt.show()    

plt.savefig("STDSTDRobustPOSTcoefficients_hourlyWAGEMimimuwage_plot.pdf", format='pdf')

#%% specfication 1997 with clsuetered std error at year occup and indysty leve   'first_three_digits'


# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real' ,'first_digit',               
                   'post1997logminimum_wage_annual_real','post1997_1',
                   'sex_of_person_2.0','post1997sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','post1997Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','post1997current_marital_status_2.0Timeslogminimum_wage_annual_real','post1997sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real','post1997sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real',              
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0',
                   'Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2', 'yeartimesfirst_digit'
                                     ]]


#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=percetile1_, return_type='dataframe')
# Add the fixed effects design matrix columns to the exogenous variables list
#exog_vars_list[0].extend(X_fe.columns.tolist())
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=percetile1_, return_type='dataframe')
# Add the fixed effects design matrix columns to the exogenous variables list
#exog_vars_list[0].extend(X_fe1.columns.tolist())




exog_list = [sm.add_constant(percetile1_[exog_vars]) for exog_vars in exog_vars_list]

# Store all the results in a list
results_list = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(percetile1_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit( cov_type="clustered", clusters=percetile1_['yeardclusttimeIndustrytimeoccupations_code_18'] )  #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results) 
    
exog_list = [sm.add_constant(percetile2_[exog_vars]) for exog_vars in exog_vars_list]
    
for exog in exog_list:
    # Run the regression
    cons = PanelOLS(percetile2_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results2 = cons.fit( cov_type="clustered", clusters=percetile2_['yeardclusttimeIndustrytimeoccupations_code_18'] ) #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results2)   
exog_list = [sm.add_constant(percetile3_[exog_vars]) for exog_vars in exog_vars_list]

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(percetile3_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results3 = cons.fit(  cov_type="clustered", clusters=percetile3_['yeardclusttimeIndustrytimeoccupations_code_18'] ) #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results3)         
exog_list = [sm.add_constant(percetile4_[exog_vars]) for exog_vars in exog_vars_list]

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(percetile4_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results4 = cons.fit( cov_type="clustered", clusters=percetile4_['yeardclusttimeIndustrytimeoccupations_code_18'] ) # cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results4) 

exog_list = [sm.add_constant(percetile5_[exog_vars]) for exog_vars in exog_vars_list]

for exog in exog_list:
#    # Run the regression
    cons = PanelOLS(percetile5_.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results5 = cons.fit( cov_type="clustered", clusters=percetile5_['yeardclusttimeIndustrytimeoccupations_code_18'] ) #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results5)         
    
#exog_list = sm.add_constant(percetile6_[exog_vars]) 
 #%% 
#exog_list = [sm.add_constant(percetile6_[exog_vars]) for exog_vars in exog_vars_list]

#for exog in exog_list:
#    # Run the regression
#    cons = PanelOLS(percetile6_.loghourly_wage, exog, entity_effects=False, time_effects=False,check_rank=True)
#    results6 = cons.fit(cov_type="clustered", clusters=percetile6_['yeardclust']  ) #cov_type='robust')   # cov_type="clustered", clusters=f_datafull['yeardclust']
#    results_list.append(results6)    

 #%%   
 
 
 
all_results = results_list
stargazer = Stargazer(all_results)


# Custom titles for each block
stargazer.title("Consolidated Regression Results post 1997 wage distribution cluster STD yea-induc-occup ")
stargazer.custom_columns(
    ['Model 1', 'Model 2', 'Model 3', 'Model 4', 'Model 5'],
    [1, 1, 1, 1, 1]
)
stargazer.add_line("Dependent Variable", ["Y"] * 5 )

# Render the consolidated LaTeX table
consolidated_latex_table = stargazer.render_latex()

# Combine all content into one LaTeX file
with open("POST97Clusterror9Comments2_Wagesminimuwagelog.tex", 'w') as f:
    f.write(beginningtex)
    f.write("\\section*{Consolidated Regression Results}\n")
    f.write(consolidated_latex_table)
    f.write(endtex) 
#%%  PLOTTING RESULTS WAGE DISTRIBUTION 



import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'text.usetex': True, 'font.family': 'serif'})


# Extract the coefficients for 'logminimum_wage_annual_real' and their confidence intervals from the results
coefficients = []
lower_bounds = []
upper_bounds = []

# Loop through the results and extract the relevant information
for results in results_list:
    # Get the coefficient for logminimum_wage_annual_real
    coef = results.params['logminimum_wage_annual_real']
    
    # Get the confidence interval for the coefficient
    conf_int = results.conf_int().loc['logminimum_wage_annual_real']
    
    # Store the coefficient and confidence interval
    coefficients.append(coef)
    lower_bounds.append(conf_int[0])
    upper_bounds.append(conf_int[1])

# Create a list of model names
#model_names = [f'(${i+1}$)' for i in range(len(coefficients))]
custom_model_names = [
    '0-20',
    '20-40 ',
    '40-60',
    '60-80',
    '80-100'
]

colors = ['#A60303','#022859','#035AA6','#73020C','#020F59','#F20505','#044BD9','#03258C','#032859']
# Create the plot
fig, ax = plt.subplots(figsize=(16, 10))

# Plot the coefficients with their confidence intervals
#ax.errorbar(model_names, coefficients, 
#            yerr=[np.array(coefficients) - np.array(lower_bounds), np.array(upper_bounds) - np.array(coefficients)],
#            fmt='o', capsize=10, color='#020F59', label='Coefficients', linewidth=2, markersize=8)

# Plot the coefficients with their confidence intervals
for i, (coef, lower, upper, model, color) in enumerate(zip(coefficients, lower_bounds, upper_bounds, custom_model_names , colors)):
    ax.errorbar(model, coef, 
                yerr=[[coef - lower], [upper - coef]],
                fmt='o', capsize=10, color=color, label=f'Model {model}', linewidth=3, markersize=8)



# Customize the plot
#ax.set_xlabel(r'Models',fontsize=14)
ax.set_ylabel(r'Coefficient of $\log$ MinWage',fontsize=24)
#ax.set_title('Coefficients of Minimum Wage from Different Models with Confidence Intervals')
ax.axhline(0, color='black', linewidth=0.7, linestyle='--')  # Horizontal line at 0 for reference
ax.grid(True, linestyle='--', alpha=0.7)


#ax.legend(fontsize=14, loc='best')

# Rotate model names for better readability
plt.xticks(rotation=45, ha='right')
plt.tick_params(axis='x', labelsize=34)  # Increase x-axis tick size
plt.tick_params(axis='y', labelsize=34)  # Increase y-axis tick size
# Show the plot
plt.tight_layout()
#plt.show()    

plt.savefig("POST97Clusterror9coefficients_hourlyWAGEMimimuwage_plot.pdf", format='pdf')
 
#%%
#%%   regression when tempertaure is below



final_df_merged_FaTEST = final_df_merged[final_df_merged['temp_index_orginNUMDAYS'] <= 5]

final_df_merged_FaTEST['first_three_digitsforindex'] = final_df_merged_FaTEST['first_three_digits'] 
#%% 

final_df_merged_FaTEST = final_df_merged_FaTEST.set_index(['first_three_digitsforindex', 'year'])








  
 
#%%
y = final_df_merged_FaTEST['loghourly_wage']
x_endog = final_df_merged_FaTEST['logminimum_wage_annual_real']


# Include controls in exogenous variables
controls = final_df_merged_FaTEST[['first_three_digits' ,
                            'first_digit',
                            'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                            'Method2_Formal_2','PUBLIC',
                            #'occupations_code_18_1.0',
                            'occupations_code_18_2.0','occupations_code_18_3.0',
'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
'occupations_code_18_7.0','occupations_code_18_8.0','sex_of_person_2.0',
                          'sex_of_person_2.0Timeslogminimum_wage_annual_real',
                          'Lowedu_1',
                          'Lowedu_1Timeslogminimum_wage_annual_real',
                          'current_marital_status_2.0',
                          'current_marital_status_2.0Timeslogminimum_wage_annual_real',
                          'sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real',
                          'sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real'
                          ,'age_at_last_birthday'
                          ,'age_at_last_birthday2'
                          ]]




x_exog = pd.concat([controls], axis=1)

# Instruments should exclude columns already in x_exog
instrument = final_df_merged_FaTEST[['temp_index']]

# Add constant to exogenous variables but avoid duplicating constants in instruments
x_exog = sm.add_constant(x_exog)

# Perform IV Regression using 2SLS
iv_model2 = IV2SLS(dependent=y, exog=x_exog, endog=x_endog, instruments=instrument)
iv_results2 = iv_model2.fit(cov_type="clustered", clusters=final_df_merged_FaTEST['yeardclusttimeIndustrytimeoccupations_code_18'] )  #cov_type='robust') )   cov_type='robust')

# Display results
print(iv_results2.summary)
#%%

controls = final_df_merged_FaTEST[['first_three_digits' ,
                            'first_digit','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                            'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
'occupations_code_18_7.0','occupations_code_18_8.0','sex_of_person_2.0',
                          'Lowedu_1',
                          'current_marital_status_2.0'
                          ,'age_at_last_birthday'
                          ,'age_at_last_birthday2'
                          ]]




# First-stage regression to diagnose instruments
instrument_with_const = sm.add_constant(pd.concat([controls, instrument ], axis=1))
first_stage_model2 = sm.OLS(x_endog, instrument_with_const)
first_stage_results2 = first_stage_model2.fit() #cov_type="cluster", cov_kwds={"groups": final_df_merged_FaTEST['yeardclusttimeIndustrytimeoccupations_code_18']})
print(first_stage_results2.summary())
   
    
#%%   above
final_df_merged_FaTEST = final_df_merged[final_df_merged['temp_index_orginNUMDAYS'] >= 15]
final_df_merged_FaTEST['first_three_digitsforindex'] = final_df_merged_FaTEST['first_three_digits'] 

#%% 

final_df_merged_FaTEST = final_df_merged_FaTEST.set_index(['first_three_digitsforindex', 'year'])
  

#%%
y = final_df_merged_FaTEST['loghourly_wage']
x_endog = final_df_merged_FaTEST['logminimum_wage_annual_real']


# Include controls in exogenous variables
controls = final_df_merged_FaTEST[['first_three_digits' ,
                            'first_digit',
                            'Industry_1.0',
                            'Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                            'Method2_Formal_2',
                            'PUBLIC',
                            #'occupations_code_18_1.0',
                            'occupations_code_18_2.0','occupations_code_18_3.0',
'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
'occupations_code_18_7.0','occupations_code_18_8.0','sex_of_person_2.0',
                          'sex_of_person_2.0Timeslogminimum_wage_annual_real',
                          'Lowedu_1',
                          'Lowedu_1Timeslogminimum_wage_annual_real',
                          'current_marital_status_2.0',
                          'current_marital_status_2.0Timeslogminimum_wage_annual_real',
                          'sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real',
                          'sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real'
                          ,'age_at_last_birthday'
                          ,'age_at_last_birthday2'
                          ]]




x_exog = pd.concat([controls], axis=1)
# Add constant to exogenous variables but avoid duplicating constants in instruments
#x_exog['const'] = 1

x_exog = sm.add_constant(x_exog)
# Instruments should exclude columns already in x_exog
instrument = final_df_merged_FaTEST[['temp_index']]



# Perform IV Regression using 2SLS
iv_model2z = IV2SLS(dependent=y, exog=x_exog, endog=x_endog, instruments=instrument)
iv_results2z = iv_model2z.fit(cov_type="clustered", clusters=final_df_merged_FaTEST['yeardclusttimeIndustrytimeoccupations_code_18'] )  #cov_type='robust') )   cov_type='robust')

# Display results
print(iv_results2z.summary)
#%%

controls = final_df_merged_FaTEST[['first_three_digits' ,
                            'first_digit','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                            'Method2_Formal_2','PUBLIC',
                            #'occupations_code_18_1.0',
                            'occupations_code_18_2.0','occupations_code_18_3.0',
'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
'occupations_code_18_7.0','occupations_code_18_8.0','sex_of_person_2.0',
                          'Lowedu_1',
                          'current_marital_status_2.0'
                          ,'age_at_last_birthday'
                          ,'age_at_last_birthday2'
                          ]]


# First-stage regression to diagnose instruments
instrument_with_const = sm.add_constant(pd.concat([controls, instrument ], axis=1))
first_stage_model2z = sm.OLS(x_endog, instrument_with_const)
first_stage_results2z = first_stage_model2z.fit() #cov_type="cluster", cov_kwds={"groups": final_df_merged_FaTEST['yeardclusttimeIndustrytimeoccupations_code_18']})
print(first_stage_results2z.summary())
   

#%%
# Use Stargazer to create LaTeX table



# Consolidated LaTeX Table
all_results =  [first_stage_results2 ,  iv_results2]  +  [first_stage_results2z , iv_results2z]
stargazer = Stargazer(all_results)

# Custom titles for each block
stargazer.title("Consolidated Regression Results cluster STD yea-induc-occup ")
stargazer.custom_columns(
    ['Model 1', 'Model 2','Model 3', 'Model 4'],
    [1, 1, 1, 1]
)
stargazer.add_line("Dependent Variable", ["Y"] * 4 )

# Render the consolidated LaTeX table
consolidated_latex_table = stargazer.render_latex()

# Combine all content into one LaTeX file
with open("TestTlessthan10.tex", 'w') as f:
    f.write(beginningtex)
    f.write("\\section*{teest Results}\n")
    f.write(consolidated_latex_table)
    f.write(endtex)

#%%   robustness check



# Define the exogenous variables
exog_vars_list = [
    #['logminimum_wage_annual_real',
    #               'first_digit','yeartimesfirst_digit','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
    #               'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
    #               'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
    #               'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday','age_at_last_birthday2'],
    #              ['logminimum_wage_annual_real',
    #               'sex_of_person_2.0','first_digit','yeartimesfirst_digit','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
    #                                 'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
    #                                 'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
    #                                 'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday','age_at_last_birthday2'],
    #              ['logminimum_wage_annual_real',
    #               'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','first_digit','yeartimesfirst_digit','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
    #                                 'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
    #                                 'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
    #                                 'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday','age_at_last_birthday2'],
    #              ['logminimum_wage_annual_real',
    #               'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','first_digit','yeartimesfirst_digit','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
    #                                 'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
    #                                 'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
    #                                 'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday','age_at_last_birthday2'],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],              
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real','sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
                   'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real','sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real','sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=f_datafull, return_type='dataframe')



exog_list = [sm.add_constant(pd.concat([f_datafull[exog_vars]], axis=1))  for exog_vars in exog_vars_list]



# Store all the results in a list
results_list = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit(cov_type='robust') #cov_type='robust')  # cov_type="clustered", clusters=f_datafull['yeardclust']
    results_list.append(results)

# Use Stargazer to create LaTeX table
stargazer = Stargazer([results for results in results_list])

# 'Model 1', 'Model 2', 'Model 3','Model 4', 
# Customize table appearance if needed
stargazer.title("Regression Results hourly wageRobust STD  ")
stargazer.custom_columns(['Model 1', 'Model 2','Model 3', 'Model 4','Model 5'], [ 1, 1, 1, 1, 1])
stargazer.show_model_numbers(False)

# Write to LaTeX file
beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\\end{document}"


with open("ROBUTSTDNEWlfpak_ols_modelsWagesminimuwagelog.tex", 'w') as dfoutput:
    dfoutput.write(beginningtex)
    dfoutput.write(stargazer.render_latex())
    dfoutput.write(endtex)    
 
    
#%% check 

#f_datafull['yeardclusttimeIndustrytimeoccupations_code_18timesfirst_three_digits']= f_datafull['yeardclusttimeIndustrytimeoccupations_code_18'] * f_datafull['first_three_digits']
#f_datafull['yeardclusttimeIndustrytimeoccupations_code_18timesfirst_digit']= f_datafull['yeardclusttimeIndustrytimeoccupations_code_18'] * f_datafull['first_digit']

# Define the list of exogenous variable names
exog_vars_list = ['logminimum_wage_annual_real','first_three_digits' ,'first_digit',
 'sex_of_person_2.0','sex_of_person_2.0Timeslogminimum_wage_annual_real','Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real','sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real','sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                   'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                   'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                   'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                   ,'age_at_last_birthday2'
                   ]
# Create a DataFrame of the exogenous variables by selecting them from f_datafull
exog_data = sm.add_constant(f_datafull[exog_vars_list]) # Add a constant as is good practice

# Run the model to get residuals
model_for_test = PanelOLS(f_datafull.logtotal_hours_annual, exog_data, entity_effects=False, time_effects=False)
results_for_test = model_for_test.fit(cov_type='robust')


 # --- Save the residuals to your dataframe ---
f_datafull['residuals'] = results_for_test.resids

print("Residuals have been calculated and added to the DataFrame.")
print(f_datafull[['residuals']].head())

 # --- Define your cluster variable name ---
 # This must be a column in your 'f_datafull' DataFrame
#cluster_variable = 'yeardclusttimeIndustrytimeoccupations_code_18timesfirst_digit'

# --- Run the Moulton test regression ---
 # We are testing if the residuals can be predicted by the cluster groups.
 
# yeardclusttimeIndustrytimeoccupations_code_18timesfirst_three_digits    (Avoid too many clsuters)
#yeardclusttimeIndustrytimeoccupations_code_18timesfirst_digit  (recomned  local labor market factors  introduce residual corelation)
#  'yeardclusttimeIndustrytimeoccupations_code_18'   (recomnded but ignor local labor market factors  -a ssume  occupational and industrial sorting over time )
sampled_data = f_datafull.sample(n=10000, random_state=42)  # or smaller if needed
test_formula = 'residuals ~ C( yeardclusttimeIndustrytimeoccupations_code_18)'
moulton_test = smf.ols(formula=test_formula, data=sampled_data).fit()
print(moulton_test.summary())


 # --- Print the summary of the test ---
print("\n--- Moulton Test for Clustering ---")
print(moulton_test.summary())
    
print("\n--- Moulton Test for Clustering ---")
print(f"F-statistic: {moulton_test.fvalue}")
print(f"Prob (F-statistic): {moulton_test.f_pvalue}")
#%%   iv with robust std 


# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real',
                   #'first_three_digits', 
                   'first_digit',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                   'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                   'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                   'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                   ,'age_at_last_birthday2'
                   ],
                  ['logminimum_wage_annual_real',
                   #'first_three_digits' ,
                   'first_digit',
                   'Lowedu_1','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real',
                   #'first_three_digits' ,
                   'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],              
                  ['logminimum_wage_annual_real'
                   #,'first_three_digits' 
                   ,'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real' #,'first_three_digits' 
                   ,'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]



exog_list = [sm.add_constant(pd.concat([f_datafull_Malesample[exog_vars]   ], axis=1))  for exog_vars in exog_vars_list]


# Store all the results in a list
results_list1 = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull_Malesample.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit(cov_type='robust' )   # cov_type="clustered", clusters=f_datafull_Malesample['yeardclust']
    results_list1.append(results)



# Define the exogenous variables
exog_vars_list = [['logminimum_wage_annual_real',
                   #'first_three_digits' ,
                   'first_digit',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                   'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                   'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                   'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                   ,'age_at_last_birthday2'
                   ],
                  ['logminimum_wage_annual_real',
                   #'first_three_digits' ,
                   'first_digit',
                   'Lowedu_1','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real',
                   #'first_three_digits' ,
                   'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],              
                  ['logminimum_wage_annual_real',
                   #'first_three_digits' ,
                   'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ],
                  ['logminimum_wage_annual_real', 
                   #'first_three_digits' ,
                   'first_digit',
                   'Lowedu_1','Lowedu_1Timeslogminimum_wage_annual_real','current_marital_status_2.0','current_marital_status_2.0Timeslogminimum_wage_annual_real',
                   'Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                                     'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
                                     'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
                                     'occupations_code_18_7.0','occupations_code_18_8.0','age_at_last_birthday'
                                     ,'age_at_last_birthday2'
                                     ]]


exog_list = [sm.add_constant(pd.concat([f_datafull_Femalesample[exog_vars]  ], axis=1))  for exog_vars in exog_vars_list]


# 'yeardclusttimeIndustry'   yeardclust

# Store all the results in a list
results_list2f = []

for exog in exog_list:
    # Run the regression
    cons = PanelOLS(f_datafull_Femalesample.loghourly_wage, exog, entity_effects=False, time_effects=False)
    results = cons.fit(cov_type='robust') #  cov_type='robust')    #cov_type="clustered", clusters=f_datafull_Femalesample['yeardclust']
    results_list2f.append(results)


# iv 
y = final_df_merged['loghourly_wage']
x_endog = final_df_merged['logminimum_wage_annual_real']


# Include controls in exogenous variables
controls = final_df_merged[[#'first_three_digits' ,
                            'first_digit','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                            'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
'occupations_code_18_7.0','occupations_code_18_8.0','sex_of_person_2.0',
                          'sex_of_person_2.0Timeslogminimum_wage_annual_real',
                          'Lowedu_1',
                          'Lowedu_1Timeslogminimum_wage_annual_real',
                          'current_marital_status_2.0',
                          'current_marital_status_2.0Timeslogminimum_wage_annual_real',
                          'sex_of_person_2.0Times_Lowedu_1Timeslogminimum_wage_annual_real',
                          'sex_of_person_2.0Timescurrent_marital_status_2.0Timeslogminimum_wage_annual_real'
                          ,'age_at_last_birthday'
                          ,'age_at_last_birthday2'
                          ]]



x_exog = pd.concat([controls], axis=1)

# Instruments should exclude columns already in x_exog
instrument = final_df_merged[['temp_index']]

# Add constant to exogenous variables but avoid duplicating constants in instruments
x_exog = sm.add_constant(x_exog)

# Perform IV Regression using 2SLS
iv_model2 = IV2SLS(dependent=y, exog=x_exog, endog=x_endog, instruments=instrument)
iv_results2 = iv_model2.fit(cov_type='robust')

# Display results
print(iv_results2.summary)

controls = final_df_merged[[#'first_three_digits' ,
                            'first_digit','Industry_1.0','Industry_2.0','Industry_3.0','Industry_4.0','Industry_5.0',
                            'Method2_Formal_2','PUBLIC','occupations_code_18_1.0','occupations_code_18_2.0','occupations_code_18_3.0',
'occupations_code_18_4.0','occupations_code_18_5.0','occupations_code_18_6.0',
'occupations_code_18_7.0','occupations_code_18_8.0','sex_of_person_2.0',
                          'Lowedu_1',
                          'current_marital_status_2.0'
                          ,'age_at_last_birthday'
                          ,'age_at_last_birthday2'
                          ]]

#fe_formula = 'first_three_digits - 1'
#y, X_fe = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')
#fe_formula = 'year22zz - 1'
#y, X_fe1 = patsy.dmatrices(f'loghourly_wage ~ {fe_formula}', data=final_df_merged, return_type='dataframe')

# First-stage regression to diagnose instruments
instrument_with_const = sm.add_constant(pd.concat([controls, instrument ], axis=1))
first_stage_model2 = sm.OLS(x_endog, instrument_with_const)
first_stage_results2 = first_stage_model2.fit( ) # cov_type='HC0')
print(first_stage_results2.summary())

# Define the beginning and ending parts of the LaTeX document
beginningtex = r"""
\documentclass{report}
\usepackage{booktabs}
\usepackage{geometry}
\geometry{a4paper, margin=1in}
\title{Consolidated Regression Results 2}
\author{Your Name}
\date{\today}
\begin{document}
\maketitle
"""

endtex = r"""
\end{document}
"""


# Consolidated LaTeX Table
all_results = results_list1[3:5] + results_list2f[3:5] + [first_stage_results2, iv_results2]
stargazer = Stargazer(all_results)


# Custom titles for each block
stargazer.title("Consolidated Regression Results robust STD ")
stargazer.custom_columns(
    ['Male Model 4', 'Male Model 5',
      'Female Model 4', 'Female Model 5',
     'IV First Stage', 'IV Second Stage (2SLS)'],
    [ 1, 1, 1, 1, 1, 1]
)
stargazer.add_line("Dependent Variable", ["Y"] * 4 + ["logminimum_wage_annual_real", "loghourly_wage"])

# Render the consolidated LaTeX table
consolidated_latex_table = stargazer.render_latex()

# Combine all content into one LaTeX file
with open("RobustSTDIV_additionacontrolsminimuwagelog.tex", 'w') as f:
    f.write(beginningtex)
    f.write("\\section*{Consolidated Regression Results}\n")
    f.write(consolidated_latex_table)
    f.write(endtex)


#%% dta file    save 



f_datafull.to_stata('f_datafull_requesetdSaite.dta', write_index=False)
