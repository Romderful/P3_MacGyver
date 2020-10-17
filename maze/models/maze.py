"""Maze class."""

import random

import maze.models.hero as heroClass
import maze.models.items as itemClass


LEVEL = "maze\data\level.txt"


class Maze:
    """Maze class."""

    def __init__(self, level: str = LEVEL, item_number: int = 3):
        """Init."""
        self.item_number = item_number
        self.items = []
        self.size = 0
        self.walls = []
        self.paths = []
        self.hero = heroClass.Hero()
        self.guardian_position = (6, 13)

        self.init_level(level)
        self.init_item(item_number)

    @property
    def free_paths(self):
        """Return the free paths."""
        return [
            coord
            for coord in self.paths
            if coord not in self.items_coords
            and coord != self.hero.hero_position
            and coord != self.guardian_position
        ]

    @property
    def items_coords(self):
        """Return the position."""
        return [coord.position for coord in self.items]

    def init_item(self, number):
        """Init_items."""
        for _ in range(number):
            position = random.choice(self.free_paths)
            item = itemClass.Item(position)
            self.items.append(item)

    def init_level(self, level):
        """Init lvl."""
        x = 0
        y = 0

        with open(level) as f:
            data = f.read()

            for char in data:
                position = (x, y)

                if char == "#":
                    self.add_walls(position)
                    x += 1

                elif char == " ":
                    self.paths.append(position)
                    x += 1

                elif char == "\n":
                    y += 1
                    x = 0
        self.size = y

    def add_walls(self, position):
        """Add walls to the maze at the position."""
        self.walls.append(position)

    def is_game_over(self):
        """Is game over."""
        if self.hero.item_number == self.item_number:
            return True

        else:
            return False

    def is_on_item(self, hero):
        """Is on item."""
        for item in self.items:

            if hero.hero_position == item.position:
                hero.add_items(item)
                self.items.remove(item)

                if(item.name is not None):
                    print("Got the", item.name + ".", len(self.items), "item(s) left !")

                else:
                    print("Got the ", str(item.id) + ".", len(self.items), "item(s) left !")

    def set_items_names(self, names):
        """Set items names."""
        counter = 0

        for item in self.items:
            item.name = names[counter]
            counter += 1

    def update(self, control: str) -> bool:
        """Update."""
        running = True

        if(control == "left"):
            self.hero.move_left(self.walls)

        elif(control == "right"):
            self.hero.move_right(self.walls)

        elif(control == "up"):
            self.hero.move_up(self.walls)

        elif(control == "down"):
            self.hero.move_down(self.walls)

        self.is_on_item(self.hero)

        if(self.hero.hero_position == self.guardian_position):
            running = False

        return running
