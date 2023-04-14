from Classes.Scene import *

class MainMenu(Scene):
    def __init__(self):
        buttonWidth = 200
        buttonHeight = 80
        offset = 80
        self.button1 = Button((offset, offset, buttonWidth, buttonHeight), "Phase 1", 45)
        self.button2 = Button((size[0] - (offset + buttonWidth), offset, buttonWidth, buttonHeight), "Phase 2", 45)
        self.button3 = Button((offset, size[1] - (offset + buttonHeight), buttonWidth, buttonHeight), "Phase 3", 45)
        self.button4 = Button((size[0] - (offset + buttonWidth), size[1] - (offset + buttonHeight), buttonWidth, buttonHeight), "Phase 4", 45)

    def update(self, keypoint_coords, leftHandPos, rightHandPos, currentScene):
        # check buttons
        if(self.button1.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.LevelSelect_01
        if(self.button2.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.LevelSelect_02
        if(self.button3.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.LevelSelect_03
        if(self.button4.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.LevelSelect_04
        
        return currentScene

    def draw(self):
        self.button1.draw(screen)
        self.button2.draw(screen)
        self.button3.draw(screen)
        self.button4.draw(screen)