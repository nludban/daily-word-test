#!python3

import gamestate

import pytest

def map_score(score):
    return ''.join([ ls.color[0] for ls in score ])

#---------------------------------------------------------------------#

class TestScoring:

    def test_score_word_guess(self):
        # Example game from wp article.
        score = gamestate.score_word_guess('REBUS', 'ARISE')
        assert map_score(score) == 'GBGBB'
        score = gamestate.score_word_guess('REBUS', 'ROUTE')
        assert map_score(score) == 'OGBGB'
        score = gamestate.score_word_guess('REBUS', 'RULES')
        assert map_score(score) == 'OBGBO'
        score = gamestate.score_word_guess('REBUS', 'REBUS')
        assert map_score(score) == 'OOOOO'

    def test_score_word_guess_dup_guess_letters(self):
        # Guess has two "O"s, only one should match.
        score = gamestate.score_word_guess('WORDS', 'DOORS')
        assert map_score(score) == 'BOGBO'

    def test_score_word_guess_dup_word_letters(self):
        # Answer has two "O"s, score the guess.
        score = gamestate.score_word_guess('DOORS', 'WORDS')
        assert map_score(score) == 'GOBBO'


class TestGameState:

    @pytest.fixture
    def state(self):
        # 2023-07-06 official game word.
        yield gamestate.GameState('WINDY')

    def test_gamestate_initial(self, state):
        assert state.status == gamestate.GameStatus.INITIAL

    def test_gamestate_winner(self, state):
        # First time playing.
        status = state.guess('LEANS')
        assert status == gamestate.GameStatus.NOPE
        assert map_score(state.score) == 'GGGBG'

        status = state.guess('WONKY')
        assert status == gamestate.GameStatus.NOPE
        assert map_score(state.score) == 'OGOGO'

        status = state.guess('WINDY')
        assert status == gamestate.GameStatus.WINNER
        assert map_score(state.score) == 'OOOOO'

    def test_gamestate_loser(self, state):
        # 5 bad guesses.
        for k in range(5):
            status = state.guess('LEANS')
            assert status == gamestate.GameStatus.NOPE
        # And lose after 6th bad guess.
        status = state.guess('LEANS')
        assert status == gamestate.GameStatus.LOSER

#--#
