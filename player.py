from circleshape import CircleShape
from constants import *
import pygame
import shot

class Player(CircleShape):
    def __init__(self, x, y, radius):
        # from the parent class (CircleShape)
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # use the screen as surface to draw on
        # set color to white
        # use the list points (self.a , self.b, self.c ) to draw the triangle
        # line width of 2
        pygame.draw.polygon(screen, 'white', self.triangle(), width=2)

    def rotate(self, amount):
        self.rotation += amount

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-PLAYER_TURN_SPEED * dt)
        if keys[pygame.K_d]:
            self.rotate(PLAYER_TURN_SPEED * dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)

        # always modify the cooldown 
        if self.cooldown > 0:
            self.cooldown -= dt 

        # attempt to shoot
        if keys[pygame.K_SPACE]:
            self.shoot()
            

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.cooldown <= 0:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot_position = self.position + forward * self.radius
            
            bullet = shot.Shot(shot_position.x, shot_position.y, 2)
            bullet.velocity = forward * PLAYER_SHOOT_SPEED
            # reset cool down
            self.cooldown = PLAYER_SHOOT_COOLDOWN




        
        
   