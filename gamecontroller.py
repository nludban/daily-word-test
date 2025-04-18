#!python3

import gamestate
import wordlist

import typing

#---------------------------------------------------------------------#

class GameController:

    def __init__(self):
        self._wordlist = wordlist.WordList()
        # TODO: Replace dict with persistent layer (mongo?)
        self._games: dict[int, gamestate.GameState] = { }
        return

    def reset_games(self):
        self._games: dict[int, gamestate.GameState] = { }

    def new_game(self, seed: typing.Optional[int]=None) -> int:
        game_id = len(self._games) + 1
        game = gamestate.GameState(
            game_id=game_id,
            word=self._wordlist.random_word(seed or 0),
        )
        self._games[game_id] = game
        return game_id

    def get_game(self, game_id: int) -> gamestate.GameState:
        # (Added for testing.)
        return self._games[game_id]

    def guess(self, game_id: int, word: str) -> gamestate.GameState:
        # TODO: subclass exceptions for readable error handling
        if game_id not in self._games:
            raise KeyError(f'Unknown {game_id=}')
        game = self._games[game_id]
        if word not in self._wordlist:
            raise ValueError(f'Invalid {word=}')
        if game.status.is_terminal:
            raise ValueError('Game is over')
        status = game.guess(word)
        return game

#--#
