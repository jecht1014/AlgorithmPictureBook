import math
# 10
with open('hightemp.txt') as f:
    full_text = f.readlines()
print(len(full_text))

# 12
with open('hightemp.txt') as f:
    full_text = f.readlines()
col1 =  [text.split('\t')[0] for text in full_text]
col2 =  [text.split('\t')[1] for text in full_text]

with open('col1.txt', mode='w') as f:
    f.write('\n'.join(col1)+'\n')

with open('col2.txt', mode='w') as f:
    f.write('\n'.join(col2)+'\n')

# 13
with open('col1.txt') as f:
    col1 = f.readlines()
with open('col2.txt') as f:
    col2 = f.readlines()
merge_text = []
for i in range(len(col1)):
    merge_text.append(col1[i][:-1]+'\t'+col2[i])

with open('merge_col.txt', mode='w') as f:
    f.write(''.join(merge_text))

# 16
N = 5
split_name = 'split_hightemp'
with open('hightemp.txt') as f:
    full_text = f.readlines()
split_num = math.ceil(len(full_text) / N)
for i in range(N):
    if (i != N-1):
        with open(split_name+str(i)+'.txt', mode='w') as f:
            f.write(''.join(full_text[i*split_num:(i+1)*split_num]))
    else:
        with open(split_name+'{0:02}.txt'.format(i), mode='w') as f:
            f.write(''.join(full_text[i*split_num:]))