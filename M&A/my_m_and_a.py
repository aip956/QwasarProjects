import pandas as pd
import io
from datetime import datetime

def clean_table_1(csv_str):
    #Read CSV
    df = pd.read_csv(io.StringIO(csv_str))

    #Rename columns for consistency
    df = df.rename(columns={
        'Gender': 'gender',
        'FirstName': 'firstname',
        'LastName': 'lastname',
        'Email': 'email',
        'Age': 'age',
        'City': 'city',
        'Country': 'country',
    })

    #Drop username if present
    if 'UserName' in df.columns:
        df = df.drop(columns=['UserName'])

    #Normalize values
    df['gender'] = df['gender'].map({
        'Male': 'Male', 'Female': 'Female',
        '0': 'Male', '1':'Female'
    }).fillna('Unknown')

    df['firstname'] = df['firstname'].str.strip().str.title()
    df['lastname'] = df['lastname'].str.strip().str.replace('"', '').str.title()
    df['city'] = df['city'].str.strip().str.title()
    df['country'] = df['country'].replace({
        'UNITED STATES': 'USA',
        'UNITED STATES OF AMERICA': 'USA',
        'United State Of America': 'USA',
        'U.S.A': 'USA',
        'U.S.A': 'USA',
        'US': 'USA',
        'U.S.': 'USA',
        'USA': 'USA',
        '12': None,
        'NULL': None,
        'null': None,
        'NAN': None,
        'NaN': None
    })
    allowed_countries = ['USA']
    df['country'] = df['country'].where(df['country'].isin(allowed_countries), None)
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    return df


if __name__ == "__main__":
    import os
    with open("only_wood_customer_us_1.csv", "r", encoding="utf-8") as f:
        csv_content = f.read()

    cleaned_df = clean_table_1(csv_content)
    print("\nCleaned data:")
    print(cleaned_df)