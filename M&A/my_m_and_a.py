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


def clean_table_2(csv_str):
    df = pd.read_csv(io.StringIO(csv_str), sep=';', header=None)
    df.columns = ['age', 'city', 'gender', 'fullname', 'email']
    df['gender'] = df['gender'].replace({
        '0': 'Male', '1':'Female',
        'M': 'Male', 'F': 'Female' 
    }).str.title().fillna('Unknown')

    name_parts = df['fullname'].str.replace(r'[\\"]', '', regex=True).str.strip().str.split()
    df['firstname'] = name_parts.str[0]
    df['lastname'] = name_parts.str[-1]
    # Normalize case
    df['firstname'] = df['firstname'].str.title()
    df['lastname'] = df['lastname'].str.title()
    
    # Fallback if last name missing:
    missing_last = df['lastname'].isna()
    df.loc[missing_last, 'lastname'] = df.loc[missing_last, 'fullname'].str.split().str[-1]
    df['city'] = df['city'].str.strip().str.title()
    df['country'] = 'USA' #Assume USA
    df['age'] = df['age'].str.extract(r'(\d+)').astype(float)
    df = df.drop(columns=['fullname'])
    return df


def clean_table_3(csv_str):
    df = pd.read_csv(io.StringIO(csv_str))
    df.columns = ['gender', 'name', 'email', 'age', 'city', 'country']

    df['gender'] = df['gender'].str.replace(r'^.*_', '', regex=True).str.title()
    df['age'] = df['age'].str.extract(r'(\d+)').astype(float)
    df['firstname'] = df['name'].str.extract(r'^.*?(\w+)')
    df['lastname'] = df['name'].str.extract(r'\s+([^\s"]+)$')
    




if __name__ == "__main__":
    import os
    # Test CSV 1
    # with open("only_wood_customer_us_1.csv", "r", encoding="utf-8") as f:
    #     csv_content = f.read()
    # Test CSV 2
    with open("only_wood_customer_us_2.csv", "r", encoding="utf-8") as f:
        csv_content = f.read()

    # cleaned_df = clean_table_1(csv_content)
    cleaned_df = clean_table_2(csv_content)
    print("\nCleaned data:")
    print(cleaned_df)