import pygame
from pygame.locals import *
import cv2
import numpy

from Classes.Scenes.MainMenu import *
from Classes.Scenes.Level import *

def main():
    pygame.init()
    pygame.display.set_caption("Semaphore Flags")

    # The loop will carry on until the user exits the game (e.g. clicks the close button).
    carryOn = True
    
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    #set up camera capture
    cap = cv2.VideoCapture(0)
    cap.set(3, size[0])
    cap.set(4, size[1])

    scene = MainMenu()
    activeScene = scenes.MainMenu
    currentScene = scenes.MainMenu

    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we can exit the while loop
        
        # First, clear the screen and draw camera
        screen.fill(0)
        frame, keypoint_coords = pose.Capture(cap)
        if frame is not None :
            frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            frame=numpy.rot90(frame)
            frame=pygame.surfarray.make_surface(frame)
            screen.blit(frame,(0,0))

        # --- Game logic should go here
        leftHandPos = fitToScreen(getHandPos(keypoint_coords[leftElbow], keypoint_coords[leftWrist]), size[0])
        rightHandPos = fitToScreen(getHandPos(keypoint_coords[rightElbow], keypoint_coords[rightWrist]), size[0])
        currentScene = scene.update(keypoint_coords, leftHandPos, rightHandPos, currentScene)

        # --- Drawing code should go here
        scene.draw()
            
        # if the scene changes update it here
        if(activeScene != currentScene):
            activeScene = currentScene
            match currentScene:
                case scenes.MainMenu:
                    scene = MainMenu()
                case scenes.Level:
                    scene = Level()
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # --- Limit to 60 frames per second
        clock.tick(frameRate)
    
    #Once we have exited the main program loop we can stop the game engine:
    pygame.quit()

if __name__ == "__main__":
    from Classes import Capture as pose

    #pose.setupCapture()
    main()