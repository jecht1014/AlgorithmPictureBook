import torch
import torch.optim as optim
import torch.nn as nn
import torch.nn.utils.rnn as rnn
import torch.backends.cudnn as cudnn
'''
if torch.cuda.is_available():
    import torch.cuda as t
else:
    import torch as t
'''
from torchvision import datasets, models, transforms, utils
import torchvision.utils as vutils

import re
import numpy as np
from numpy.random import normal
import os
import random
import time
import math
import matplotlib.pyplot as plt
import pickle

from mahjong.shanten import Shanten
from mahjong.tile import TilesConverter

cudnn.deterministic = True
cudnn.benchmark = False
seed = 1
random.seed(seed)
torch.manual_seed(seed)

def load_list(file_name):
    f = open(file_name, 'rb')
    l = pickle.load(f)
    return l

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
        output = self.linear(self.hidden[0])
        return self.sigmoid(output)

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

train_size = 0.8
epochs = 300
input_dim = 36
hidden_dim = 64
output_dim = 35
batch_size = 64
save_path = 'logs'

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#device = torch.device("cpu")

sutehai_jikeiretsu_data = load_list('data/mahjong_lstm_inputdata.txt')
tenpai_jikeiretsu_data = load_list('data/mahjong_lstm_outputlabel.txt')

input_data = rnn.pad_sequence([torch.FloatTensor(i) for i in sutehai_jikeiretsu_data], batch_first=True)
label_data = [i[len(i)-1] for i in tenpai_jikeiretsu_data]
label_data = torch.IntTensor(label_data)

train_num = int(label_data.size()[0]*train_size)
batch_num = math.ceil(train_num / batch_size)

learning_dataset = mydataset(len(input_data), input_data, label_data)
train_dataset, test_dataset = torch.utils.data.random_split(learning_dataset, [train_num, label_data.size()[0]-train_num])
train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

model = LSTM(input_dim, hidden_dim, output_dim).float().to(device)
#loss_function = nn.BCEWithLogitsLoss()
loss_function = nn.BCELoss()
optimizer = optim.Adam(model.parameters())

def all_accuracy(output, label):
    output = output.reshape(output.size()[1], output.size()[2])
    label = label.reshape(label.size()[1], label.size()[2])
    b_num = output.size()[0]
    
    result = ((output > 0.5) == label).all(dim=1).sum().item()
    return result / b_num

def accuracy1(output, label):
    output = output.reshape(output.size()[1], output.size()[2])
    label = label.reshape(label.size()[1], label.size()[2])

    #print(((torch.argmax(output*label, dim=1) == torch.argmax(output, dim=1)).sum().float())/output.size()[0])
    return ((torch.argmax(output*label, dim=1) == torch.argmax(output, dim=1)).sum().float()/output.size()[0]).item()

def accuracy3(output, label):
    output = output.reshape(output.size()[1], output.size()[2])
    label = label.reshape(label.size()[1], label.size()[2])

    output_arg = torch.argsort(-output, dim=1)
    count = 0
    for i in range(output.size()[0]):
        for j in range(3):
            if label[i][output_arg[i][j]] == 1:
                count+=1
                break

    return count/output.size()[0]
            

start_time = time.time()
history = {'loss': [], 'acc': [], 'acc3': []}
for epoch in range(1, epochs+1):
    epoch_loss = 0
    acc = 0
    acc3 = 0
    all_acc = 0

    for data, label in train_dataloader:
        model.zero_grad()

        data = data.to(device)
        label = label.to(device)
        label = label.float().reshape(1, label.size()[0], label.size()[1])
        
        model.hidden = model.init_hidden(len(data))

        output = model(data)
        loss = loss_function(output, label)
        all_acc += all_accuracy(output, label)
        #acc += accuracy1(output, label)
        loss.backward()
        optimizer.step()

        epoch_loss += loss.cpu().item()
    
    with torch.no_grad():
        test_data, test_label = test_dataset[:]
        test_data = test_data.to(device)
        test_label = test_label.to(device)
        test_label = test_label.float().reshape(1, test_label.size()[0], test_label.size()[1])

        model.hidden = model.init_hidden(len(test_data))
        output = model(test_data)
        acc = accuracy1(output, test_label)
        acc3 = accuracy3(output, test_label)

    history['loss'].append(epoch_loss/batch_num)
    history['acc'].append(acc)
    history['acc3'].append(acc3)
    print('epoch:{0:03} time:{1:.1f} loss:{2:.3} acc:{3:.3f} acc3:{4:.3f}'.format(epoch, time.time()-start_time, epoch_loss/batch_num, acc, acc3))

plt.figure()
plt.title("accuracy")
plt.plot(history['acc'],label="accuracy")
plt.plot(history['acc3'], label='accuracy3')
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.legend()
plt.savefig(save_path + '/acc.png')
plt.close()