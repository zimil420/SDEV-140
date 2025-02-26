"""
This module implements a simple simulation of the game of Craps.
Players roll two dice and attempt to win based on the rules of Craps.
The Player class manages individual games, tracking rolls and game state.
The script allows playing a single interactive game or multiple automated games
for statistical analysis.

Author: Cash Kiefer
Updated on: 2/26/25
"""

from die import Die

class Player:
    def __init__(self):
        """Initializes the player's game state."""
        self.die1 = Die()
        self.die2 = Die()
        self.roll = ""
        self.rollsCount = 0
        self.atStartup = True
        self.winner = False
        self.loser = False
        self.initialSum = None

    def rollDice(self):
        """Rolls the dice, updates the game state, and returns the roll values."""
        self.die1.roll()
        self.die2.roll()
        v1, v2 = self.die1.getValue(), self.die2.getValue()
        self.roll = f"({v1}, {v2}) total = {v1 + v2}"
        self.rollsCount += 1
        
        if self.atStartup:
            self.initialSum = v1 + v2
            self.atStartup = False
            if self.initialSum in (2, 3, 12):
                self.loser = True
            elif self.initialSum in (7, 11):
                self.winner = True
        else:
            laterSum = v1 + v2
            if laterSum == 7:
                self.loser = True
            elif laterSum == self.initialSum:
                self.winner = True
        
        return v1, v2

    def getNumberOfRolls(self):
        """Returns the number of rolls made."""
        return self.rollsCount

    def isWinner(self):
        """Returns True if the player has won the game."""
        return self.winner

    def isLoser(self):
        """Returns True if the player has lost the game."""
        return self.loser


def playOneGame():
    """Plays a single game interactively."""
    player = Player()
    while not player.isWinner() and not player.isLoser():
        player.rollDice()
        print(player.roll)
    
    if player.isWinner():
        print("You win!")
    else:
        print("You lose!")


def playManyGames(number):
    """Plays multiple games and prints statistics."""
    wins, losses = 0, 0
    winRolls, lossRolls = 0, 0
    
    for _ in range(number):
        player = Player()
        while not player.isWinner() and not player.isLoser():
            player.rollDice()
        
        if player.isWinner():
            wins += 1
            winRolls += player.getNumberOfRolls()
        else:
            losses += 1
            lossRolls += player.getNumberOfRolls()
    
    print("The total number of wins is", wins)
    print("The total number of losses is", losses)
    print("The average number of rolls per win is %0.2f" % (winRolls / wins if wins else 0))
    print("The average number of rolls per loss is %0.2f" % (lossRolls / losses if losses else 0))
    print("The winning percentage is %0.3f" % (wins / number))


def main():
    """Prompts the user to enter the number of games and runs the simulation."""
    number = int(input("Enter the number of games: "))
    playManyGames(number)


if __name__ == "__main__":
    main()
