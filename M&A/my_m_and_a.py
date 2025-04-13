import pandas as pd
import io
import os
# from datetime import datetime
from my_ds_babel import csv_to_sql
from my_ds_babel import sql_to_csv


def clean_table_1(csv_str):
    #Read CSV
    df = pd.read_csv(io.StringIO(csv_str))

    #Manually name columns for consistency
    df.columns = ['gender','firstname','lastname','email','age''city','country']

    #Drop username if present
    if 'UserName' in df.columns:
        df = df.drop(columns=['UserName'])

    #Normalize values
    df['gender'] = normalize_gender(df['gender'])
    full_names = df['firstname'].astype(str).str.strip() + ' ' + df['lastname'].astype(str).str.strip()
    df['firstname'], df['lastname'] = clean_name_column(full_names)
    df['city'] = df['city'].str.strip().str.title()
    df['country'] = normalize_country(df['country'])
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['created_at'] = None
    df['referral'] = None
    return df


def clean_table_2(csv_str):
    df = pd.read_csv(io.StringIO(csv_str), sep=';', header=None)
    df.columns = ['age', 'city', 'gender', 'fullname', 'email']
    #Drop username if present
    if 'UserName' in df.columns:
        df = df.drop(columns=['UserName'])

    df['gender'] = normalize_gender(df['gender'])
    df['firstname'], df['lastname'] = clean_name_column(df['fullname'])
    df = df.drop(columns=['fullname'])
    df['city'] = df['city'].str.strip().str.title()
    df['country'] = 'USA' #Assume USA; no country in CSV
    df['age'] = df['age'].str.extract(r'(\d+)').astype(float)
    df['created_at'] = None
    df['referral'] = None
    return df

def clean_table_3(csv_str):
    df = pd.read_csv(io.StringIO(csv_str), sep='\t', header=None, skiprows=1)
    df.columns = ['gender', 'name', 'email', 'age', 'city', 'country']
    #Drop username if present
    if 'UserName' in df.columns:
        df = df.drop(columns=['UserName'])

    df['gender'] = normalize_gender(df['gender'])
    df['age'] = df['age'].astype(str).str.extract(r'(\d+)').astype(float)
    #Extract names
    df['firstname'], df['lastname'] = clean_name_column(df['name'])
    df['email'] = df['email'].astype(str).str.replace(r'^string_','', regex=True)
    df['city'] = df['city'].astype(str).str.replace(r'^.*_', '', regex=True).str.title()
    df['country'] = normalize_country(df['country'])
    df = df.drop(columns=['name'])
    df['created_at'] = None
    df['referral'] = None
    return df

def normalize_country(country_series):
    return (
        country_series.astype(str)
        .str.replace(r'^.*_', '', regex=True) #Remove string prefix
        .str.upper()
        .str.replace(r'[^\w\s]', '', regex=True) #Remove punctuation
        .replace({
            'UNITED STATES': 'USA',
            'UNITED STATES OF AMERICA': 'USA',
            'UNITED STATE OF AMERICA': 'USA',
            'U.S.A': 'USA',
            'U.S.A': 'USA',
            'US': 'USA',
            'U.S.': 'USA',
            'U S': 'USA',
            'USA': 'USA',
            '12': None,
            'NULL': None,
            'NAN': None,
        })
        .where(lambda s: s.isin(['USA']), None)
    )

def normalize_gender(gender_series):
    return(
        gender_series.astype(str)
        .str.replace(r'^.*_', '', regex=True)
        .str.title()
        .replace({
            '0': 'Male', 
            '1':'Female',
            'M': 'Male', 
            'F': 'Female' 
        })
        .where(lambda s: s.isin(['Male', 'Female']),'Unknown')
    )

def clean_name_column(name_series):
    name_series = name_series.astype(str).str.replace(r'[\\"]', '', regex=True).str.strip()
    name_parts = name_series.str.split()
    # name_parts = name_series.str.extract(r'^(\w+)\s+(\w+)$')
    firstname = name_parts.str[0].str.replace(r'^string_', '', regex=True).str.title()
    lastname = name_parts.str[-1].str.replace(r'^string_', '', regex=True).str.title()
    return firstname, lastname


def my_m_and_a(csv_str_1, csv_str_2, csv_str_3):
    df1 = clean_table_1(csv_content1)
    df1['source'] = 'table_1'
    df2 = clean_table_2(csv_content2)
    df2['source'] = 'table_2'
    df3 = clean_table_3(csv_content3)
    df3['source'] = 'table_3'
    return pd.concat([df1, df2, df3], ignore_index=True)



if __name__ == "__main__":
    # Test CSV 1
    with open("only_wood_customer_us_1.csv", "r", encoding="utf-8") as f:
        csv_content1 = f.read()
    # Test CSV 2
    with open("only_wood_customer_us_2.csv", "r", encoding="utf-8") as f:
        csv_content2 = f.read()
    # Test CSV 3
    with open("only_wood_customer_us_3.csv", "r", encoding="utf-8") as f:
        csv_content3 = f.read()
    
    merged_df = my_m_and_a(csv_content1, csv_content2, csv_content3)
    # print("\nCleaned data:")
    # print(merged_df.head())

    # Convert to CSV format in memory
    csv_buffer = io.StringIO()
    merged_df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    # Save to SQLite db
    csv_to_sql(csv_buffer, "plastic_free_boutique.sql", "customers")

    # Check it worked by converting sql to csv
    csv_output = sql_to_csv("plastic_free_boutique.sql", "customers")
    print("\nSQL to CSV check: ")
    lines = csv_output.splitlines()
    for line in lines[:20000]:
        print(line)
