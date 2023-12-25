import requests

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}

try:
    # Send HTTP GET request
    r = requests.get(url, headers=headers)
    
    # Check if the request was successful
    r.raise_for_status()

    # Print the status code
    print(f"Status code: {r.status_code}")

    # Convert the response object to a dictionary.
    response_dict = r.json()

    # Process results.
    print(f"Total repositories: {response_dict['total_count']}")
    print(f"Complete results: {not response_dict['incomplete_results']}")

    # Explore information about the repositories.
    repo_dicts = response_dict['items']
    print(f"Repositories returned: {len(repo_dicts)}")

    # Examine the first repository.
    repo_dict = repo_dicts[0]
    print(f"\nKeys: {len(repo_dict)}")
    for key in sorted(repo_dict.keys()):
        print(key)

    # Selected information about the first repository.
    print("\nSelected information about the first repository:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")
