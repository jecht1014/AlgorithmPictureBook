import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import pandas as pd
import numpy as np
import time
import math
import matplotlib.pyplot as plt
import os
import pickle

class mydataset(torch.utils.data.Dataset):
    def __init__(self, data_num, input_data, label, transform = None):
        self.transform = transform
        self.data_num = data_num
        self.data = input_data
        self.label = label

    def __len__(self):
        return self.data_num

    def __getitem__(self, idx):
        out_data = self.data[idx]
        out_label = self.label[idx]

        if self.transform:
            out_data = self.transform(out_data)

        return out_data, out_label

class LSTM(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(LSTM, self).__init__()
        self.hidden_dim = hidden_dim

        self.lstm = nn.LSTM(input_dim, hidden_dim, batch_first = True)
        self.linear = nn.Linear(hidden_dim, output_dim)
        self.sigmoid = nn.Sigmoid()
        self.hidden = None

    def init_hidden(self, batch_size):
        return (torch.zeros(1, batch_size, self.hidden_dim).to(device), torch.zeros(1, batch_size, self.hidden_dim).to(device))

    def forward(self, inputs):
        lstm_out, self.hidden = self.lstm(inputs, self.hidden)
        linear_out = self.linear(self.hidden[0])
        output = self.sigmoid(linear_out)
        return output

idx = ['Open', 'High', 'Low', 'Close', 'SMA20']
window = 30
epochs = 1000

input_dim = len(idx)
hidden_dim = 32
output_dim = 1
batch_size = 64
save_path = 'result/20191128h2SMA'

data = pd.read_csv('data/oanda-H2-5000.csv')
#data = data[idx].diff()[1:]
data['SMA20'] = data['Close'].rolling(20).sum() / 20
data = data.dropna()
data = data.reset_index(drop=True)

max_value = data[idx].max().max()
min_value = data[idx].min().min()
data[idx] = ((data[idx] - min_value) / (max_value - min_value))
split_data = []
label_data = []
for i in range(0, len(data)-window):
    split_data.append(data[idx][i:i+window].values)
    #label_data.append(data['Close'][i+window])
    if data['Close'][i+window]-data['Close'][i+window-1] > 0:
        label_data.append(1)
    else:
        label_data.append(0)

split_line = 4000
train_data = split_data[:split_line]
test_data = split_data[split_line:]
train_label = label_data[:split_line]
test_label = label_data[split_line:]


'''
train_data = []
train_label = []
for i in range(0, len(train)-window):
    train_data.append(((train[idx][i:i+window] - min_value) / (max_value - min_value)).values)
    if train['Close'][i+window+1] > 0:
        train_label.append(1)
    else:
        train_label.append(0)

test_data = []
test_label = []
for i in range(0, len(test)-window):
    test_data.append(((test[idx][i:i+window] - min_value) / (max_value - min_value)).values)
    #print(len(test[idx][i:i+window]))
    if test['Close'][split_line+i+window+1] > 0:
        test_label.append(1)
    else:
        test_label.append(0)
'''
'''
train_label = []
test_label = []
for i in range(1, len(train)-window):
    if train['Close'][i+window+1] > 0:
        train_label.append(1)
    else:
        train_label.append(0)

for i in range(1, len(test)-window):
    if test['Close'][split_line+i+window+1] > 0:
        test_label.append(1)
    else:
        test_label.append(0)

train_data = []
test_data = []
for i in range(1, len(train)-window):
    train_data.append([])
    for j in range(window):
        if (train[idx][i+j] < 0):
            train_data[i].append(train[idx][i+j] / min_value)
        else:
            train_data[i].append(train[idx][i+j] / max_value)

for i in range(1, len(test)-window):
    test_data.append([])
    for j in range(window):
        if (test[idx][split_line+i+j] < 0):
            test_data[i].append(test[idx][split_line+i+j] / min_value)
        else:
            test_data[i].append(test[idx][split_line+i+j] / max_value)
'''

train_set = mydataset(len(train_data), train_data, train_label)
train_dataloader = torch.utils.data.DataLoader(train_set, batch_size = batch_size, shuffle = True)
test_set = mydataset(len(test_data), test_data, test_label)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = LSTM(input_dim, hidden_dim, output_dim).float().to(device)
#loss_function = nn.MSELoss()
loss_function = nn.BCELoss()
optimizer = optim.Adam(model.parameters())

batch_num = math.ceil(len(train_data) / batch_size)
history = {'loss': [], 'acc': [], 'acc0_2': [], 'acc2_4': [], 'acc4_5': [], 'acc5_6': [], 'acc6_8': [], 'acc8_10': [], 'count0_2': [], 'count2_4': [], 'count4_5': [], 'count5_6': [], 'count6_8': [], 'count8_10': []}
start_time = time.time()
os.makedirs(save_path+'/model', exist_ok=True)
'''
def accuracy(data, output, label):
    #print(torch.sum(label-data[:, 29, 3] > 0 == output-data[:, 29, 3] > 0))
    l = label-data[:, 29, 3] > 0
    r = output-data[:, 29, 3] > 0
    count = 0
    for i in range(output.shape[0]):
        if (l[i] == r[i]):
            count+=1
    return count
'''

def accuracy(output, label):
    return torch.sum((output >= 0.5) == (label == 1)).item()

def accuracy2(output, label, threshould1, threshould2):
    if (threshould1 >= 0.5 and torch.sum(torch.BoolTensor(output > threshould1) & torch.BoolTensor(output <= threshould2)).item() != 0):
        return torch.sum((torch.BoolTensor(output > threshould1) & torch.BoolTensor(output <= threshould2)) & (label == 1)).item() / torch.sum(torch.BoolTensor(output > threshould1) & torch.BoolTensor(output <= threshould2)).item()
    elif (threshould2 <= 0.5 and torch.sum(torch.BoolTensor(output >= threshould1) & torch.BoolTensor(output < threshould2)).item() != 0):
        return torch.sum((torch.BoolTensor(output >= threshould1) & torch.BoolTensor(output < threshould2)) & (label == 0)).item() / torch.sum(torch.BoolTensor(output >= threshould1) & torch.BoolTensor(output < threshould2)).item()
        
def accuracy2_counter(output, label, threshould1, threshould2):
    if (threshould1 >= 0.5 and torch.sum(torch.BoolTensor(output > threshould1) & torch.BoolTensor(output <= threshould2)).item() != 0):
        return torch.sum(torch.BoolTensor(output > threshould1) & torch.BoolTensor(output <= threshould2)).item()
    elif (threshould2 <= 0.5 and torch.sum(torch.BoolTensor(output >= threshould1) & torch.BoolTensor(output < threshould2)).item() != 0):
        return torch.sum(torch.BoolTensor(output >= threshould1) & torch.BoolTensor(output < threshould2)).item()

for epoch in range(1, epochs + 1):
    epoch_loss = 0
    acc = 0
    acc0_2 = 0
    acc2_4 = 0
    acc4_5 = 0
    acc5_6 = 0
    acc6_8 = 0
    acc8_10 = 0

    for data, label in train_dataloader:
        model.zero_grad()
        
        data = data.to(device)
        label = label.to(device)

        model.hidden = model.init_hidden(len(data))
        
        output = model(data.float())
        loss = loss_function(output, label.float().reshape(1, label.size()[0], 1))

        loss.backward()
        optimizer.step()

        epoch_loss += loss.cpu().item()

    with torch.no_grad():
        data, label = test_set[:]
        data = torch.Tensor(data).to(device)
        label = torch.Tensor(label).to(device)

        model.hidden = model.init_hidden(len(data))
        output = model(data)
        acc += accuracy(output.reshape(output.shape[1]), label)
        history['acc5_6'].append(accuracy2(output.reshape(output.shape[1]), label, 0.5, 0.6))
        history['acc6_8'].append(accuracy2(output.reshape(output.shape[1]), label, 0.6, 0.8))
        history['acc8_10'].append(accuracy2(output.reshape(output.shape[1]), label, 0.8, 1))
        history['acc4_5'].append(accuracy2(output.reshape(output.shape[1]), label, 0.4, 0.5))
        history['acc2_4'].append(accuracy2(output.reshape(output.shape[1]), label, 0.2, 0.4))
        history['acc0_2'].append(accuracy2(output.reshape(output.shape[1]), label, 0, 0.2))
        history['count5_6'].append(accuracy2_counter(output.reshape(output.shape[1]), label, 0.5, 0.6))
        history['count6_8'].append(accuracy2_counter(output.reshape(output.shape[1]), label, 0.6, 0.8))
        history['count8_10'].append(accuracy2_counter(output.reshape(output.shape[1]), label, 0.8, 1))
        history['count4_5'].append(accuracy2_counter(output.reshape(output.shape[1]), label, 0.4, 0.5))
        history['count2_4'].append(accuracy2_counter(output.reshape(output.shape[1]), label, 0.2, 0.4))
        history['count0_2'].append(accuracy2_counter(output.reshape(output.shape[1]), label, 0, 0.2))

    torch.save(model.state_dict(), save_path + '/model/model{0:04}.pth'.format(epoch))
    torch.save(optimizer.state_dict(), save_path + '/model/optimizer{0:04}.pth'.format(epoch))

    history['loss'].append(epoch_loss / batch_num)
    history['acc'].append(acc / len(test_label))
    print('epoch:{0:03} time:{1:.1f} loss:{2:.3} acc:{3:.1%}'.format(epoch, time.time() - start_time, epoch_loss / batch_num, acc / len(test_label)))

#    if epoch % 10 == 0:
#        torch.save(model.state_dict(), save_path + '/model/model{0:04}.pth'.format(epoch))
#        torch.save(optimizer.state_dict(), save_path + '/model/optimizer{0:04}.pth'.format(epoch))
with open(save_path + '/history.pickle', mode='wb') as f:
    pickle.dump(history, f)

os.makedirs(save_path+'/image', exist_ok=True)

plt.figure()
plt.title("Loss")
plt.plot(history['loss'],label="loss")
plt.xlabel("epochs")
plt.ylabel("Loss")
plt.savefig(save_path+'/image/loss.png')
plt.close()

idx = ["acc", "acc0_2", "acc2_4", "acc4_5", "acc5_6", "acc6_8", "acc8_10"
        , "count0_2", "count2_4", "count4_5", "count5_6", "count6_8", "count8_10"]
def image_plot(acc_name):
    plt.figure()
    plt.title(acc_name)
    plt.plot(history[acc_name],label=acc_name)
    plt.xlabel("epochs")
    plt.ylabel(acc_name)
    plt.legend()
    plt.savefig(save_path+'/image/{0}.png'.format(acc_name))
    plt.close()

for s in idx:
    image_plot(s)

'''
plt.figure()
plt.title("acc")
plt.plot(history['acc'],label="acc")
plt.plot(history['acc0_2'],label="acc0_2")
plt.plot(history['acc2_4'],label="acc2_4")
plt.plot(history['acc4_5'],label="acc4_5")
plt.plot(history['acc5_6'],label="acc5_6")
plt.plot(history['acc6_8'],label="acc6_8")
plt.plot(history['acc8_10'],label="acc8_10")
plt.xlabel("epochs")
plt.ylabel("acc")
plt.legend()
plt.savefig(save_path+'/acc.png')
plt.close()

plt.figure()
plt.title("count")
plt.plot(history['count0_2'],label="count0_2")
plt.plot(history['count2_4'],label="count2_4")
plt.plot(history['count4_5'],label="count4_5")
plt.plot(history['count5_6'],label="count5_6")
plt.plot(history['count6_8'],label="count6_8")
plt.plot(history['count8_10'],label="count8_10")
plt.xlabel("epochs")
plt.ylabel("num")
plt.legend()
plt.savefig(save_path+'/num.png')
plt.close()
'''