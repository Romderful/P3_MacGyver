"""Hero's class."""


class Hero:
    """Hero's class."""

    def __init__(self):
        """Init."""
        self.items_list = []
        self.hero_position = (2, 1)

    def item_number(self):
        """Get item number."""
        return len(self.items_list)

    def add_items(self, item):
        """Add items."""
        self.items_list.append(item)

    def is_valid_move(self, forbidden_moves, position):
        """Return move's validity."""
        if position in forbidden_moves:
            return False

        else:
            return True

    def move_up(self, forbidden_moves):
        """Move upward."""
        new_x = self.hero_position[0]
        new_y = self.hero_position[1] - 1

        if self.is_valid_move(forbidden_moves, (new_x, new_y)):
            self.hero_position = (new_x, new_y)

    def move_down(self, forbidden_moves):
        """Move downward."""
        new_x = self.hero_position[0]
        new_y = self.hero_position[1] + 1

        if self.is_valid_move(forbidden_moves, (new_x, new_y)):
            self.hero_position = (new_x, new_y)

    def move_right(self, forbidden_moves):
        """Move to the right."""
        new_x = self.hero_position[0] + 1
        new_y = self.hero_position[1]

        if self.is_valid_move(forbidden_moves, (new_x, new_y)):
            self.hero_position = (new_x, new_y)

    def move_left(self, forbidden_moves):
        """Move to the left."""
        new_x = self.hero_position[0] - 1
        new_y = self.hero_position[1]

        if self.is_valid_move(forbidden_moves, (new_x, new_y)):
            self.hero_position = (new_x, new_y)
