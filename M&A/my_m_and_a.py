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

    

