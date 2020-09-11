import os, sys
import pygame
from pygame.locals import *
import move_it
import random
import numpy as np
from tkinter import messagebox
pygame.init()

size = width, heigh = 800, 600
back_color = 255, 255, 255
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)

k_b = pygame.image.load('knight_b2.png')
k_b = pygame.transform.smoothscale(k_b, (100, 100))
green = pygame.image.load('green.png')
red = pygame.image.load('red.png')

loc = [random.randint(0, 5), random.randint(0, 5)]
loc_ori = loc[:]
map = np.zeros(36).reshape(6, 6)
times = 0

pygame.display.set_caption('House')

done = False
do = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        map, loc, do, times = move_it.move(map, loc, do, times, event)

    screen.fill(back_color)
    for x in range(0, 6, 2):
        for y in range(0, 6, 2):
            pygame.draw.rect(screen, black, [x*100, y*100, 100, 100])
    for x in range(1, 6, 2):
        for y in range(1, 6, 2):
            pygame.draw.rect(screen, black, [x*100, y*100, 100, 100])


    [rows, cols] = map.shape
    for i in range(rows):
        for j in range(cols):
            if map[i, j] != 0:
                screen.blit(green, (i*100, j*100))

    screen.blit(red, (loc_ori[0]*100, loc_ori[1]*100))
    screen.blit(k_b, (loc[0]*100, loc[1]*100))
    pygame.display.flip()

    if do == True:
        if times < 36:
            messagebox.showinfo("FishC Demo","你走了{times}步, 加油!".format(times = times))
            done = True
        else:
            messagebox.showinfo("FishC Demo","你走了36步, 你真棒!")
            done = True