from Classes.Defines import *

# should be inherited
class Scene:
    def update(self, keypoint_coords, leftHandPos, rightHandPos, currentScene):
        return currentScene
      
    def draw(self):
        pass