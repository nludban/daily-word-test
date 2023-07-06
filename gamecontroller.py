#!python3

import gamestate
import wordlist

import typing

#---------------------------------------------------------------------#

class GameController:

    def __init__(self):
        self._wordlist = wordlist.WordList()
        self._games: dict[int, gamestate.GameState] = { }
        return

    def new_game(self, seed: typing.Optional[int]=None) -> int:
        game_id = len(self._games) + 1
        game = gamestate.GameState(
            game_id=game_id,
            word=self._wordlist.random_word(seed),
        )
        self._games[game_id] = game
        return game_id

    def get_game(self, game_id: int) -> gamestate.GameState:
        return self._games[game_id]

    def guess(self, game_id: int, word: str) -> gamestate.GameState:
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
