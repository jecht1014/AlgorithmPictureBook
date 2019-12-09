import matplotlib.pyplot as plt
import numpy as np

save_path = 'image'

rule_num = 90
rule_dict = {}
rule_num_c = rule_num
for i in range(8-1, -1, -1):
    bin_str = format(i, '03b')
    
    if (rule_num_c >= 2**i):
        rule_dict[(int(bin_str[0]), int(bin_str[1]), int(bin_str[2]))] = 1
        rule_num_c -= 2**i
    else:
        rule_dict[(int(bin_str[0]), int(bin_str[1]), int(bin_str[2]))] = 0

cells = []
cell_len = 131
first_cells = [0] * cell_len
first_cells[int(cell_len/2)] = 1
cells.append(first_cells)

for i in range(int(cell_len / 2)-1):
    cell = [0] * cell_len
    for j in range(cell_len-2):
        cell[j+1] = rule_dict[tuple(cells[len(cells)-1][j:j+3])]
    cells.append(cell)

cells = np.array(cells[::-1])
X,Y = np.meshgrid(np.arange(cells.shape[1]),np.arange(cells.shape[0]))
plt.pcolormesh(X, Y, cells, cmap='Greys')
plt.savefig(save_path+'/1_dim_cell_{0:03}_{1:03}.png'.format(rule_num, cell_len))