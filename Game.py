import pygame
from pygame.locals import *
import cv2
import numpy

from Classes.Scenes.MainMenu import *
from Classes.Scenes.Lesson import *
from Classes.Scenes.Practice import *
from Classes.Scenes.Test import *
from Classes.Scenes.LevelSelect import *

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
        pygame.draw.circle(screen, (255, 0, 0), leftHandPos, 5)
        pygame.draw.circle(screen, (255, 0, 0), rightHandPos, 5)
            
        # if the scene changes update it here
        if(activeScene != currentScene):
            activeScene = currentScene
            scene = changeScene(currentScene)
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # --- Limit to 60 frames per second
        clock.tick(frameRate)
    
    #Once we have exited the main program loop we can stop the game engine:
    pygame.quit()

def changeScene(currentScene):
    match currentScene:
        case scenes.MainMenu:
            scene = MainMenu()
        case scenes.LevelSelect_01:
            scene = LevelSelect(1)
        case scenes.LevelSelect_02:
            scene = LevelSelect(2)
        case scenes.LevelSelect_03:
            scene = LevelSelect(3)
        case scenes.LevelSelect_04:
            scene = LevelSelect(4)
        case scenes.Level_01:
            scene = Lesson(["EndWord", "Reset", "A", "B", "C", "D", "E", "F", "G"], 2)
        case scenes.Level_02:
            scene = Practice(["EndWord", "Reset","A", "B", "C", "D", "E", "F", "G"], 2)
        case scenes.Level_03:
            scene = Test(["ACE", "BED"], 2)
        case scenes.Level_04:
            scene = Lesson(["H", "I", "K", "L", "M", "N"], 2)
        case scenes.Level_05:
            scene = Practice(["H", "I", "K", "L", "M", "N"], 2)
        case scenes.Level_06:
            pass
        case scenes.Level_07:
            scene = Lesson(["O", "P", "Q", "R", "S"], 2)
        case scenes.Level_08:
            scene = Practice(["O", "P", "Q", "R", "S"], 2)
        case scenes.Level_09:
            pass
        case scenes.Level_10:
            scene = Lesson(["T", "U", "Y", "K", "W", "X", "Z"], 2)
        case scenes.Level_11:
            scene = Practice(["T", "U", "Y", "K", "W", "X", "Z"], 2)
        case scenes.Level_12:
            pass
        case scenes.Level_13:
            scene = Lesson(["Num"], 2)
        case scenes.Level_14:
            scene = Practice(["Num"], 2)
        case scenes.Level_15:
            pass
        case scenes.Level_16:
            pass

    try:
        scene
    except:
        scene = MainMenu()
    
    return scene

if __name__ == "__main__":
    from Classes import Capture as pose

    #pose.setupCapture()
    main()