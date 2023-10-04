import pandas as pd

df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
df_1 = pd.DataFrame(df)

print(df_1.dtypes)

fumadores_hombres = df_1[(df_1['smoking'] == 1) & (df_1['sex'] == 1)]
Total_hombres_fumadores = fumadores_hombres['smoking'].count()
print(Total_hombres_fumadores)

fumadoras_mujeres = df_1[(df_1['smoking'] == 1) & (df_1['sex'] == 0)]
Total_mujeres_fumadoras = fumadoras_mujeres['smoking'].count()
print(Total_mujeres_fumadoras)