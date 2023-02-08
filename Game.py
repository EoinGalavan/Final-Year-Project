import pygame
from pygame.locals import *
import cv2
import numpy

from Classes.Defines import *
from Classes.AnalysePose import *

def main():
    pygame.init()

    # Open a new window
    size = (1280, 720)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My First Game")

    # The loop will carry on until the user exits the game (e.g. clicks the close button).
    carryOn = True
    
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    #seting up font for text display
    pygame.font.init() 
    my_font = pygame.font.SysFont('arial', 30)

    #set up camera capture
    cap = cv2.VideoCapture(0)
    cap.set(3, size[0])
    cap.set(4, size[1])

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
        poseResult = AnalysePose(keypoint_coords[leftShoulder], keypoint_coords[leftWrist], keypoint_coords[rightShoulder], keypoint_coords[rightWrist])
        if(len(poseResult) == 1):
            poseResult

        # --- Drawing code should go here
        text_surface = my_font.render(poseResult, False, (0, 0, 0))
        screen.blit(text_surface, (0,0))
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # --- Limit to 60 frames per second
        clock.tick(60)
    
    #Once we have exited the main program loop we can stop the game engine:
    pygame.quit()

if __name__ == "__main__":
    from Classes import Capture as pose

    #pose.setupCapture()
    main()