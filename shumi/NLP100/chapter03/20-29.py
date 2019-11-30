import json
import gzip
import re

# 20
filename = 'jawiki-country.json.gz'
country_data = {}
with gzip.open(filename, 'rt', encoding='utf-8') as f:
    for line in f:
        json_data = json.loads(line)
        country_data[json_data['title']] = json_data
#print(country_data['イギリス']['text'])

# 21
pattern = '\[\[Category:[^\n]+?\]\]'
for s in re.findall(pattern, country_data['イギリス']['text']):
    print(s)

# 22
pattern = '\[\[Category:([^\n]+?)\]\]'
for s in re.findall(pattern, country_data['イギリス']['text']):
    print(s)

# 23
pattern = '(={2,}?)([^={2,}]+)={2,}'
for s in re.findall(pattern, country_data['イギリス']['text']):
    print(len(s[0])-1,':', s[1])

# 24
pattern = '\[\[File:(.+?)\|thumb'
for s in re.findall(pattern, country_data['イギリス']['text']):
    print(s)