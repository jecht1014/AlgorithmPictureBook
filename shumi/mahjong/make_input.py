import re
import copy
import pickle

from mahjong.shanten import Shanten
from mahjong.tile import TilesConverter

#字牌変換用テーブル
jihai_table = str.maketrans('東南西北白発中', '1234567', '')

def get_horashya_data():
    end_pattern1 = re.compile("  ---- 試合結果 ----")
    end_pattern2 = re.compile(" *[1-4]位")
    end_pattern3 = re.compile('----- 終了 -----')
    pattern_start = re.compile('=====*')  # ゲームスタート行の先頭文字列パターン
    pattern_player = re.compile(' *持点')  # プレイヤー情報行の先頭文字列パターン
    pattern_kyoku = re.compile(' *[東南西][1-4]局')  # 局情報行の先頭文字列パターン
    pattern_tehai = re.compile(' *\[[1-4][東南西北]\]')  # 手牌情報行の先頭文字列パターン
    pattern_dahai = re.compile(' *\*')  # 打牌情報行の先頭文字列パターン

    game_id = 0
    kyoku_id = 0
    learning = []
    dahai_lines = 0
    tehai_lines = []  # 手配
    winner = 0  # 和了者

    file = 'data/hounan2009utf-8.txt'
    f = open(file, errors='ignore')
    # line = f.readline()
    for line in f:
        if end_pattern1.match(line) or end_pattern2.match(line):
            ''' 試合結果行の処理 '''
            continue
        elif end_pattern3.match(line):
            line = f.readline()
            continue
        elif pattern_start.match(line) != None:
            ''' 試合スタート行の処理 '''
            game_id += 1
        ryukyoku_flag = 0  # 流局フラグ初期化
        tehai_lines = []  # 手配
        dahai_lines = 0  # 打牌行格納用リスト
        winner = 0  # 和了者
        while line != '\n':
            '''
            １局分の処理
            '''
            #print(line)
            if "流局" in line:
                ''' 流局フラグ '''
                ryukyoku_flag = 1

            elif pattern_tehai.match(line) != None:
                ''' 手牌情報行の処理 '''
                tmp = line.strip()  # 行頭のスペース削除
                tmp = re.sub('\[[1-4][東西南北]\]', '', tmp)
                tehai_lines.append(tmp)

            elif pattern_dahai.match(line) != None:
                '''
                打牌情報行の処理
                スペース削除作業をしてリストに追加
                '''
                if ryukyoku_flag == 1:
                    '''
                    流局フラグが立っていたら、打牌情報から和了者を特定しなくてよい
                    '''
                else:
                    tmp = line.strip()  # 行頭のスペース削除
                    tmp = tmp.replace("* ", "")  # 行頭のアスタリスクとスペース削除
                    if(len(tmp) == 2 and dahai_lines == 0):
                        ryukyoku_flag = 1
                    elif(len(tmp) != 2):
                        if "A" in tmp:
                            winner = tmp[-2]  # while を抜けるまで固定
                            if(dahai_lines == 0):
                                dahai_lines = tmp[:len(tmp)-3]
                            else:
                                dahai_lines = dahai_lines + " " + tmp[:len(tmp)-3]
                        elif(dahai_lines == 0):
                            dahai_lines = tmp
                        else:
                            dahai_lines = dahai_lines + " " + tmp
                    else:
                        winner = tmp[-2]
            line = f.readline()
            
        if(ryukyoku_flag == 0):
            dahai_lines = dahai_lines.split()
            newdahai = []
            for i in dahai_lines:
                if(re.match(winner, i) != None):
                    if(re.match(winner, i).start() == 0 and i != winner + 'R'):
                        newdahai.append(i)
            dahai_lines = newdahai
            learning.append([tehai_lines[int(winner)-1], dahai_lines])
    f.close()
    return learning

def remove_tehai(man, pin, sou, honors, dahai):
    if re.search(r'[mM]', dahai) is not None:
        man = list(man)
        man.remove(dahai[0])
        man = "".join(man)
    elif re.search(r'[pP]', dahai) is not None:
        pin = list(pin)
        pin.remove(dahai[0])
        pin = "".join(pin)
    elif re.search(r'[sS]', dahai) is not None:
        sou = list(sou)
        sou.remove(dahai[0])
        sou = "".join(sou)
    elif re.search(r'[東南西北白発中]', dahai):
        honors = list(honors)
        honors.remove(dahai[0].translate(jihai_table))
        honors = "".join(honors)
    return man, pin, sou, honors

# 通常手牌からponかchiしたときの手牌に変換
def pon_and_chi_tehai(man, pin, sou, honors, hai):
    if re.search(r'[mMpPsS]', hai) is not None:
        man, pin, sou, honors = remove_tehai(man, pin, sou, honors, hai[0:2])
        man, pin, sou, honors = remove_tehai(man, pin, sou, honors, hai[2:4])
    else:
        man, pin, sou, honors = remove_tehai(man, pin, sou, honors, hai[0:1])
        man, pin, sou, honors = remove_tehai(man, pin, sou, honors, hai[1:2])
    return man, pin, sou, honors
    
# 通常手牌からkanしたときの手牌に変換
def kan_tehai(man, pin, sou, honors, hai):
    if re.search(r'[mMpPsS]', hai) is not None:
        man, pin, sou, honors = remove_tehai(man, pin, sou, honors, hai)
        if ((re.search(r'[mM]', hai) is not None) & (re.search(hai[0], man) is not None)) | ((re.search(r'[pP]', hai) is not None) & (re.search(hai[0], pin) is not None)) | ((re.search(r'[sS]', hai) is not None) & (re.search(hai[0], sou) is not None)):
            man, pin, sou, honors = remove_tehai(man, pin, sou, honors, hai)
            man, pin, sou, honors = remove_tehai(man, pin, sou, honors, hai)
            if ((re.search(r'[mM]', hai) is not None) & (re.search(hai[0], man) is not None)) | ((re.search(r'[pP]', hai) is not None) & (re.search(hai[0], pin) is not None)) | ((re.search(r'[sS]', hai) is not None) & (re.search(hai[0], sou) is not None)):
                man, pin, sou, honors = remove_tehai(man, pin, sou, honors, hai)
    else:
        man, pin, sou, honors = remove_tehai(man, pin, sou, honors, hai)
        if re.search(hai.translate(jihai_table), honors):
            man, pin, sou, honors = remove_tehai(man, pin, sou, honors, hai)
            man, pin, sou, honors = remove_tehai(man, pin, sou, honors, hai)
            if re.search(hai.translate(jihai_table), honors):
                man, pin, sou, honors = remove_tehai(man, pin, sou, honors, hai)
    return man, pin, sou, honors

# 牌を引いてきたときの手牌に変換
def add_tehai(man, pin, sou, honors, tsumo):
    if re.search(r'[mM]', tsumo) is not None:
        man = man + tsumo[0]
    elif re.search(r'[pP]', tsumo) is not None:
        pin = pin + tsumo[0]
    elif re.search(r'[sS]', tsumo) is not None:
        sou = sou + tsumo[0]
    else:
        honors = honors + tsumo[0].translate(jihai_table)
    return man, pin, sou, honors
  
def split_hai(player_behavior_and_hai):
    pattern = r'[GDdNCK]'
    matchOB = re.search(pattern, player_behavior_and_hai)
    player_behavior = matchOB.group()
    hai = player_behavior_and_hai[matchOB.start()+1:]
    return player_behavior, hai

# 入力データの作成
# 0~8:man,9~17:pin,18~26:sou,27~33:honor,
# 左から33番目までは切った牌を1,34は赤なら1,35は手出しなら1 
def make_input_data(player_behavior, dahai):
    input_list = [0 for i in range(9*3 + 7 + 2)]
    if re.search('d', player_behavior) is not None:
        input_list[34] = 1
    if re.search(r'[MPS]', dahai) is not None:
        input_list[33] = 1
    if re.search(r'[Mm]', dahai) is not None:
        input_list[int(dahai[0]) - 1] = 1
    elif re.search(r'[Pp]', dahai) is not None:
        input_list[int(dahai[0]) + 9 - 1] = 1
    elif re.search(r'[Ss]', dahai) is not None:
        input_list[int(dahai[0]) + 9 * 2 - 1] = 1
    else:
        input_list[int(dahai[0].translate(jihai_table)) + 9 * 3 - 1]
    return input_list

# 出力ラベルの作成
# 0~8:man,9~17:pin,18~26:sou,27~33:honor,
# 左から33番目までは切った牌を1,34は聴牌してないなら1
def make_output_label(man, pin, sou, honors):
    output_label = [0 for i in range(9 * 3 + 7 + 1)]
    tiles = TilesConverter.string_to_34_array(
        man,
        pin,
        sou,
        honors
    )
    shanten = Shanten()
    shanten_result = shanten.calculate_shanten(tiles)
    
    # 聴牌していないなら
    if shanten_result != 0:
        output_label[34] = 1
    else:
        for i in range(34):
            new_tiles = copy.copy(tiles)
            new_tiles[i] += 1
            if(shanten.calculate_shanten(new_tiles) == -1):
                if i < 9:
                    output_label[i + 9 * 2] = 1
                elif (i < 27) & (i >= 18):
                    output_label[i - 9 * 2] = 1
                else:
                    output_label[i] = 1
    return output_label

def save_list(l, file_name):
    f = open(file_name, 'wb')
    pickle.dump(l, f)

def load_list(file_name):
    f = open(file_name, 'rb')
    l = pickle.load(f)
    return l

def make_data():
    learning = get_horashya_data()
    sutehai_jikeiretsu_data = []
    tenpai_jikeiretsu_data = []

    # 文字列からマンズ、ピンズ、ソーズ、字牌にそれぞれ変換
    for count, i in enumerate(learning):
        if count % 100 == 0:
            print(count + 1, '/', len(learning))
        man = ''
        pin = ''
        sou = ''
        honors = ''

        tehai = i[0]
        #print(tehai)
        flag = tehai.rfind('m')
        flag2 = tehai.rfind('M')
        if(flag2 > flag):
            flag = flag2
        if flag != -1:
            man = tehai[0:flag+1].replace('m', '').replace('M', '')
        if len(tehai) != flag+1:
            tehai = tehai[flag+1:]
            
            flag = tehai.rfind('p')
            flag2 = tehai.rfind('P')
            if(flag2 > flag):
                flag = flag2
            if flag != -1:
                pin = tehai[0:flag+1].replace('p', '').replace('P', '')
            if len(tehai) != flag+1:
                tehai = tehai[flag+1:]
                
                flag = tehai.rfind('s')
                flag2 = tehai.rfind('S')
                if flag2 > flag:
                    flag = flag2
                if flag != -1:
                    sou = tehai[0:flag+1].replace('s', '').replace('S', '')
                if len(tehai) != flag+1:
                    tehai = tehai[flag+1:]
                    honors = tehai.translate(jihai_table)
        
        #0~8:man,9~17:pin,18~26:sou,27~33:honor,左から33番目までは切った牌を1,34は赤なら1,35は手出しなら1      
        #[0,0,..,0,0]
        sutehai_jikeiretsu = []
        tenpai_jikeiretsu = []
        for player_behavior_and_hai in i[1]:
            player_behavior, hai = split_hai(player_behavior_and_hai)
            if re.search('G', player_behavior) is not None:
                man, pin, sou, honors = add_tehai(man, pin, sou, honors, hai)
            elif re.search(r'[NC]', player_behavior) is not None:
                man, pin, sou, honors = pon_and_chi_tehai(man, pin, sou, honors, hai)
            elif re.search('K', player_behavior) is not None:
                man, pin, sou, honors = kan_tehai(man, pin, sou, honors, hai)
            elif re.search(r'[dD]', player_behavior) is not None:
                man, pin, sou, honors = remove_tehai(man, pin, sou, honors, hai)
                sutehai_jikeiretsu.append(make_input_data(player_behavior, hai))
                tenpai_jikeiretsu.append(make_output_label(man, pin, sou, honors))
            
        sutehai_jikeiretsu_data.append(sutehai_jikeiretsu)
        tenpai_jikeiretsu_data.append(tenpai_jikeiretsu)

    save_list(sutehai_jikeiretsu_data, 'data/mahjong_lstm_inputdata.txt')
    save_list(tenpai_jikeiretsu_data, 'data/mahjong_lstm_outputlabel.txt')

make_data()