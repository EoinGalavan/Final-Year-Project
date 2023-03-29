import pygame

class Timer:
    def __init__(self, size, waitTime):
        self.maxWidth = size[0] * 0.9
        self.screenWidth = size[0]
        width, height = self.maxWidth, 20
        X, Y = size[0] / 2 - width / 2, 10
        self.rect = (X,Y,width,height)
        
        self.waitTime = waitTime * 1000
        self.maxWaitTime = waitTime * 1000

        self.startTime = pygame.time.get_ticks()

    def update(self):
        ticks = pygame.time.get_ticks()
        self.waitTime = self.maxWaitTime - (ticks - self.startTime)
        print(self.waitTime)
        if(self.waitTime <= 0):
            self.waitTime = self.maxWaitTime
            self.startTime = ticks
        tempList = list(self.rect)
        tempList[2] = (self.waitTime * self.maxWidth) / self.maxWaitTime
        tempList[0] = self.screenWidth / 2 - tempList[2] / 2
        self.rect = tuple(tempList)

        return self.waitTime == self.maxWaitTime

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)