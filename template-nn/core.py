# -*- coding: utf-8 -*-
"""

notebook上での使用などインタラクティブなクラスを提供

@author: tadahaya
"""
# packages installed in the current environment
import os
import datetime
import time
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm, trange

# original packages in src
from .src import utils
from .src import data_handler as dh
from .src.trainer import Trainer
from .src.models import MyNet

class Interactive:
    def __init__(self):
        pass

    def prepare_data(self):
        """ dataの準備 """
        raise NotImplementedError

    def prepare_model(self):
        """ modelの準備 """
        raise NotImplementedError

    def fit(self):
        """ 学習 """
        raise NotImplementedError

    def predict(self):
        """ 予測 """
        raise NotImplementedError

    def evaluate(self):
        """ 評価 """
        raise NotImplementedError