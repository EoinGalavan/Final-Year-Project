from Classes.Scene import *

class LevelSelect(Scene):
    def __init__(self, phase):
        phase *= 4
        self.phase = phase
        self.button1 = Button((40, 40, 80, 80), str(phase - 3), 45)
        self.button2 = Button((size[0] - 120, 40, 80, 80), str(phase - 2), 45)
        self.button3 = Button((40, size[1] - 120, 80, 80), str(phase - 1), 45)
        self.button4 = Button((size[0] - 120, size[1] - 120, 80, 80), str(phase), 45)
        buttonWidth, buttonHeight = 100, 100
        buttonX, buttonY= size[0] / 2 - buttonWidth / 2, size[1] / 2 - buttonHeight / 2
        self.backButton = Button((buttonX, buttonY, buttonWidth, buttonHeight), "Back", 60)

    def update(self, keypoint_coords, leftHandPos, rightHandPos, currentScene):
        # check buttons
        if(self.button1.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.Level_01
            currentScene = scenes(currentScene.value + self.phase - 4)
        if(self.button2.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.Level_02
            currentScene = scenes(currentScene.value + self.phase - 4)
        if(self.button3.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.Level_03
            currentScene = scenes(currentScene.value + self.phase - 4)
        if(self.button4.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.Level_04
            currentScene = scenes(currentScene.value + self.phase - 4)
        if(self.backButton.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.MainMenu
        
        return currentScene

    def draw(self):
        self.button1.draw(screen)
        self.button2.draw(screen)
        self.button3.draw(screen)
        self.button4.draw(screen)
        self.backButton.draw(screen)