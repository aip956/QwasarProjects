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