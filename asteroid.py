from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        # circle(surface, color, center, radius, width=0, draw_top_right=None,
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        # check if asteroid is already at smallest size and stops here
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 

        # random angle in degrees between 20 and 50
        angle = random.uniform(20, 50)
        # calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
   
        # generate 2 new asteroids using current position and new radius
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        # rotate old velocity vector to create two diverging directions
        new_asteroid1.velocity = self.velocity.rotate(angle) * 1.2
        new_asteroid2.velocity = self.velocity.rotate(-angle) * 1.2




    

        

