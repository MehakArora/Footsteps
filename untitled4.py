# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:31:44 2023

@author: marora42
"""

print("Pre-Operative")

print("GERD")
t_stat, p = ttest_ind(pre_food_data.loc[high_carb_pre]['gerd_presurg'], pre_food_data.loc[~high_carb_pre]['gerd_presurg'])
print("High Carbs (Mean) = {}".format(pre_food_data.loc[high_carb_pre]['gerd_presurg'].mean()))
print("Low Carbs (Mean) = {}".format( pre_food_data.loc[~high_carb_pre]['gerd_presurg'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERS")
t_stat, p = ttest_ind(pre_food_data.loc[high_carb_pre]['bodyq_ers_pre'], pre_food_data.loc[~high_carb_pre]['bodyq_ers_pre'])
print("High Carbs (Mean) = {}".format(pre_food_data.loc[high_carb_pre]['bodyq_ers_pre'].mean()))
print("Low Carbs (Mean) = {}".format( pre_food_data.loc[~high_carb_pre]['bodyq_ers_pre'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERB")
t_stat, p = ttest_ind(pre_food_data.loc[high_carb_pre]['bodyq_erb_pre'], pre_food_data.loc[~high_carb_pre]['bodyq_erb_pre'])
print("High Carbs (Mean) = {}".format(pre_food_data.loc[high_carb_pre]['bodyq_erb_pre'].mean()))
print("Low Carbs (Mean) = {}".format( pre_food_data.loc[~high_carb_pre]['bodyq_erb_pre'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

print("BODYQ ERD")
t_stat, p = ttest_ind(pre_food_data.loc[high_carb_pre]['bodyq_erd_pre'], pre_food_data.loc[~high_carb_pre]['bodyq_erd_pre'])
print("High Carbs (Mean) = {}".format(pre_food_data.loc[high_carb_pre]['bodyq_erd_pre'].mean()))
print("Low Carbs (Mean) = {}".format( pre_food_data.loc[~high_carb_pre]['bodyq_erd_pre'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

#%%
print("Post-Operative")

print("GERD")
t_stat, p = ttest_ind(post_food_data.loc[high_carb_post]['gerd_postsurg'], post_food_data.loc[~high_carb_post]['gerd_postsurg'])
print("High Carbs (Mean) = {}".format(post_food_data.loc[high_carb_post]['gerd_postsurg'].mean()))
print("Low Carbs (Mean) = {}".format( post_food_data.loc[~high_carb_post]['gerd_postsurg'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERS")
t_stat, p = ttest_ind(post_food_data.loc[high_carb_post]['bodyq_ers_post'], post_food_data.loc[~high_carb_post]['bodyq_ers_post'])
print("High Carbs (Mean) = {}".format(post_food_data.loc[high_carb_post]['bodyq_ers_post'].mean()))
print("Low Carbs (Mean) = {}".format( post_food_data.loc[~high_carb_post]['bodyq_ers_post'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))


print("BODYQ ERB")
t_stat, p = ttest_ind(post_food_data.loc[high_carb_post]['bodyq_erb_post'], post_food_data.loc[~high_carb_post]['bodyq_erb_post'])
print("High Carbs (Mean) = {}".format(post_food_data.loc[high_carb_post]['bodyq_erb_post'].mean()))
print("Low Carbs (Mean) = {}".format( post_food_data.loc[~high_carb_post]['bodyq_erb_post'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))

print("BODYQ ERD")
t_stat, p = ttest_ind(post_food_data.loc[high_carb_post]['bodyq_erd_post'], post_food_data.loc[~high_carb_post]['bodyq_erd_post'])
print("High Carbs (Mean) = {}".format(post_food_data.loc[high_carb_post]['bodyq_erd_post'].mean()))
print("Low Carbs (Mean) = {}".format( post_food_data.loc[~high_carb_post]['bodyq_erd_post'].mean()))
print("T Statistic : {}, p-value : {}".format(t_stat, p))