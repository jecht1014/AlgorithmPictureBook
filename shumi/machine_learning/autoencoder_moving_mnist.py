import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.utils import shuffle
import copy
import time
import pickle

from torchvision import datasets, transforms
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.utils as vutils

class Encoder(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(Encoder, self).__init__()
        self.hidden_size = hidden_size

        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=False)

    def forward(self, inputs, batch_size):
        _, state = self.lstm(inputs, (torch.zeros(1, batch_size, self.hidden_size).to(device), torch.zeros(1, batch_size, self.hidden_size).to(device)))
        
        return state

class Decoder(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(Decoder, self).__init__()
        self.hidden_size = hidden_size

        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=False)
        self.linear = nn.Linear(hidden_size, input_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, inputs, state):
        lstm_out, state = self.lstm(inputs, state)
        linear_out = self.linear(lstm_out)
        output = self.sigmoid(linear_out)
        return output, state

# 時系列長, データ数, 縦, 横
data = torch.from_numpy(np.load('data/mnist_test_seq.npy'))
data = data.float() / 255
data = data.reshape(20, 10000, 64*64)
split_line = 9000
train_data = data[:, :split_line, :]
test_data = data[:, split_line:, :]

'''
for i in range(10):
    plt.imshow(data[i, 0, :, :])
    plt.show()
'''
batch_size = 64
input_size = 64*64
hidden_size = 1024
epochs = 200
save_path = 'result/moving_mnist_LSTM_autoencoder_h{0}_2'.format(hidden_size)
os.makedirs(save_path + '/model', exist_ok=True)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
mnist_sample = train_data[:, :2, :].to(device)

encoder = Encoder(input_size, hidden_size).to(device)
decoder = Decoder(input_size, hidden_size).to(device)
criterion = nn.MSELoss()
encoder_optimizer = optim.Adam(encoder.parameters(), lr=0.001)
decoder_optimizer = optim.Adam(decoder.parameters(), lr=0.001)

def train2batch(data, batch_size):
    input_batch = []
    shuffle_arg = np.random.choice(range(split_line), split_line, replace=False)
    data = data[:, shuffle_arg, :]
    for i in range(0, split_line, batch_size):
        input_batch.append(data[:, i:i+batch_size, :])
    return input_batch

os.makedirs(save_path+'/image', exist_ok=True)
# 本物の画像の作成
real_image = copy.deepcopy(mnist_sample)
real_image = real_image * torch.tensor(255, device=device)
real_image = real_image.int()
real_image_c = torch.tensor([], device=device).int()
for i in range(real_image.size(1)):
    real_image_c = torch.cat([real_image_c, real_image[:, i, :]])
real_image_c = real_image_c.reshape(real_image_c.size(0), 1, 64, 64)
real_image = real_image_c
plt.imshow(np.transpose(vutils.make_grid(real_image, nrow=10, pad_value=200).cpu().numpy(), (1, 2, 0)))
plt.savefig(save_path+'/image/genuine_sample.png')
plt.close()

# 学習結果を画像に変換
def makeImage(encoder_model, decoder_model, epoch):
    image_tensor = torch.tensor([], device=device)
    with torch.no_grad():
        encoder_hidden = encoder_model(mnist_sample, mnist_sample.size(1))
        decoder_hidden = encoder_hidden
        decoder_input = torch.zeros((1, mnist_sample.shape[1], mnist_sample.shape[2]), device=device)
        for i in range(mnist_sample.size(0)):
            decoder_output, decoder_hidden = decoder_model(decoder_input, decoder_hidden)
            decoder_input = decoder_output
            image_tensor = torch.cat([image_tensor, copy.deepcopy(decoder_output)])
    image_tensor = image_tensor * torch.tensor(255, device=device)
    image_tensor = image_tensor.int()
    image_tensor_c = torch.tensor([], device=device).int()
    for i in range(image_tensor.size(1)):
        image_tensor_c = torch.cat([image_tensor_c, image_tensor[:, i, :]])
    image_tensor_c = image_tensor_c.reshape(image_tensor_c.size(0), 1, 64, 64)
    image_tensor = image_tensor_c
    
    plt.imshow(np.transpose(vutils.make_grid(image_tensor, nrow=10, pad_value=200).cpu().numpy(), (1, 2, 0)))
    plt.savefig(save_path + '/image/train_sample_{0:03}.png'.format(epoch))
    plt.close()

makeImage(encoder, decoder, 1)
print('end')

history = {'loss': []}
start_time = time.time()
for epoch in range(1, epochs+1):
    input_batch = train2batch(data, batch_size)
    sum_loss = 0
    for i in range(len(input_batch)):
        encoder_optimizer.zero_grad()
        decoder_optimizer.zero_grad()

        encoder_inputs = input_batch[i].to(device)
        start_sequence = torch.zeros((1, encoder_inputs.shape[1], encoder_inputs.shape[2]), device=device)
        decoder_inputs = torch.cat([start_sequence, copy.deepcopy(encoder_inputs[:-1, :, :])])

        encoder_hidden = encoder(encoder_inputs, encoder_inputs.size(1))
        decoder_hidden = encoder_hidden

        loss = 0
        for j in range(decoder_inputs.size(0)):
            decoder_output, decoder_hidden = decoder(decoder_inputs[j:j+1, :, :], decoder_hidden)
            loss += criterion(decoder_output, encoder_inputs[j:j+1, :, :])

        loss.backward()
        encoder_optimizer.step()
        decoder_optimizer.step()

        sum_loss += loss.cpu().item()
    makeImage(encoder, decoder, epoch)
    history['loss'].append(sum_loss/len(input_batch))
    print('epoch:{0:04} time:{1} loss:{2:.3}'.format(epoch, time.time()-start_time, sum_loss/len(input_batch)))

    # Save Model
    if epoch % 10 == 0:
        model_name = save_path+"/model/autoencoder_v{0:03}.pt".format(epoch)
        torch.save({
            'encoder_model': encoder.state_dict(),
            'decoder_model': decoder.state_dict(),
            'encoder_optimizer': encoder_optimizer.state_dict(),
            'decoder_optimizer': decoder_optimizer.state_dict(),
        }, model_name)

plt.figure()
plt.title("Autoencoder Loss During Training")
plt.plot(history['loss'],label="L")
plt.xlabel("epochs")
plt.ylabel("Loss")
plt.savefig(save_path + '/loss.png')
plt.close()

with open(save_path + '/history.pickle', mode='wb') as f:
    pickle.dump(history, f)