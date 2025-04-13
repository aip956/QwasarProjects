

# Welcome to My M&A
This is a data cleaning and transformation project.

## Task
The goal is to implement a function that receives 3 raw CSV strings
and produces a clean, merged DataFrame with the following schema:
| Column       | Type   |
|--------------|--------|
| gender       | string |
| firstname    | string |
| lastname     | string |
| email        | string |
| age          | string |
| city         | string |
| country      | string |
| created_at   | string |
| referral     | string |

The task is to create a function that will:
- Standardize inconsistent formats
- Extract missing values (e.g. names)
- Normalize and clean corrupted entries
- Add missing fields ('created_at', 'referral')
- Return a clean merge DataFram




## Description
Table-by-Table Cleaning Strategy
Table 1
- Already has:
  - Gender, FirstName, LastName, Email, Age, City, Country
- Need to:
  - Normalize capitalization (e.g. JOHNSON -> Johnson)
  - Fix "gender" values: convert 0, 1 to "Male"/"Female" or drop if unclear
  - Standardize "country" (e.g. U.S.A., 12, null -> "USA" or None)
  - Add "created_at" and "referral"
  - Drop unnecessary column 'username'
  
Table 2
- Columns are unnamed and loosely ordered
  - Age, City, Gender, Name, Email
- Need to:
  - Assign column names manually
  - Extract firstname and lastname from Name (careful with quoted names)
  - Clean age (e.g. "51years" -> 51)
  - Standardize gender (e.g. "0" -> unknown or "Male")
  - Fix cities and countries (can default to "USA" if country missing)
  - Add "created_at" and "referral"

Table 3
- Fields are prefixed oddly:
  - "string_Male", "integer_87", "string_san francisco"
- Need to:
  - Strip prefixes (string_, integer_, boolean_)
  - Split Name into firstname, lastname
  - Handle missing emails (N/A)
  - Fix inconsistent country values ("1" -> "USA")
  - Add "created_at" and "referral"

## Installation
This project uses Python and pandas:
```bash
pip install pandas
```
Key pandas methods used:
- Reading CSVs: pd.read_csv
- Cleaning values: .str.lower(), .str.strip(), .replace()
- Splitting names: .str.split(" ", 1)
- Removing prefixes: .str.replace('string_', '')
- Fixing tyes: pd.to_numeric(..., errors='coerce')
- Filling columns: df['created_at'] = pd.Timestamp.today()
- Merging: pd.concat([df1, df2, df3], ignore_index=True)

## Usage
Final Function
- Take in 3 CSV string inputs
- Clean each as described
- Combine into one DataFrame
- Return the cleaned DataFrame
- Then use:
  - from my_ds_babel import csv_to_sql
  - csv_to_sql(merged_df, 'plastic_free_boutique.sql', 'customers')

## Do Not Commit CSVs
.csv files are not to be git committed, as they may contain sensitive customer data.
Add to .gitignore:
- *.csv
Remove any committed csvs:
- git rm --cached *.csv
- git commit -m "Removed CSVs"


### The Core Team
Anthea Ip