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
        self.hero = heroClass.Hero()
        self.guardian_position = (6, 13)

        self.init_level(level)
        self.init_item(item_number)

    def init_item(self, number):
        """Init_items."""
        items = []

        for _ in range(number):
            item_position_x = random.randint(0, self.size)
            item_position_y = random.randint(0, self.size)
            item_position = (item_position_x, item_position_y)

            while (
                item_position in self.walls
                or item_position in items
                or item_position == self.hero.hero_position
                or item_position == self.guardian_position
            ):
                item_position_x = random.randint(0, self.size)
                item_position_y = random.randint(0, self.size)
                item_position = (item_position_x, item_position_y)

            items.append(item_position)
            new_item = itemClass.Item(item_position, len(items))
            self.items.append(new_item)

    def init_level(self, level):
        """Init lvl."""
        x = 0
        y = 0

        with open(level) as f:
            data = f.read()

            for walls in data:

                if walls == "#":
                    self.add_walls((x, y))
                    x += 1

                elif walls == " ":
                    x += 1
                    pass

                elif walls == "\n":
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
