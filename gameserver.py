#!/usr/bin/env python3

import gamecontroller
import gamestate

import fastapi
import pydantic

#---------------------------------------------------------------------#

class NewGameResponse(pydantic.BaseModel):
    game_id: int

class GuessRequest(pydantic.BaseModel):
    game_id: int
    guess: str

class GuessResponse(pydantic.BaseModel):
    guess_result: gamestate.GameStatus
    letter1: gamestate.LetterStatus
    letter2: gamestate.LetterStatus
    letter3: gamestate.LetterStatus
    letter4: gamestate.LetterStatus
    letter5: gamestate.LetterStatus
    incorrectly_guessed_letters: list[str]

#---------------------------------------------------------------------#

app = fastapi.FastAPI()
gamec = gamecontroller.GameController()
seed = 3093	# WINDY.

@app.post('/new_game')
async def new_game() -> NewGameResponse:
    return NewGameResponse(game_id=gamec.new_game(seed=seed))

@app.post('/guess')
async def guess(request: GuessRequest) -> GuessResponse:
    # TODO: catch exceptions and map to error responses
    state = gamec.guess(request.game_id, request.guess)
    score = state.score
    response = GuessResponse(
        guess_result = state.status,
        letter1 = score[0],
        letter2 = score[1],
        letter3 = score[2],
        letter4 = score[3],
        letter5 = score[4],
        incorrectly_guessed_letters = [ 'notyet' ],
    )
    return response

#--#
