import re
import random

# 00
s = 'stressed'
print(s[::-1])

# 01
s = 'パラトクカシーー'
print(s[::2])

# 02
s1 = 'パトカー'
s2 = 'タクシー'
s = ''
for i in range(len(s1)):
    s += s1[i]+s2[i]
print(s)

# 03
s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
s_num = [len(i) for i in re.split('[ ,.]+', s[:-1])]
print(s_num)

# 04
l = [1, 5, 6, 7, 8, 9, 15, 16, 19]
s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
split_s = [i for i in re.split('[ ,.]+', s[:-1])]
element_dict = {}
count = 0
for i, elem in enumerate(split_s):
    if l[count]-1 == i:
        if (count < len(l)-1):
            count += 1
        element_dict[elem[:1]] = i+1
    else:
        element_dict[elem[:2]] = i+1
print(element_dict)

# 05
def character_ngram(s, n):
    l = [s[i:i+n] for i in range(len(s)-(n-1))]
    return l

def word_ngram(s, n):
    split_s = s.split(' ')
    l = []
    for i in range(len(split_s)-(n-1)):
        a = ''
        for j in range(n):
            if j != 0:
                a += ' '
            a += split_s[i+j]
        l.append(a)
    return l

s = 'I am an NLPer'
print(character_ngram(s, 2))
print(word_ngram(s, 2))

# 06
s1 = 'paraparaparadise'
s2 = 'paragraph'
s1gram = set(character_ngram(s1, 2))
s2gram = set(character_ngram(s2, 2))
print(s1gram)
print(s2gram)
print(s1gram | s2gram)
print(s1gram & s2gram)
print(s1gram - s2gram)
if 'se' in s1gram:
    print('se in X')
else:
    print('se not in X')
if 'se' in s2gram:
    print('se in Y')
else:
    print('se not in Y')

# 07
def return_word(s1, s2, s3):
    return str(s1)+'時の'+str(s2)+'は'+str(s3)

s1 = 12
s2 = '気温'
s3 = 22.7
print(return_word(s1, s2, s3))

# 08
def cipher(s):
    new_s = ''
    for i in s:
        if i.islower():
            new_s += chr(219-ord(i))
        else:
            new_s += i
    return new_s
s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
print(cipher(s))

# 09
s = 'I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
split_s = s.split(' ')
l = []
for i in split_s:
    if (len(i) > 4):
        a = list(i[1:-1])
        random.shuffle(a)
        l.append(i[0]+''.join(a)+i[-1])
    else:
        l.append(i)
print(' '.join(l))