# @Time : 2019/9/8 8:41
# @Author : Ylxy
# @File : main.py.py
# -*- coding: utf-8 -*-
from settings import Settings
import pygame
import game_function as gf
from snake import Snake
from food import Food


ai_settings = Settings()  # 设置屏幕

screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

pygame.display.set_caption('贪吃蛇')  # 添加游戏标题

snake = Snake(ai_settings)  # 创建蛇
food = Food(ai_settings, snake)  # 创建食物

# 游戏难度1
def run_game1_1():
    ai_settings.clock_frq = 5
    gf.check_play_events(snake)
    gf.update_screen(ai_settings, screen, snake, food)

# 游戏难度2
def run_game1_2():
    ai_settings.clock_frq = 10
    gf.check_play_events(snake)
    gf.update_screen(ai_settings, screen, snake, food)

# 游戏难度3
def run_game1_3():
    ai_settings.clock_frq = 15
    gf.check_play_events(snake)
    gf.update_screen(ai_settings, screen, snake, food)


def run_game():
    music = pygame.mixer.music.load("bgm.wav")
    pygame.mixer.music.play()

    while True:
        if ai_settings.game_stats == 0:
            gf.show_start_interface(ai_settings, screen)
        elif ai_settings.game_stats == -1:
            gf.show_end_interface(ai_settings, screen)
            snake.reset(ai_settings)
            ai_settings.score = 0
            ai_settings.length = 0
        elif ai_settings.game_stats == 5:
            gf.show_choose_level(ai_settings, screen)
        elif ai_settings.game_stats == 1:
            run_game1_1()
        elif ai_settings.game_stats == 2:
            run_game1_2()
        elif ai_settings.game_stats == 3:
            run_game1_3()
        elif ai_settings.game_stats == 4:
            gf.show_list(ai_settings, screen)


if __name__ == "__main__":
    pygame.init()
    run_game()



