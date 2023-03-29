from Classes.Scene import *

class Level(Scene):
    def __init__(self):
        buttonWidth, buttonHeight = 100, 100
        buttonX, buttonY= size[0] / 2 - buttonWidth / 2, size[1] / 2 - buttonHeight / 2
        self.button = Button((buttonX, buttonY, buttonWidth, buttonHeight), "Back", 60)
        self.output = ""
        self.timer = Timer(size, 2)

    def update(self, keypoint_coords, leftHandPos, rightHandPos, currentScene):
        if(self.timer.update()):
            poseResult = AnalysePose(keypoint_coords[leftShoulder], keypoint_coords[leftWrist], keypoint_coords[rightShoulder], keypoint_coords[rightWrist])
            if(len(poseResult) == 1):
                self.output += poseResult
        # check buttons
        if(self.button.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.MainMenu
        
        

        return currentScene

    def draw(self):
        self.button.draw(screen)
        self.timer.draw(screen)
        text_surface = my_font.render(self.output, False, (0, 0, 0))
        screen.blit(text_surface, (0,0))