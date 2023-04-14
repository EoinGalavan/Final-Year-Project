from Classes.Scene import *

class Lesson(Scene):
    def __init__(self, toLearn, time):
        buttonWidth, buttonHeight = 100, 100
        buttonX, buttonY= size[0] / 2 - buttonWidth / 2, size[1] * 0.6 - buttonHeight / 2
        self.button = Button((buttonX, buttonY, buttonWidth, buttonHeight), "Back", 60)
        self.timer = Timer(size, time)
        self.toLearn = toLearn
        self.learnt = []
        self.currentLearn = 0
        self.learning = False
        self.exampleSize = (256.4, 152.8)
        self.questionSize = (114, 150)
        self.imagePos = (size[0] / 2, size[1] / 5)
        self.counter = 0
        self.lessonCpmplete = False
        self.correctnessTransparency = 0
        self.correctnessTicksVisible = 1500
        self.ticks = 0
        self.learnLetter()

    def update(self, keypoint_coords, leftHandPos, rightHandPos, currentScene):
        if(self.timer.update()):
            poseResult = AnalysePose(keypoint_coords[leftShoulder], keypoint_coords[leftWrist], keypoint_coords[rightShoulder], keypoint_coords[rightWrist])
            if(poseResult == self.currentLetter):
                if(self.learning):
                    self.learnt.append(self.currentLetter)
                    self.learning = False
                    self.counter = min(len(self.learnt), 3)
                    self.newLetter()
                else:
                    self.counter -= 1
                    self.newLetter()
                self.correctnessTransparency = 255
                self.ticks = pygame.time.get_ticks()
        if(self.correctnessTransparency > 0):
            timeSinceLastCheck = pygame.time.get_ticks() - self.ticks
            self.ticks += timeSinceLastCheck
            self.correctnessTransparency -= 255 * timeSinceLastCheck / self.correctnessTicksVisible

        # check buttons
        if(self.button.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.MainMenu

        return currentScene

    def draw(self):
        if(self.correctnessTransparency > 0):
            image = pygame.transform.scale(images["correct"], [200, 200])
            image.set_alpha(self.correctnessTransparency)
            pos = image.get_rect(center=(size[0] / 2, size[1] * 0.42))
            screen.blit(image, pos)
        self.button.draw(screen)
        self.timer.draw(screen)
        if(not self.lessonCpmplete):
            if(self.learning):
                image = pygame.transform.scale(images[self.currentLetter], self.exampleSize)
            else:
                image = pygame.transform.scale(images[self.currentLetter + "-"], self.questionSize)
            pos = image.get_rect(center=(self.imagePos))
            screen.blit(image, pos)
        else:
            input = my_font.render("Continue to next stage to practice", False, (0, 0, 0))
            inputRect = input.get_rect(center=(size[0] / 2, size[1] / 4))
            screen.blit(input, inputRect)

    def newLetter(self):
        if(self.counter > 0):
            self.currentLetter = random.choice(self.learnt)
        else:
            self.learnLetter()

    def learnLetter(self):
        if(self.currentLearn < len(self.toLearn)):
            self.currentLetter = self.toLearn[self.currentLearn]
            self.currentLearn += 1
            self.learning = True
        else:
            self.lessonCpmplete = True