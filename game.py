#! /usr/bin/python2                                                                                                                                                                          # -*- coding: utf-8 -*-

import pygame
import time
from pygame.locals import *

lala = [ [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

spc = 0.5

class Position():
    x = 5.0
    y = 15.0
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Proof():
    image = None
    isPrinted = True
    def __init__(self, name):
        self.pos = Position(5.0, 5.0)
        self.image = pygame.image.load(name).convert_alpha()

class Player():
    color = "red"
    proof = None
    isPaused = False
    def __init__(self):
        self.pos = Position(5.0, 15.0)
    def takeProof(self, proof):
        proof.isPrinted = false
    def putProof(self, proof):
        proof.pos = self.pos
        proof.isPrinted = True
        proof = None

class inspectorPedro():
    direction = 0
    #direction = { UP, DOWN, LEFT, RIGHT }
    checkingPlayer = None
    goToRoom = False
    #room = { RED, GREEN, ORANGE, PURP } (7931)
    def __init__(self):
        self.pos = Position(21.0, 29.0)
    def move(self, fenetre, players):
        if (self.checkingPlayer != None):
            if (self.goToRoom == False):
                self.goNearPlayer()
                if ((self.checkingPlayer.pos.x - self.pos.x) > -1 and (self.checkingPlayer.pos.x - self.pos.x) < 1):
                    self.lookFor(self.checkingPlayer)
            else:
                self.goToPlayerRoom()
        else:
            if (self.direction == 0):
                if (lala[int(self.pos.y) - 1][int(self.pos.x)] == 1):
                    self.changeDirection()
                else:
                    self.pos.y -= spc
            elif (self.direction == 1):
                if (lala[int(self.pos.y) + 1][int(self.pos.x)] == 1):
                    self.changeDirection()
                else:
                    self.pos.y += spc
            elif (self.direction == 2):
                if (lala[int(self.pos.y)][int(self.pos.x) - 1] == 1):
                    self.changeDirection()
                else:
                    self.pos.x -= spc
            elif (self.direction == 0):
                if (lala[int(self.pos.y)][int(self.pos.x) + 1] == 1):
                    self.changeDirection()
                else:
                    self.pos.x += spc
            for player in players:
                #add walls here
                if ((player.pos.x - self.pos.x) > -2 and (player.pos.x - self.pos.x) < 2 and random.randint(0, 1) == 1):
                    player.isPaused = True
                    self.checkingPlayer = player
                    break
        fenetre.blit(block1bas, Rect(self.pos.x * 32, self.pos.y * 32, 32, 32))
    def goNearPlayer(self):
        if (not((self.checkingPlayer.pos.x - self.pos.x) > -1 and (self.checkingPlayer.pos.x - self.pos.x) < 1)):
            if (self.checkingPlayer.pos.x > self.pos.x):
                self.pos.x += spc
            else:
                self.pos.x += spc
        elif (not((self.checkingPlayer.pos.y - self.pos.y) > -1 and (self.checkingPlayer.pos.y - self.pos.y) < 1)):
            if (self.checkingPlayer.pos.y > self.pos.y):
                self.pos.y += spc
            else:
                self.pos.y += spc
    def changeDirection(self):
        if (self.direction == 0):
            self.direction = 1
        elif (self.direction == 1):
            self.direction = 0
        elif (self.direction == 2):
            self.direction = 3
        elif (self.direction == 3):
            self.direction = 2
    def goToCell(self, a, b):
        if ((a == self.pos.x) and (b == self.pos.y)):
            return 1
        if (abs(a - self.pos.x) > abs(b - self.pos.y)):
            if ((a - self.pos.x) > 0):
                self.direction = 2
            else:
                self.direction = 3
        else:
            if ((b - self.pos.y) > 0):
                self.direction = 1
            else:
                self.direction = 0
        return 0
    def getOutOfRoom(self):
        if ((self.pos.x == 12 and self.pos.y  == 9) or (self.pos.x == 19 and self.pos.y == 9) or (self.pos.x == 27 and self.pos.y == 9) or (self.pos.x == 8 and self.pos.y == 15) or (self.pos.x == 31 and self.pos.y == 15) or (self.pos.x == 12 and self.pos.y == 20) or (self.pos.x == 19 and self.pos.y == 20) or (self.pos.x == 27 and self.pos.y == 20)):
            return 19, 15
        elif (self.pos.y < 10):
            if (self.pos.x < 15):
                return 12, 9
            elif (self.pos.x < 24):
                return 19, 9
            else:
                return 27, 9
        elif (self.pos.y < 19):
            if (self.pos.x < 9):
                return 8, 15
            elif (self.pos.x < 24):
                return 19, 15
            else:
                return 31, 15
        else:
            if (self.pos.x < 15):
                return 12, 20
            elif (self.pos.x < 24):
                return 19, 20
            else:
                return 27, 20
    def goToPlayerRoom(self):
        if (self.checkingPlayer.color == "red"):
            printf("red")
        elif (self.checkingPlayer.color == "green"):
            print("green")
        elif (self.checkingPlayer.color == "orange"):
            print("orange")
        elif (self.checkingPlayer.color == "purple"):
            print("purple")
    def lookFor(self, player):
        if (player.proof != None):
            self.goToPlayerRoom()
            #tutulu UNE PREUVE HAHAHAHA LE JEU
            return
        else:
            player.isPaused = False

taille = hauteur, largeur = 1920, 1080

fenetre = pygame.display.set_mode(taille)

block1bas = pygame.image.load("block1bas.png").convert_alpha()

continuer = 1
inspector = inspectorPedro()
players = [Player()]
proofs = [Proof("block1bas.png"), Proof("block1bas.png")]
while continuer:
    for event in pygame.event.get():
        if (event.type == QUIT):
            continuer = 0
        if (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                continuer = 0
    fenetre.fill((0, 0, 0))
    inspector.move(fenetre, players)
    for player in players:
        fenetre.blit(block1bas, Rect(player.pos.x * 32, player.pos.y * 32, 32, 32))
    for proof in proofs:
        fenetre.blit(proof.image, Rect(proof.pos.x * 32, proof.pos.y * 32, 32, 32))
    time.sleep(spc)
    pygame.display.flip()
