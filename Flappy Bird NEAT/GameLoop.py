import pygame
import Bird
import Obstacle
import random
import Population
import numpy as np

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill('white')

from pygame.locals import (
    K_SPACE,
    KEYDOWN,
    QUIT,
)

running = True
obstacles = []

alivePlayers = Population.population(5)
for player in alivePlayers.population:
    print(player.brain)
deadPlayers = []

#print(player.brain)

a = 0

distances = np.random.rand(1, 4)

while len(deadPlayers) < 10:
    screen.fill('white')
    #print("Score: " + str(player.score))
    for event in pygame.event.get():
        #if event.type == KEYDOWN:
            #if event.key == K_SPACE:
                #player.flap(-20)
        if event.type == QUIT:
            running = False
            pygame.quit()
            break
        
    if a % 40 == 0:
        length = random.randint(50, 500)
        obstac = Obstacle.obstacle(700, 0, length, 20, True)
        obstac2 = Obstacle.obstacle(700, length+100, HEIGHT-(length+100), 20, True)
        obstac3 = Obstacle.obstacle(720, length, 100, 1, False)
        obstacles.append(obstac)
        obstacles.append(obstac2)
        obstacles.append(obstac3)

    dt = pygame.time.Clock().tick(60)

    i = 0
    while i < len(obstacles):
        if obstacles[i].checkBounds2():
            del obstacles[i]
            del obstacles[i]
            del obstacles[i]   
        else:
            obstacles[i].update(dt/1000, -200)
            if obstacles[i].checkBounds2() != True:
                for player in alivePlayers.population:
                    obstacles[i].checkCollision(player)
            i += 1
    
    if len(obstacles) > 0:
        for player in alivePlayers.population:
            distToObstac1 = (((100-obstacles[0].x)**2) + ((player.y-obstacles[0].length)**2))**0.5
            distToObstac2 = (((100-obstacles[0].x)**2) + ((player.y-obstacles[1].y)**2))**0.5
            distToTop = player.y
            distToBottom = HEIGHT-player.y

            distances[0][0] = distToObstac1/1000
            distances[0][1] = distToObstac2/1000
            distances[0][2] = distToTop/600
            distances[0][3] = distToBottom/600

            if player.brain.forwardProp(distances):
                player.flap(-20)
            else:
                player.fall(dt/1000, 40)
        print("")
        
    else:
        for player in alivePlayers.population:
            player.fall(dt/1000, 40)
    
    for player in alivePlayers.population:
        if player.alive:
            player.checkBounds()
            if player.alive:
                player.draw(screen)
            else:
                deadPlayers.append(player)
        else:
            deadPlayers.append(player)
            

    for i in range(len(obstacles)):
        obstacles[i].draw(screen)
    
    pygame.display.update()

    a += 1
