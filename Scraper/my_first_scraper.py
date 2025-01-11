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

if __name__ == "__main__":
    url = "https://github.com/trending"
    try:
        page_content = request_github_trending(url)
        print("Request success")
        print(page_content)
    except Exception as e:
        print(f"Error: {e}")

        