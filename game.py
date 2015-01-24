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

class Node(object):
    def __init__(self, x, y, nodeList):
        self.pos = Position(x, y)
        self.nodeList = nodeList
        i = 0
        while i < len(nodeList):
            nodeList[i].nodeList.append(self)
            i += 1
    def append(self, node):
        self.nodeList.append(node)
        node.nodeList.append(self)
        
class inspectorPedro():
    direction = 0
    #direction = { UP, DOWN, LEFT, RIGHT ]
    checkingPlayer = None
    goToRoom = 0
    room = 0
    #room = { IDLE, GET OUT, RED, GREEN, ORANGE, PURP ] (7931)
    def __init__(self):
        self.pos = Position(21.0, 2.0)
    def move(self, fenetre, players):
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
        
    def lookFor(self, player):
        if (player.proof != None):
            self.goToPlayerRoom()
            #tutulu UNE PREUVE
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
background = pygame.image.load("map.png").convert_alpha()


n = [Node(21.0, 2.0, None)]
n.append(Node(21.0, 9.0, [n[0]]))
n.append(Node(21.0, 11.0, [n[1]]))
n.append(Node(14.0, 11.0, [n[2]]))
n.append(Node(10.0, 15.0, [n[3]]))

n.append(Node(12.0, 18.0, [n[4], n[3]]))
n.append(Node(15.0, 15.0, [n[2], n[3], n[4], n[5]]))
n.append(Node(19.0, 18.0, [n[5], n[6]]))
n.append(Node(27.0, 18.0, [n[7]]))
n.append(Node(24.0, 15.0, [n[8], n[7], n[2]]))

n.append(Node(27.0, 11.0, [n[9], n[2]]))
n.append(Node(29.0, 15.0, [n[10], n[9], n[8]]))
n.append(Node(7.0, 9.0, [n[3]]))
n.append(Node(10.0, 7.0, [n[12]]))
n.append(Node(11.0, 3.0, [n[13]]))

n.append(Node(5.0, 3.0, [n[14]]))
n.append(Node(5.0, 7.0, [n[15], n[13]]))
n.append(Node(6.0, 9.0, [n[16], n[13]]))
n.append(Node(6.0, 11.0, [n[17]]))
n.append(Node(8.0, 11.0, [n[18]]))

n.append(Node(8.0, 15.0, [n[19]]))
n.append(Node(8.0, 18.0, [n[20]]))
n.append(Node(1.0, 18.0, [n[21]]))
n.append(Node(1.0, 11.0, [n[22], n[18]]))
n.append(Node(27.0, 9.0, [n[10]]))

n.append(Node(29.0, 7.0, [n[24]]))
n.append(Node(28.0, 3.0, [n[25]]))
n.append(Node(34.0, 3.0, [n[26]]))
n.append(Node(34.0, 7.0, [n[27], n[25]]))
n.append(Node(33.0, 9.0, [n[28], n[25]]))

n.append(Node(33.0, 11.0, [n[29]]))
n.append(Node(37.0, 13.0, [n[30]]))
n.append(Node(36.0, 18.0, [n[31]]))
n.append(Node(31.0, 18.0, [n[32]]))
n.append(Node(31.0, 15.0, [n[33], n[31], n[30], n[11]]))

n.append(Node(27.0, 20.0, [n[8]]))
n.append(Node(28.0, 22.0, [n[35]]))
n.append(Node(34.0, 22.0, [n[36]]))
n.append(Node(34.0, 27.0, [n[37]]))
n.append(Node(27.0, 27.0, [n[38], n[36]]))

n.append(Node(25.0, 24.0, [n[39], n[36], n[35]]))
n.append(Node(23.0, 24.0, [n[40]]))
n.append(Node(20.0, 27.0, [n[41]]))
n.append(Node(16.0, 24.0, [n[42], n[41]]))
n.append(Node(19.0, 20.0, [n[43], n[42], n[41], n[7]]))

n.append(Node(14.0, 24.0, [n[43]]))
n.append(Node(11.0, 27.0, [n[45]]))
n.append(Node(5.0, 27.0, [n[46]]))
n.append(Node(5.0, 22.0, [n[47]]))
n.append(Node(10.0, 22.0, [n[48], n[46], n[45]]))

n.append(Node(12.0, 20.0, [n[45], n[49], n[5]]))

while continuer:
    for event in pygame.event.get():
        if (event.type == QUIT):
            continuer = 0
        if (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                continuer = 0
    fenetre.fill((0, 0, 0))
    fenetre.blit(background, (0, 0))
    inspector.move(fenetre, players)
    for player in players:
        fenetre.blit(block1bas, Rect(player.pos.x * 32, player.pos.y * 32, 32, 32))
    for proof in proofs:
        fenetre.blit(proof.image, Rect(proof.pos.x * 32, proof.pos.y * 32, 32, 32))
    time.sleep(spc)
    pygame.display.flip()
