import requests
import json

response = requests.get('https://www.google.com')

print(f"status code : {response.status_code}")
print(f"encoding : {response.encoding}")

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

if response.status_code == 200:
  posts = response.json()

  first_post = posts[0]

  print(f"title : {first_post['title']}")
  print(f"body : {first_post['body']}")
else:
  print(f"error")