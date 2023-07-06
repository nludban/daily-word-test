#!python3

import gamecontroller
import gamestate

import mock
import pytest

#---------------------------------------------------------------------#

class TestGameController:

    @pytest.fixture
    def gamec(self):
        yield gamecontroller.GameController()

    @pytest.fixture
    def game_id(self, gamec):
        with mock.patch.object(gamec._wordlist,
                               'random_word') as random_word:
            random_word.return_value = 'WINDY'
            game_id = gamec.new_game()
            yield game_id

    def test_new_game(self, gamec):
        # Create one new game
        game_id_1 = gamec.new_game()
        game_1 = gamec.get_game(game_id_1)
        assert game_1.status == gamestate.GameStatus.INITIAL
        assert game_1.game_id == game_id_1

        # And a second new game
        game_id_2 = gamec.new_game()
        game_2 = gamec.get_game(game_id_2)
        assert game_2.status == gamestate.GameStatus.INITIAL
        assert game_2.game_id == game_id_2

        # They are not the same
        assert game_1.game_id != game_2.game_id

    def test_play(self, gamec, game_id):
        #state = gamec.guess(game_id, 'LEANS')	# Not in words file :^/
        #assert state.game_id == game_id
        #assert not state.status.is_terminal
        state = gamec.guess(game_id, 'WONKY')
        assert not state.status.is_terminal
        state = gamec.guess(game_id, 'WINDY')
        assert state.status.is_terminal

    def test_invalid_game_id(self, gamec):
        with pytest.raises(KeyError):
            gamec.guess(42, 'WINDY')

    def test_invalid_word(self, gamec, game_id):
        with pytest.raises(ValueError):
            gamec.guess(game_id, 'windy')

    def test_game_over(self, gamec, game_id):
        gamec.guess(game_id, 'WINDY')
        with pytest.raises(ValueError):
            gamec.guess(game_id, 'LEANS')
        with pytest.raises(ValueError):
            gamec.guess(game_id, 'WINDY')

#--#
