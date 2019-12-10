import re
import collections
import matplotlib.pyplot as plt

# 30
with open('neko.txt.mecab', encoding='utf-8') as f:
    lines = f.readlines()

all_line = []
ichibun = []
for line in lines:
    line = line[:-1]
    if (line != 'EOS'):
        line = re.split('[\t,]', line)
        neko_dict = {'surface': line[0], 'base': line[6], 'pos': line[1], 'pos1': line[2]}
        ichibun.append(neko_dict)
        if (neko_dict['pos1'] == '句点'):
            all_line.append(ichibun)
            ichibun = []
print(len(all_line))
print(all_line[:5])

# 31
surface_verb_set = set()
[surface_verb_set.add(word['surface']) for line in all_line for word in line if word['pos'] == '動詞']
print(len(surface_verb_set))
print(list(surface_verb_set)[:5])

# 32
base_verb_set = set()
[base_verb_set.add(word['base']) for line in all_line for word in line if word['pos'] == '動詞']
print(len(base_verb_set))
print(list(base_verb_set)[:5])

# 33

# 34
noun_of_noun_list = []
for line in all_line:
    count = 0
    noun_of_noun = ''
    for word in line:
        if ((count == 0 or count == 2) and word['pos'] == '名詞'):
            count += 1
            noun_of_noun += word['surface']
            if count == 3:
                count = 0
                noun_of_noun_list.append(noun_of_noun)
                noun_of_noun = ''
        elif (count == 1 and word['pos'] == '助詞' and word['surface'] == 'の'):
            count += 1
            noun_of_noun += word['surface']
        else:
            count = 0
            noun_of_noun = ''
print(len(noun_of_noun_list))
print(noun_of_noun_list[:5])

# 35
noun_series_list = []
for line in all_line:
    noun = ''
    count = 0
    for word in line:
        if (word['pos'] == '名詞'):
            count += 1
            noun += word['surface']
        elif (count >= 2):
            noun_series_list.append(noun)
            noun = ''
            count = 0
        else:
            noun = ''
            count = 0
    if (count >= 2):
        noun_series_list.append(noun)
print(len(noun_series_list))
print(noun_series_list[:5])

# 36
all_word = [word['surface'] for line in all_line for word in line]
word_count = collections.Counter(all_word)
print(word_count.most_common()[:5])

# 37
w = []
c = []
for i in range(10):
    w.append(word_count.most_common()[i][0])
    c.append(word_count.most_common()[i][1])
plt.bar(w, c)
plt.show()
