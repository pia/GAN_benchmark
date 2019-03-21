import torch


class Config():
    visdom_env = 'benchmark'
    device = torch.device('cuda:0')
