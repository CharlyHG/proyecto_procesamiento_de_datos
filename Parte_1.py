"""from datasets import load_dataset

dataset = load_dataset("heart_failure_clinical_records_dataset.csv")

data = dataset["train"]

dataset({
    features: [
        'age',
        'has_anaemia',
        'creatinine_phosphokinase_concentration_in_blood',
        'has_diabetes',
        'heart_ejection_fraction',
        'has_high_blood_pressure',
        'platelets_concentration_in_blood',
        'serum_creatinine_concentration_in_blood', 
        'serum_sodium_concentration_in_blood',
        'is_male', 'is_smoker',
        'days_in_study',
        'is_dead'
    ],
    num_rows: 299
})
print(data)"""