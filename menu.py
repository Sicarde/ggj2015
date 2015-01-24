#! /usr/bin/python2                                                                                                                                                                          # -*- coding: utf-8 -*-


import pygame
from pygame.locals import *

pygame.joystick.init()

taille = hauteur, largeur = 1920, 1080

fenetre = pygame.display.set_mode(taille)

menu_c = 1
menu = pygame.image.load("super_menu.png").convert()
new_rec = pygame.image.load("hand.png").convert_alpha()
merci = pygame.image.load("OPTION.png").convert()

position_new_rec = new_rec.get_rect()
position_new_rec.x = 650
position_new_rec.y = 100
fenetre.blit(menu, (0,0))
fenetre.blit(new_rec, position_new_rec)
while menu_c == 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            menu_c = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                position_new_rec.y = position_new_rec.y + 80
                if position_new_rec.y >= 420:
                    position_new_rec.y = 100
            if event.key == K_UP:
                position_new_rec.y = position_new_rec.y - 80
                if position_new_rec.y <= 20:
                    position_new_rec.y = 340
            if position_new_rec.y == 100 and event.key == K_SPACE:
                menu_c = 0
            if position_new_rec.y == 260 and event.key == K_SPACE:
                while menu_c == 1:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            menu_c = 0
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                fenetre.blit(menu, (0,0))
                                pygame.display.flip()
                                menu_c = 0
                        fenetre.blit(merci, (0,0))
                        pygame.display.flip()
                menu_c = 1
            if position_new_rec.y == 340 and event.key == K_SPACE:
                exit(0)

    fenetre.blit(menu, (0,0))
    fenetre.blit(new_rec, position_new_rec)
    pygame.display.flip()

fond = pygame.image.load("Purple-planet-meteors-in-space_1920x1200.jpg").convert()
fenetre.blit(fond, (0,0))

block1bas = pygame.image.load("block1bas.png").convert_alpha()
block1bas2 = pygame.image.load("block1bas.png").convert_alpha()
block1bas3 = pygame.image.load("block1bas.png").convert_alpha()
block1bas4 = pygame.image.load("block1bas.png").convert_alpha()

position_block1bas = block1bas.get_rect()
position_block1bas.x = 200
position_block1bas.y = 200

position_block1bas2 = block1bas2.get_rect()
position_block1bas2.x = 300
position_block1bas2.y = 300

position_block1bas3 = block1bas3.get_rect()
position_block1bas3.x = 400
position_block1bas3.y = 400

position_block1bas4 = block1bas4.get_rect()
position_block1bas4.x = 500
position_block1bas4.y = 500

fenetre.blit(block1bas, position_block1bas)
fenetre.blit(block1bas2, position_block1bas2)
fenetre.blit(block1bas3, position_block1bas3)
fenetre.blit(block1bas4, position_block1bas4)

pygame.display.flip()

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continuer = 0

    fenetre.blit(fond, (0,0))
    fenetre.blit(block1bas, position_block1bas)
    fenetre.blit(block1bas2, position_block1bas2)
    fenetre.blit(block1bas3, position_block1bas3)
    fenetre.blit(block1bas4, position_block1bas4)
    
    pygame.display.flip()
