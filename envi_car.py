# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 16:15:34 2020

@author: karan
"""
import pygame as pg
import random
import numpy as np
pg.init()
running = True
#window size
width = 800
height = 600
screen = pg.display.set_mode((width,height))
#initializing images
carimg = pg.image.load('car.png')
rockimg = pg.image.load('landslide.png')
finishimg = pg.image.load('finish-line.png')
#positions
carx = 100
cary = 500
rockx = 400
rocky = 300
finishx = 700
finishy = 66
#count = 0
fp = 0
car_l=[(carx,cary)]


def car(carx,cary):
    screen.blit(carimg, (carx, cary))
    #count+=1
def rock():
    screen.blit(rockimg, (rockx, rocky))
    screen.blit(rockimg, (rockx+150, rocky+150))
def finishl():
    screen.blit(finishimg, (finishx, finishy))
def rand_choice(car_l, carx, cary):
    while((carx,cary) in car_l or carx < 0 or carx >800 or cary >600 or cary < 0 ):
        num1 = random.choice([-3, 0, 3])
        num2 = random.choice([-3, 0, 3])
        carx+=num1
        cary+=num2
    return carx,cary
def qtable(carx,cary,carx_new,cary_new,finishx,finishy,fp):
    if fp == 0:
        distance_old = np.sqrt((carx - finishx)**2 + (cary - finishy)**2)
        distance_new = np.sqrt((carx_new - finishx)**2 + (cary_new - finishy)**2)
        dif = distance_old - distance_new
        distance_old = distance_new
    else:
        distance_new = np.sqrt((carx_new - finishx)**2 + (cary_new - finishy)**2)
        dif = distance_old - distance_new
        distance_old = distance_new
    
    print(dif)

while running:
    carx_new,cary_new = rand_choice(car_l, carx, cary)
    (carx,cary) = car_l[-1]
    qtable(carx,cary,carx_new,cary_new,finishx,finishy,fp)
    fp += 1
    car_l.append((carx_new,cary_new))
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    car(carx_new,cary_new)        
    rock()
    finishl()
    pg.display.update()        
    