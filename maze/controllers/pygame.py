"""Pygame controls."""

import pygame as pygame_lib


class Controller:
    """pygame controller."""

    def __init__(self, maze):
        """Init."""
        self.maze = maze

    def get_control(self) -> str:
        """Control entry point."""
        command = ""

        for _ in pygame_lib.event.get():

            if pygame_lib.key.get_pressed()[115]:
                command = "down"

            elif pygame_lib.key.get_pressed()[97]:
                command = "left"

            elif pygame_lib.key.get_pressed()[100]:
                command = "right"

            elif pygame_lib.key.get_pressed()[119]:
                command = "up"

        return command
