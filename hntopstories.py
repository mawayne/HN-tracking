import requests
import json

source_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
source_response = requests.get(source_url)
source_content = source_response.content
source_content_list = json.loads(source_content)

#print source_content_list
#print(type(source_content_list))
#print source_content_list[0]
#print(type(source_content_list[0]))

hnapi_baseurl = 'https://hacker-news.firebaseio.com/v0/item/'
hnapi_suffix = '.json'

full_url_list = []

for id in source_content_list:
    full_url = hnapi_baseurl + str(id) + hnapi_suffix
    full_url_list.append(full_url)

for url in full_url_list:
    fullurl_response = requests.get(url)
    fullurl_response_content = fullurl_response.content
    print fullurl_response_content