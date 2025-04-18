import gameserver
import gamestate

import mock
import pytest

from fastapi.testclient import TestClient


class TestGameServer:

    @pytest.fixture
    def gamec(self):
        yield gameserver.gamec
        gameserver.gamec.reset_games()

    @pytest.fixture
    def client(self, gamec):
        yield TestClient(gameserver.app)

    @pytest.fixture
    def game_id(self, client):
        rsp = client.post('/new_game')
        assert rsp.status_code == 200
        assert rsp.json() == {
            'game_id': 1,
        }

    def test_new_game(self, client):
        # Create one new game
        game_id_1 = client.post('/new_game').json()['game_id']
        assert game_id_1 == 1

        # And a second new game
        game_id_2 = client.post('/new_game').json()['game_id']
        assert game_id_2 == 2

    def test_play(self, client):
        #new_game = gameserver.NewGameResponse.parse_raw( -- (deprecated)
        # model_validate_json
        new_game = gameserver.NewGameResponse.model_validate_json(
            client.post('/new_game').text)
        # model_validate
        #new_game = gameserver.NewGameResponse.model_validate(
        #    client.post('/new_game').json())
        assert new_game.game_id == 1

        #state = gamec.guess(game_id, 'LEANS')	# Not in words file :^/
        #assert state.game_id == game_id
        #assert not state.status.is_terminal

        #state = gamec.guess(game_id, 'WONKY')
        guess_1 = gameserver.GuessResponse.model_validate_json(
            client.post(
                '/guess',
                json=dict(gameserver.GuessRequest(
                    game_id = 1,
                    guess = 'WONKY'))
            ).text
        )
        assert not guess_1.guess_result.is_terminal

        #state = gamec.guess(game_id, 'WINDY')
        guess_2 = gameserver.GuessResponse.model_validate_json(
            client.post(
                '/guess',
                json=dict(gameserver.GuessRequest(
                    game_id = 1,
                    guess = 'WINDY'))
            ).text
        )
        assert guess_2.guess_result.is_terminal

    def test_invalid_game_id(self, client):
        rsp = client.post(
            '/guess',
            json=dict(gameserver.GuessRequest(
                game_id = 42,
                guess = 'WINDY'))
        )
        assert rsp.status_code == 404

    def test_invalid_word(self, client):
        client.post('/new_game')
        rsp = client.post(
            '/guess',
            json=dict(gameserver.GuessRequest(
                game_id = 1,
                guess = 'windy'))
        )
        assert rsp.status_code == 400
        #with pytest.raises(ValueError):
        #    gamec.guess(game_id, 'windy')

    def test_game_over(self, client):
        client.post('/new_game')

        #gamec.guess(game_id, 'WINDY')
        client.post(
            '/guess',
            json=dict(gameserver.GuessRequest(
                game_id = 1,
                guess = 'WINDY'))
        )

        # Try an invalid word - happens to check first
        #with pytest.raises(ValueError):
        #    gamec.guess(game_id, 'LEANS')
        rsp_1 = client.post(
            '/guess',
            json=dict(gameserver.GuessRequest(
                game_id = 1,
                guess = 'LEANS'))
        )
        assert rsp_1.status_code == 400
        assert rsp_1.json() == {'detail': "Invalid word='LEANS'"}

        # A new valid word fails
        rsp_2 = client.post(
            '/guess',
            json=dict(gameserver.GuessRequest(
                game_id = 1,
                guess = 'SNAIL'))
        )
        assert rsp_2.status_code == 400
        assert rsp_2.json() == {'detail': 'Game is over'}

        # The correct guess fails
        #with pytest.raises(ValueError):
        #    gamec.guess(game_id, 'WINDY')
        rsp_3 = client.post(
            '/guess',
            json=dict(gameserver.GuessRequest(
                game_id = 1,
                guess = 'WINDY'))
        )
        assert rsp_3.status_code == 400
        assert rsp_3.json() == {'detail': 'Game is over'}
