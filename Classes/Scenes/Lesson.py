from Classes.Scene import *

class Lesson(Scene):
    def __init__(self, toLearn, time):
        buttonWidth, buttonHeight = 100, 100
        buttonX, buttonY= size[0] / 2 - buttonWidth / 2, size[1] / 2 - buttonHeight / 2
        self.button = Button((buttonX, buttonY, buttonWidth, buttonHeight), "Back", 60)
        self.timer = Timer(size, time)
        self.toLearn = toLearn
        self.learnt = []
        self.currentLearn = 0
        self.learning = False
        self.imageSize = (256.4, 152.8)
        self.imagePos = (size[0] / 2 - self.imageSize[0] / 2, size[1] / 4 - self.imageSize[1] / 2)
        self.learnLetter()

    def update(self, keypoint_coords, leftHandPos, rightHandPos, currentScene):
        if(self.timer.update()):
            poseResult = AnalysePose(keypoint_coords[leftShoulder], keypoint_coords[leftWrist], keypoint_coords[rightShoulder], keypoint_coords[rightWrist])
            if(len(poseResult) == 1):
                if(poseResult == self.currentLetter):
                    if(self.learning):
                        self.learnt.append(self.currentLetter)
                        self.learning = False
                        self.learnLetter()
                    else:
                        self.newLetter()
        # check buttons
        if(self.button.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.MainMenu
        
        

        return currentScene

    def draw(self):
        self.button.draw(screen)
        self.timer.draw(screen)
        # if(self.learning):
        images[self.currentLetter] = pygame.transform.scale(images[self.currentLetter], self.imageSize)
        screen.blit(images[self.currentLetter], self.imagePos)

    def newLetter(self):
        self.currentLetter = random.choice(self.toLearn)

    def learnLetter(self):
        if(self.currentLearn < len(self.toLearn)):
            self.currentLetter = self.toLearn[self.currentLearn]
            self.currentLearn += 1
            self.learning = True
        else:
            self.newLetter()