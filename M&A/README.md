

# Welcome to My M&A
This is a data cleaning and transformation project.

## Task
The final merged DataFram must have the following schema:
"gender" - 'string'
"firstname" - 'string'
"Lastname" - 'string'
"email" - 'string'
"age" - 'string'
"city" - 'string'
"country" - 'string'
"created_at" - 'string'
"referral" - 'string'

The task is to create a function that will receive 3 CSV files.
- Only table 1 resembles the schema, but needs cleanup.
  - Standardize the field names across all tables
  - Split/clean names if full names are in one column
  - Fix weird formatting or corrupted values (e.g. string_female, 1, etc.)
  - Create missing fields like created_at and referral


## Description
Table-by-Table Cleaning Strategy
Table 1
- Already has:
  - Gender, FirstName, LastName

## Installation
TODO - How to install your project? npm install? make? make re?

## Usage
TODO - How does it work?
```
./my_project argument1 argument2
```

### The Core Team