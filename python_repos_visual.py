import requests
import plotly.express as px
import pandas as pd

# Construct API URL using f-strings for readability
url = f"https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"

# Make the API request and handle potential errors
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for error codes
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    # Add appropriate handling for the error, e.g., exit the script or log the error
    # return or exit(1)

# Process response directly as JSON
data = response.json()

# Extract repository information using list comprehensions
repo_links = [
    f"<a href='{repo['html_url']}' target='_blank'>{repo['name']}</a>"
    for repo in data["items"]
]
stars = [repo["stargazers_count"] for repo in data["items"]]
forks = [repo["forks_count"] for repo in data["items"]]  # New: Extract forks count

# Create a DataFrame from the lists
df = pd.DataFrame({"Repository": repo_links, "Stars": stars, "Forks": forks})

# Create the scatter plot with enhanced interactivity and styling
fig = px.scatter(
    df,
    x="Stars",
    y="Forks",
    title="GitHub Python Projects: Stars vs Forks",
    template="plotly_dark",  # Apply a dark theme for a modern look
    labels={"Stars": "Number of Stars", "Forks": "Number of Forks"},
    size="Stars",  # Size of markers represents the number of stars
    color="Forks",  # Color of markers represents the number of forks
    hover_name="Repository",  # Display repository names on hover
)
fig.update_layout(
    title_font_size=32,  # Increased title font size for better readability
    title_x=0.8,         # Centered the title
    xaxis_title_font_size=20,
    yaxis_title_font_size=20,
    grid=dict(rows=1, columns=1),
    hovermode="closest",
    dragmode="zoom",
    selectdirection="h",
    autosize=True,
    margin=dict(autoexpand=True, l=40, r=40, t=50, b=30),  # Increased top margin
    height=600,
    width=1100,
)

fig.show()


