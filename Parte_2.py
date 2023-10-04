import pandas as pd

df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
df_1 = pd.DataFrame(df)
print(df_1)

muertos = df_1['DEATH_EVENT'] == 1 
df_muertos = df_1[muertos]
promedio = df_muertos['age'].mean()
print(promedio)

no_muertos = df_1['DEATH_EVENT'] == 0 
df_no_muertos = df_1[no_muertos]
promedio_1 = df_no_muertos['age'].mean()
print(promedio_1)
