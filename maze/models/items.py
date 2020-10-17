"""Items class."""


class Item:
    """Class Items."""

    ID = 0
    NAMES = {1: "ether", 2: "needle", 3: "tube"}

    def __init__(self, position):
        """Constructeur."""
        Item.ID += 1
        self.position = position
        self.id = Item.ID
        self.name = self.NAMES[self.id]
