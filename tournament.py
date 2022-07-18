# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    # The below error message will be returned if the user does not enter the correct input(argv)
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    # Dictionary called "teams", and the program will read "teams" from file into memory
    teams = []
    # Read teams into memory from file
    filename = sys.argv[1]
    # Open "filename"
    with open(filename) as file:
        reader = csv.DictReader(file)
        # By default, all values read from the file will be strings, so the team's rating needs to be converted to an integer
        for team in reader:
            team["rating"] = int(team["rating"])
            # Append each team's dictionary to teams - which means adding a single item to an existing list
            teams.append(team)

    # Dictionary called "counts" that stores the names of each team,
    # and how many tournaments each team has won out of N number of simulations
    counts = {}
    # Simulate N tournaments and keep track of win counts
    for i in range(N):
        winner = simulate_tournament(teams)
        # The program needs to keep track of the winners and add 1 count to the team's total wins
        if winner in counts:
            counts[winner] += 1
        else:
            counts[winner] = 1


# Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


# The simulate_game function will simulate a game where it puts 2 teams against each other
# and returns True if team 1 wins and False if team 2 wins
def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


# The simulate_round function will simulate each round between many different teams.
# It will take in a list of teams and consider each of these pairs of teams, one at a time and simulates a game between each of them
# And will return a list of all the winners
def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams, and will return a list of the winner of the rounds
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


# The simulate_tournament function will simulate the entire tornament and repeatedly simulate rounds until it has one winner
def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # As long as the number of teams left is greater than 1, we will keep simulating rounds
    while len(teams) > 1:
        teams = simulate_round(teams)
    # Now that the system has simulated rounds until we are left with the winning team, we can return the name of the winner
    # Since there is only 1 team left in "teams", that means that the winning team is located in "teams[0]"
    return teams[0]["team"]


if __name__ == "__main__":
    main()
