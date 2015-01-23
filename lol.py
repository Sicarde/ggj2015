#! /usr/bin/python2                                                                                                                                                                          # -*- coding: utf-8 -*-


import pygame
from pygame.locals import *

taille = hauteur, largeur = 1920, 1080

fenetre = pygame.display.set_mode(taille)

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
        


fenetre.blit(block1bas, position_block1bas)
fenetre.blit(block1bas2, position_block1bas2)
fenetre.blit(block1bas3, position_block1bas3)
fenetre.blit(block1bas4, position_block1bas4)

pygame.display.flip()
