import requests
from send_email import send_email

topic = "tesla"
api_key = "de0dfb2627464607a5b965fdb2bceded"
url = ('https://newsapi.org/v2/everything?'
       f'q={topic}&sortBy=publishedAt'
       '&apiKey=de0dfb2627464607a5b965fdb2bceded&'
       'language=en')

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today`s news" + "\n"
for article in content['articles'][0:20]:
    if article['title'] is not None:
        body = body + article['title'] + "\n" + str(article['description']) + "\n" \
               + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

