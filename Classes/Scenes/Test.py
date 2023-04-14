from Classes.Scene import *

class Test(Scene):
    def __init__(self, toSpell, time):
        buttonWidth, buttonHeight = 100, 100
        buttonX, buttonY= size[0] / 2 - buttonWidth / 2, size[1] * 0.6 - buttonHeight / 2
        self.button = Button((buttonX, buttonY, buttonWidth, buttonHeight), "Back", 60)
        self.timer = Timer(size, time)
        self.toSpell = toSpell
        self.counter = 0
        self.maxQuestions = 10
        self.numbersMode = False
        self.check = True
        self.newSentence()

    def update(self, keypoint_coords, leftHandPos, rightHandPos, currentScene):
        if(self.timer.update()):
            if(self.check):
                poseResult = AnalysePose(keypoint_coords[leftShoulder], keypoint_coords[leftWrist], keypoint_coords[rightShoulder], keypoint_coords[rightWrist])
                if(len(poseResult) == 1):
                    if(self.numbersMode):
                        self.addNumber(poseResult)
                    else:
                        self.sentence += poseResult
                    self.checkSentence()
                elif(poseResult == "Reset"):
                    self.sentence = ""
                    self.numbersMode = False
                elif(poseResult == "EndWord"):
                    if(len(self.sentence) != 0 and self.sentence[-1] != " "):
                        self.sentence += " "
                        self.numbersMode = False
                elif(poseResult == "Num"):
                    self.numbersMode = True
                
        # check buttons
        if(self.button.checkCollision(leftHandPos, rightHandPos)):
            currentScene = scenes.MainMenu

        return currentScene

    def draw(self):
        self.button.draw(screen)
        self.timer.draw(screen)

        input = my_font.render(self.sentence, False, (0, 0, 0))
        inputRect = input.get_rect(center=(size[0] / 2, size[1] * 0.2))
        goal = my_font.render(self.goalSentence, False, (0, 0, 0))
        goalRect = goal.get_rect(center=(size[0] / 2, size[1] * 0.3))
        screen.blit(input, inputRect)
        screen.blit(goal, goalRect)

    def checkSentence(self):
        if(self.sentence == self.goalSentence):
            self.newSentence()

    def newSentence(self):
        self.goalSentence = "Win"
        self.sentence = "You"
        if(self.counter < self.maxQuestions):
            numWords = ((self.counter - self.counter%3) / 3) + 1
            self.goalSentence = ""
            for i in range(int(numWords)):
                self.goalSentence += random.choice(self.toSpell) + " "
            self.goalSentence = self.goalSentence[:-1]
            self.sentence = ""
            self.counter += 1
        else:
            self.check = False

    def addNumber(self, pose):
        match(pose):
            case "A":
                self.sentence += "1"
            case "B":
                self.sentence += "2"
            case "C":
                self.sentence += "3"
            case "D":
                self.sentence += "4"
            case "E":
                self.sentence += "5"
            case "F":
                self.sentence += "6"
            case "G":
                self.sentence += "7"
            case "H":
                self.sentence += "8"
            case "I":
                self.sentence += "9"
            case "K":
                self.sentence += "0"
