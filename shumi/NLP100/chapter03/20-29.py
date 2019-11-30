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

# 25
pattern = '\{\{基礎情報 国\n([\s\S]+?)}}\n'
basic_data = re.findall(pattern, country_data['イギリス']['text'])
basic_data_dict = {}
for s in basic_data[0][1:].split('\n|'):
    a = s.split(' = ')
    if a[1][-1] == '\n':
        a[1] = a[1][:-1]
    basic_data_dict[a[0]] = a[1]
    print('({0}, {1})'.format(a[0], a[1]))