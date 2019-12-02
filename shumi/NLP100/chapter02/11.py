with open('hightemp.txt') as f:
    full_text = f.readlines()
full_text =  [text.replace('\t', ' ') for text in full_text]
for text in full_text:
    print(text, end='')