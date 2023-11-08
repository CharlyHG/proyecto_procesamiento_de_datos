import pandas as pd

df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
df_1 = pd.DataFrame(df)
df_1.isnull().sum()

def categorizar_edades(edad):
    if edad <= 12:
        return 'Niño'
    elif edad <= 19:
        return 'Adolescente'
    elif edad <= 39:
        return 'Jóvenes adulto'
    elif edad <= 59:
        return 'Adulto'
    else:
        return 'Adulto mayor'

df_1['Categoría de Edad'] = df_1['age'].apply(categorizar_edades)
def remove_outliers(df, column_name):
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    return df[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]
df_cleaned = remove_outliers(df, 'creatinine_phosphokinase')
df_cleaned_1 = remove_outliers(df_cleaned, 'platelets')
df_cleaned_2 = remove_outliers(df_cleaned_1, 'serum_creatinine')
df_cleaned_3 = remove_outliers(df_cleaned_2, 'serum_sodium')
df_cleaned_3.to_csv('datos.csv', index=False)

