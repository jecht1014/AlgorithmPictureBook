import collections

with open('hightemp.txt') as f:
    full_text = f.readlines()
full_text = [text.split('\t')[0] for text in full_text]
text1c = collections.Counter(full_text)

for text in text1c.most_common():
    print(text[0])