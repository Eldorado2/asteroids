import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "White", self.position, self.radius, LINE_WIDTH)

    def split(self) -> None:
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        split_direction_1 = self.velocity.rotate(random_angle)
        split_direction_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_new_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_new_2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_new_1.velocity = split_direction_1 * 1.2
        asteroid_new_2.velocity = split_direction_2 * 1.2
