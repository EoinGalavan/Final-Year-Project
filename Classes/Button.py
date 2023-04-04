import pygame

class Button:
    def __init__(self, rect, text, fontSize):
        self.rect = rect
        self.text = text
        self.font = pygame.font.SysFont('arial', fontSize)
        self.colliding = False
        self.currentTime = pygame.time.get_ticks()
        self.timeLimit = 1000 # 1000 = 1s
        self.waitTime = 0

    def checkCollision(self, leftHandPos, rightHandPos):
        left = self.rect[0] < leftHandPos[0] and self.rect[0] + self.rect[2] > leftHandPos[0] \
        and self.rect[1] < leftHandPos[1] and self.rect[1] + self.rect[3] > leftHandPos[1]
        right = self.rect[0] < rightHandPos[0] and self.rect[0] + self.rect[2] > rightHandPos[0] \
        and self.rect[1] < rightHandPos[1] and self.rect[1] + self.rect[3] > rightHandPos[1]

        self.colliding = left or right
        

        if(self.colliding):
            self.waitTime += (pygame.time.get_ticks() - self.currentTime)
        else:
            self.waitTime = 0
        
        self.currentTime = pygame.time.get_ticks()

        return self.waitTime > self.timeLimit
    
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)
        if(self.colliding):
            tempRect = (self.rect[0] ,self.rect[1] ,self.rect[2] * self.waitTime / self.timeLimit ,self.rect[3])
            pygame.draw.rect(screen, (0, 0, 255), tempRect)

        text_surface = self.font.render(self.text, False, (0, 0, 0))
        textRect = text_surface.get_rect(center=(self.rect[0] + (self.rect[2]/ 2), self.rect[1] + (self.rect[3]/ 2)))
        screen.blit(text_surface, textRect)
        