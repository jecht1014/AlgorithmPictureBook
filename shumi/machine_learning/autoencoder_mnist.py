from torchvision import datasets, transforms
import torch
import torch.nn as nn
import torch.optim as optim

import math

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

mnist_sample = train_input[:64].to(device)
target_label = 1
batch_size = 64
input_size = 28*28
hidden_size = 128
epochs = 1000
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

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

for epoch in range(1, epochs+1):
    sum_loss = 0
    for i, data in enumerate(train_dataloader, 0):
        autoencoder.zero_grad()
        inputs, label = data
        inputs = inputs.to(device)
        outputs = autoencoder(inputs)
        loss = criterion(outputs, inputs)
        sum_loss += loss.item()
        optimizer.step()
        loss.backward()

    print('epoch:{0:04}\tloss:{1:}'.format(epoch, sum_loss/batch_num))