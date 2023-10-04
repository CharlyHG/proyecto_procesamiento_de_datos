import pandas as pd

df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
df_1 = pd.DataFrame(df)
print(df_1)