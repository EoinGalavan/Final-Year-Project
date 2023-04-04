from Classes.Scene import *

class Practice(Scene):
    def __init__(self, testedLetters, time):
        buttonWidth, buttonHeight = 100, 100
        buttonX, buttonY= size[0] / 2 - buttonWidth / 2, size[1] / 2 - buttonHeight / 2
        self.button = Button((buttonX, buttonY, buttonWidth, buttonHeight), "Back", 60)
        self.score = 0
        self.timer = Timer(size, time)
        self.letterPos = (size[0] / 2, size[1] / 4)
        self.testedLetters = testedLetters
        self.imageSize = (95, 125)
        self.imagePos = (size[0] / 2 - self.imageSize[0] / 2, size[1] / 4 - self.imageSize[1] / 2)
        self.newLetter()

    def update(self, keypoint_coords, leftHandPos, rightHandPos, currentScene):
        if(self.timer.update()):
            poseResult = AnalysePose(keypoint_coords[leftShoulder], keypoint_coords[leftWrist], keypoint_coords[rightShoulder], keypoint_coords[rightWrist])
            if(poseResult == self.currentLetter):
                self.score += 1
            self.newLetter()
        # check buttons
        if(self.button.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.MainMenu
        
        

        return currentScene

    def draw(self):
        self.button.draw(screen)
        self.timer.draw(screen)
        text_surface = my_font.render(str(self.score), False, (0, 0, 0))
        screen.blit(text_surface, (0,0))
        images[self.currentLetter + "-"] = pygame.transform.scale(images[self.currentLetter + "-"], self.imageSize)
        screen.blit(images[self.currentLetter + "-"], self.imagePos)

    def newLetter(self):
        self.currentLetter = random.choice(self.testedLetters)