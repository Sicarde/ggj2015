#! /usr/bin/python2
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *


pygame.init()
fenetre = pygame.display.set_mode((300,300))

#On compte les joysticks
nb_joysticks = pygame.joystick.get_count()
#Et on en cree un s'il y a en au moins un
if nb_joysticks > 0:
    mon_joystick = pygame.joystick.Joystick(0)

    mon_joystick.init()

    #On compte les boutons
    nb_boutons = mon_joystick.get_numaxes()
    if nb_boutons >= 4:
        
        continuer = 1
        while continuer:
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
            
                if event.type == JOYAXISMOTION:
                    if event.axis == 0 and event.value > 0:
                        print("lol")
                    if event.axis == 0 and event.value < 0:
                        print("ta mere")
                    if event.axis == 1 and event.value > 0:
                        print("franck_r")
                    if event.axis ==1 and event.value < 0:
                        print("miest_l")
    else:
        print("Votre Joystick ne possede pas au moins 4 boutons")
else:
    print("ta mere")
