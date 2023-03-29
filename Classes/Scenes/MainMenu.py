from Classes.Scene import *

class MainMenu(Scene):
    button = Button((400, 40, 100, 100))
    poseResult = ""

    def update(self, keypoint_coords, leftHandPos, rightHandPos):
        self.button.checkCollision(leftHandPos, rightHandPos)
        self.poseResult = AnalysePose(keypoint_coords[leftShoulder], keypoint_coords[leftWrist], keypoint_coords[rightShoulder], keypoint_coords[rightWrist])
        if(len(self.poseResult) == 1):
            pass

    def draw(self):
        self.button.draw(screen)
        text_surface = my_font.render(self.poseResult, False, (0, 0, 0))
        screen.blit(text_surface, (0,0))