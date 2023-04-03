from Classes.Scene import *

class MainMenu(Scene):
    def __init__(self):
        self.learnButton = Button((40, 40, 300, 80), "Learn Letters", 45)
        self.practiceButton = Button((40, size[1] - 120, 300, 80), "Practice Letters", 45)

    def update(self, keypoint_coords, leftHandPos, rightHandPos, currentScene):
        # check buttons
        if(self.practiceButton.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.Practice
        if(self.learnButton.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.Lesson
        
        return currentScene

    def draw(self):
        self.learnButton.draw(screen)
        self.practiceButton.draw(screen)