import visdom
from config import *


class Visualizer():
    def __init__(self):
        self.opt = Config()
        self.viz = visdom.Visdom(env=self.opt.visdom_env, port=80)

    def img(self, name):
        self.viz.images()