N = 10
with open('hightemp.txt') as f:
    full_text = f.readlines()

for i in range(len(full_text)-N, len(full_text)):
    print(full_text[i], end='')