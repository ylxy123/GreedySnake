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
        self.free_place = (self.cell_w + 1) * (self.cell_h + 1)
        self.snake_place = 2 * self.free_place

        # 运动方向字典
        self.move_directions = {
            'left': -1,
            'right': 1,
            'up': -self.cell_w,
            'down': self.cell_w
        }

        self.ERR = -404
        self.best_move = self.ERR
        self.Head_index = 0

        self.length = 0    # 蛇长度
        self.game_stats = 0  # 游戏状态
        self.score = 0  # 游戏得分

        self.clock_frq = 5  #刷新频率
        self.display_clock = 60  # ai模式刷新率
        self.my_clock = pygame.time.Clock()




