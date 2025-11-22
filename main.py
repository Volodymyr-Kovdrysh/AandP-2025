import requests
from libs import send_email


text='Київ'

url = ("https://newsapi.org/v2/everything?"
       f"q={text}"
       "&apiKey=4af3611d0f074756b6d60e0b8eb6608c")

request = requests.get(url)

content = request.json()

body = "Subject: From newsAPI\n"
for article in content["articles"]:
    if text in article["title"]:
        body += article["title"] + '\n'+ article["description"]+ '\n'+ article['url'] + 2*'\n'


send_email(message=body.encode('utf-8'))
