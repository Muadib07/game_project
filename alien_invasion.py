import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class GameAlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("THE Alien Invasion")

        # Initialize ship object
        self.ship = Ship(self) # ten self to self od inita calssy GAI

        # Initialize sprite group
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            #self.ship.update()
            #self._update_bullets()
            self._update_aliens()
            self._update_screen()

            # Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            # Redraw the screen during each pass through the loop.
            # self.screen.fill(self.settings.bg_color)

            # !!! Ship object !!!
            # self.ship.blitme()

            # Make the most recently drawn screen visible.
            # pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        """First version which spawn one alien"""
        # # Make an alien.
        # alien = Alien(self)
        # self.aliens.add(alien)

        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size # crate row I
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the first row of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)

        alien_width, alien_height = alien.rect.size # ADD ROW II # PO CO TO ???

        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x

        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number # ADD ROW III

        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                """stara wersja 2.0"""
                # if event.key == pygame.K_RIGHT:
                #     self.ship.moving_right = True
                # elif event.key == pygame.K_LEFT:
                #     self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                """stara wersja 2.0"""
                # if event.key == pygame.K_RIGHT:
                #     self.ship.moving_right = False
                # elif event.key == pygame.K_LEFT:
                #     self.ship.moving_left = False

                """Stara wersja 1.0"""
                    # Move the ship to the right.
                #     self.ship.rect.x += 3
                # elif event.key == pygame.K_LEFT:
                #     self.ship.rect.x -= 3

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            """Super shot"""
        elif event.key == pygame.K_b:
            self._fire_super_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _fire_super_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.super_bullets_allowed:
            new_super_bullet = Bullet(self)
            self.bullets.add(new_super_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                                                True, True)
        """(To make a high-powered
        bullet that can travel to the top of the screen, destroying every alien in its
        path, you could set the first Boolean argument to False and keep the second
        Boolean argument set to True. The aliens hit would disappear, but all bullets
        would stay active until they disappeared off the top of the screen.)
        When you run Alien Invasion now, aliens you hit should disappe"""

    def _update_aliens(self):
        #"""Update the positions of all aliens in the fleet."""
        """
        Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        # ship method
        self.ship.update()
        self._update_bullets()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()




if __name__ == '__main__':
    # Make a game instance, and run the game.
    gai = GameAlienInvasion()
    gai.run_game()
