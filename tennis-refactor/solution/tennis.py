from typing import List, Union, Dict


class Player:

    def __init__(self):
        self.points = 0
        self.sets = 0
        self.advantage = False

    def increment_points(self):
        if self.points == 0 or self.points == 15:
            self.points += 15
        elif self.points == 30:
            self.points += 10

    def won_set(self):
        self.sets += 1
        self.points = 0
        self.advantage = False

    def lost_set(self):
        self.points = 0


class Point:

    def __init__(self, winner: Player, loser: Player):
        self.winner = winner
        self.loser = loser

    def add_points(self):
        if self.winner.points < 40:
            self.winner.increment_points()
        else:
            self._winner_has_forty()

    def _winner_has_forty(self):
        if self._deuce():
            self._check_for_advantage_win()
        else:
            self.winner.won_set()
            self.loser.lost_set()

    def _check_for_advantage_win(self):
        if self.winner.advantage:
            self.winner.won_set()
            self.loser.lost_set()
        elif self.loser.advantage:
            self.loser.advantage = False
        else:
            self.winner.advantage = True

    def _deuce(self) -> bool:
        return self.winner.points == 40 and self.loser.points == 40


class Game:

    def __init__(self):
        self.players = [Player(), Player()]

    def add_point(self, point_winner):
        opponent = self._opponent(point_winner)
        Point(point_winner, opponent).add_points()

    def get_players(self) -> List[Player]:
        return self.players

    def _opponent(self, player) -> Player:
        return list(filter(lambda x: x != player, self.players))[0]


def convert_advantage(has_advantage):
    return "A" if has_advantage else ""


def display(game: Game):
    print("---------------------------")
    print(f"Points: {game.players[0].points}{convert_advantage(game.players[0].advantage)} | {game.players[1].points}{convert_advantage(game.players[1].advantage)}")
    print("---------------------------")
    print(f"Sets: {game.players[0].sets} | {game.players[1].sets}")
    print("---------------------------")


def update_scores(game):
    while True:
        user_input = input("Enter the number of the player that scored: ")
        try:
            game.add_point(game.players[int(user_input) - 1])
        except (IndexError, ValueError):
            print("Bad input :(")
        display(game)


game = Game()
update_scores(game)
