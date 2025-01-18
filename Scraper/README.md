# Welcome to My First Scraper Ds
***

## Task
The task is to create a web scraper that fetches and extracts trending GitHub 
repos from the GitHub trending page. The challenge lies in correctly parsing 
the HTML structure and ensuring that the scraper can handle potential errors 
(e.g. missing data, incorrect elements, or changes to the webpage structure).

## Description
This project is a Python=based scarper that extracts information about trending 
repositories from GitHub. It fetches the HTML content of the GitHub trending
age, parses the relevant details about repos ( e.g. developer name, number of 
stars, formats the data.)

## Steps followed
1. Request: Fetches the HTML content from GitHub's trending page using the 'requests' library
2. Extract: Parses the HTML content to find repo rows using BeautifulSoup.
3. Transform: Extracts the repo data (dev name, repo name, number of stars) and stores in a structured format.
4. Format: Converts the extracted data into a CSV frmat and saves it into a file.

## Installation
1. Clone the repo or download the project files
2. Install necessary dependencies
``` 
    bash
    pip install reqeusts beautifulsoup4
    ```
3. Ensure that Python 3.x is installed




## Usage
Run the Python script to fetch trending repos:
```
python3 my_first_scraper.py 
```

### The Core Team
Anthea Ip

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
