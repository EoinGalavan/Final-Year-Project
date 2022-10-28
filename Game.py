import pygame
from pygame.locals import *
import cv2
import numpy

def main():
    pygame.init()

    # Define some colors
    BLACK = ( 0, 0, 0)
    WHITE = ( 255, 255, 255)
    GREEN = ( 0, 255, 0)
    RED = ( 255, 0, 0)

    # Open a new window
    size = (1280, 720)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My First Game")

    # The loop will carry on until the user exits the game (e.g. clicks the close button).
    carryOn = True
    
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

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
    
        # --- Game logic should go here
    
        # --- Drawing code should go here
        # First, clear the screen and draw camera
        screen.fill(0) 
        frame = getCamFrame(False , cap)
        #pose.Capture()
        if frame is not None :
            screen.blit(frame,(0,0))
        #The you can draw different shapes and lines or add text to your background stage.
        
        pygame.draw.rect(screen, BLACK, [0, 0, size[0], size[1]],2)
        pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
        pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)

        #frame=cap.read()
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # --- Limit to 60 frames per second
        clock.tick(60)
    
    #Once we have exited the main program loop we can stop the game engine:
    pygame.quit()

def getCamFrame(color,camera):
    retval, frame=camera.read()
    if frame is not None :
        if not color:
            frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame=numpy.rot90(frame)
        frame=pygame.surfarray.make_surface(frame)
    return frame

if __name__ == "__main__":
    #from Classes import Capture as pose

    #pose.setupCapture()
    main()