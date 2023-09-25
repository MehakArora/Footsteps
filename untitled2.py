# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:33:01 2023

@author: marora42
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('BariPROMs_MasterData_FebToSep2023_v2.xlsx')
df = pd.read_csv('extracted_variables.csv')
pat_info = pd.read_csv('pat_info_new.csv')

#%%

pat_info = pd.DataFrame(columns = ['mrn'], data = data['mrn'].unique())
data_medical_baseline = data.loc[data['interview'] == 'Medical_Baseline']
data_surgical_baseline = data.loc[data['interview'] == 'Surgical_Baseline']
data_PreSurg = data.loc[data['interview'].isin(['PreSurgPaperFormFUP', 'PresurgPaperFormFUP'])]
data_PostSurg =  data.loc[data['interview'].isin(['PostSurgPaperFormFUP', 'PostsurgPaperFormFUP'])]
data_followup = data.loc[data['interview'] == 'FollowUp']


#%%

gerd_med_baseline = []
for mrn in pat_info.mrn:
    select = data_medical_baseline.loc[data_medical_baseline.mrn == mrn]
    if len(select) > 0:
        gerd_med_baseline.append(select['gerdhrql_score'].values[0])
    else:
        gerd_med_baseline.append(float("nan"))

pat_info['gerd_med_baseline'] = gerd_med_baseline

gerd_presurg = []
for mrn in pat_info.mrn:
    select = data_PreSurg.loc[data_PreSurg.mrn == mrn]
    if len(select) > 0:
        gerd_presurg.append(select['gerdhrql_score'].values[0])
    else:
        gerd_presurg.append(float("nan"))

pat_info['gerd_presurg'] = gerd_presurg

gerd_postsurg = []
for mrn in pat_info.mrn:
    select = data_PostSurg.loc[data_PostSurg.mrn == mrn]
    if len(select) > 0:
        gerd_postsurg.append(select['gerdhrql_score'].values[0])
    else:
        gerd_postsurg.append(float("nan"))

pat_info['gerd_postsurg'] = gerd_postsurg

#%%

bmi_med_baseline = []
for mrn in pat_info.mrn:
    select = data_medical_baseline.loc[data_medical_baseline.mrn == mrn]
    if len(select) > 0:
        bmi_med_baseline.append(select['bmi'].values[0])
    else:
        bmi_med_baseline.append(float("nan"))

pat_info['bmi_med_baseline'] = bmi_med_baseline

bmi_presurg = []
for mrn in pat_info.mrn:
    select = data_surgical_baseline.loc[data_surgical_baseline.mrn == mrn]
    if len(select) > 0:
        bmi_presurg.append(select['bmi'].values[0])
    else:
        bmi_presurg.append(float("nan"))

pat_info['bmi_presurg'] = bmi_presurg

bmi_postsurg = []
for mrn in pat_info.mrn:
    select = data_PostSurg.loc[data_PostSurg.mrn == mrn]
    if len(select) > 0:
        bmi_postsurg.append(select['Postop BMI'].values[0])
    else:
        bmi_postsurg.append(float("nan"))

pat_info['bmi_postsurg'] = bmi_postsurg

#%%
def convert_to_numerical_yes_no_nan(x):
    if x == 'yes':
        return 1
    elif x == 'no':
        return 0
    else:
        return -1 
    
def convert_to_numerical_degree(x):
    if x == 'never or rarely':
        return 0
    elif x == 'sometimes':
        return 1 
    elif x == 'often':
        return 2
    elif x == 'always':
        return 3
    else:
        return -1 
    
bed7_1 = []
bed7_2 = []
bed7_3 = []
bed7_4 = []
bed7_5 = []
bed7_6 = []
bed7_7 = []


for mrn in pat_info.mrn:
    select = data_medical_baseline.loc[data_medical_baseline.mrn == mrn]
    if len(select) > 0:
        bed7_1.append(convert_to_numerical_yes_no_nan(select['beds7_01_episodes'].values[0]))
        bed7_2.append(convert_to_numerical_yes_no_nan(select['beds7_02_distress'].values[0]))
        bed7_3.append(convert_to_numerical_degree(select['beds7_03_no_control'].values[0]))
        bed7_4.append(convert_to_numerical_degree(select['beds7_04_eat_after_full'].values[0]))
        bed7_5.append(convert_to_numerical_degree(select['beds7_05_embarrassed'].values[0]))
        bed7_6.append(convert_to_numerical_degree(select['beds7_06_guilt'].values[0]))
        bed7_7.append(convert_to_numerical_degree(select['beds7_07_vomit'].values[0]))
    else:
        bed7_1.append(-1)
        bed7_2.append(-1)
        bed7_3.append(-1)
        bed7_4.append(-1)
        bed7_5.append(-1)
        bed7_6.append(-1)
        bed7_7.append(-1)

pat_info['bed7_1'] = bed7_1
pat_info['bed7_2'] = bed7_2
pat_info['bed7_3'] = bed7_3
pat_info['bed7_4'] = bed7_4
pat_info['bed7_5'] = bed7_5
pat_info['bed7_6'] = bed7_6
pat_info['bed7_7'] = bed7_7

#%%

bodyq_ers = []
bodyq_erb = []
bodyq_erd = []

for mrn in pat_info.mrn:
    select = data_PreSurg.loc[data_PreSurg.mrn == mrn]
    if len(select) > 0:
        bodyq_ers.append(select['bodyq_ers_rasch'].values[0])
        bodyq_erb.append(select['bodyq_erb_rasch'].values[0])
        bodyq_erd.append(select['bodyq_erd_rasch'].values[0])
    else:
        bodyq_ers.append(-1)
        bodyq_erb.append(-1)
        bodyq_erd.append(-1)


pat_info['bodyq_erd_pre'] = bodyq_erd
pat_info['bodyq_erb_pre'] = bodyq_erb
pat_info['bodyq_ers_pre'] = bodyq_ers

#%%

bodyq_ers = []
bodyq_erb = []
bodyq_erd = []

for mrn in pat_info.mrn:
    select = data_PostSurg.loc[data_PostSurg.mrn == mrn]
    if len(select) > 0:
        bodyq_ers.append(select['bodyq_ers_rasch'].values[0])
        bodyq_erb.append(select['bodyq_erb_rasch'].values[0])
        bodyq_erd.append(select['bodyq_erd_rasch'].values[0])
    else:
        bodyq_ers.append(-1)
        bodyq_erb.append(-1)
        bodyq_erd.append(-1)


pat_info['bodyq_erd_post'] = bodyq_erd
pat_info['bodyq_erb_post'] = bodyq_erb
pat_info['bodyq_ers_post'] = bodyq_ers

#%%


    
data_alc = pd.get_dummies(data['alcohol_consumption'])
alc_less_than1 = []
alc_12 = []
alc_34 = []
alc_more_5 = []

for mrn in pat_info.mrn:
    select = data_alc.loc[data.mrn == mrn]
    if len(select) > 0:
        alc_12.append(int(select['1-2 drinks/day'].any()))
        alc_34.append(int(select['3-4 drinks/day'].any()))
        alc_more_5.append(int(select[['5-6 drinks/day', '> 7 drinks/day']].any().any()))
        alc_less_than1.append(int(select[['none', '< 1 drink/day']].any().any()))
    else:
        alc_less_than1.append(-1)
        alc_12.append(-1)
        alc_34.append(-1)
        alc_more_5.append(-1)
        
pat_info['alc_less_than1'] = alc_less_than1
pat_info['alc_12'] = alc_12
pat_info['alc_34'] = alc_34
pat_info['alc_more_5'] = alc_more_5

#%%

data_tobacco_use = pd.get_dummies(data['tobacco_use'])

never_smoked = []
used_to_smoke = []


for mrn in pat_info.mrn:
    select = data_tobacco_use.loc[data.mrn == mrn]
    if len(select) > 0:
        never_smoked.append(int(select['never smoked'].any()))
        used_to_smoke.append(int(select[ 'used to smoke, but quit'].any()))
    else:
        never_smoked.append(-1)
        used_to_smoke.append(-1)
        
pat_info['never_smoked'] = never_smoked
pat_info['used_to_smoke'] = used_to_smoke

#%%


illicit_drugs = []
rec_drugs = []


for mrn in pat_info.mrn:
    select = data.loc[data.mrn == mrn]
    if len(select) > 0:
        illicit_drugs.append(int((select['illicit_drugs'] == 'yes').any()))
        rec_drugs.append(int((select['recreational_drugs'] == 'yes').any()))
    else:
        illicit_drugs.append(-1)
        rec_drugs.append(-1)
        
pat_info['illicit_drugs'] = illicit_drugs
pat_info['rec_drugs'] = rec_drugs

#%%


list1 = []

def rate_income(x):
    if x == 'Less than $10,000':
        return 1 
    elif x == '$10,000 to $24,999':
        return 2 
    elif x == '$25,000 to $44,999':
        return 3 
    elif x == '$45,000 to $75,000':
        return 4 
    elif x == 'Over $75,000':
        return 5 
    else:
        return -1

for mrn in pat_info.mrn:
    select = data.loc[data.mrn == mrn]
    selected = select.loc[select['family_income'].isin(['$10,000 to $24,999', '$25,000 to $44,999', '$45,000 to $75,000',
            'Less than $10,000', 'Over $75,000',
           'declined', 'none'])]
    if len(selected) > 0:
        
        list1.append(rate_income(selected['family_income'].values[0]))
    else:
        list1.append(-1)
        

pat_info['income'] = list1 

#%%

list1 = []


for mrn in pat_info.mrn:
    select = df.loc[(data.mrn == mrn) & (data.interview.isin(['PostSurgPaperFormFUP', 'PostsurgPaperFormFUP']))]
    selected = select['exercise_frequency'].values
    selected_ = selected[selected != -1]
    if len(selected_) > 0:
        list1.append(selected_[0])
    elif len(selected) > 1:
        list1.append(selected[0])
    else:
        list1.append(-2)
    
    

pat_info['exercise_frequency_post'] = list1 

#%%

list1 = []


for mrn in pat_info.mrn:
    select = df.loc[(data.mrn == mrn) & (data.interview.isin(['Medical_Baseline', 'PreSurgPaperFormFUP', 'PresurgPaperFormFUP']))]
    selected = select['exercise_frequency'].values
    selected_ = selected[selected != -1]
    if len(selected_) > 0:
        list1.append(selected_[0])
    elif len(selected) > 1:
        list1.append(selected[0])
    else:
        list1.append(-2)
    
    

pat_info['exercise_frequency_pre'] = list1 

#%%

list1 = []


for mrn in pat_info.mrn:
    select = df.loc[data.mrn == mrn]
    selected = select['soda_intake'].values
    selected_ = selected[selected != -1]
    if len(selected_) > 0:
        list1.append(selected_[0])
    else:
        list1.append(selected[0])
    

pat_info['soda_intake'] = list1 

#%%

list1 = []


for mrn in pat_info.mrn:
    select = df.loc[data.mrn == mrn]
    selected = select['water_intake'].values
    selected_ = selected[selected != -1]
    if len(selected_) > 0:
        list1.append(selected_[0])
    else:
        list1.append(selected[0])
    

pat_info['water_intake'] = list1 


#%%

list1 = []


for mrn in pat_info.mrn:
    select = df.loc[data.mrn == mrn]
    selected = select['sugary_beverages_intake'].values
    selected_ = selected[selected != -1]
    if len(selected_) > 0:
        list1.append(selected_[0])
    else:
        list1.append(selected[0])
    

pat_info['sugary_beverages_intake'] = list1 

#%%

list1 = []

for mrn in pat_info.mrn:
    select = data.loc[data.mrn == mrn & (data.interview.isin(['Medical_Baseline', 'PreSurgPaperFormFUP', 'PresurgPaperFormFUP']))]
    selected = select.loc[select['exercise_limitations_yn'].isin(['yes', 'no'])]
    if len(selected) > 0:
        list1.append(int(selected['exercise_limitations_yn'].values == 'yes'))
    else:
        list1.append(-1)
    

pat_info['exercise_limitations_pre'] = list1 

#%%

list1 = []

for mrn in pat_info.mrn:
    select = data.loc[data.mrn == mrn]
    selected = select.loc[select['after_dinner_snacking'].isin(['yes', 'no'])]
    if len(selected) > 0:
        list1.append(int(selected['after_dinner_snacking'].values[0] == 'yes'))
    else:
        list1.append(-1)
    

pat_info['after_dinner_snacking'] = list1 

#%%

list1 = []
list2 = []
list3 = []
list4 = []


for mrn in pat_info.mrn:
    select = df.loc[(data.mrn == mrn) & (data.interview == 'Medical_Baseline')]
    selected = select.loc[~select['food_log_protein'].isna()]
    if len(selected) > 0:
        list1.append(selected['food_log_protein'].values[0])
        list2.append(selected['food_log_carb'].values[0])
        list3.append(selected['food_log_fat'].values[0])
        list4.append(selected['food_log_fiber'].values[0])
    else:
        list1.append(-1)
        list2.append(-1)
        list3.append(-1)
        list4.append(-1)
    

pat_info['protein_baseline'] = list1 
pat_info['carbs_baseline'] = list2 
pat_info['fats_baseline'] = list3
pat_info['fiber_baseline'] = list4 

#%%

list1 = []
list2 = []
list3 = []
list4 = []


for mrn in pat_info.mrn:
    select = df.loc[(data.mrn == mrn) & (data['interview'].isin(['PreSurgPaperFormFUP', 'PresurgPaperFormFUP']))]
    selected = select.loc[~select['food_log_protein'].isna()]
    if len(selected) > 0:
        list1.append(selected['food_log_protein'].values[0])
        list2.append(selected['food_log_carb'].values[0])
        list3.append(selected['food_log_fat'].values[0])
        list4.append(selected['food_log_fiber'].values[0])
    else:
        list1.append(-1)
        list2.append(-1)
        list3.append(-1)
        list4.append(-1)
    

pat_info['protein_pre_'] = list1 
pat_info['carbs_pre_'] = list2 
pat_info['fats_pre_'] = list3
pat_info['fiber_pre_'] = list4 

#%%

list1 = []
list2 = []
list3 = []
list4 = []


for mrn in pat_info.mrn:
    select = df.loc[(data.mrn == mrn) & (data['interview'].isin(['PostSurgPaperFormFUP', 'PostsurgPaperFormFUP']))]
    selected = select.loc[~select['food_log_protein'].isna()]
    if len(selected) > 0:
        list1.append(selected['food_log_protein'].values[0])
        list2.append(selected['food_log_carb'].values[0])
        list3.append(selected['food_log_fat'].values[0])
        list4.append(selected['food_log_fiber'].values[0])
    else:
        list1.append(-1)
        list2.append(-1)
        list3.append(-1)
        list4.append(-1)
    

pat_info['protein_post_'] = list1 
pat_info['carbs_post_'] = list2 
pat_info['fats_post_'] = list3
pat_info['fiber_post_'] = list4 

#%%

pat_info.to_csv('pat_info_new.csv')