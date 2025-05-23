# -*- coding: utf-8 -*-

import gdown
import joblib
import warnings

from sklearn.preprocessing import LabelEncoder

warnings.filterwarnings("ignore")

!gdown --id '1qbLVeMxGrid4-uiIkwAmq5ll952lg87R'

import pandas as pd
df = pd.read_csv("https://docs.google.com/spreadsheets/d/1DReaD8nQaj7-rNTH5PkgYDl_OdRtaqHqBBII6GDtOgM/export?format=csv")

inference_df = df.sample(n=10, random_state=42)
actual_attrition = inference_df[['EmployeeId', 'Attrition']].copy()
inference_df = inference_df.drop(columns='Attrition')
inference_df

# Identify categorical features - Assuming all object type columns are categorical
categorical_features = inference_df.select_dtypes(include=['object']).columns.tolist()

# Create and fit LabelEncoders for each categorical feature
encoders = {}
for feature in categorical_features:
    encoders[feature] = LabelEncoder()
    # Fit on the original dataframe to include all possible categories
    encoders[feature].fit(df[feature])

for feature in categorical_features:
    inference_df[feature] = encoders[feature].transform(inference_df[feature])

final_inference_df = inference_df

training_columns = loaded_model.feature_names_in_
final_inference_df = final_inference_df[training_columns]

hasil_prediksi = loaded_model.predict(final_inference_df)

final_inference_df['EmployeeId'] = inference_df['EmployeeId']
final_inference_df['Prediksi_Attrition'] = hasil_prediksi

hasil_akhir = final_inference_df.merge(actual_attrition, on='EmployeeId', how='left')

hasil_akhir['Prediksi_Attrition_Label'] = hasil_akhir['Prediksi_Attrition'].apply(lambda x: 'Attrition' if x == 1 else 'No Attrition')
hasil_akhir['Actual_Attrition_Label'] = hasil_akhir['Attrition'].apply(lambda x: 'Attrition' if x == 1 else 'No Attrition')

print(hasil_akhir[['EmployeeId', 'Actual_Attrition_Label', 'Prediksi_Attrition_Label']])
