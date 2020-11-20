# @Time : 2019/9/8 8:44
# @Author : Ylxy
# @File : game_function.py.py
# -*- coding: utf-8 -*-

import pygame
import sys
import random
from pygame.locals import *



# 检测启动页的键盘操作
def check_events(ai_settings):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_1:
                ai_settings.game_stats = 5
            elif event.key == pygame.K_2:
                ai_settings.game_stats = 22
            elif event.key == pygame.K_F2:
                ai_settings.game_stats = 4



# 绘制启动页
def show_start_interface(ai_settings, screen):
    title_Font = pygame.font.Font("../font/STXINGKA.TTF", 90)  # 设置标题字体
    title_image = title_Font.render("贪吃蛇", True, (0, 0, 0))  #
    background = pygame.image.load(r"../image/贪吃蛇启动界面背景2.jpg")
    author_font = pygame.font.Font("../font/STXINGKA.TTF", 40)
    author_image = author_font.render(u"made by : ylxy~~~", True, (0, 0, 0))

    presskey_font = pygame.font.Font("../font/STKAITI.TTF", 35)  # 设置说明文字的字体
    presskey_image = presskey_font.render('按 1 开始游戏 按 Esc 退出游戏', True, (0, 0, 0))
    presskey_ai = presskey_font.render('按 2 进入AI模式',True,(0,0,0))
    list_font = pygame.font.Font("../font/STKAITI.TTF", 35)   # 设置排行榜说明文字字体
    list_image = list_font.render('按 F2 进入排行榜', True, (0, 0, 0))

    while True:

        screen.fill(ai_settings.bg_color)  # 绘制屏幕
        screen.blit(background, (0, 0))  # 背景图
        screen.blit(presskey_ai, (525, 250))
        screen.blit(title_image, (400,50))  # 绘制标题
        screen.blit(presskey_image, (300,160))  # 绘制说明文字
        screen.blit(author_image,(400,550))   #作者~~
        screen.blit(list_image,(525,326))  # 排行榜
        check_events(ai_settings)  # 检测键盘
        if ai_settings.game_stats != 0:  # 说明按了键，退出循环
            pygame.mixer.music.stop()
            break
        pygame.display.flip()


# 检测难度选择页的键盘操作
def check_choose_events(ai_settings):
    for event in pygame.event.get():
        # 当按关闭或者按ESC键退出游戏
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # 按1键选择难度1
            elif event.key == pygame.K_1:
                ai_settings.game_stats = 1
            # 按2键选择难度2
            elif event.key == pygame.K_2:
                ai_settings.game_stats = 2
            # 按3键选择难度3
            elif event.key == pygame.K_3:
                ai_settings.game_stats = 3
            elif event.key == pygame.K_F1:
                ai_settings.game_stats = 0


# 绘制难度选择页
def show_choose_level(ai_settings, screen):
    background1 = pygame.image.load(r"../image/选择难度1.jpg")
    level_font = pygame.font.Font("../font/STKAITI.TTF",40)      # 设置难度选择标题
    level_image = level_font.render('↓ 选择你想要的难度 ↓',True,(255, 255, 240))

    key1_font = pygame.font.Font("../font/STKAITI.TTF", 20)       # 设置说明文字的字体
    key1_image = key1_font.render('按 1 选择难度1', True, (0, 0, 0))

    key2_font = pygame.font.Font("../font/STKAITI.TTF", 20)
    key2_image = key2_font.render('按 2 选择难度2', True, (0, 0, 0))

    key3_font = pygame.font.Font("../font/STKAITI.TTF", 20)
    key3_image = key3_font.render('按 3 选择难度3', True, (0, 0, 0))

    key4_font = pygame.font.Font("../font/STKAITI.TTF", 25)
    key4_image = key4_font.render('按 F1 返回主界面', True, (0, 0, 0))


    while True:
        screen.fill(ai_settings.bg_color)    # 绘制屏幕
        screen.blit(background1, (0, 0))     #背景图
        screen.blit(level_image, (100, 200))   # 绘制难度选择标题
        screen.blit(key1_image, (150, 300))      # 绘制说明选项，下同
        screen.blit(key2_image, (150, 400))
        screen.blit(key3_image, (150, 500))
        screen.blit(key4_image, (250, 550))

        check_choose_events(ai_settings)  # 检测键盘
        if ai_settings.game_stats == 1 or ai_settings.game_stats == 2 or ai_settings.game_stats == 3 or ai_settings.game_stats == 0:
            break
        pygame.display.flip()


# 绘制结束页，game over位于屏幕中间
def show_end_interface(ai_settings, screen):
    title_font = pygame.font.SysFont('calibri', 80)
    game_image = title_font.render('G a m e', True, (0, 51, 51))
    over_image = title_font.render('O v e r', True, (0, 51, 51))
    game_rect = game_image.get_rect()
    over_rect = over_image.get_rect()
    screen_rect = screen.get_rect()
    game_rect.midtop = (ai_settings.screen_width / 2, screen_rect.top + 70)
    over_rect.midtop = (ai_settings.screen_width / 2, game_rect.bottom + 50)
    screen.blit(game_image, game_rect)
    screen.blit(over_image, over_rect)
    pygame.display.flip()
    # 将得分情况写入txt文件
    if ai_settings.score != 0 and ai_settings.length != 0:
        with open('游戏得分统计.txt', 'a', encoding='utf-8-sig') as f:
            f.write('%d %d'%(ai_settings.score,ai_settings.length))
            if ai_settings.score / ai_settings.length == 5:
                f.write(' 1\n')
            elif ai_settings.score / ai_settings.length == 50:
                f.write(' 3\n')
            else:
                f.write(' 2\n')
    # 结束页维持一段时间后，返回启动页，通过修改ai_settings中的game_stats实现
    pygame.time.wait(2000)
    ai_settings.game_stats = 0


# 在游戏界面上绘制格子
def draw_grid(ai_settings, screen):
    # 绘制横向线
    for x in range(0, ai_settings.screen_width, ai_settings.cell_size):
        pygame.draw.line(screen, (255,204,204), (x, 0), (x, ai_settings.screen_height))
    # 绘制竖向线
    for y in range(0, ai_settings.screen_height, ai_settings.cell_size):
        pygame.draw.line(screen, (255,204,204), (0, y), (ai_settings.screen_width, y))


def update_screen(ai_settings, screen):
    screen.fill(ai_settings.bg_color)
    draw_grid(ai_settings, screen)


# 绘制蛇
def draw_snake(ai_settings, screen, snake):
    # 头部用蓝色
    x = snake.coords[0]['x'] * ai_settings.cell_size
    y = snake.coords[0]['y'] * ai_settings.cell_size
    snake_head_rect = pygame.Rect(x, y, ai_settings.cell_size, ai_settings.cell_size)
    pygame.draw.rect(screen, (0, 0, 255), snake_head_rect)
    # 蛇身内部用浅绿，外框用深绿
    for coord in snake.coords[1: -1]:
        x = coord['x'] * ai_settings.cell_size
        y = coord['y'] * ai_settings.cell_size
        snake_part_rect = pygame.Rect(x, y, ai_settings.cell_size, ai_settings.cell_size)
        pygame.draw.rect(screen, (0, 155, 0), snake_part_rect)
        snake_part_inner_rect = pygame.Rect(x + 4, y + 4, ai_settings.cell_size - 8, ai_settings.cell_size - 8)
        pygame.draw.rect(screen, (0, 255, 0), snake_part_inner_rect)
    # 蛇尾用浅绿
    coord = snake.coords[-1]
    x = coord['x'] * ai_settings.cell_size
    y = coord['y'] * ai_settings.cell_size
    snake_tail_rect = pygame.Rect(x, y, ai_settings.cell_size, ai_settings.cell_size)
    pygame.draw.rect(screen, (0, 255, 0), snake_tail_rect)


# 绘制游戏界面
def update_screen(ai_settings, screen, snake):
    screen.fill(ai_settings.bg_color)

    draw_grid(ai_settings, screen)
    draw_snake(ai_settings, screen, snake)

    # 移动蛇
    del snake.coords[-1]  # 加蛇头
    snake.update()  # 去蛇尾
    pygame.display.flip()

    # 暂停一下
    ai_settings.my_clock.tick(ai_settings.clock_frq)

#检测游戏过程中的按键
def check_play_events(snake):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
			elif event.key == pygame.K_LEFT and not snake.direction == 'right':
				snake.direction = 'left'
			elif event.key == pygame.K_RIGHT and not snake.direction == 'left':
				snake.direction = 'right'
			elif event.key == pygame.K_UP and not snake.direction == 'down':
				snake.direction = 'up'
			elif event.key == pygame.K_DOWN and not snake.direction == 'up':
				snake.direction = 'down'


def update_screen(ai_settings, screen, snake):
    screen.fill(ai_settings.bg_color)
    draw_grid(ai_settings, screen)
    screen.blit(scores_image, (0, 0))
    # 移动蛇
    del snake.coords[-1]  # 加蛇头
    snake.update()  # 去蛇尾
    if not is_game_over(ai_settings, snake):
        ai_settings.game_stats = -1
    else:
        draw_snake(ai_settings, screen, snake)
        pygame.display.flip()
        # 暂停一下
        ai_settings.my_clock.tick(ai_settings.clock_frq)


def is_game_over(ai_settings, snake):
    # 碰到左右墙壁
    if (snake.coords[snake.head_index]['x'] == -1 or snake.coords[snake.head_index]['x'] == ai_settings.cell_w):
        return False
    # 碰到上下墙壁
    if (snake.coords[snake.head_index]['y'] == -1 or snake.coords[snake.head_index]['y'] == ai_settings.cell_h):
        return False
    # 碰到自己
    if (snake.coords[snake.head_index] in snake.coords[1:]):
        return False
    return True


# 绘制食物
def draw_food(ai_settings, screen, food):
    x = food.coord['x'] * ai_settings.cell_size
    y = food.coord['y'] * ai_settings.cell_size
    food_rect = pygame.Rect(x, y, ai_settings.cell_size, ai_settings.cell_size)
    # 将食物的位置涂成红色
    pygame.draw.rect(screen, (255, 0, 0), food_rect)

# 是否吃到食物
def is_eat_food(ai_settings, snake, food):
    # 当蛇头在食物处，吃到食物，更新食物位置
    if snake.coords[snake.head_index] == food.coord:
        food.update(ai_settings, snake)
        ai_settings.length += 1
        if ai_settings.game_stats == 1:
            ai_settings.score += 5
        elif ai_settings.game_stats == 2:
            ai_settings.score += 10
        elif ai_settings.game_stats == 3:
            ai_settings.score += 50
        else:
            ai_settings.score += 1
        return True
    return False


# 绘制游戏界面
def update_screen(ai_settings, screen, snake,food):
    scores_font = pygame.font.Font("../font/STKAITI.TTF", 30 )
    scores_image = scores_font.render(u"当前得分: %d "% ai_settings.score , True, (0,51,51))
    length_font = pygame.font.Font("../font/STKAITI.TTF", 30 )
    length_image = length_font.render(u"蛇身长度: %d "% ai_settings.length , True, (0,51,51))
    screen.fill(ai_settings.bg_color)
    draw_grid(ai_settings, screen)
    screen.blit(scores_image, (10, 10))
    screen.blit(length_image,(600, 10))
    # 移动蛇
    flag = is_eat_food(ai_settings, snake, food)
    if not flag:
        del snake.coords[-1]
    snake.update()
    if not is_game_over(ai_settings, snake):
        ai_settings.game_stats = -1
    else:
        draw_snake(ai_settings, screen, snake)
        draw_food(ai_settings, screen, food)
        pygame.display.flip()
        # 暂停一下
        ai_settings.my_clock.tick(ai_settings.clock_frq)



# 检测排行榜的键盘操作
def check_list_events(ai_settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_1:
                ai_settings.game_stats = 0

# 从txt文件中读取排行榜数据
def read_list_txt(file_name, list_mode1, list_mode2, list_mode3):
    """
    file_name: 读取的txt文件名
    list_mode1: 难度1排行榜
    list_mode2: 难度2排行榜
    list_mode3: 难度3排行榜
    :return: list_mode1, list_mode2, list_mode3

    """
    # 读取原始数据
    with open(file_name, 'r', encoding='utf-8-sig') as f:
        content = f.readlines()[1:]
    list_data = []
    game_mode1 = []
    game_mode2 = []
    game_mode3 = []
    for line in content:
        list_data.append(line.strip('\n').split(' '))
    for i in range(len(list_data)):
        if list_data[i][-1] == '1':
            for j in range(3):
                list_data[i][j] = int(list_data[i][j])
            game_mode1.append(list_data[i])
        elif list_data[i][-1] == '2':
            for j in range(3):
                list_data[i][j] = int(list_data[i][j])
            game_mode2.append(list_data[i])
        else:
            for j in range(3):
                list_data[i][j] = int(list_data[i][j])
            game_mode3.append(list_data[i])
    # 去除重复数据
    game_mode1 = list(set(tuple(i) for i in game_mode1))
    game_mode2 = list(set(tuple(i) for i in game_mode2))
    game_mode3 = list(set(tuple(i) for i in game_mode3))
    # 排序
    game_mode1.sort()
    game_mode2.sort()
    game_mode3.sort()
    # 将排行数据放入列表
    for i in range(5):
        list_mode1[i] = ("NO.%d     %d" % (i + 1, game_mode1[-i - 1][0]))
        list_mode2[i] = ("NO.%d     %d" % (i + 1, game_mode2[-i - 1][0]))
        list_mode3[i] = ("NO.%d     %d" % (i + 1, game_mode3[-i - 1][0]))

    return list_mode1, list_mode2, list_mode3



# 绘制排行榜
def show_list(ai_settings,screen):
    排 = pygame.image.load('../image/排.png')
    行 = pygame.image.load('../image/行.png')
    榜 = pygame.image.load('../image/榜.png')
    background = pygame.image.load(r"../image/排行榜.jpg")
    font1 = pygame.font.Font("../font/STKAITI.TTF", 35)
    image1 = font1.render('按 1 返回主界面', True, (0, 0, 0))

    # 读取排行榜数据
    l1 = [0] * 5
    l2 = [0] * 5
    l3 = [0] * 5
    read_list_txt('游戏得分统计.txt', l1, l2, l3)

    while True:
        screen.fill(ai_settings.bg_color)    # 绘制屏幕
        screen.blit(background, (0, 0))     #背景图
        screen.blit(排, (50, 30))
        screen.blit(行, (310, 30))
        screen.blit(榜, (590, 30))
        screen.blit(image1, (400 ,500))
        screen.blit(pygame.font.Font('../font/STKAITI.TTF',35).render('↓  难度1  ↓', True, (0, 0, 0)),(50, 200))
        screen.blit(pygame.font.Font('../font/STKAITI.TTF', 35).render('↓  难度2  ↓', True, (0, 0, 0)), (310, 200))
        screen.blit(pygame.font.Font('../font/STKAITI.TTF', 35).render('↓  难度3  ↓', True, (0, 0, 0)), (560, 200))
        for i in range(5):
            screen.blit(pygame.font.Font('../font/STKAITI.TTF', 25).render(l1[i], True, (0, 0, 0)), (80 ,263 + i * 37))
        for i in range(5):
            screen.blit(pygame.font.Font('../font/STKAITI.TTF', 25).render(l2[i], True, (0, 0, 0)), (340 ,263 + i * 37))
        for i in range(5):
            screen.blit(pygame.font.Font('../font/STKAITI.TTF', 25).render(l3[i], True, (0, 0, 0)), (600, 263 + i * 37))

        check_list_events(ai_settings)  # 检测键盘
        if ai_settings.game_stats == 0:
            break
        pygame.display.flip()

# /* ----------AI版实现-------------*/
# /*-----------基于BFS--------------*/

# 显示当前得分
def Show_Score(ai_settings,score):
	score_Content = Main_Font.render('当前长度：%s' % (score), True, (0, 0, 0))
	score_Rect = score_Content.get_rect()
	score_Rect.topleft = (ai_settings.screen_width-120, 10)
	Main_Display.blit(score_Content, score_Rect)


# 获得果实位置
def Get_Apple_Location(ai_settings, snake_Coords):
	flag = True
	while flag:
		apple_location = {'x': random.randint(0, ai_settings.cell_w-1), 'y': random.randint(0, ai_settings.cell_h-1)}
		if apple_location not in snake_Coords:
			flag = False
	return apple_location


# 显示果实
def Show_Apple(ai_settings,coord):
	x = coord['x'] * ai_settings.cell_size
	y = coord['y'] * ai_settings.cell_size
	apple_Rect = pygame.Rect(x, y, ai_settings.cell_size, ai_settings.cell_size)
	pygame.draw.rect(Main_Display, (255, 0, 0), apple_Rect)


# 显示蛇
def Show_Snake(ai_settings,coords):
	x = coords[0]['x'] * ai_settings.cell_size
	y = coords[0]['y'] * ai_settings.cell_size
	Snake_head_Rect = pygame.Rect(x, y, ai_settings.cell_size, ai_settings.cell_size)
	pygame.draw.rect(Main_Display, (0, 80, 255), Snake_head_Rect)
	Snake_head_Inner_Rect = pygame.Rect(x+4, y+4, ai_settings.cell_size-8, ai_settings.cell_size-8)
	pygame.draw.rect(Main_Display, (0, 80, 255), Snake_head_Inner_Rect)
	for coord in coords[1:]:
		x = coord['x'] * ai_settings.cell_size
		y = coord['y'] * ai_settings.cell_size
		Snake_part_Rect = pygame.Rect(x, y, ai_settings.cell_size, ai_settings.cell_size)
		pygame.draw.rect(Main_Display, (0, 155, 0), Snake_part_Rect)
		Snake_part_Inner_Rect = pygame.Rect(x+4, y+4, ai_settings.cell_size-8, ai_settings.cell_size-8)
		pygame.draw.rect(Main_Display, (0, 255, 0), Snake_part_Inner_Rect)


# 画网格
def draw_Grid(ai_settings):
	# 垂直方向
	for x in range(0, ai_settings.screen_width, ai_settings.cell_size):
		pygame.draw.line(Main_Display, (255, 204, 204), (x, 0), (x, ai_settings.screen_height))
	# 水平方向
	for y in range(0, ai_settings.screen_height, ai_settings.cell_size):
		pygame.draw.line(Main_Display, (255, 204, 204), (0, y), (ai_settings.screen_width, y))


# 判断该位置是否为空
def Is_Cell_Free(ai_settings,idx, psnake):
	location_x = idx % ai_settings.cell_w
	location_y = idx // ai_settings.cell_w
	idx = {'x': location_x, 'y': location_y}
	return (idx not in psnake)


# 重置board
def board_reset(ai_settings,psnake, pboard, pfood):
	temp_board = pboard[:]
	pfood_idx = pfood['x'] + pfood['y'] * ai_settings.cell_w
	for i in range(ai_settings.num):
		if i == pfood_idx:
			temp_board[i] = 0
		elif Is_Cell_Free(ai_settings,i, psnake):
			temp_board[i] = ai_settings.free_place
		else:
			temp_board[i] = ai_settings.snake_place
	return temp_board


# 检查位置idx是否可以向当前move方向运动
def is_move_possible(ai_settings, idx, move_direction):
	flag = False
	if move_direction == 'left':
		if idx%ai_settings.cell_w > 0:
			flag = True
		else:
			flag = False
	elif move_direction == 'right':
		if idx%ai_settings.cell_w < ai_settings.cell_w-1:
			flag = True
		else:
			flag = False
	elif move_direction == 'up':
		if idx > ai_settings.cell_w-1:
			flag = True
		else:
			flag = False
	elif move_direction == 'down':
		if idx < ai_settings.num - ai_settings.cell_w:
			flag = True
		else:
			flag = False
	return flag


# 广度优先搜索遍历整个board
# 计算出board中每个非SNAKE_PLACE元素到达食物的路径长度
def board_refresh(ai_settings, psnake, pfood, pboard):
	temp_board = pboard[:]
	pfood_idx = pfood['x'] + pfood['y'] * ai_settings.cell_w
	queue = []
	queue.append(pfood_idx)
	inqueue = [0] * ai_settings.num
	found = False
	while len(queue) != 0:
		idx = queue.pop(0)
		if inqueue[idx] == 1:
			continue
		inqueue[idx] = 1
		for move_direction in ['left', 'right', 'up', 'down']:
			if is_move_possible(ai_settings, idx, move_direction):
				if (idx+ai_settings.move_directions[move_direction]) == (psnake[ai_settings.Head_index]['x'] + psnake[ai_settings.Head_index]['y']*ai_settings.cell_w):
					found = True
				# 该点不是蛇身(食物是0才可以这样子写)
				if temp_board[idx+ai_settings.move_directions[move_direction]] < ai_settings.snake_place:
					if temp_board[idx+ai_settings.move_directions[move_direction]] > temp_board[idx]+1:
						temp_board[idx+ai_settings.move_directions[move_direction]] = temp_board[idx] + 1
					if inqueue[idx+ai_settings.move_directions[move_direction]] == 0:
						queue.append(idx+ai_settings.move_directions[move_direction])
	return (found, temp_board)


# 根据board中元素值
# 从蛇头周围4个领域点中选择最短路径
def choose_shortest_safe_move(ai_settings,psnake, pboard):
	best_move = ai_settings.ERR
	min_distance = ai_settings.snake_place
	for move_direction in ['left', 'right', 'up', 'down']:
		idx = psnake[ai_settings.Head_index]['x'] + psnake[ai_settings.Head_index]['y']*ai_settings.cell_w
		if is_move_possible(ai_settings,idx, move_direction) and (pboard[idx+ai_settings.move_directions[move_direction]]<min_distance):
			min_distance = pboard[idx+ai_settings.move_directions[move_direction]]
			best_move = move_direction
	return best_move


# 找到移动后蛇头的位置
def find_snake_head(ai_settings,snake_Coords, direction):
	if direction == 'up':
		newHead = {'x': snake_Coords[ai_settings.Head_index]['x'],
				   'y': snake_Coords[ai_settings.Head_index]['y']-1}
	elif direction == 'down':
		newHead = {'x': snake_Coords[ai_settings.Head_index]['x'],
				   'y': snake_Coords[ai_settings.Head_index]['y']+1}
	elif direction == 'left':
		newHead = {'x': snake_Coords[ai_settings.Head_index]['x']-1,
				   'y': snake_Coords[ai_settings.Head_index]['y']}
	elif direction == 'right':
		newHead = {'x': snake_Coords[ai_settings.Head_index]['x']+1,
				   'y': snake_Coords[ai_settings.Head_index]['y']}
	return newHead


# 虚拟地运行一次
def virtual_move(ai_settings,psnake, pboard, pfood):
	temp_snake = psnake[:]
	temp_board = pboard[:]
	reset_tboard = board_reset(ai_settings,temp_snake, temp_board, pfood)
	temp_board = reset_tboard
	food_eated = False
	while not food_eated:
		refresh_tboard = board_refresh(ai_settings,temp_snake, pfood, temp_board)[1]
		temp_board = refresh_tboard
		move_direction = choose_shortest_safe_move(ai_settings,temp_snake, temp_board)
		snake_Coords = temp_snake[:]
		temp_snake.insert(0, find_snake_head(ai_settings,snake_Coords, move_direction))
		# 如果新的蛇头正好是食物的位置
		if temp_snake[ai_settings.Head_index] == pfood:
			reset_tboard = board_reset(ai_settings, temp_snake, temp_board, pfood)
			temp_board = reset_tboard
			pfood_idx = pfood['x'] + pfood['y'] * ai_settings.cell_w
			temp_board[pfood_idx] = ai_settings.snake_place
			food_eated = True
		else:
			newHead_idx = temp_snake[0]['x'] + temp_snake[0]['y'] * ai_settings.cell_w
			temp_board[newHead_idx] = ai_settings.snake_place
			end_idx = temp_snake[-1]['x'] + temp_snake[-1]['y'] * ai_settings.cell_w
			temp_board[end_idx] = ai_settings.free_place
			del temp_snake[-1]
	return temp_snake, temp_board


# 检查蛇头和蛇尾间是有路径的
# 避免蛇陷入死路
def is_tail_inside(ai_settings,psnake, pboard, pfood):
	temp_board = pboard[:]
	temp_snake = psnake[:]
	# 将蛇尾看作食物
	end_idx = temp_snake[-1]['x'] + temp_snake[-1]['y'] * ai_settings.cell_w
	temp_board[end_idx] = 0
	v_food = temp_snake[-1]
	# 食物看作蛇身(重复赋值了)
	pfood_idx = pfood['x'] + pfood['y'] * ai_settings.cell_w
	temp_board[pfood_idx] = ai_settings.snake_place
	# 求得每个位置到蛇尾的路径长度
	result, refresh_tboard = board_refresh(ai_settings,temp_snake, v_food, temp_board)
	temp_board = refresh_tboard
	for move_direction in ['left', 'right', 'up', 'down']:
		idx = temp_snake[ai_settings.Head_index]['x'] + temp_snake[ai_settings.Head_index]['y']*ai_settings.cell_w
		end_idx = temp_snake[-1]['x'] + temp_snake[-1]['y']*ai_settings.cell_w
		if is_move_possible(ai_settings,idx, move_direction) and (idx+ai_settings.move_directions[move_direction] == end_idx) and (len(temp_snake)>3):
			result = False
	return result


# 根据board中元素值
# 从蛇头周围4个领域点中选择最远路径
def choose_longest_safe_move(ai_settings,psnake, pboard):
	best_move = ai_settings.ERR
	max_distance = -1
	for move_direction in ['left', 'right', 'up', 'down']:
		idx = psnake[ai_settings.Head_index]['x'] + psnake[ai_settings.Head_index]['y']*ai_settings.cell_w
		if is_move_possible(ai_settings,idx, move_direction) and (pboard[idx+ai_settings.move_directions[move_direction]]>max_distance) and (pboard[idx+ai_settings.move_directions[move_direction]]<ai_settings.free_place):
			max_distance = pboard[idx+ai_settings.move_directions[move_direction]]
			best_move = move_direction
	return best_move


# 让蛇头朝着蛇尾运行一步
def follow_tail(ai_settings,psnake, pboard, pfood):
	temp_snake = psnake[:]
	temp_board = board_reset(ai_settings,temp_snake, pboard, pfood)
	# 将蛇尾看作食物
	end_idx = temp_snake[-1]['x'] + temp_snake[-1]['y'] * ai_settings.cell_w
	temp_board[end_idx] = 0
	v_food = temp_snake[-1]
	# 食物看作蛇身
	pfood_idx = pfood['x'] + pfood['y'] * ai_settings.cell_w
	temp_board[pfood_idx] = ai_settings.snake_place
	# 求得每个位置到蛇尾的路径长度
	result, refresh_tboard = board_refresh(ai_settings,temp_snake, v_food, temp_board)
	temp_board = refresh_tboard
	# 还原
	temp_board[end_idx] = ai_settings.snake_place
	# temp_board[pfood_idx] = FOOD
	return choose_longest_safe_move(ai_settings,temp_snake, temp_board)


# 如果蛇和食物间有路径
# 则需要找一条安全的路径
def find_safe_way(ai_settings,psnake, pboard, pfood):
	safe_move = ai_settings.ERR
	real_snake = psnake[:]
	real_board = pboard[:]
	v_psnake, v_pboard = virtual_move(ai_settings,psnake, pboard, pfood)
	# 如果虚拟运行后，蛇头蛇尾间有通路，则选最短路运行
	if is_tail_inside(ai_settings,v_psnake, v_pboard, pfood):
		safe_move = choose_shortest_safe_move(ai_settings,real_snake, real_board)
	else:
		safe_move = follow_tail(ai_settings,real_snake, real_board, pfood)
	return safe_move


# 各种方案均无效时，随便走一步
def any_possible_move(ai_settings,psnake, pboard, pfood):
	best_move = ai_settings.ERR
	reset_board = board_reset(ai_settings,psnake, pboard, pfood)
	pboard = reset_board
	result, refresh_board = board_refresh(ai_settings,psnake, pfood, pboard)
	pboard = refresh_board
	min_distance = ai_settings.snake_place
	for move_direction in ['left', 'right', 'up', 'down']:
		idx = psnake[ai_settings.Head_index]['x'] + psnake[ai_settings.Head_index]['y']*ai_settings.cell_w
		if is_move_possible(ai_settings,idx, move_direction) and (pboard[idx+ai_settings.move_directions[move_direction]]<min_distance):
			min_distance = pboard[idx+ai_settings.move_directions[move_direction]]
			best_move = move_direction
	return best_move

def run_game_ai(ai_settings):
    pygame.display.set_caption('贪吃蛇-AI')
    global Main_Display, Main_Font, Snake_Clock
    Snake_Clock = pygame.time.Clock()
    Main_Display = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    Main_Font = pygame.font.Font('../font/STKAITI.TTF', 18)

    # 一维数组来表示蛇运动的矩形场地
    board = [0] * ai_settings.num
    # 蛇出生地
    start_x = random.randint(5, ai_settings.cell_w - 6)
    start_y = random.randint(5, ai_settings.cell_h - 6)
    snake_Coords = [{'x': start_x, 'y': start_y},
                    {'x': start_x - 1, 'y': start_y},
                    {'x': start_x - 2, 'y': start_y}]
    apple_location = Get_Apple_Location(ai_settings,snake_Coords)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        Main_Display.fill(ai_settings.bg_color)
        draw_Grid(ai_settings)
        Show_Snake(ai_settings,snake_Coords)
        Show_Apple(ai_settings,apple_location)
        Show_Score(ai_settings,len(snake_Coords) - 3)
        # 重置board
        reset_board = board_reset(ai_settings,snake_Coords, board, apple_location)
        board = reset_board
        result, refresh_board = board_refresh(ai_settings,snake_Coords, apple_location, board)
        board = refresh_board
        # 如果蛇可以吃到食物
        if result:
            best_move = find_safe_way(ai_settings,snake_Coords, board, apple_location)
        else:
            best_move = follow_tail(ai_settings,snake_Coords, board, apple_location)
        if best_move == ai_settings.ERR:
            best_move = any_possible_move(ai_settings,snake_Coords, board, apple_location)
        if best_move != ai_settings.ERR:
            newHead = find_snake_head(ai_settings,snake_Coords, best_move)
            snake_Coords.insert(0, newHead)
            head_idx = snake_Coords[ai_settings.Head_index]['x'] + snake_Coords[ai_settings.Head_index]['y'] * ai_settings.cell_w
            end_idx = snake_Coords[-1]['x'] + snake_Coords[-1]['y'] * ai_settings.cell_w
            if (snake_Coords[ai_settings.Head_index]['x'] == apple_location['x']) and (snake_Coords[ai_settings.Head_index]['y'] == apple_location['y']):
                board[head_idx] = ai_settings.snake_place
                if len(snake_Coords) < ai_settings.num:
                    apple_location = Get_Apple_Location(ai_settings,snake_Coords)
            else:
                board[head_idx] = ai_settings.snake_place
                board[end_idx] = ai_settings.free_place
                del snake_Coords[-1]
        else:
            return
        pygame.display.update()
        Snake_Clock.tick(ai_settings.display_clock)