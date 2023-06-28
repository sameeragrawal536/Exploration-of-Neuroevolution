import pygame
from Bird import bird

class obstacle():
    x = 0
    y = 0
    length = 0
    width = 0
    score = False
    scoreCollidedWith = False
    r = pygame.Rect(x, y, width, length)

    def __init__(self, x, y, length, width, score):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.score = score
        self.r = pygame.Rect(self.x, self.y, self.width, self.length)

    def checkCollision(self, bird):
        if (self.r.colliderect(bird.r)):
            if self.score == False:
                if self.scoreCollidedWith == False:
                    self.scoreCollidedWith = True
                    bird.updateScore()
            else:
                bird.alive = False

    def update(self, dt, speed):
        self.x += speed*dt
        self.r = pygame.Rect(self.x, self.y, self.width, self.length)
        
    def draw(self, screen):
        if self.score != False:
            #screen.fill('white')
            pygame.draw.rect(screen, (0, 255, 0), self.r)

    def checkBounds(self):
        if self.x < -50:
            return True
        else:
            return False

    def checkBounds2(self):
        return (self.x+20) < 80
