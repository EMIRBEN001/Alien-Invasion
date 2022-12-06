import pygame
import sys

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    
    # Set the background color.
    bg_color = (230, 230, 230)

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        
        # Watch for keyboard and mouse events.

        # Redraw the screen during each pass through the loop.
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Make the most recetly drawn screen visible.
        pygame.display.flip()

run_game()