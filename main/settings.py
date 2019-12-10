# @Time : 2019/9/6 15:27
# @Author : Ylxy
# @File : settings.py
# -*- coding: utf-8 -*-
import pygame
import time
class Settings():
    def __init__(self):
        self.bg_color = (204,255,153)
        self.screen_width = 800
        self.screen_height = 600

        self.cell_size = 20
        assert self.screen_height % self.cell_size == 0
        assert self.screen_width % self.cell_size == 0
        self.cell_w = int(self.screen_width / self.cell_size)  # 一行的格子数
        self.cell_h = int(self.screen_height / self.cell_size)  # 一列的格子数
        self.num = self.cell_w * self.cell_h

        self.length = 0    # 蛇长度
        self.game_stats = 0  # 游戏状态
        self.score = 0  # 游戏得分

        self.clock_frq = 5  #刷新频率
        self.my_clock = pygame.time.Clock()




