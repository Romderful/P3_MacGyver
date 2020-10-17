"""Main."""

from maze.app import Application


def main():
    """Entry point."""
    choices = {
        "1": "cli",
        "2": "pygame"
    }
    choice = "0"

    while choice not in choices:
        choice = input("Console version : Press 1 \nPygame version : Press 2\n")

    app = Application()
    app.run(choices[choice])


if __name__ == "__main__":
    main()
