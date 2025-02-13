import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

def is_valid_url(url):
    """Check if the URL is valid and has a valid scheme."""
    parsed = urlparse(url)
    return parsed.scheme in ('http', 'https')

def get_all_child_urls(parent_url, visited_urls=None):
    if visited_urls is None:
        visited_urls = set()
    
    try:
        response = requests.get(parent_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {parent_url}: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    
    child_urls = []
    # Select the specific part of the HTML
    specific_part = soup.select_one('#reactele > div:nth-of-type(1) > div:nth-of-type(2)')
    if specific_part:
        for link in specific_part.find_all('a', href=True):
            href = urljoin(parent_url, link['href'])
            # Avoid re-visiting the same URLs and filter out invalid URLs
            if href not in visited_urls and is_valid_url(href):
                visited_urls.add(href)
                child_urls.append(href)
                # Recursively find child URLs
                child_urls.extend(get_all_child_urls(href, visited_urls))
                # Add a delay to avoid overwhelming the server
                time.sleep(1)
    
    return child_urls

parent_url = 'https://locations.dunkindonuts.com/en/ar'
all_child_urls = get_all_child_urls(parent_url)

print(len(all_child_urls))
print(all_child_urls)

# import requests
# from bs4 import BeautifulSoup

# def get_child_urls(parent_url):
#     response = requests.get(parent_url)
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     child_urls = []
#     for link in soup.find_all('a', href=True):
#         href = link['href']
#         if href.startswith('/'):
#             href = parent_url + href
#         elif not href.startswith('http'):
#             href = parent_url + '/' + href
#         child_urls.append(href)
    
#     return child_urls

# parent_url = 'https://locations.dunkindonuts.com/en'
# child_urls = get_child_urls(parent_url)

# print(child_urls)