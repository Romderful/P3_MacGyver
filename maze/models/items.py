"""Items class."""


class Item:
    """Class Items."""

    def __init__(self, position, id, name=None):
        """Constructeur."""
        self.position = position
        self.id = id
        self.name = name

    def set_name(self, name):
        """Set item's name."""
        self.name = name
