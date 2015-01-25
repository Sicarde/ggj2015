#! /usr/bin/python2                                                                                                                                                                          # -*- coding: utf-8 -*-

import random
import pygame
import sys
import time
import math
from math import exp, expm1
from pygame.locals import *
pygame.mixer.init()

lala = [ [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
         [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
         [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
         [ 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
         [ 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1 ],
         [ 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1 ],
         [ 1, 0, 0, 1, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 1 ],
         [ 1, 0, 0, 1, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 1 ],
         [ 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1 ],
         [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
         [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
         [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
         [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
         [ 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
         [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]


spc = 0.01

class TestSprite(pygame.sprite.Sprite):
    isPlaying = True
    def __init__(self, name):
        super(TestSprite, self).__init__()
        tmp = pygame.Surface((32, 32))
        self.images = []
        self.rect = Rect(100, 100, 32, 32)
        plop = pygame.image.load(name).convert_alpha()
        tmp.blit(plop, (0, 0), (0, 0, 32, 32))
        tmp.set_colorkey(0)
        self.images.append(tmp)
        tmp = pygame.Surface((32, 32))
        tmp.blit(plop, (0, 0), (32, 0, 32, 32))
        tmp.set_colorkey(0)
        self.images.append(tmp)
        self.index = 0
        self.image = self.images[self.index]
        self.start = time.time()
    def update(self):
        if (self.isPlaying == True):
            if (time.time() - self.start > 0.25):
                self.start = time.time()
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
    def pause(self):
        if (self.isPlaying == True):
            self.isPlaying = False
            self.index = 0
            self.image = self.images[self.index]
    def play(self):
        if (self.isPlaying == False):
            self.isPlaying = True
            self.start = time.time()

class Position():
    x = 5.0
    y = 15.0
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Proof():
    image = None
    isPrinted = False
    isOnFloor = True
    def __init__(self, name, x, y):
        self.pos = Position(x, y)
        self.image = pygame.image.load(name).convert_alpha()

class Player():
    rotate = 0
    proof = None
    haveProof = False
    isPaused = False
    def __init__(self):
        self.pos = Position(2.0, 15.0)
        self.Sprite = TestSprite("img/Perso/red.png")
        self.Sprite.pause()
    def takeProof(self, proof):
        self.proof = proof
        self.proof.isPrinted = False
        self.proof.isOnFloor = False
        self.haveProof = True
    def putProof(self):
        if (self.haveProof == True):
            self.proof.pos = Position(self.pos.x, self.pos.y)
            self.proof.isPrinted = True
            self.haveProof = False
            self.proof.isOnFloor = True
    def draw(self, fenetre):
        self.Sprite.update()
        self.Sprite.rect.x = self.pos.x * 32
        self.Sprite.rect.y = self.pos.y * 32
        fenetre.blit(self.Sprite.image, self.Sprite.rect)
#    def move

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
    

def testlist(nodelist):
    node = nodelist[0]
    for n in nodelist:
        if (node.weigth != n.weigth):
            return 1
    return 0

def clean(nlist):
    for n in nlist:
        n.weigth = 50

def checkProofNearby(players, proofs):
    for player in players:
        for proof in proofs:
            if (proof.isPrinted == False and proof.isOnFloor == True):
                if (proof.pos.x - player.pos.x > -2 and proof.pos.y - player.pos.y > -2 and proof.pos.x - player.pos.x < 2 and proof.pos.y - player.pos.y < 2):
                    proof.isPrinted = True

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
        self.Sprite = TestSprite("img/Perso/pedro.png")
        self.Sprite.pause()
        self.image = self.Sprite.image
    def rotate(self):
        lol = math.sqrt(pow(self.node.pos.x - self.direction.pos.x, 2) +  pow(self.node.pos.y - self.direction.pos.y, 2))
        if (lol != 0):
            vecteur = Position((self.pos.x - self.direction.pos.x) / lol, (self.pos.y - self.direction.pos.y) / lol)
            if (vecteur.x != 0):
                angle = math.degrees(math.tan(vecteur.y / vecteur.x))
                self.image = pygame.transform.rotate(self.Sprite.image, -1 * angle - 90)
    def draw(self, fenetre):
        self.Sprite.update()
        self.Sprite.rect.x = self.pos.x * 32
        self.Sprite.rect.y = self.pos.y * 32
        fenetre.blit(self.image, self.Sprite.rect)
    def move(self, fenetre, players):
        if ((round(self.pos.x * 10) == round(self.direction.pos.x * 10)) and (round(self.pos.y * 10) == round(self.direction.pos.y * 10))):
            self.node = self.direction
            self.direction = min(self.node.nodeList)
            self.rotate()
        else:
            lol = math.sqrt(pow(self.pos.x - self.direction.pos.x, 2) +  pow(self.pos.y - self.direction.pos.y, 2))
            vecteur = Position((self.pos.x - self.direction.pos.x) / lol, (self.pos.y - self.direction.pos.y) / lol)
            self.pos.x -= vecteur.x / 10
            self.pos.y -= vecteur.y / 10
        if (self.node.weigth == 0):
            clean(n)
            onVaMangerDesChips(n[random.choice([15, 22, 47, 42, 38, 31, 27, 0, 51])], 0)
        self.draw(fenetre)
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
        if (player.haveProof != False):
            #self.goToPlayerRoom()
            #tutulu UNE PREUVE
            return
        else:
            player.isPaused = False

taille = hauteur, largeur = 1920, 1080

fenetre = pygame.display.set_mode(taille)

continuer = 1
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for joy in joysticks:
    joy.init()

players = [Player()]
proofsPaths = [ "img/Preuves/red_proof/red_cut_32.png", "img/Preuves/red_proof/red_lighter_32.png", "img/Preuves/red_proof/red_rope_32.png", "img/Preuves/red_proof/red_spoon__32.png", "img/Preuves/red_proof/red_nes_32.png", "img/Preuves/red_proof/red_screwdriver_32.png", "img/Preuves/green_proof/green_cut_32.png", "img/Preuves/green_proof/green_lighter_32.png", "img/Preuves/green_proof/green_rope_32.png", "img/Preuves/green_proof/green_spoon_32.png", "img/Preuves/green_proof/green_nes_32.png", "img/Preuves/green_proof/green_screwdriver_32.png", "img/Preuves/orange_proof/orange_cut_32.png", "img/Preuves/orange_proof/orange_lighter_32.png", "img/Preuves/orange_proof/orange_rope_32.png", "img/Preuves/orange_proof/orange_spoon_32.png", "img/Preuves/orange_proof/orange_nes_32.png", "img/Preuves/orange_proof/orange_screwdriver_32.png", "img/Preuves/purple_proof/purple_cut_32.png", "img/Preuves/purple_proof/purple_lighter_32.png", "img/Preuves/purple_proof/purple_rope_32.png", "img/Preuves/purple_proof/purple_spoon_32.png", "img/Preuves/purple_proof/purple_nes_32.png", "img/Preuves/purple_proof/purple_screwdriver_32.png" ]
proofs = []
for proofPath in proofsPaths:
    x = random.randint(1, 28)
    y = random.randint(1, 38)
    while (lala[x][y] != 0):
        x = random.randint(1, 28)
        y = random.randint(1, 38)
    proofs.append(Proof(proofPath, y, x))
background = pygame.image.load("img/Map/map.png").convert_alpha()
menu_c = 1
menu = pygame.image.load("img/UI/menu/main_menu.png").convert()
new_rec = pygame.image.load("img/UI/menu/hand.png").convert_alpha()
merci = pygame.image.load("img/UI/menu/credits.png").convert()
son = pygame.mixer.Sound("audio/sounds/move_menu.wav")
son2 = pygame.mixer.Sound("audio/sounds/select_menu.wav")

n = [Node(19.0, 2.0, [])]
n.append(Node(19.0, 9.0, [n[0]]))
n.append(Node(19.0, 11.0, [n[1]]))
n.append(Node(12.0, 11.0, [n[2]]))
n.append(Node(10.0, 15.0, [n[3]]))

n.append(Node(12.0, 18.0, [n[4], n[3]]))
n.append(Node(13.5, 15.0, [n[2], n[3], n[4], n[5]]))
n.append(Node(19.0, 18.0, [n[5], n[6]]))
n.append(Node(27.0, 18.0, [n[7]]))
n.append(Node(25.5, 15.0, [n[8], n[7], n[2]]))

n.append(Node(27.0, 11.0, [n[9], n[2], n[8]]))
n.append(Node(29.0, 15.0, [n[10], n[9], n[8]]))
n.append(Node(12.0, 9.0, [n[3]]))
n.append(Node(11.0, 7.0, [n[12]]))
n.append(Node(11.0, 2.0, [n[13]]))

n.append(Node(5.0, 2.0, [n[14]]))
n.append(Node(5.0, 7.0, [n[15], n[13]]))
n.append(Node(6.0, 9.0, [n[16], n[13], n[12]]))
n.append(Node(6.0, 11.0, [n[17]]))
n.append(Node(8.0, 11.0, [n[18]]))

n.append(Node(8.0, 15.0, [n[19]]))
n.append(Node(8.0, 18.0, [n[20]]))
n.append(Node(1.0, 18.0, [n[21]]))
n.append(Node(1.0, 11.0, [n[22], n[18]]))
n.append(Node(27.0, 9.0, [n[10]]))

n.append(Node(28.0, 7.0, [n[24]]))
n.append(Node(28.0, 2.0, [n[25]]))
n.append(Node(34.0, 2.0, [n[26]]))
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
n.append(Node(19.0, 16.0, [n[7]]))

inspector = inspectorPedro(n[0])

onVaMangerDesChips(n[51], 0)

pygame.font.init()

def getEvent(e, joy):
    ev = [0, 0, 0]
    if (e.type == KEYDOWN and joy == -1):
        k = pygame.key.get_pressed()
        if k[K_DOWN]:
            ev[0] = -1
        if k[K_UP]:
            ev[0] = 1
        if k[K_LEFT]:
            ev[1] = -1
        if k[K_RIGHT]:
            ev[1] = 1
        if k[K_SPACE]:
            ev[2] = 1
        if k[K_ESCAPE]:
            ev[2] = -1
    if (e.type == JOYHATMOTION):
        if (e.joy == joy):
            g = joysticks[joy].get_hat(0)
            ev[0] = g[1]
            ev[1] = g[0]
    if (e.type == JOYBUTTONDOWN):
        if (e.joy == joy or joy == -1):
            if (e.button == 0):
                ev[2] = 1
            if (e.button == 1):
                ev[2] = -1
    return ev

speed = 2.5
position_new_rec = new_rec.get_rect()
position_new_rec.x = 200
position_new_rec.y = 250
fenetre.blit(menu, (0,0))
fenetre.blit(new_rec, position_new_rec)
clock = pygame.time.Clock()
while menu_c == 1:
    clock.tick(60)
    for event in pygame.event.get():
        e = getEvent(event, -1)    
        if e[2] == -1:
            exit(0)
        if e[0] < 0:
            son.play()
            position_new_rec.y = position_new_rec.y + 120
            if position_new_rec.y >= 620:
                    position_new_rec.y = 250
        if e[0] > 0:
            son.play()
            position_new_rec.y = position_new_rec.y - 120
            if position_new_rec.y <= 220:
                    position_new_rec.y = 610
        if position_new_rec.y == 250 and e[2] == 1:
            menu_c = 0
            son2.play()
        if position_new_rec.y == 610 and e[2] == 1:
            son2.play()
            while menu_c == 1:
                for event in pygame.event.get():
                    e = getEvent(event, -1)
                    if e[2] == -1:
                        menu_c = 0
                    if e[0] == -1:
                        if e[2] == -1:
                            fenetre.blit(menu, (0,0))
                            pygame.display.flip()
                            menu_c = 0
                    fenetre.blit(merci, (0,0))
                    pygame.display.flip()
            menu_c = 1
        if position_new_rec.y == 490 and e[2] == 1:
                exit(0)
    fenetre.blit(menu, (0,0))
    fenetre.blit(new_rec, position_new_rec)
    pygame.display.flip()

pygame.key.set_repeat(100, 10)
k = pygame.key.get_pressed()
spc_player = 0.25
while continuer:
    clock.tick(60)
    for event in pygame.event.get():
        e = getEvent(event, 0)
        if (e[2] == -1):
            continuer = 0
        if (e[2] == 1):
            if (players[0].haveProof == False):
                for proof in proofs:
                    if (proof.pos.x - players[0].pos.x > -1 and proof.pos.x - players[0].pos.x < 1):
                        if (proof.pos.y - players[0].pos.y > -1 and proof.pos.y - players[0].pos.y < 1):
                            players[0].takeProof(proof)
                            break
            else:
                players[0].putProof()
        if (e[1] == -1):
            if (lala[int(players[0].pos.y)][int(players[0].pos.x - spc)] != 1 and lala[int(players[0].pos.y)][int(math.ceil(players[0].pos.x - spc))] != 1):
                if (lala[int(math.ceil(players[0].pos.y))][int(players[0].pos.x - spc)] != 1 and lala[int(math.ceil(players[0].pos.y))][int(math.ceil(players[0].pos.x - spc))] != 1):
                    players[0].pos.x -= spc_player
            players[0].Sprite.play()
        elif (e[1] == 1):
            if (lala[int(players[0].pos.y)][int(math.ceil((players[0].pos.x + spc)))] != 1 and lala[int(players[0].pos.y)][int(players[0].pos.x + spc)] != 1):
                if (lala[int(math.ceil(players[0].pos.y))][int(math.ceil((players[0].pos.x + spc)))] != 1 and lala[int(math.ceil(players[0].pos.y))][int(players[0].pos.x + spc)] != 1):
                    players[0].pos.x += spc_player
            players[0].Sprite.play()
        if (e[0] == 1):
            if (lala[int(players[0].pos.y - spc)][int(players[0].pos.x)] != 1 and lala[int(math.ceil(players[0].pos.y - spc))][int(players[0].pos.x)] != 1):
                if (lala[int(players[0].pos.y - spc)][int(math.ceil(players[0].pos.x))] != 1 and lala[int(math.ceil(players[0].pos.y - spc))][int(math.ceil(players[0].pos.x))] != 1):
                    players[0].pos.y -= spc_player
            players[0].Sprite.play()
        elif (e[0] == -1):
            if (lala[int(math.ceil((players[0].pos.y + spc)))][int(players[0].pos.x)] != 1 and lala[int(players[0].pos.y + spc)][int(players[0].pos.x)] != 1):
                if (lala[int(math.ceil((players[0].pos.y + spc)))][int(math.ceil(players[0].pos.x))] != 1 and lala[int(players[0].pos.y + spc)][int(math.ceil(players[0].pos.x))] != 1):
                    players[0].pos.y += spc_player
            players[0].Sprite.play()
        if (e[0] == 1):
            players[0].Sprite.pause()
        checkProofNearby(players, proofs)
    fenetre.fill((0, 0, 0))
    fenetre.blit(background, (0, 0))
    for proof in proofs:
        if (proof.isPrinted == True):
            fenetre.blit(proof.image, Rect(proof.pos.x * 32, proof.pos.y * 32, 32, 32))
    for player in players:
        player.draw(fenetre)
    inspector.move(fenetre, players)
#    time.sleep(0.01)
#    for node in n:
#        basicfont = pygame.font.SysFont(None, 48)
#        text = basicfont.render(unicode(node.weigth), True, (255, 0, 0), (255, 255, 255))
#        textrect = text.get_rect()
#        textrect.centerx = node.pos.x * 32
#        textrect.centery = node.pos.y * 32
#        fenetre.blit(text, textrect)
    pygame.display.flip()
