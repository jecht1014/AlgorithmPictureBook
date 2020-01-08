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

class CAE(nn.Module):
    def __init__(self, input_ch, kernel_size, basic_ch):
        super(CAE, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(input_ch, 16, 3, stride=3, padding=1),  # b, 16, 10, 10
            nn.ReLU(True),
            nn.MaxPool2d(2, stride=2),  # b, 16, 5, 5
            nn.Conv2d(16, 8, 3, stride=2, padding=1),  # b, 8, 3, 3
            nn.ReLU(True),
            nn.MaxPool2d(2, stride=1)  # b, 8, 2, 2
        )
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(8, 16, 3, stride=2),  # b, 16, 5, 5
            nn.ReLU(True),
            nn.ConvTranspose2d(16, 8, 5, stride=3, padding=1),  # b, 8, 15, 15
            nn.ReLU(True),
            nn.ConvTranspose2d(8, 1, 2, stride=2, padding=1),  # b, 1, 28, 28
            nn.Tanh()
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

batch_size = 64
batch_num = int(60000/64)
input_ch = 1
conv_kernel_size = 5
basic_ch = 32
epochs = 200
save_path = 'result/cae_mnist'
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
cae = CAE(input_ch, conv_kernel_size, basic_ch).to(device)
criterion = nn.MSELoss()
optimizer = optim.Adam(cae.parameters())

writer = SummaryWriter(save_path+'/runs')

# train sample
mnist_sample = train_set.data[:64].reshape((64, 1, 28, 28)).float() * 2 / 255 - 1
print(mnist_sample.shape)
img_grid = torchvision.utils.make_grid(mnist_sample, nrow=8, pad_value=200)
#matplotlib_imshow(img_grid, one_channel=True)
writer.add_image('sample_image', img_grid)

# modelをtensorboardに追加
writer.add_graph(cae, mnist_sample.to(device)[0:1])

mnist_sample = mnist_sample.to(device)
def makeImage(model, epoch):
    with torch.no_grad():
        outputs = model(mnist_sample).detach().cpu()# * 255
    outputs = outputs.reshape((outputs.shape[0], 1, 28, 28))#.int()
    writer.add_image('sample_output', torchvision.utils.make_grid(outputs, nrow=8, pad_value=200), epoch)

# 学習
for epoch in range(1, epochs+1):
    running_loss = 0.0
    for _, data in enumerate(train_loader, 0):
        optimizer.zero_grad()

        inputs, labels = [i.to(device) for i in data]

        outputs = cae(inputs)
        loss = criterion(outputs, inputs)
        
        loss.backward()
        optimizer.step()
        running_loss += loss.cpu().item()
    makeImage(cae, epoch)
    writer.add_scalar('training loss', running_loss/batch_num, epoch)
    print('epoch:{0:04} loss: {1:.3}'.format(epoch, running_loss/batch_num))

writer.close()