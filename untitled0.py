# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 07:40:35 2023

@author: marora42
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('BariPROMs_MasterData_FebToSep2023_v2.xlsx')
df = pd.read_csv('extracted_variables.csv')

#%%

numerical_features = ['food_log_protein',
 'food_log_carb',
 'food_log_fat',
 'food_log_fiber',
 'soda_intake', 
 'water_intake', 
 'sugary_beverages_intake']

outcome_variables = ['bodyq_ers',
 'bodyq_erd',
 'bodyq_erb',
 'gerd',
 'bmi',
 'post_op_bmi',
 'beds7_01_episodes',
 'beds7_02_distress',
 'beds7_03_no_control',
 'beds7_04_eat_after_full',
 'beds7_05_embarrassed',
 'beds7_06_guilt',
 'beds7_07_vomit',
'bodyq_phys_score']

#%%

gerd_data = df.loc[~df['gerd'].isna()]
gerd_0 = gerd_data.loc[gerd_data['exercise_frequency'] == -1]['gerd']
gerd_1 = gerd_data.loc[gerd_data['exercise_frequency'] == 1]['gerd']
gerd_2 = gerd_data.loc[gerd_data['exercise_frequency'] == 2]['gerd']
gerd_3 = gerd_data.loc[gerd_data['exercise_frequency'] == 3]['gerd']
gerd_4 = gerd_data.loc[gerd_data['exercise_frequency'] == 4]['gerd']
gerd_5 = gerd_data.loc[gerd_data['exercise_frequency'] == 5]['gerd']
gerd_6 = gerd_data.loc[gerd_data['exercise_frequency'] == 6]['gerd']
gerd_7 = gerd_data.loc[gerd_data['exercise_frequency'] == 7]['gerd']


dd = [gerd_0, gerd_1, gerd_2, gerd_3, gerd_4, gerd_5, gerd_6, gerd_7]

# Create a boxplot using Seaborn (which offers better aesthetics)
plt.figure(figsize=(8, 6))
sns.boxplot(data=dd)
plt.title('Gerd Score versus Exercise Frequency')
plt.xticks(ticks = [0, 1, 2, 3, 4, 5, 6, 7])
plt.xlabel('Exercise Frequency per week')
plt.ylabel('GERD Vales')
plt.show()

#%%

gerd_data = df.loc[~df['gerd'].isna()]
gerd_0 = gerd_data.loc[gerd_data['water_intake'] == -1]['gerd']
gerd_1 = gerd_data.loc[gerd_data['water_intake'] == 1]['gerd']
gerd_2 = gerd_data.loc[gerd_data['water_intake'] == 2]['gerd']
gerd_3 = gerd_data.loc[gerd_data['water_intake'] == 3]['gerd']
gerd_4 = gerd_data.loc[gerd_data['water_intake'] == 4]['gerd']
gerd_5 = gerd_data.loc[gerd_data['water_intake'] == 5]['gerd']
gerd_6 = gerd_data.loc[gerd_data['water_intake'] == 6]['gerd']
gerd_7 = gerd_data.loc[gerd_data['water_intake'] == 7]['gerd']
gerd_8 = gerd_data.loc[gerd_data['water_intake'] == 8]['gerd']
gerd_9 = gerd_data.loc[gerd_data['water_intake'] == 9]['gerd']
gerd_10 = gerd_data.loc[gerd_data['water_intake'] == 10]['gerd']


dd = [gerd_0, gerd_1, gerd_2, gerd_3, gerd_4, gerd_5, gerd_6, gerd_7, gerd_8, gerd_9, gerd_10]

# Create a boxplot using Seaborn (which offers better aesthetics)
plt.figure(figsize=(8, 6))
sns.boxplot(data=dd)
plt.title('Gerd Score versus Water Intake')
plt.xticks(ticks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.xlabel('Water Intake (cups/day)')
plt.ylabel('GERD Values')
plt.show()

#%%

gerd_data = df.loc[~df['gerd'].isna()]
gerd_0 = gerd_data.loc[gerd_data['sugary_beverages_intake'] == -1]['gerd']
gerd_1 = gerd_data.loc[gerd_data['sugary_beverages_intake'] == 1]['gerd']
gerd_2 = gerd_data.loc[gerd_data['sugary_beverages_intake'] == 2]['gerd']
gerd_3 = gerd_data.loc[gerd_data['sugary_beverages_intake'] == 3]['gerd']
gerd_4 = gerd_data.loc[gerd_data['sugary_beverages_intake'] == 4]['gerd']
gerd_5 = gerd_data.loc[gerd_data['sugary_beverages_intake'] == 5]['gerd']
gerd_6 = gerd_data.loc[gerd_data['sugary_beverages_intake'] == 6]['gerd']
gerd_7 = gerd_data.loc[gerd_data['sugary_beverages_intake'] >= 7]['gerd']


dd = [gerd_0, gerd_1, gerd_2, gerd_3, gerd_4, gerd_5, gerd_6, gerd_7]

# Create a boxplot using Seaborn (which offers better aesthetics)
plt.figure(figsize=(8, 6))
sns.boxplot(data=dd)
plt.title('Gerd Score versus Sugary Beverages Intake')
plt.xticks(ticks = [0, 1, 2, 3, 4, 5, 6, 7], labels = ['0', '1', '2', '3', '4', '5', '6', '>=7'])
plt.xlabel('Sugary Beverages Intake (cups/day)')
plt.ylabel('GERD Values')
plt.show()

#%%

gerd_data = df.loc[~df['gerd'].isna()]
gerd_1 = gerd_data.loc[gerd_data['1-2 drinks/day'] == 1]['gerd']
gerd_2 = gerd_data.loc[gerd_data['3-4 drinks/day'] == 1]['gerd']
gerd_3 = gerd_data.loc[gerd_data['5-6 drinks/day'] == 1]['gerd']
gerd_0 = gerd_data.loc[gerd_data['< 1 drink/day'] == 1]['gerd']
gerd_4 = gerd_data.loc[gerd_data['> 7 drinks/day'] == 1]['gerd']

dd = [gerd_0, gerd_1, gerd_2, gerd_3, gerd_4]

# Create a boxplot using Seaborn (which offers better aesthetics)
plt.figure(figsize=(8, 6))
sns.boxplot(data=dd)
plt.title('Gerd Score versus Alcohol Consumption')
plt.xticks(ticks = [0, 1, 2, 3, 4, 5], labels =  ['< 1 drink/day', '1-2 drink/day', '3-4 drink/day', '5-6 drink/day', '> 7 drink/day'])
plt.xlabel('Alcohol Consumption')
plt.ylabel('GERD Values')
plt.show()

#%%

gerd_data = df.loc[~df['gerd'].isna()]
gerd_yes = gerd_data.loc[gerd_data['after_dinner_snack_yes'] == 1]['gerd']
gerd_no = gerd_data.loc[gerd_data['after_dinner_snack_no'] == 1]['gerd']


dd = [gerd_yes, gerd_no]

# Create a boxplot using Seaborn (which offers better aesthetics)
plt.figure(figsize=(8, 6))
sns.boxplot(data=dd)
plt.title('Gerd Score versus After Dinner Snacking')
plt.xticks(ticks = [0, 1], labels =  ['yes', 'no'])
plt.xlabel('After Dinner Snacking')
plt.ylabel('GERD Values')
plt.show()

#%%

gerd_data = df.loc[~df['gerd'].isna()]
gerd_yes = gerd_data.loc[gerd_data['exercise_limitations_yes'] == 1]['gerd']
gerd_no = gerd_data.loc[gerd_data['exercise_limitations_no'] == 1]['gerd']


dd = [gerd_yes, gerd_no]

# Create a boxplot using Seaborn (which offers better aesthetics)
plt.figure(figsize=(8, 6))
sns.boxplot(data=dd)
plt.title('Gerd Score versus Exercise Limitations')
plt.xticks(ticks = [0, 1], labels =  ['yes', 'no'])
plt.xlabel('Exercise Limitations')
plt.ylabel('GERD Values')
plt.show()

#%%

gerd_data = df.loc[~df['gerd'].isna()]
gerd_1 = gerd_data.loc[gerd_data['exercise_walking'] == 1]['gerd']
gerd_2 = gerd_data.loc[gerd_data['exercise_jogging'] == 1]['gerd']
gerd_3 = gerd_data.loc[gerd_data['exercise_swimming'] == 1]['gerd']
gerd_4 = gerd_data.loc[gerd_data['exercise_cycling'] == 1]['gerd']
gerd_5 = gerd_data.loc[gerd_data['exercise_yoga'] == 1]['gerd']
gerd_6 = gerd_data.loc[gerd_data['exercise_weightlifting'] == 1]['gerd']
gerd_7 = gerd_data.loc[gerd_data['exercise_aerobics'] == 1]['gerd']

dd = [ gerd_1, gerd_2, gerd_3, gerd_4, gerd_5, gerd_6, gerd_7]

# Create a boxplot using Seaborn (which offers better aesthetics)
plt.figure(figsize=(8, 6))
sns.boxplot(data=dd)
plt.title('Gerd Score versus Exercise Type')
plt.xticks(ticks = [0, 1, 2, 3, 4, 5, 6], labels = ['walking', 'jogging', 'swimming', 'cycling', 'yoga', 'weightlifting', 'aerobics'])
plt.xlabel('Exercise Type')
plt.ylabel('GERD Values')
plt.show()

#%%

import pingouin as pg

data_gerd = data.loc[~df['gerd'].isna()]
df_anova = pd.DataFrame({'values': gerd_data['gerd'], 'groups': data_gerd['alcohol_consumption']})

pg.welch_anova(dv='values', between='groups', data=df_anova)

#%%

