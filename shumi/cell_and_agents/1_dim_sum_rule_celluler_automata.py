import matplotlib.pyplot as plt
import numpy as np
import random

class NeighborhoodAndRuleNumMismatchError(Exception):
    pass
class NeighborhoodError(Exception):
    pass

# 規則番号から自動的にルールの生成
neighborhood = 7 #n近傍
rule_num = 100 #規則番号
save_path = 'image'

if (neighborhood % 2 == 0):
    raise NeighborhoodError('neighborhoodは奇数です')
if (rule_num >= 2**(neighborhood+1)):
    raise NeighborhoodAndRuleNumMismatchError('rule_numとneighborhoodの関係が不一致です')

rule_dict = {}
rule_num_c = rule_num
for i in range(neighborhood, -1, -1):
    if (rule_num_c >= 2**i):
        rule_dict[i] = 1
        rule_num_c -= 2**i
    else:
        rule_dict[i] = 0

cells = []
cell_len = 131 #セルの数
first_cells = [int(random.random() >= 0.3) for i in range(cell_len)]
cells.append(first_cells)
for i in range(int(cell_len / 2)-1):
    cell = [0] * cell_len
    for j in range(cell_len-4):
        cell[j+2] = rule_dict[sum(cells[len(cells)-1][j:j+5])]
    cells.append(cell)

cells = np.array(cells[::-1])
X,Y = np.meshgrid(np.arange(cells.shape[1]),np.arange(cells.shape[0]))
plt.pcolormesh(X, Y, cells, cmap='Greys')
plt.savefig(save_path+'/1_dim_cell_neighborhood{0}_sum_transition_rules{1:03}_{2:03}.png'.format(neighborhood,rule_num, cell_len))