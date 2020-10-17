"""Make the hero move."""


class Controller:
    """CLI controller."""

    def __init__(self, maze):
        """Init."""
        self.maze = maze

    def get_control(self) -> str:
        """Control entry point."""
        command = ""
        user_choice = input("Please enter a key : ")

        if user_choice == "z":
            command = "up"

        elif user_choice == "q":
            command = "left"

        elif user_choice == "d":
            command = "right"

        elif user_choice == "s":
            command = "down"

        return command
