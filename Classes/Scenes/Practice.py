from Classes.Scene import *

class Practice(Scene):
    def __init__(self, testedLetters, time):
        buttonWidth, buttonHeight = 100, 100
        buttonX, buttonY= size[0] / 2 - buttonWidth / 2, size[1] * 0.6 - buttonHeight / 2
        self.button = Button((buttonX, buttonY, buttonWidth, buttonHeight), "Back", 60)
        self.score = 0
        self.timer = Timer(size, time)
        self.testedLetters = testedLetters
        self.imageSize = (114, 150)
        self.imagePos = (size[0] / 2, size[1] / 5)
        self.text = "0"
        self.textPos = (0, 0)
        self.numQuestions = 20
        self.questionsLeft = self.numQuestions
        self.correct = True
        self.correctnessTransparency = 0
        self.correctnessTicksVisible = 1500
        self.ticks = pygame.time.get_ticks()
        self.newLetter()
        

    def update(self, keypoint_coords, leftHandPos, rightHandPos, currentScene):
        if(self.timer.update()):
            poseResult = AnalysePose(keypoint_coords[leftShoulder], keypoint_coords[leftWrist], keypoint_coords[rightShoulder], keypoint_coords[rightWrist])
            if(poseResult == self.currentLetter):
                self.score += 1
                self.text = str(self.score)
                self.correct = True
            else:
                self.correct = False
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
            if(self.correct):
                image = pygame.transform.scale(images["correct"], [200, 200])
            else:
                image = pygame.transform.scale(images["incorrect"], [200, 200])
            image.set_alpha(self.correctnessTransparency)
            pos = image.get_rect(center=(size[0] / 2, size[1] * 0.42))
            screen.blit(image, pos)
        self.button.draw(screen)
        self.timer.draw(screen)
        text_surface = my_font.render(self.text, False, (0, 0, 0))
        screen.blit(text_surface, self.textPos)
        if(self.questionsLeft >= 0):
            image = pygame.transform.scale(images[self.currentLetter + "-"], self.imageSize)
            pos = image.get_rect(center=(self.imagePos))
            screen.blit(image, pos)
        

    def newLetter(self):
        self.currentLetter = random.choice(self.testedLetters)
        self.questionsLeft -= 1
        if(self.questionsLeft < 0):
            self.timer.setActive(False)
            self.text = "Final Score: " + str(self.score) + "/" + str(self.numQuestions)
            text_surface = my_font.render(self.text, False, (0, 0, 0))
            self.textPos = text_surface.get_rect(center=(size[0] / 2, size[1] * 0.3))
            