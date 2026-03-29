# Day 9 - Neural Networks

## Assignment

Build and train a **feedforward neural network** using **PyTorch** for handwritten digit recognition on the MNIST dataset.

### Dataset

**MNIST** — downloaded automatically via `torchvision.datasets.MNIST`:
- Training set: 60,000 images
- Test set: 10,000 images
- Image size: 28×28 grayscale pixels

### Network Architecture

```
Input:   784 neurons  (28×28 flattened)
Hidden:  512 neurons  (ReLU activation)
Output:   10 neurons  (digit classes 0–9)
```

### Tasks

1. Load and preprocess the MNIST dataset:
   - Apply `transforms.ToTensor()`
   - Normalize with `mean=0.1307, std=0.3081`
   - Create `DataLoader` with `batch_size=64`
2. Define the network as a `nn.Module` subclass with the architecture above.
3. Train for **10 epochs** using:
   - Loss: `nn.CrossEntropyLoss()`
   - Optimizer: `torch.optim.SGD(lr=0.01)`
4. After each epoch, print training loss and accuracy.
5. Evaluate on the test set and report final **test accuracy**.

### Libraries

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
```

> No external data file required — MNIST downloads automatically via torchvision.
