import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, gai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = gai_game.screen
        self.settings = gai_game.settings

        self.color = self.settings.bullet_color
        self.super_bullet_color = self.settings.super_bullet_color # SUPER BULLET


        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)

        self.super_bullet_rect = pygame.Rect(0, 0, self.settings.super_bullet_width,
                                             self.settings.super_bullet_height) # SUPER BULLET


        self.rect.midtop = gai_game.ship.rect.midtop
        self.super_bullet_rect.midtop = gai_game.ship.rect.midtop # SUPER BULLET

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.s_y = float(self.super_bullet_rect.y) # SUPER BULLET

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

        # Update the decimal position of the bullet.
        self.s_y -= self.settings.super_bullet_speed
        # Update the rect position.
        self.super_bullet_rect.y = self.s_y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def draw_super_bullet(self):
        """Draw the super bullet to the screen."""
        pygame.draw.rect(self.screen, self.super_bullet_color, self.super_bullet_rect)
