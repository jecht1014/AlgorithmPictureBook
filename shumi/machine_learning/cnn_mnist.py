# mnistのtrainデータをすべて学習にかけるオートエンコーダ
from torchvision import datasets, transforms
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
#from torch.utils.tensorboard import SummaryWriter
from tensorboardX import SummaryWriter
import torchvision

import math
import os
import matplotlib.pyplot as plt
import numpy as np
import pickle
import cv2
import copy

class CNN(nn.Module):
    def __init__(self, input_ch, conv_kernel_size):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(input_ch, 6, conv_kernel_size)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, conv_kernel_size)
        self.fc1 = nn.Linear(16*4*4, 120)
        self.fc2 = nn.Linear(120, 60)
        self.fc3 = nn.Linear(60, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16*4*4)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

def matplotlib_imshow(img, one_channel=False):
    if one_channel:
        img = img.mean(dim=0)
    img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    if one_channel:
        plt.imshow(npimg, cmap="Greys")
    else:
        plt.imshow(np.transpose(npimg, (1, 2, 0)))

batch_size = 64
batch_num = int(60000/64)
input_ch = 1
conv_kernel_size = 5
epochs = 10
save_path = 'result/cnn_mnist'
os.makedirs(save_path, exist_ok=True)
classes = [str(i) for i in range(10)]
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

# データセット
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
train_set = datasets.MNIST('./data/mnist/train', train=True, download=True, transform=transform)
test_set = datasets.MNIST('./data/mnist/test', train=False, download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_set, batch_size=batch_size, shuffle=False)

# model
cnn = CNN(input_ch, conv_kernel_size)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(cnn.parameters(), lr=0.001, momentum=0.9)

writer = SummaryWriter(save_path+'/runs')

# train sample
dataiter = iter(train_loader)
images, labels = dataiter.next()
img_grid = torchvision.utils.make_grid(images)
#matplotlib_imshow(img_grid, one_channel=True)
writer.add_image('train_sample', img_grid)

# modelをtensorboardに追加
print(images.shape)
writer.add_graph(CNN(input_ch, conv_kernel_size), images[0:1])
cnn.to(device)
# 学習
for epoch in range(1, epochs+1):
    running_loss = 0.0
    for i, data in enumerate(train_loader, 0):
        optimizer.zero_grad()

        inputs, labels = [i.to(device) for i in data]

        outputs = cnn(inputs)
        loss = criterion(outputs, labels)
        
        loss.backward()
        optimizer.step()

        running_loss += loss.cpu().item()
    
    writer.add_scalar('training loss', running_loss/batch_num, epoch)
    print('epoch:{0:04} loss: {1:.3}'.format(epoch, running_loss/batch_num))

writer.close()