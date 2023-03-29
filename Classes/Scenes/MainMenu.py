from Classes.Scene import *

class MainMenu(Scene):
    def __init__(self):
        self.button = Button((400, 40, 100, 100), "Play", 45)

    def update(self, keypoint_coords, leftHandPos, rightHandPos, currentScene):
        # check buttons
        if(self.button.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.Level
        
        return currentScene

    def draw(self):
        self.button.draw(screen)