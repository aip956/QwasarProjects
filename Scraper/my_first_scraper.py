import requests
from bs4 import BeautifulSoup
import csv

# Part 0: Request
def request_github_trending(url):
    """Fetch the HTML content from GitHub trending page."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch URL: {url}, Status code: {response.status_code}")
    return response.text

# Part 1: Extract
def extract (page):
    """Extracts the repo rows from the HTML content."""
    soup = BeautifulSoup(page, "html.parser")
    repo_rows = soup.find_all('article', class_='Box-row') #GitHub trending repositories are in 'article' tags with 'Box-row' class
    return repo_rows



if __name__ == "__main__":
    url = "https://github.com/trending"
    try:
        # Part 0, Fetch page content
        page_content = request_github_trending(url)
        print("Request success")
        # print(page_content[:1000])

        # Part 1, Extract
        repo_rows = extract(page_content)
        print(f"Number of repos extracted: {len(repo_rows)}")
        # Print 1st repo's HTML to validate
        if repo_rows:
            print("First repo HTML:")
            print(repo_rows[0].prettify()) # Prettifies HTML for easier reading

    except Exception as e:
        print(f"Error: {e}")

