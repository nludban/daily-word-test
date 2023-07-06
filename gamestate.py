#!python3

import dataclasses
import enum

#---------------------------------------------------------------------#

class LetterStatus(enum.Enum):
    CORRECT = 'correct'		# Orange (Green)
    CLOSE = 'wrong_position'	# Blue (Yellow)
    NOPE = 'incorrect'		# Gray

    @property
    def color(self):
        return {
            self.CORRECT.value: 'Orange',
            self.CLOSE.value: 'Blue',
            self.NOPE.value: 'Gray',
        }[self.value]


def score_word_guess(word, guess):
    # Assume nothing matches
    score = [ LetterStatus.NOPE ] * 5
    resid = list(word)
    # Exact matches are CORRECT
    for i, ( w, g ) in enumerate(zip(word, guess)):
        if w == g:
            score[i] = LetterStatus.CORRECT
            resid.remove(w)
    # Matching leftovers are CLOSE
    for i, w in enumerate(guess):
        if score[i] == LetterStatus.NOPE and w in resid:
            score[i] = LetterStatus.CLOSE
            resid.remove(w)
    return score


class GameStatus(enum.Enum):
    INITIAL = 'new'
    NOPE = 'incorrect'
    WINNER = 'correct'
    LOSER = 'lost'


@dataclasses.dataclass
class GameState:

    word: str
    game_id: int = None
    guesses: list[str] = dataclasses.field(default_factory=list)

    def guess(self, word: str) -> GameStatus:
        self.guesses.append(word)
        return self.status

    @property
    def status(self) -> GameStatus:
        if not self.guesses:
            return GameStatus.INITIAL
        if self.guesses[-1] == self.word:
            return GameStatus.WINNER
        if len(self.guesses) == 6:
            return GameStatus.LOSER
        return GameStatus.NOPE

    @property
    def score(self):
        return score_word_guess(self.word, self.guesses[-1])

#--#
