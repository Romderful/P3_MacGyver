"""Display maze."""


class View:
    """CLI view."""

    def __init__(self, maze):
        """Init."""
        self.maze = maze

    def find_item(self, items, position):
        """Find an item at the position."""
        for item in items:

            if item.position == position:
                return item

    def display(self):
        """Display."""
        maze = self.maze
        walls = self.maze.walls
        Macgyver = self.maze.hero
        result = ""
        items_position = []

        for i in range(len(maze.items)):
            items_position.append(maze.items[i].position)

        for row in range(maze.size + 1):

            for column in range(maze.size + 1):
                position = (column, row)

                if position in walls:
                    result += "#"

                elif position == Macgyver.hero_position:
                    result += "@"

                elif position == maze.guardian_position:
                    result += "G"

                elif position in items_position:
                    item = self.find_item(maze.items, position)
                    result += str(item.id)

                else:
                    result += " "

            result += "\n"

        print(result)
