#!/usr/bin/python3
# from: https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
# The built-in json package has the magic code that transforms your Python
#  dict object in to the serialized JSON string.
import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})



with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
