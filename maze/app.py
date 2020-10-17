"""Application module."""

import time

from maze import views
from maze import controllers
from maze.models.maze import Maze


class Application:
    """Application class."""

    def __init__(self):
        """Initializate."""

    def run(self, choice: str):
        """Run the app."""
        maze = Maze()

        if choice == "cli":
            controller = controllers.console.Controller(maze)
            view = views.console.View(maze)

        elif choice == "pygame":
            controller = controllers.pygame.Controller(maze)
            view = views.pygame.View(maze)

        running = True
        view.display()

        while running:
            control = controller.get_control()
            running = maze.update(control)
            view.display()

            if not running:

                if(len(maze.hero.items_list) != maze.item_number):
                    print("You lost")
                else:
                    print("You won")

                time.sleep(1)
