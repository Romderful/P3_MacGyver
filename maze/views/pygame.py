"""Pygame views."""

import os
from pathlib import Path

import pygame as pygame_lib
from pygame.locals import *

import maze.config as icon


class View:
    """pygame view."""

    def __init__(self, maze):
        """Init."""
        self.maze = maze
        self.images = {}

        pygame_lib.init()

        self.window = pygame_lib.display.set_mode((600, 600))
        self.size = 40

        self.create_images()
        self.scale_images()

    def create_images(self):
        """Create the images."""
        self.images = {
            "wall": pygame_lib.image.load(icon.WALL),
            "floor": pygame_lib.image.load(icon.FLOOR),
            "guardian": pygame_lib.image.load(icon.GUARDIAN).convert_alpha(),
            "mcgyver": pygame_lib.image.load(icon.MACGYVER).convert_alpha(),
            "ether": pygame_lib.image.load(icon.ETHER).convert_alpha(),
            "needle": pygame_lib.image.load(icon.NEEDLE).convert_alpha(),
            "tube": pygame_lib.image.load(icon.TUBE).convert_alpha(),
        }

    def scale_images(self):
        """Scale the images."""
        for key, value in self.images.items():
            self.images[key] = pygame_lib.transform.scale(value, (self.size, self.size))

    def display(self):
        """Display pygame."""
        items_position = []
        maze = self.maze
        walls = self.maze.walls
        Macgyver = self.maze.hero


        for i in range(len(maze.items)):
            items_position.append(maze.items[i].position)

        for row in range(maze.size + 1):

            for column in range(maze.size + 1):
                images = []
                position = (column, row)

                if position in walls:
                    images.append(self.images["wall"])

                elif position == Macgyver.hero_position:
                    images.append(self.images["floor"])
                    images.append(self.images["mcgyver"])

                elif position == maze.guardian_position:
                    images.append(self.images["floor"])
                    images.append(self.images["guardian"])

                elif position in items_position:
                    item = self.find_item(maze.items, position)
                    images.append(self.images["floor"])

                    if item.id == 1:
                        images.append(self.images["ether"])

                    elif item.id == 2:
                        images.append(self.images["needle"])

                    elif item.id == 3:
                        images.append(self.images["tube"])

                else:
                    images.append(self.images["floor"])

                for image in images:
                    self.window.blit(image, (column * self.size, row * self.size))

        pygame_lib.display.flip()

    def find_item(self, items, position):
        """Find an item at the position."""
        for item in items:

            if item.position == position:
                return item

    def quit(self):
        """Quit."""
        pygame_lib.quit()
