import pygame
import Model

class bird():
    x = 0
    y = 0
    yvel = 0
    score = 0
    alive = True
    r = pygame.Rect(x, y, 20, 20)
    brain = Model.Model(4,1)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = pygame.Rect(self.x, self.y, 20, 20)
        self.alive = True
        self.brain = Model.Model(4,1)
        
    def fall(self, dt, gravity):
        self.yvel += gravity*dt
        self.y += self.yvel
        self.r = pygame.Rect(self.x, self.y, 20, 20)

    def flap(self, yvel):
        self.yvel = yvel
        self.r = pygame.Rect(self.x, self.y, 20, 20)

    def updateScore(self):
        self.score += 1
        self.brain.setFitness(self.score)

    def draw(self, screen):
        pygame.draw.circle(screen, 'yellow', (self.x, self.y), 10)

    def checkBounds(self):
        if self.y > 620:
            self.alive = False
        if self.y < -50:
            self.alive = True

    def __lt__ (self, other):
        return self.brain < other.brain

    def __gt__ (self, other):
        return self.brain > other.brain
