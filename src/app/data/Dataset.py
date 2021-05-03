
import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import numpy as np
from facenet_pytorch import  training

import os


class Dataset:

    @staticmethod
    def load_data(path,size=160):
        # image_path = os.path.join(path, dir)
        return datasets.ImageFolder(path, transform=transforms.Resize((size, size)))
        