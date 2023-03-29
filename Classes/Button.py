import pygame

class Button:
    def __init__(self, rect, text, fontSize):
        self.rect = rect
        self.text = text
        self.font = pygame.font.SysFont('arial', fontSize)
        self.colliding = False

    def checkCollision(self, leftHandPos, rightHandPos):
        left = self.rect[0] < leftHandPos[0] and self.rect[0] + self.rect[2] > leftHandPos[0] \
        and self.rect[1] < leftHandPos[1] and self.rect[1] + self.rect[3] > leftHandPos[1]
        right = self.rect[0] < rightHandPos[0] and self.rect[0] + self.rect[2] > rightHandPos[0] \
        and self.rect[1] < rightHandPos[1] and self.rect[1] + self.rect[3] > rightHandPos[1]

        self.colliding = left or right
        return self.colliding
    
    def draw(self, screen):
        if(self.colliding):
            pygame.draw.rect(screen, (0, 0, 255), self.rect)
        else:
            pygame.draw.rect(screen, (0, 255, 0), self.rect)
        text_surface = self.font.render(self.text, False, (0, 0, 0))
        textRect = text_surface.get_rect(center=(self.rect[0] + (self.rect[2]/ 2), self.rect[1] + (self.rect[3]/ 2)))
        screen.blit(text_surface, textRect)
        