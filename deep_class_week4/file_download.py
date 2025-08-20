import requests

url = 'myurl'
response = requests.get(url)
with open('image.jpg', 'wb') as f:
  f.write(response.content)

# 스트리밍 

stream_url = 'my_stream_url'
response = requests.get(stream_url, stream=True)

with open('bigfile.zip', 'wb') as f:
  for chunk in response.iter_content(chunk_size=8192):
    f.write(chunk)


def get_weather(city):
  api_key = ""
  # base_api = 