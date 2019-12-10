# @Time : 2019/9/8 8:47
# @Author : Ylxy
# @File : snake.py.py
# -*- coding: utf-8 -*-


import random


class Snake():
    def __init__(self, ai_settings):
        self.reset(ai_settings)

    # 蛇的初始化
    def reset(self, ai_settings):
        # 蛇头的坐标
        self.start_x = random.randint(5, ai_settings.cell_w - 6)
        self.start_y = random.randint(5, ai_settings.cell_h - 6)
        self.head_index = 0
        # 蛇的初始运动方向
        self.direction = 'right'
        # 蛇的初始坐标字典，初始蛇为蛇头位置及其左边的两个格子
        self.coords = [{'x': self.start_x, 'y': self.start_y},
                       {'x': self.start_x - 1, 'y': self.start_y},
                       {'x': self.start_x - 2, 'y': self.start_y}]

    # 更新蛇，每次蛇移动一步，因此相当于每次移动在蛇的坐标字典中再插入一个新蛇头
    # 按常识，每次移动后，不仅仅是蛇头向前移动一个，更重要的是蛇尾也要向前移，但是在该函数中先不处理蛇尾
    # 因为如果蛇吃了食物，此时蛇尾其实并没有移动
    def update(self):
        newHead = {}
        # 根据移动方向确定蛇头
        if self.direction == 'up':
            newHead = {'x': self.coords[self.head_index]['x'],
                       'y': self.coords[self.head_index]['y'] - 1}
        elif self.direction == 'down':
            newHead = {'x': self.coords[self.head_index]['x'],
                       'y': self.coords[self.head_index]['y'] + 1}
        elif self.direction == 'left':
            newHead = {'x': self.coords[self.head_index]['x'] - 1,
                       'y': self.coords[self.head_index]['y']}
        elif self.direction == 'right':
            newHead = {'x': self.coords[self.head_index]['x'] + 1,
                       'y': self.coords[self.head_index]['y']}
        self.coords.insert(0, newHead)


