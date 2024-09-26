import requests

api_key = "de0dfb2627464607a5b965fdb2bceded"
url = 'https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=de0dfb2627464607a5b965fdb2bceded'

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])