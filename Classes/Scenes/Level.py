from Classes.Scene import *

class Level(Scene):
    def __init__(self):
        buttonWidth, buttonHeight = 100, 100
        buttonX, buttonY= size[0] / 2 - buttonWidth / 2, size[1] / 2 - buttonHeight / 2
        self.button = Button((buttonX, buttonY, buttonWidth, buttonHeight), "Back", 60)
        self.output = ""
        self.score = 0
        self.timer = Timer(size, 2)
        self.letterPos = (size[0] / 2, size[1] / 4)
        self.newLetter()

    def update(self, keypoint_coords, leftHandPos, rightHandPos, currentScene):
        if(self.timer.update()):
            poseResult = AnalysePose(keypoint_coords[leftShoulder], keypoint_coords[leftWrist], keypoint_coords[rightShoulder], keypoint_coords[rightWrist])
            if(len(poseResult) == 1):
                if(poseResult == self.currentLetter):
                    self.score += 1
                self.output += poseResult
            self.newLetter()
        # check buttons
        if(self.button.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.MainMenu
        
        

        return currentScene

    def draw(self):
        self.button.draw(screen)
        self.timer.draw(screen)
        text_surface = my_font.render(str(self.score), False, (0, 0, 0))
        currentLetterText = my_font.render(str(self.currentLetter), False, (0, 0, 0))
        screen.blit(text_surface, (0,0))
        screen.blit(currentLetterText, self.letterPos)

    def newLetter(self):
        self.currentLetter = random.choice(["A", "B", "C", "D", "E", "F", "G"])