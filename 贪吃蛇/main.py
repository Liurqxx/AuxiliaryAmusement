import pygame
from LinkList import *
import time
from random import randint
Box=pygame.image.load("Box.png")
Food=pygame.image.load("Food.png")
SnakeBar=pygame.image.load("Snake.png")

difficult=10
unit_edge=30
width,height=900,600
screen=pygame.display.set_mode((width,height))
snake=[[2,0],[1,0],[0,0]]
snake_last=[0,0]
direct=[0,0]
food_pos=[15,10]

def DrawSnake(screen,snake,image):

    for i in snake:
        screen.blit(image,[i[0]*30,i[1]*30])
    
def UpdateData(snake,direct):

    #print(snake)

    global snake_last
    snake_last=snake[len(snake)-1]
    last=snake.pop()
    x=snake[0][0];y=snake[0][1]
    x+=direct[0];y+=direct[1]
    new_pos=[x,y]
    snake.reverse()
    snake.append(new_pos)
    snake.reverse()
    


def GetValues():

    return [randint(1,29),randint(1,19)]

def CheckWorked(values,snake):

    global snake_last
    global food_pos

    for i in snake:
        if values==i:
            return False
    
    if values==food_pos:
        return False

    if values==snake_last:
        return False


    return True

def UpdateFood(snake):

    global food_pos
    pos=GetValues()
    if CheckWorked(pos,snake):

        food_pos=pos

def DrawFood(screen):

    global food_pos
    global Food

    screen.blit(Food,[food_pos[0]*30,food_pos[1]*30])

def EatFood(snake):

    global food_pos
    global difficult
    if snake[0]==food_pos:
        snake.append(snake_last)
        UpdateFood(snake)
        difficult+=3

def Die(snake):

    for i in range(len(snake)):
        try:
            if snake[0]==snake[i+1]:
                return True
        except IndexError:
            pass
    if snake[0][0]<0 or snake[0][0]>30 or snake[0][1]<0 or snake[0][1]>20:
        return True

timer=[time.time(),0]
running=1
while running:
    
    #time_passed_second = time_passed/1000.0
    screen.fill((255,255,255))
    for i in range(int(width/unit_edge)):
        for j in range(int(height/unit_edge)):
            screen.blit(Box,(i*30,j*30))
    DrawSnake(screen,snake,SnakeBar)
    
    timer[1]=time.time()
    if timer[1]-timer[0]>=10/difficult:
        if direct[0] or direct[1]:
            UpdateData(snake,direct)
        timer[0]=timer[1]
    DrawFood(screen)
    EatFood(snake)
    if Die(snake):
        running=0

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                direct=[0,-1]
            elif event.key==pygame.K_DOWN:
                direct=[0,1]
            elif event.key==pygame.K_LEFT:
                direct=[-1,0]
            elif event.key==pygame.K_RIGHT:
                direct=[1,0]