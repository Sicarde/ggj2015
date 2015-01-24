#! /usr/bin/python2                                                                                                                                                                          # -*- coding: utf-8 -*-

import random
import pygame
import sys
import time
import math
from math import exp, expm1
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


spc = 0.01

class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        tmp = pygame.Surface((32, 32))
        self.images = []
        self.rect = Rect(100, 100, 32, 32)
        plop = pygame.image.load("img/Perso/red.png").convert_alpha()
        tmp.blit(plop, (0, 0), (0, 0, 32, 32))
        self.images.append(tmp)
        tmp = pygame.Surface((32, 32))
        plop = pygame.image.load("block1bas.png").convert_alpha()
        tmp.blit(plop, (0, 0), (0, 0, 32, 32))
        self.images.append(tmp)
        # assuming both images are 64x64 pixels
        self.index = 0
        self.image = self.images[self.index]
    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

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
        self.Sprite = TestSprite()
    def takeProof(self, proof):
        proof.isPrinted = false
    def putProof(self, proof):
        proof.pos = self.pos
        proof.isPrinted = True
        proof = None
    def draw(self, fenetre):
        self.Sprite.update()
        self.Sprite.rect.x = self.pos.x * 32
        self.Sprite.rect.y = self.pos.y * 32
        fenetre.blit(self.Sprite.image, self.Sprite.rect)

class Node():
    weigth = 50
    def __cmp__ (self, other):
        return cmp(self.weigth, other.weigth)
    def __init__(self, x, y, nodeList):
        self.pos = Position(x, y)
        self.nodeList = nodeList
        for node in nodeList:
            node.nodeList.append(self)
    def append(self, node):
        self.nodeList.append(node)
        node.nodeList.append(self)

def onVaMangerDesChips(node, weigth):
    node.weigth = weigth
    for n in node.nodeList:
        if (weigth < n.weigth):
            onVaMangerDesChips(n, weigth + 1)

def clean(nlist):
    for n in nlist:
        n.weigth = 50

def testlist(nodelist):
    node = nodelist[0]
    for n in nodelist:
        if (node.weigth != n.weigth):
            return 1
    return 0

random.seed()

class inspectorPedro():
    direction = None
    #direction = { UP, DOWN, LEFT, RIGHT ]
    checkingPlayer = None
    goToRoom = 0
    room = 0
    moving = 0
    #room = { IDLE, GET OUT, RED, GREEN, ORANGE, PURP ] (7931)
    def __init__(self, node):
        self.node = node
        self.direction = node
        self.pos = node.pos
    def move(self, fenetre, players):
        if ((round(self.pos.x) == round(self.direction.pos.x)) and (round(self.pos.y) == round(self.direction.pos.y))):
            self.direction = min(self.node.nodeList)
            self.node = self.direction
        else:
            lol = math.sqrt(pow(self.pos.x - self.direction.pos.x, 2) +  pow(self.pos.y - self.direction.pos.y, 2))
            vecteur = Position((self.pos.x - self.direction.pos.x) / lol, (self.pos.y - self.direction.pos.y) / lol)
            self.pos.x -= vecteur.x / 10
            self.pos.y -= vecteur.y / 10
        if (self.node.weigth == 0):
            clean(n)
            onVaMangerDesChips(n[random.randint(0, 51)], 0)
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
players = [Player()]
proofs = [Proof("block1bas.png"), Proof("block1bas.png")]
background = pygame.image.load("img/Map/map.png").convert_alpha()
menu_c = 1
menu = pygame.image.load("super_menu.png").convert()
new_rec = pygame.image.load("hand.png").convert_alpha()
merci = pygame.image.load("OPTION.png").convert()

n = [Node(19.0, 1.2, [])]
n.append(Node(19.0, 9.0, [n[0]]))
n.append(Node(19.0, 11.0, [n[1]]))
n.append(Node(12.0, 11.0, [n[2]]))
n.append(Node(10.0, 15.0, [n[3]]))

n.append(Node(12.0, 18.0, [n[4], n[3]]))
n.append(Node(13.5, 15.0, [n[2], n[3], n[4], n[5]]))
n.append(Node(19.0, 18.0, [n[5], n[6]]))
n.append(Node(27.0, 18.0, [n[7]]))
n.append(Node(25.5, 15.0, [n[8], n[7], n[2]]))

n.append(Node(27.0, 11.0, [n[9], n[2]]))
n.append(Node(29.0, 15.0, [n[10], n[9], n[8]]))
n.append(Node(12.0, 9.0, [n[3]]))
n.append(Node(11.0, 7.0, [n[12]]))
n.append(Node(12.0, 1.2, [n[13]]))

n.append(Node(5.0, 1.2, [n[14]]))
n.append(Node(5.0, 7.0, [n[15], n[13]]))
n.append(Node(6.0, 9.0, [n[16], n[13]]))
n.append(Node(6.0, 11.0, [n[17]]))
n.append(Node(8.0, 11.0, [n[18]]))

n.append(Node(8.0, 15.0, [n[19]]))
n.append(Node(8.0, 18.0, [n[20]]))
n.append(Node(1.0, 18.0, [n[21]]))
n.append(Node(1.0, 11.0, [n[22], n[18]]))
n.append(Node(27.0, 9.0, [n[10]]))

n.append(Node(28.0, 7.0, [n[24]]))
n.append(Node(27.0, 1.2, [n[25]]))
n.append(Node(34.0, 1.2, [n[26]]))
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
n.append(Node(27.0, 27.0, [n[38]]))

n.append(Node(25.0, 24.0, [n[39], n[36], n[35]]))
n.append(Node(23.0, 24.0, [n[40]]))
n.append(Node(20.0, 27.0, [n[41]]))
n.append(Node(16.0, 24.0, [n[42], n[41]]))
n.append(Node(19.0, 20.0, [n[43], n[42], n[41], n[7]]))

n.append(Node(14.0, 24.0, [n[43]]))
n.append(Node(11.0, 27.0, [n[45]]))
n.append(Node(5.0, 27.0, [n[46]]))
n.append(Node(5.0, 22.0, [n[47]]))
n.append(Node(10.0, 22.0, [n[48], n[45]]))

n.append(Node(12.0, 20.0, [n[45], n[49], n[5]]))
n.append(Node(19.0, 16.0, [n[7]]))

inspector = inspectorPedro(n[0])

onVaMangerDesChips(n[51], 0)

pygame.font.init()
    
speed = 2.5
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

while continuer:
    for event in pygame.event.get():
        if (event.type == QUIT):
            continuer = 0
        if (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                continuer = 0
            if (event.key == K_LEFT):
                if (lala[int(players[0].pos.y)][int(players[0].pos.x - spc)] != 1):
                    players[0].pos.x -= spc
            elif (event.key == K_RIGHT):
                if (lala[int(players[0].pos.y)][int(math.ceil((players[0].pos.x + spc)))] != 1):
                    players[0].pos.x += spc
            elif (event.key == K_UP):
                if (lala[int(players[0].pos.y - spc)][int(players[0].pos.x)] != 1):
                    players[0].pos.y -= spc
            elif (event.key == K_DOWN):
                if (lala[int(math.ceil((players[0].pos.y + spc)))][int(players[0].pos.x)] != 1):
                    players[0].pos.y += spc
    fenetre.fill((0, 0, 0))
    fenetre.blit(background, (0, 0))
    inspector.move(fenetre, players)
    for player in players:
        player.draw(fenetre)
    for proof in proofs:
        fenetre.blit(proof.image, Rect(proof.pos.x * 32, proof.pos.y * 32, 32, 32))
    time.sleep(spc)
#    for node in n:
#        basicfont = pygame.font.SysFont(None, 48)
#        text = basicfont.render(unicode(node.weigth), True, (255, 0, 0), (255, 255, 255))
#        textrect = text.get_rect()
#        textrect.centerx = node.pos.x * 32
#        textrect.centery = node.pos.y * 32
#        fenetre.blit(text, textrect)
    pygame.display.flip()
