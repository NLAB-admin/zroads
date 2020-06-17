import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.models as models

from PIL import Image

# Load the ResNet101 architecture
resnet101 = models.resnet101()

# Adjust the number of output classes
num_ftrs = resnet101.fc.in_features
resnet101.fc = nn.Linear(num_ftrs, 2)

# Setup option data parallelism
resnet101 = torch.nn.DataParallel(resnet101).cuda()

# Load weights from trained model
weights = torch.load('model_best.pth.tar')

resnet101.load_state_dict(weights['state_dict'])
resnet101.eval()

# Open the image to be predicted
img = Image.open("test/good_example.png")

# Normalise and resize the image to match the original dataset
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])

transform = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        normalize,
    ])

img_t = transform(img)

# Add the image to a batch for processing
batch_t = torch.unsqueeze(img_t, 0)

# Generate prediction
prediction = resnet101(batch_t)

# Unpack the results
_, index = torch.max(prediction, 1)
percentage = torch.nn.functional.softmax(prediction, dim=1)[0] * 100

labels = ['Good Road', 'Bad Road']
print("The CNN predicted a {} with a confidence of {}%".format(labels[index[0]], percentage[index[0]].item()))
