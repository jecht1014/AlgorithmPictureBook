import numpy as np
import copy

black_num = 22
white_num = 23
satisfaction_rate = 0.2
field_size = (8, 8)
field_cell_num = field_size[0]*field_size[1]

# ランダムに初期座標の決める
field = np.zeros(field_cell_num)
black_idx = np.random.choice(range(0, field_cell_num), black_num, replace=False)
field[black_idx] = 1
white_idx = np.random.choice(np.where(field == 0)[0], white_num, replace=False)
field[white_idx] = -1
field = field.reshape(field_size)

window = [-1, 0, 1]
change_num = 1
while change_num != 0:
    change_num = 0
    black_and_whete_idx = np.where((field == -1) | (field == 1))
    for x, y in zip(black_and_whete_idx[0], black_and_whete_idx[1]):
        # 8近傍で同じ人種の数のカウント
        same_race_num = 0
        interracial_num = 0
        for i in window:
            for j in window:
                if 0 <= x+i < field_size[0] and 0 <= y+j < field_size[1]:
                    if field[x, y] == field[x+i, y+j]:
                        same_race_num += 1
                    elif field[x, y] != 0:
                        interracial_num += 1
        
        # 8近傍に同じ人種が住んでいる率がsatisfaction_rate以下なら引っ越す
        if (same_race_num-1)/(same_race_num-1+interracial_num) < satisfaction_rate:
            zero_idx = np.where(field == 0)
            change_num = np.random.choice(range(zero_idx[0].shape[0]))
            field[zero_idx[0][change_num], zero_idx[1][change_num]] = field[x, y]
            field[x, y] = 0
            change_num += 1
print(field)