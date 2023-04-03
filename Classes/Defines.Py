#pragma once
from Classes.AnalysePose import *
from Classes.Button import *
from Classes.Timer import *
from enum import Enum
import random
import os
    
def load_images(path_to_directory):
    """Load images and return them as a dict."""
    image_dict = {}
    for filename in os.listdir(path_to_directory):
        if filename.endswith('.png'):
            path = os.path.join(path_to_directory, filename)
            key = filename[:-4]
            image_dict[key] = pygame.image.load(path).convert()
    return image_dict

# Open a new window
size = (1280, 720)
screen = pygame.display.set_mode(size)
frameRate = 60

# load the images
images = load_images("Images/")

# scene enum
scenes = Enum('Scenes', ['MainMenu', 'Lesson', 'Practice'])

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

