#pragma once
from Classes.AnalysePose import *
from Classes.Button import *
from enum import Enum

# Open a new window
size = (1280, 720)
screen = pygame.display.set_mode(size)

# scene enum
scenes = Enum('Scenes', ['MainMenu', 'Level'])
currentScene = scenes.MainMenu

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

# Define pose references
nose = 0
leftEye = 1
rightEye = 2
leftEar = 3
rightEar = 4
leftShoulder = 5
rightShoulder = 6
leftElbow = 7
rightElbow = 8
leftWrist = 9
rightWrist = 10
leftHip = 11
rightHip = 12
leftKnee = 13
rightKnee = 14
leftAnkle = 15
rightAnkle = 16

#seting up font for text display
pygame.font.init() 
my_font = pygame.font.SysFont('arial', 72)