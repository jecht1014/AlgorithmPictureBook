from torchvision import datasets, transforms
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.utils as vutils

import math
import os
import matplotlib.pyplot as plt
import numpy as np
import pickle
import cv2

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

class Autoencoder(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(Autoencoder, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.layer2 = nn.Linear(hidden_size, input_size)

        self.encoder = nn.Sequential(
            self.layer1,
            nn.Sigmoid()
        )
        self.decoder = nn.Sequential(
            self.layer2,
            nn.Sigmoid()
        )

    def forward(self, inputs):
        encoded = self.encoder(inputs)
        decoded = self.decoder(encoded)
        return decoded

train_data = datasets.MNIST('./mnist/train', train=True, download=True, transform=transforms.ToTensor())
test_data = datasets.MNIST('./mnist/test', train=False, download=True, transform=transforms.ToTensor())
print(len(test_data))
train_input, train_label = train_data.data/255, train_data.targets
train_input = torch.flatten(train_input, start_dim=1, end_dim=2)

target_label = 1
batch_size = 64
input_size = 28*28
hidden_size = 128
epochs = 400
save_path = 'result/compression_autoencoder_h{0}'.format(hidden_size)
os.makedirs(save_path, exist_ok=True)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
mnist_sample = train_input[:64].float().to(device)

# 0~9の中でtargetのみのデータセットを作成する
train_target_arg = torch.where(train_label == target_label)
print(train_input.shape)
print(train_target_arg[0].shape)
print(train_input[train_target_arg[0]].shape)
train_input_data = train_input[train_target_arg[0]].float()
train_label_data = train_label[train_target_arg[0]]
train_dataset = mydataset(len(train_label_data), train_input_data, train_label_data)
train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle = True)

autoencoder = Autoencoder(input_size, hidden_size).to(device)
criterion = nn.MSELoss()
optimizer = optim.Adam(autoencoder.parameters())

batch_num = math.ceil(train_label_data.shape[0] / batch_size)

os.makedirs(save_path+'/image', exist_ok=True)
def makeImage(model, epoch):
    with torch.no_grad():
        outputs = autoencoder(mnist_sample).detach().cpu() * 255
    outputs = outputs.reshape((outputs.shape[0], 1, 28, 28)).int()
    plt.figure(figsize=(8, 8))
    plt.axis('off')
    plt.title('{0:04} epochs Autoencoder Result'.format(epoch))
    plt.imshow(np.transpose(vutils.make_grid(outputs), (1, 2, 0)))
    plt.savefig(save_path + '/image/{0:04}_epochs.png'.format(epoch))
    plt.close()

history = {'loss': []}
for epoch in range(1, epochs+1):
    sum_loss = 0
    for i, data in enumerate(train_dataloader, 0):
        autoencoder.zero_grad()
        inputs, label = data
        inputs = inputs.to(device)
        outputs = autoencoder(inputs)
        loss = criterion(outputs, inputs)
        loss.backward()
        optimizer.step()
        sum_loss += loss.item()

    history['loss'].append(sum_loss/batch_num)
    makeImage(autoencoder, epoch)
    print('epoch:{0:04}\tloss:{1:.4}'.format(epoch, sum_loss/batch_num))

plt.figure()
plt.title("Loss During Training")
plt.plot(history['loss'],label="loss")
plt.xlabel("epochs")
plt.ylabel("Loss")
plt.savefig(save_path + '/loss.png')
plt.close()

# サンプルの出力結果の保存
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
video = cv2.VideoWriter(save_path + '/video.mov', fourcc, 40.0, (800, 800))
for i in range(1, epochs+1):
    img = cv2.imread(save_path + '/image/{0:04}_epochs.png'.format(i))
    video.write(img)
video.release()

# 学習による
with open(save_path + '/history.pickle', mode='wb') as f:
    pickle.dump(history, f)