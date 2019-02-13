#!/usr/bin/python3
# from: https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
# reading JSON data from a file is just as easy as writing it to a file.
# Using the same json package again, we can extract and parse the JSON string # directly from a file object
import json

with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
