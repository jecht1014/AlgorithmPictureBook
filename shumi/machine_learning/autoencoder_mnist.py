from torchvision import datasets, transforms
mnist_data = datasets.MNIST('./mnist', train=True, download=True, transform=transforms.ToTensor())
print(mnist_data)