# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:49:43 2023

@author: marora42
"""

import xgboost as xgb
import shap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



# Split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.1, 
                                                    random_state=12)

# Train an XGBoost model
model = xgb.XGBRegressor()
model.fit(X_train, y_train)

#%%
# Plot feature importances
xgb.plot_importance(model, importance_type='weight', max_num_features=10)
plt.show()

#%%
# Calculate SHAP values
explainer = shap.Explainer(model)
shap_values = explainer(X_test)

# Plot SHAP summary plot
shap.summary_plot(shap_values, X_test, plot_type="bar")
plt.show()

# Individual SHAP value plots (e.g., for a single data point)
# Replace the index with the desired data point
#shap.initjs()
#shap.force_plot(explainer.expected_value, shap_values[0], X_test.iloc[0, :])

#%%
shap.plots.beeswarm(shap_values)
plt.show()




