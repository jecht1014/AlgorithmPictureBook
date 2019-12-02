with open('col1.txt') as f:
    full_text = f.readlines()
full_text = set(full_text)
full_text = list(full_text)
full_text.sort()

for text in full_text:
    print(text, end='')