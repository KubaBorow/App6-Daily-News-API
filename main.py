import requests
from send_email import send_email

api_key = "de0dfb2627464607a5b965fdb2bceded"
url = 'https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=de0dfb2627464607a5b965fdb2bceded'

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content['articles']:
    if article['title'] is not None:
        body = body + article['title'] + "\n" + str(article['description']) + 2* "\n"

body = body.encode("utf-8")
send_email(message=body)

