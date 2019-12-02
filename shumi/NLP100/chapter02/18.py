from operator import itemgetter

with open('hightemp.txt') as f:
    full_text = f.readlines()
full_text = [text.split('\t') for text in full_text]
full_text.sort(key=itemgetter(2))
full_text.reverse()

for text in full_text:
    print('\t'.join(text), end='')