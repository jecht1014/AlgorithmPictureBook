N = 10
with open('hightemp.txt') as f:
    full_text = f.readlines()

for i in range(N):
    print(full_text[i], end='')