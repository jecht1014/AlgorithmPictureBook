import re
with open('neko.txt.mecab') as f:
    lines = f.readlines()

neko_dict = {}
for line in lines:
    line = line[:-1]
    if (line != 'EOS'):
        line = re.split('[\t,]', line)
        neko_dict[(line[0], line[1], line[2], line[3])] = line

print(neko_dict)