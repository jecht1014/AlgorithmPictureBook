import re

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

#04
s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
split_s = (i for i in re.split('[ ,.]+', s[:-1]))
element_dict = {}