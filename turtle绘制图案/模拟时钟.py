# _*_ coding:utf-8 _*_
# Author:liu
import sys
import pygame
import math
import random
from pygame.locals import *
from datetime import datetime, date, time


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgtext = font.render(text, True, color)
    screen.blit(imgtext, (x, y))


def wrap_angle(angle):
    return abs(angle % 360)


# main
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("CLOCK")
font = pygame.font.Font(None, 36)
orange = 220, 180, 0
white = 255, 255, 255
yellow = 255, 255, 0
pink = 255, 100, 100

pos_x = 300
pos_y = 250
radius = 250
angle = 360

# repeating loop
in_y = math.sin(min_angle) * (radius - 60)
    target = (pos_x + min_x, pos_y + min_y)
    pygame.draw.line(screen, orange, (pos_x, pos_y), target, 12)

    # draw the seconds hand
    sec_angle = wrap_angle(seconds * (360 / 60) - 90)
    sec_angle = math.radians(sec_angle)
    sec_x = math.cos(sec_angle) * (radius - 40)
    sec_y = math.sin(sec_angle) * (radius - 40)
    target = (pos_x + sec_x, pos_y + sec_y)
    pygame.draw.line(screen, yellow, (pos_x, pos_y), target, 12)

    # draw the center
    pygame.draw.circle(screen, white, (pos_x, pos_y), 20)

    print_text(font, 0, 0, str(hours) + ":" + str(minutes) + ":" + str(seconds))
    pygame.display.update()
