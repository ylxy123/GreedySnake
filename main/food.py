# @Time : 2019/9/8 8:56
# @Author : Ylxy
# @File : food.py.py
# -*- coding: utf-8 -*-
import random


class Food():
    def __init__(self, ai_settings, snake):
        self.update(ai_settings, snake)

    # 每次食物被吃后，自动找一个空白的地方放置食物
    def update(self, ai_settings, snake):
        flag = True
        food = {}
        while flag:
            food = {'x': random.randint(0, ai_settings.cell_w - 1),
                    'y': random.randint(0, ai_settings.cell_h - 1)}
            # 当新找的地方在蛇身，重新找
            if food not in snake.coords:
                flag = False
        self.coord = food

