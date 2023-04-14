#pragma once
from Classes.AnalysePose import *
from Classes.Button import *
from Classes.Timer import *
from enum import Enum
import random
import os
    
DEBUG = True   

def load_images(path_to_directory):
    """Load images and return them as a dict."""
    image_dict = {}
    for filename in os.listdir(path_to_directory):
        if filename.endswith('.png'):
            path = os.path.join(path_to_directory, filename)
            key = filename[:-4]
            image_dict[key] = pygame.image.load(path).convert_alpha()
    return image_dict

# Open a new window
size = (1280, 720)
screen = pygame.display.set_mode(size)
frameRate = 60

# load the images
images = load_images("Images/")

# scene enum
class scenes(Enum):
    MainMenu = 0 
    LevelSelect_01 = 1 
    LevelSelect_02 = 2 
    LevelSelect_03 = 3 
    LevelSelect_04 = 4 
    Level_01 = 5 
    Level_02 = 6 
    Level_03 = 7 
    Level_04 = 8 
    Level_05 = 9 
    Level_06 = 10 
    Level_07 = 11
    Level_08 = 12
    Level_09 = 13
    Level_10 = 14
    Level_11 = 15
    Level_12 = 16
    Level_13 = 17
    Level_14 = 18
    Level_15 = 19
    Level_16 = 20


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

timerLength = 2
lettersPhase1 = ["EndWord", "Reset", "A", "B", "C", "D", "E", "F", "G"]
lettersPhase2 = ["H", "I", "K", "L", "M", "N"]
lettersPhase3 = ["O", "P", "Q", "R", "S", "J", "V"]
lettersPhase4 = ["T", "U", "Y", "K", "W", "X", "Z"]
lettersPhase5 = ["Num", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

wordsPhase1 = ["ACE", "ADD", "AGE", "BAD", "BAG", "BED", "BEE", "BEG", "CAB", "DAB", "DAD", "EBB", "EGG", "FAB", "FAD", "FED", "FEE", "GAB", "GAG"]
wordsPhase2 = ["ABLE", "ACHE", "ACID", "AKIN", "BAKE", "BEND", "BIDE", "BIKE", "CALM", "CHIN", "CLAD", "CHEF", "DANK", "DAME", "DEAF", "DIAL", 
            "EACH", "FACE", "FAKE", "FEND", "FILM", "FLEA", "GAIN", "GAME", "GILD", "GLAD", "HAKE", "HALF", "HELM", "HIND", "ICED", "INCH", 
            "KALE", "KING", "LACK", "LEND", "LIMB", "LICK", "MACH", "MAGE", "MELD", "MICE", "NAIL", "NECK", "NICE", "NIGH"]
wordsPhase3 = ["MINCE", "FLIER", "GREEN", "LEARN", "NIQAB", "QAIDS", "BASIS", "PENNY", "ALARM", "SOLID", "CARVE", "GRAIN", 
            "PEACE", "RANCH", "ARENA", "COLOR", "COVER", "PRICE", "DRAIN", "PLACE", "SLIME", "SLAVE", "RAISE", "OPERA", 
            "CHEAP", "BLADE", "MEDAL", "MAJOR", "LASER", "GLASS", "BRAID", "AGILE"]
wordsPhase4 = ["BRIDGE", "LEADER", "DIRECT", "INSIST", "ASYLUM", "BREEZE", "GRUDGE", "TUMBLE", "STRIKE", "WORKER", "CRISIS", "SAMPLE", "MINUTE", 
            "RESIGN", "IMPORT", "CRITIC", "MATRIX", "DEMAND", "REDEEM", "GOSSIP", "SUMMER", "FILTER", "EXCUSE", "SPHERE", "MEDIUM", "EXTEND", 
            "SAILOR", "MIDDLE", "RETURN", "APATHY", "ACCENT", "PACKET", "RESCUE", "SILVER", "THANKS", "VOYAGE", "NOTICE", "CANDLE", "CRUTCH", "CANVAS"]
wordsPhase5 = []
for i in range(0, 30):
    wordsPhase5.append(str(random.randint(100000, 9999999)))
wordsPhase6 = []

