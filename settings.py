class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 132, 255)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Super bullet settings
        self.super_bullet_speed = 0.5
        self.super_bullet_width = 5
        self.super_bullet_height = 20
        self.super_bullet_color = (70, 20, 35)
        self.super_bullets_allowed = 1

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
