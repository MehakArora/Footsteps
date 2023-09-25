# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:57:58 2023

@author: marora42
"""

import statsmodels.api as sm
import pandas as pd

# Sample data (replace this with your own dataset)



categorical = [ 'bed7_1', 'bed7_2',
       'bed7_3', 'bed7_4', 'bed7_5', 'bed7_6', 'bed7_7', 
        'alc_less_than1', 'alc_12',
       'alc_34', 'alc_more_5', 'never_smoked', 'used_to_smoke',
       'illicit_drugs', 'rec_drugs', 'income', 'exercise_frequency',
       'soda_intake', 'water_intake', 'sugary_beverages_intake',
       'exercise_limitations',
       'after_dinner_snacking', 'protein_baseline', 'carbs_baseline',
       'fats_baseline', 'fiber_baseline', 'protein_post', 'carbs_post',
       'fats_post', 'fiber_post', 'protein_pre', 'carbs_pre', 'fats_pre',
       'fiber_pre']


x_data = pat_info.loc[~pat_info['gerd_postsurg'].isna()]
# Define the predictor variables (X1, X2) and the outcome variable (Y)
X = x_data['exercise_frequency']
y = x_data['gerd_postsurg']

#%%
# Fit a logistic regression model
logit_model = sm.OLS(y.values, X)
result = logit_model.fit()

# Print the model summary, which includes the coefficients and statistics
print(result.summary())

#%%

gerd_data_post = pat_info.loc[~pat_info['gerd_postsurg'].isna()]
gerd_data_pre = pat_info.loc[~pat_info['gerd_presurg'].isna()]

#%%
post_food_data = gerd_data_post.loc[gerd_data_post['protein_post_']!=-1][['mrn', 'protein_post_', 'carbs_post_','fats_post_','fiber_post_',
                                                                          'gerd_postsurg', 'bodyq_ers_post', 'bodyq_erd_post', 'bodyq_erb_post']]
pre_food_data = gerd_data_pre.loc[gerd_data_pre['protein_pre_']!=-1][['mrn', 'protein_pre_', 'carbs_pre_','fats_pre_','fiber_pre_',
                                                                      'gerd_presurg', 'bodyq_ers_pre', 'bodyq_erd_pre', 'bodyq_erb_pre']]

#%%

total_cals_pre = pre_food_data['protein_pre_']*4 + pre_food_data['carbs_pre_']*4 + pre_food_data['fats_pre_']*9 + pre_food_data['fiber_pre_']*2
carb_perc_pre = (pre_food_data['carbs_pre_']*4)/total_cals_pre
high_carb_pre = carb_perc_pre > 0.6

#%%

total_cals_post = post_food_data['protein_post_']*4 + post_food_data['carbs_post_']*4 + post_food_data['fats_post_']*9 + post_food_data['fiber_post_']*2
carb_perc_post = (post_food_data['carbs_post_']*4)/total_cals_post
high_carb_post = carb_perc_post > 0.6

#%%

std_preop_high_carb_gerd = pre_food_data.loc[high_carb_pre]['gerd_presurg'].std()
std_postop_high_carb_gerd = post_food_data.loc[high_carb_post]['gerd_postsurg'].std()

std_preop_low_carb_gerd = pre_food_data.loc[~high_carb_pre]['gerd_presurg'].std()
std_postop_low_carb_gerd = post_food_data.loc[~high_carb_post]['gerd_postsurg'].std()
print(round(std_preop_high_carb_gerd, 3))
print(round(std_postop_high_carb_gerd,3))
print(round(std_preop_low_carb_gerd,3))
print(round(std_postop_low_carb_gerd,3))

#%%
std_preop_high_carb_ers = pre_food_data.loc[high_carb_pre]['bodyq_ers_pre'].std()
std_postop_high_carb_ers = post_food_data.loc[high_carb_post]['bodyq_ers_post'].std()

std_preop_low_carb_ers = pre_food_data.loc[~high_carb_pre]['bodyq_ers_pre'].std()
std_postop_low_carb_ers = post_food_data.loc[~high_carb_post]['bodyq_ers_post'].std()
print(round(std_preop_high_carb_ers,3))
print(round(std_postop_high_carb_ers,3))
print(round(std_preop_low_carb_ers,3))
print(round(std_postop_low_carb_ers,3))

#%%
std_preop_high_carb_erb = pre_food_data.loc[high_carb_pre]['bodyq_erb_pre'].std()
std_postop_high_carb_erb = post_food_data.loc[high_carb_post]['bodyq_erb_post'].std()

std_preop_low_carb_erb= pre_food_data.loc[~high_carb_pre]['bodyq_erb_pre'].std()
std_postop_low_carb_erb = post_food_data.loc[~high_carb_post]['bodyq_erb_post'].std()
print(round(std_preop_high_carb_erb,3))
print(round(std_postop_high_carb_erb,3))
print(round(std_preop_low_carb_erb,3))
print(round(std_postop_low_carb_erb,3))

#%%

std_preop_high_carb_erd = pre_food_data.loc[high_carb_pre]['bodyq_erd_pre'].std()
std_postop_high_carb_erd = post_food_data.loc[high_carb_post]['bodyq_erd_post'].std()

std_preop_low_carb_erd = pre_food_data.loc[~high_carb_pre]['bodyq_erd_pre'].std()
std_postop_low_carb_erd = post_food_data.loc[~high_carb_post]['bodyq_erd_post'].std()
print(round(std_preop_high_carb_erd,3))
print(round(std_postop_high_carb_erd,3))
print(round(std_preop_low_carb_erd,3))
print(round(std_postop_low_carb_erd,3))

#%%

print(len(pre_food_data.loc[high_carb_pre]))
print(len(post_food_data.loc[high_carb_post]))
print(len(pre_food_data.loc[~high_carb_pre]))
print(len(post_food_data.loc[~high_carb_post]))


#%%

from scipy.stats import ttest_ind
from scipy.stats import t

print("Pre-Operative")


print("GERD")
t_stat, p = ttest_ind(pre_food_data.loc[high_carb_pre]['gerd_presurg'], pre_food_data.loc[~high_carb_pre]['gerd_presurg'])
print("High carbs (Mean) = {}".format(pre_food_data.loc[high_carb_pre]['gerd_presurg'].mean()))
print("Low carbs (Mean) = {}".format( pre_food_data.loc[~high_carb_pre]['gerd_presurg'].mean()))
print("High carbs (std) = {}".format(pre_food_data.loc[high_carb_pre]['gerd_presurg'].std()))
print("Low carbs (std) = {}".format( pre_food_data.loc[~high_carb_pre]['gerd_presurg'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERS")
t_stat, p = ttest_ind(pre_food_data.loc[high_carb_pre]['bodyq_ers_pre'], pre_food_data.loc[~high_carb_pre]['bodyq_ers_pre'])
print("High carbs (Mean) = {}".format(pre_food_data.loc[high_carb_pre]['bodyq_ers_pre'].mean()))
print("Low carbs (Mean) = {}".format( pre_food_data.loc[~high_carb_pre]['bodyq_ers_pre'].mean()))
print("High carbs (std) = {}".format(pre_food_data.loc[high_carb_pre]['bodyq_ers_pre'].std()))
print("Low carbs (std) = {}".format( pre_food_data.loc[~high_carb_pre]['bodyq_ers_pre'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERB")
t_stat, p = ttest_ind(pre_food_data.loc[high_carb_pre]['bodyq_erb_pre'], pre_food_data.loc[~high_carb_pre]['bodyq_erb_pre'])
print("High carbs (Mean) = {}".format(pre_food_data.loc[high_carb_pre]['bodyq_erb_pre'].mean()))
print("Low carbs (Mean) = {}".format( pre_food_data.loc[~high_carb_pre]['bodyq_erb_pre'].mean()))
print("High carbs (std) = {}".format(pre_food_data.loc[high_carb_pre]['bodyq_erb_pre'].std()))
print("Low carbs (std) = {}".format( pre_food_data.loc[~high_carb_pre]['bodyq_erb_pre'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

print("BODYQ ERD")
t_stat, p = ttest_ind(pre_food_data.loc[high_carb_pre]['bodyq_erd_pre'], pre_food_data.loc[~high_carb_pre]['bodyq_erd_pre'])
print("High carbs (Mean) = {}".format(pre_food_data.loc[high_carb_pre]['bodyq_erd_pre'].mean()))
print("Low carbs (Mean) = {}".format( pre_food_data.loc[~high_carb_pre]['bodyq_erd_pre'].mean()))
print("High carbs (std) = {}".format(pre_food_data.loc[high_carb_pre]['bodyq_erd_pre'].std()))
print("Low carbs (std) = {}".format( pre_food_data.loc[~high_carb_pre]['bodyq_erd_pre'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

#%%
print("Post-Operative")

print("GERD")
t_stat, p = ttest_ind(post_food_data.loc[high_carb_post]['gerd_postsurg'], post_food_data.loc[~high_carb_post]['gerd_postsurg'])
print("High carbs (Mean) = {}".format(post_food_data.loc[high_carb_post]['gerd_postsurg'].mean()))
print("Low carbs (Mean) = {}".format( post_food_data.loc[~high_carb_post]['gerd_postsurg'].mean()))
print("High carbs (std) = {}".format(post_food_data.loc[high_carb_post]['gerd_postsurg'].std()))
print("Low carbs (std) = {}".format( post_food_data.loc[~high_carb_post]['gerd_postsurg'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERS")
t_stat, p = ttest_ind(post_food_data.loc[high_carb_post]['bodyq_ers_post'], post_food_data.loc[~high_carb_post]['bodyq_ers_post'])
print("High carbs (Mean) = {}".format(post_food_data.loc[high_carb_post]['bodyq_ers_post'].mean()))
print("Low carbs (Mean) = {}".format( post_food_data.loc[~high_carb_post]['bodyq_ers_post'].mean()))
print("High carbs (std) = {}".format(post_food_data.loc[high_carb_post]['bodyq_ers_post'].std()))
print("Low carbs (std) = {}".format( post_food_data.loc[~high_carb_post]['bodyq_ers_post'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERB")
t_stat, p = ttest_ind(post_food_data.loc[high_carb_post]['bodyq_erb_post'], post_food_data.loc[~high_carb_post]['bodyq_erb_post'])
print("High carbs (Mean) = {}".format(post_food_data.loc[high_carb_post]['bodyq_erb_post'].mean()))
print("Low carbs (Mean) = {}".format( post_food_data.loc[~high_carb_post]['bodyq_erb_post'].mean()))
print("High carbs (std) = {}".format(post_food_data.loc[high_carb_post]['bodyq_erb_post'].std()))
print("Low carbs (std) = {}".format( post_food_data.loc[~high_carb_post]['bodyq_erb_post'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

print("BODYQ ERD")
t_stat, p = ttest_ind(post_food_data.loc[high_carb_post]['bodyq_erd_post'], post_food_data.loc[~high_carb_post]['bodyq_erd_post'])
print("High carbs (Mean) = {}".format(post_food_data.loc[high_carb_post]['bodyq_erd_post'].mean()))
print("Low carbs (Mean) = {}".format( post_food_data.loc[~high_carb_post]['bodyq_erd_post'].mean()))
print("High carbs (std) = {}".format(post_food_data.loc[high_carb_post]['bodyq_erd_post'].std()))
print("Low carbs (std) = {}".format( post_food_data.loc[~high_carb_post]['bodyq_erd_post'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

#%%

print("High carbs")

print("GERD")
t_stat, p = ttest_ind(pre_food_data.loc[high_carb_pre]['gerd_presurg'], post_food_data.loc[high_carb_post]['gerd_postsurg'])
print("Pre Op (Mean) = {}".format(pre_food_data.loc[high_carb_pre]['gerd_presurg'].mean()))
print("Post Op (Mean) = {}".format( post_food_data.loc[high_carb_post]['gerd_postsurg'].mean()))
print("Pre Op (std) = {}".format(pre_food_data.loc[high_carb_pre]['gerd_presurg'].std()))
print("Post Op (std) = {}".format( post_food_data.loc[high_carb_post]['gerd_postsurg'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERS")
t_stat, p = ttest_ind(pre_food_data.loc[high_carb_pre]['bodyq_ers_pre'], post_food_data.loc[high_carb_post]['bodyq_ers_post'])
print("Pre Op (Mean) = {}".format(pre_food_data.loc[high_carb_pre]['bodyq_ers_pre'].mean()))
print("Post Op (Mean) = {}".format( post_food_data.loc[high_carb_post]['bodyq_ers_post'].mean()))
print("Pre Op (std) = {}".format(pre_food_data.loc[high_carb_pre]['bodyq_ers_pre'].std()))
print("Post Op (std) = {}".format( post_food_data.loc[high_carb_post]['bodyq_ers_post'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERB")
t_stat, p = ttest_ind(pre_food_data.loc[high_carb_pre]['bodyq_erb_pre'], post_food_data.loc[high_carb_post]['bodyq_erb_post'])
print("Pre Op (Mean) = {}".format(pre_food_data.loc[high_carb_pre]['bodyq_erb_pre'].mean()))
print("Post Op (Mean) = {}".format( post_food_data.loc[high_carb_post]['bodyq_erb_post'].mean()))
print("Pre Op (std) = {}".format(pre_food_data.loc[high_carb_pre]['bodyq_erb_pre'].std()))
print("Post Op (std) = {}".format( post_food_data.loc[high_carb_post]['bodyq_erb_post'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

print("BODYQ ERD")
t_stat, p = ttest_ind(pre_food_data.loc[high_carb_pre]['bodyq_erd_pre'], post_food_data.loc[high_carb_post]['bodyq_erd_post'])
print("Pre Op (Mean) = {}".format(pre_food_data.loc[high_carb_pre]['bodyq_erd_pre'].mean()))
print("Post Op (Mean) = {}".format( post_food_data.loc[high_carb_post]['bodyq_erd_post'].mean()))
print("Pre Op (std) = {}".format(pre_food_data.loc[high_carb_pre]['bodyq_erd_pre'].std()))
print("Post Op (std) = {}".format( post_food_data.loc[high_carb_post]['bodyq_erd_post'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


#%%

print("Low carbs")

print("GERD")
t_stat, p = ttest_ind(pre_food_data.loc[~high_carb_pre]['gerd_presurg'], post_food_data.loc[~high_carb_post]['gerd_postsurg'])
print("Pre Op (Mean) = {}".format(pre_food_data.loc[~high_carb_pre]['gerd_presurg'].mean()))
print("Post Op (Mean) = {}".format( post_food_data.loc[~high_carb_post]['gerd_postsurg'].mean()))
print("Pre Op (std) = {}".format(pre_food_data.loc[~high_carb_pre]['gerd_presurg'].std()))
print("Post Op (std) = {}".format( post_food_data.loc[~high_carb_post]['gerd_postsurg'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERS")
t_stat, p = ttest_ind(pre_food_data.loc[~high_carb_pre]['bodyq_ers_pre'], post_food_data.loc[~high_carb_post]['bodyq_ers_post'])
print("Pre Op (Mean) = {}".format(pre_food_data.loc[~high_carb_pre]['bodyq_ers_pre'].mean()))
print("Post Op (Mean) = {}".format( post_food_data.loc[~high_carb_post]['bodyq_ers_post'].mean()))
print("Pre Op (std) = {}".format(pre_food_data.loc[~high_carb_pre]['bodyq_ers_pre'].std()))
print("Post Op (std) = {}".format( post_food_data.loc[~high_carb_post]['bodyq_ers_post'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERB")
t_stat, p = ttest_ind(pre_food_data.loc[~high_carb_pre]['bodyq_erb_pre'], post_food_data.loc[~high_carb_post]['bodyq_erb_post'])
print("Pre Op (Mean) = {}".format(pre_food_data.loc[~high_carb_pre]['bodyq_erb_pre'].mean()))
print("Post Op (Mean) = {}".format( post_food_data.loc[~high_carb_post]['bodyq_erb_post'].mean()))
print("Pre Op (std) = {}".format(pre_food_data.loc[~high_carb_pre]['bodyq_erb_pre'].std()))
print("Post Op (std) = {}".format( post_food_data.loc[~high_carb_post]['bodyq_erb_post'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

print("BODYQ ERD")
t_stat, p = ttest_ind(pre_food_data.loc[~high_carb_pre]['bodyq_erd_pre'], post_food_data.loc[~high_carb_post]['bodyq_erd_post'])
print("Pre Op (Mean) = {}".format(pre_food_data.loc[~high_carb_pre]['bodyq_erd_pre'].mean()))
print("Post Op (Mean) = {}".format( post_food_data.loc[~high_carb_post]['bodyq_erd_post'].mean()))
print("Pre Op (std) = {}".format(pre_food_data.loc[~high_carb_pre]['bodyq_erd_pre'].std()))
print("Post Op (std) = {}".format( post_food_data.loc[~high_carb_post]['bodyq_erd_post'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


#%%
post_exercise_data = gerd_data_post.loc[gerd_data_post['exercise_frequency_post'] != -3][['exercise_frequency_post',
                                     'gerd_postsurg', 'bodyq_ers_post', 'bodyq_erd_post', 'bodyq_erb_post']]
pre_exercise_data = gerd_data_pre.loc[gerd_data_pre['exercise_frequency_pre'] != -2][['exercise_frequency_pre',
                                     'gerd_presurg', 'bodyq_ers_pre', 'bodyq_erd_pre', 'bodyq_erb_pre']]
#%%



#exercise_no_post = post_exercise_data['exercise_frequency_post'] <=0
exercise_low_post = post_exercise_data['exercise_frequency_post'].isin([-1, 0,1,2])
exercise_high_post = post_exercise_data['exercise_frequency_post'] > 2

#exercise_no_pre = pre_exercise_data['exercise_frequency_pre'] == -1
exercise_low_pre = pre_exercise_data['exercise_frequency_pre'].isin([-1, 0,1,2])
exercise_high_pre = pre_exercise_data['exercise_frequency_pre'] > 2
#%%

print("No Exercise")

print("GERD")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_no_post]['gerd_postsurg'], pre_exercise_data.loc[exercise_no_pre]['gerd_presurg'])
print("Pre Op (Mean) = {}".format(pre_exercise_data.loc[exercise_no_pre]['gerd_presurg'].mean()))
print("Post Op (Mean) = {}".format( post_exercise_data.loc[exercise_no_post]['gerd_postsurg'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERS")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_no_post]['bodyq_ers_post'], pre_exercise_data.loc[exercise_no_pre]['bodyq_ers_pre'])
print("Pre Op (Mean) = {}".format(pre_exercise_data.loc[exercise_no_pre]['bodyq_ers_pre'].mean()))
print("Post Op (Mean) = {}".format( post_exercise_data.loc[exercise_no_post]['bodyq_ers_post'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERB")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_no_post]['bodyq_erb_post'], pre_exercise_data.loc[exercise_no_pre]['bodyq_erb_pre'])
print("Pre Op (Mean) = {}".format(pre_exercise_data.loc[exercise_no_pre]['bodyq_erb_pre'].mean()))
print("Post Op (Mean) = {}".format( post_exercise_data.loc[exercise_no_post]['bodyq_erb_post'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

print("BODYQ ERD")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_no_post]['bodyq_erd_post'], pre_exercise_data.loc[exercise_no_pre]['bodyq_erd_pre'])
print("Pre Op (Mean) = {}".format(pre_exercise_data.loc[exercise_no_pre]['bodyq_erd_pre'].mean()))
print("Post Op (Mean) = {}".format( post_exercise_data.loc[exercise_no_post]['bodyq_erd_post'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


#%%

print("Low Exercise")

print("GERD")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_low_post]['gerd_postsurg'], pre_exercise_data.loc[exercise_low_pre]['gerd_presurg'])
print("Pre Op (Mean) = {}".format(pre_exercise_data.loc[exercise_low_pre]['gerd_presurg'].mean()))
print("Post Op (Mean) = {}".format( post_exercise_data.loc[exercise_low_post]['gerd_postsurg'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERS")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_low_post]['bodyq_ers_post'], pre_exercise_data.loc[exercise_low_pre]['bodyq_ers_pre'])
print("Pre Op (Mean) = {}".format(pre_exercise_data.loc[exercise_low_pre]['bodyq_ers_pre'].mean()))
print("Post Op (Mean) = {}".format( post_exercise_data.loc[exercise_low_post]['bodyq_ers_post'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERB")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_low_post]['bodyq_erb_post'], pre_exercise_data.loc[exercise_low_pre]['bodyq_erb_pre'])
print("Pre Op (Mean) = {}".format(pre_exercise_data.loc[exercise_low_pre]['bodyq_erb_pre'].mean()))
print("Post Op (Mean) = {}".format( post_exercise_data.loc[exercise_low_post]['bodyq_erb_post'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

print("BODYQ ERD")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_low_post]['bodyq_erd_post'], pre_exercise_data.loc[exercise_low_pre]['bodyq_erd_pre'])
print("Pre Op (Mean) = {}".format(pre_exercise_data.loc[exercise_low_pre]['bodyq_erd_pre'].mean()))
print("Post Op (Mean) = {}".format( post_exercise_data.loc[exercise_low_post]['bodyq_erd_post'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


#%%

print("High Exercise")

print("GERD")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_high_post]['gerd_postsurg'], pre_exercise_data.loc[exercise_high_pre]['gerd_presurg'])
print("Pre Op (Mean) = {}".format(pre_exercise_data.loc[exercise_high_pre]['gerd_presurg'].mean()))
print("Post Op (Mean) = {}".format( post_exercise_data.loc[exercise_high_post]['gerd_postsurg'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERS")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_high_post]['bodyq_ers_post'], pre_exercise_data.loc[exercise_high_pre]['bodyq_ers_pre'])
print("Pre Op (Mean) = {}".format(pre_exercise_data.loc[exercise_high_pre]['bodyq_ers_pre'].mean()))
print("Post Op (Mean) = {}".format( post_exercise_data.loc[exercise_high_post]['bodyq_ers_post'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERB")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_high_post]['bodyq_erb_post'], pre_exercise_data.loc[exercise_high_pre]['bodyq_erb_pre'])
print("Pre Op (Mean) = {}".format(pre_exercise_data.loc[exercise_high_pre]['bodyq_erb_pre'].mean()))
print("Post Op (Mean) = {}".format( post_exercise_data.loc[exercise_high_post]['bodyq_erb_post'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

print("BODYQ ERD")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_high_post]['bodyq_erd_post'], pre_exercise_data.loc[exercise_high_pre]['bodyq_erd_pre'])
print("Pre Op (Mean) = {}".format(pre_exercise_data.loc[exercise_high_pre]['bodyq_erd_pre'].mean()))
print("Post Op (Mean) = {}".format( post_exercise_data.loc[exercise_high_post]['bodyq_erd_post'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

#%%

print("High Exercise")

print("GERD")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_high_post]['gerd_postsurg'], pre_exercise_data.loc[exercise_high_pre]['gerd_presurg'])
print("Pre Op (Mean) = {}".format(pre_exercise_data.loc[exercise_high_pre]['gerd_presurg'].mean()))
print("Post Op (Mean) = {}".format( post_exercise_data.loc[exercise_high_post]['gerd_postsurg'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERS")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_high_post]['bodyq_ers_post'], pre_exercise_data.loc[exercise_high_pre]['bodyq_ers_pre'])
print("Pre Op (Mean) = {}".format(pre_exercise_data.loc[exercise_high_pre]['bodyq_ers_pre'].mean()))
print("Post Op (Mean) = {}".format( post_exercise_data.loc[exercise_high_post]['bodyq_ers_post'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERB")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_high_post]['bodyq_erb_post'], pre_exercise_data.loc[exercise_high_pre]['bodyq_erb_pre'])
print("Pre Op (Mean) = {}".format(pre_exercise_data.loc[exercise_high_pre]['bodyq_erb_pre'].mean()))
print("Post Op (Mean) = {}".format( post_exercise_data.loc[exercise_high_post]['bodyq_erb_post'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

print("BODYQ ERD")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_high_post]['bodyq_erd_post'], pre_exercise_data.loc[exercise_high_pre]['bodyq_erd_pre'])
print("Pre Op (Mean) = {}".format(pre_exercise_data.loc[exercise_high_pre]['bodyq_erd_pre'].mean()))
print("Post Op (Mean) = {}".format( post_exercise_data.loc[exercise_high_post]['bodyq_erd_post'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

#%%

print("Pre Op")

print("GERD")
t_stat, p = ttest_ind(pre_exercise_data.loc[exercise_high_pre]['gerd_presurg'], pre_exercise_data.loc[exercise_low_pre]['gerd_presurg'])
print("Low Exercise (Mean) = {}".format(pre_exercise_data.loc[exercise_low_pre]['gerd_presurg'].mean()))
print("High Exercise (Mean) = {}".format( pre_exercise_data.loc[exercise_high_pre]['gerd_presurg'].mean()))
print("Low Exercise (std) = {}".format(pre_exercise_data.loc[exercise_low_pre]['gerd_presurg'].std()))
print("High Exercise (std) = {}".format( pre_exercise_data.loc[exercise_high_pre]['gerd_presurg'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERS")
t_stat, p = ttest_ind(pre_exercise_data.loc[exercise_low_pre]['bodyq_ers_pre'], pre_exercise_data.loc[exercise_high_pre]['bodyq_ers_pre'])
print("Low Exercise  (Mean) = {}".format(pre_exercise_data.loc[exercise_low_pre]['bodyq_ers_pre'].mean()))
print("High Exercise (Mean) = {}".format( pre_exercise_data.loc[exercise_high_pre]['bodyq_ers_pre'].mean()))
print("Low Exercise  (std) = {}".format(pre_exercise_data.loc[exercise_low_pre]['bodyq_ers_pre'].std()))
print("High Exercise (std) = {}".format( pre_exercise_data.loc[exercise_high_pre]['bodyq_ers_pre'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERB")
t_stat, p = ttest_ind(pre_exercise_data.loc[exercise_low_pre]['bodyq_erb_pre'], pre_exercise_data.loc[exercise_high_pre]['bodyq_erb_pre'])
print("Low Exercise  (Mean) = {}".format(pre_exercise_data.loc[exercise_low_pre]['bodyq_erb_pre'].mean()))
print("High Exercise  (Mean) = {}".format( pre_exercise_data.loc[exercise_high_pre]['bodyq_erb_pre'].mean()))
print("Low Exercise  (std) = {}".format(pre_exercise_data.loc[exercise_low_pre]['bodyq_erb_pre'].std()))
print("High Exercise  (std) = {}".format( pre_exercise_data.loc[exercise_high_pre]['bodyq_erb_pre'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

print("BODYQ ERD")
t_stat, p = ttest_ind(pre_exercise_data.loc[exercise_low_pre]['bodyq_erd_pre'], pre_exercise_data.loc[exercise_high_pre]['bodyq_erd_pre'])
print("Low Exercise (Mean) = {}".format(pre_exercise_data.loc[exercise_low_pre]['bodyq_erd_pre'].mean()))
print("High Exercise  (Mean) = {}".format( pre_exercise_data.loc[exercise_high_pre]['bodyq_erd_pre'].mean()))
print("Low Exercise (std) = {}".format(pre_exercise_data.loc[exercise_low_pre]['bodyq_erd_pre'].std()))
print("High Exercise  (std) = {}".format( pre_exercise_data.loc[exercise_high_pre]['bodyq_erd_pre'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


#%%

print("Post Op")

print("GERD")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_high_post]['gerd_postsurg'], post_exercise_data.loc[exercise_low_post]['gerd_postsurg'])
print("Low Exercise (Mean) = {}".format(post_exercise_data.loc[exercise_low_post]['gerd_postsurg'].mean()))
print("High Exercise (Mean) = {}".format( post_exercise_data.loc[exercise_high_post]['gerd_postsurg'].mean()))
print("Low Exercise (std) = {}".format(post_exercise_data.loc[exercise_low_post]['gerd_postsurg'].std()))
print("High Exercise (std) = {}".format( post_exercise_data.loc[exercise_high_post]['gerd_postsurg'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERS")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_low_post]['bodyq_ers_post'], post_exercise_data.loc[exercise_high_post]['bodyq_ers_post'])
print("Low Exercise  (Mean) = {}".format(post_exercise_data.loc[exercise_low_post]['bodyq_ers_post'].mean()))
print("High Exercise (Mean) = {}".format( post_exercise_data.loc[exercise_high_post]['bodyq_ers_post'].mean()))
print("Low Exercise  (std) = {}".format(post_exercise_data.loc[exercise_low_post]['bodyq_ers_post'].std()))
print("High Exercise (std) = {}".format( post_exercise_data.loc[exercise_high_post]['bodyq_ers_post'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERB")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_low_post]['bodyq_erb_post'], post_exercise_data.loc[exercise_high_post]['bodyq_erb_post'])
print("Low Exercise  (Mean) = {}".format(post_exercise_data.loc[exercise_low_post]['bodyq_erb_post'].mean()))
print("High Exercise  (Mean) = {}".format( post_exercise_data.loc[exercise_high_post]['bodyq_erb_post'].mean()))
print("Low Exercise  (std) = {}".format(post_exercise_data.loc[exercise_low_post]['bodyq_erb_post'].std()))
print("High Exercise  (std) = {}".format( post_exercise_data.loc[exercise_high_post]['bodyq_erb_post'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

print("BODYQ ERD")
t_stat, p = ttest_ind(post_exercise_data.loc[exercise_low_post]['bodyq_erd_post'], post_exercise_data.loc[exercise_high_post]['bodyq_erd_post'])
print("Low Exercise (Mean) = {}".format(post_exercise_data.loc[exercise_low_post]['bodyq_erd_post'].mean()))
print("High Exercise  (Mean) = {}".format( post_exercise_data.loc[exercise_high_post]['bodyq_erd_post'].mean()))
print("Low Exercise (std) = {}".format(post_exercise_data.loc[exercise_low_post]['bodyq_erd_post'].std()))
print("High Exercise  (std) = {}".format( post_exercise_data.loc[exercise_high_post]['bodyq_erd_post'].std()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

#%%

print(len(pre_exercise_data.loc[exercise_low_pre]))
print(len(pre_exercise_data.loc[exercise_high_pre]))
print(len(post_exercise_data.loc[exercise_low_post]))
print(len(post_exercise_data.loc[exercise_high_post]))




#%%
post_exercise_data['groups'] = np.zeros(len(post_exercise_data))
post_exercise_data['groups'].loc[exercise_low_post] = 1
post_exercise_data['groups'].loc[exercise_high_post] = 2

pre_exercise_data['groups'] = np.zeros(len(pre_exercise_data))
pre_exercise_data['groups'].loc[exercise_low_pre] = 1
pre_exercise_data['groups'].loc[exercise_high_pre] = 2

#%%

from scipy.stats import f_oneway

print("Post Op")
print("GERD")

result = f_oneway(post_exercise_data.loc[exercise_no_post]['gerd_postsurg'],
         post_exercise_data.loc[exercise_low_post]['gerd_postsurg'],
         post_exercise_data.loc[exercise_high_post]['gerd_postsurg'])
print("No Exercise (Mean) = {}".format(post_exercise_data.loc[exercise_no_post]['gerd_postsurg'].mean()))
print("Low Exercise (Mean) = {}".format( post_exercise_data.loc[exercise_low_post]['gerd_postsurg'].mean()))
print("High Exercise (Mean) = {}".format( post_exercise_data.loc[exercise_high_post]['gerd_postsurg'].mean()))
print("P value (ANOVA) : {}".format(result.pvalue))


print("BODYQ ERS")
result = f_oneway(post_exercise_data.loc[exercise_no_post]['bodyq_ers_post'],
         post_exercise_data.loc[exercise_low_post]['bodyq_ers_post'],
         post_exercise_data.loc[exercise_high_post]['bodyq_ers_post'])
print("No Exercise (Mean) = {}".format(post_exercise_data.loc[exercise_no_post]['bodyq_ers_post'].mean()))
print("Low Exercise (Mean) = {}".format( post_exercise_data.loc[exercise_low_post]['bodyq_ers_post'].mean()))
print("High Exercise (Mean) = {}".format( post_exercise_data.loc[exercise_high_post]['bodyq_ers_post'].mean()))
print("P value (ANOVA) : {}".format(result.pvalue))

print("BODYQ ERB")
result = f_oneway(post_exercise_data.loc[exercise_no_post]['bodyq_erb_post'],
         post_exercise_data.loc[exercise_low_post]['bodyq_erb_post'],
         post_exercise_data.loc[exercise_high_post]['bodyq_erb_post'])
print("No Exercise (Mean) = {}".format(post_exercise_data.loc[exercise_no_post]['bodyq_erb_post'].mean()))
print("Low Exercise (Mean) = {}".format( post_exercise_data.loc[exercise_low_post]['bodyq_erb_post'].mean()))
print("High Exercise (Mean) = {}".format( post_exercise_data.loc[exercise_high_post]['bodyq_erb_post'].mean()))
print("P value (ANOVA) : {}".format(result.pvalue))


print("BODYQ ERD")
result = f_oneway(post_exercise_data.loc[exercise_no_post]['bodyq_erd_post'],
         post_exercise_data.loc[exercise_low_post]['bodyq_erd_post'],
         post_exercise_data.loc[exercise_high_post]['bodyq_erd_post'])
print("No Exercise (Mean) = {}".format(post_exercise_data.loc[exercise_no_post]['bodyq_erd_post'].mean()))
print("Low Exercise (Mean) = {}".format( post_exercise_data.loc[exercise_low_post]['bodyq_erd_post'].mean()))
print("High Exercise (Mean) = {}".format( post_exercise_data.loc[exercise_high_post]['bodyq_erd_post'].mean()))
print("P value (ANOVA) : {}".format(result.pvalue))

#%%

print("Pre Op")
print("GERD")

result = f_oneway(pre_exercise_data.loc[exercise_no_pre]['gerd_presurg'],
         pre_exercise_data.loc[exercise_low_pre]['gerd_presurg'],
         pre_exercise_data.loc[exercise_high_pre]['gerd_presurg'])
print("No Exercise (Mean) = {}".format(pre_exercise_data.loc[exercise_no_pre]['gerd_presurg'].mean()))
print("Low Exercise (Mean) = {}".format( pre_exercise_data.loc[exercise_low_pre]['gerd_presurg'].mean()))
print("High Exercise (Mean) = {}".format( pre_exercise_data.loc[exercise_high_pre]['gerd_presurg'].mean()))
print("P value (ANOVA) : {}".format(result.pvalue))


print("BODYQ ERS")
result = f_oneway(pre_exercise_data.loc[exercise_no_pre]['bodyq_ers_pre'],
         pre_exercise_data.loc[exercise_low_pre]['bodyq_ers_pre'],
         pre_exercise_data.loc[exercise_high_pre]['bodyq_ers_pre'])
print("No Exercise (Mean) = {}".format(pre_exercise_data.loc[exercise_no_pre]['bodyq_ers_pre'].mean()))
print("Low Exercise (Mean) = {}".format( pre_exercise_data.loc[exercise_low_pre]['bodyq_ers_pre'].mean()))
print("High Exercise (Mean) = {}".format( pre_exercise_data.loc[exercise_high_pre]['bodyq_ers_pre'].mean()))
print("P value (ANOVA) : {}".format(result.pvalue))

print("BODYQ ERB")
result = f_oneway(pre_exercise_data.loc[exercise_no_pre]['bodyq_erb_pre'],
         pre_exercise_data.loc[exercise_low_pre]['bodyq_erb_pre'],
         pre_exercise_data.loc[exercise_high_pre]['bodyq_erb_pre'])
print("No Exercise (Mean) = {}".format(pre_exercise_data.loc[exercise_no_pre]['bodyq_erb_pre'].mean()))
print("Low Exercise (Mean) = {}".format( pre_exercise_data.loc[exercise_low_pre]['bodyq_erb_pre'].mean()))
print("High Exercise (Mean) = {}".format( pre_exercise_data.loc[exercise_high_pre]['bodyq_erb_pre'].mean()))
print("P value (ANOVA) : {}".format(result.pvalue))


print("BODYQ ERD")
result = f_oneway(pre_exercise_data.loc[exercise_no_pre]['bodyq_erd_pre'],
         pre_exercise_data.loc[exercise_low_pre]['bodyq_erd_pre'],
         pre_exercise_data.loc[exercise_high_pre]['bodyq_erd_pre'])
print("No Exercise (Mean) = {}".format(pre_exercise_data.loc[exercise_no_pre]['bodyq_erd_pre'].mean()))
print("Low Exercise (Mean) = {}".format( pre_exercise_data.loc[exercise_low_pre]['bodyq_erd_pre'].mean()))
print("High Exercise (Mean) = {}".format( pre_exercise_data.loc[exercise_high_pre]['bodyq_erd_pre'].mean()))
print("P value (ANOVA) : {}".format(result.pvalue))


#%%





























