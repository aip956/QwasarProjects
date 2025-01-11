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

# Part 2: Transform
def transform(html_repos):
    """ Transforms the HTML repo rows into structured data."""
    repositories = []
    for i, repo in enumerate(html_repos):
        try:
            # Selector for developer and repo name
            dev_repo = repo.find('h2', class_='h3 lh-condensed').find('a')
            if not dev_repo:
                print(f"Repo {i} missing dev/repo link.")
                continue
            # Extract developer and repo name
            repo_link = dev_repo['href']
            developer = repo_link.split('/')[1]
            repo_name = repo_link.split('/')[2]

            # Find number of stars
            stars = repo.find('a', class_='Link Link--muted d-inline-block mr-3')
            if not stars:
                print(f"Repo {i} missing stars.")
                continue
            nbr_stars = stars.text.strip().replace(',', '')

            # Append the parsed data
            repositories.append({
                'developer': developer,
                'repository_name': repo_name,
                'nbr_stars': nbr_stars
            })
        except AttributeError as e:
            print(f"Error processing repo {i}: {e}")
    return repositories

   



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
            # print(repo_rows[0].prettify()[:500]) # Prettifies HTML for easier reading

        # Part 2, Transform
        repositories_data = transform(repo_rows)
        print(f"Number of repos transformed: {len(repositories_data)}")
        print(repositories_data[0])

    except Exception as e:
        print(f"Error: {e}")

