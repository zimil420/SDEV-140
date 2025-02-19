"""
Guessing Game (GUI-based)

This program implements a number-guessing game where the computer attempts to guess 
a number between 1 and 100, and the user provides hints to guide the computer's guesses.
The game uses a binary search approach to efficiently find the correct number.

Features:
- The computer makes a guess and displays it in a label.
- The user provides feedback by clicking one of the buttons: 
    - "Too small" (guess is too low)
    - "Too large" (guess is too high)
    - "Correct" (guess is correct)
- The game disables the buttons when the correct number is found.
- The "New game" button resets the game to start over.

The GUI is built using the `breezypythongui` module.

Author: Cash Kiefer
Date: 02/19/2025
"""

from breezypythongui import EasyFrame

class GuessingGame(EasyFrame):
    """A GUI-based game where the computer guesses a number between 1 and 100."""

    def __init__(self):
        """Sets up the game window, initializes variables, and creates GUI components."""
        EasyFrame.__init__(self, title="Guessing Game")

        # Initialize game variables
        self.low = 1
        self.high = 100
        self.guess = (self.low + self.high) // 2  # Start with the midpoint guess

        # Create GUI components
        self.label = self.addLabel(text=f"Is the number {self.guess}?", row=0, column=0, columnspan=4)

        # Buttons for user input
        self.smallButton = self.addButton(text="Too small", row=1, column=0, command=self.tooSmall)
        self.largeButton = self.addButton(text="Too large", row=1, column=1, command=self.tooLarge)
        self.correctButton = self.addButton(text="Correct", row=1, column=2, command=self.correct)
        self.newGameButton = self.addButton(text="New game", row=1, column=3, command=self.newGame)

    def tooSmall(self):
        """Adjusts the guess when the number is too small."""
        self.low = self.guess + 1  # Narrow the range upwards
        self.makeGuess()

    def tooLarge(self):
        """Adjusts the guess when the number is too large."""
        self.high = self.guess - 1  # Narrow the range downwards
        self.makeGuess()

    def makeGuess(self):
        """Updates the guess and displays it in the label."""
        if self.low > self.high:  # This should not happen unless the user makes mistakes
            self.label["text"] = "Something went wrong! Please restart."
            return
        self.guess = (self.low + self.high) // 2  # New midpoint guess
        self.label["text"] = f"Is the number {self.guess}?"

    def correct(self):
        """Handles the correct guess scenario by displaying a success message and disabling buttons."""
        self.label["text"] = f"I guessed it! The number is {self.guess}."
        self.smallButton["state"] = "disabled"
        self.largeButton["state"] = "disabled"
        self.correctButton["state"] = "disabled"

    def newGame(self):
        """Resets the game variables and re-enables buttons for a new round."""
        self.low = 1
        self.high = 100
        self.guess = (self.low + self.high) // 2
        self.label["text"] = f"Is the number {self.guess}?"
        self.smallButton["state"] = "normal"
        self.largeButton["state"] = "normal"
        self.correctButton["state"] = "normal"

# Run the program
if __name__ == "__main__":
    GuessingGame().mainloop()
