#!python3

import random
import time

#---------------------------------------------------------------------#

class WordList:

    def __init__(self,
                 filter=lambda w: len(w) == 5,
                 words_path='/usr/share/dict/words'):
        words = [ word.strip()
                  for word in open(words_path).readlines() ]
        words = set(( word.upper() for word in words
                      if filter(word) ))
        self._words = sorted(words)
        return

    def __len__(self):
        return len(self._words)

    def __contains__(self, word):
        return word in self._words

    def random_word(self, seed=None):
        if seed is None:
            # Daily word game.
            seed = time.strftime('%Y%m%d')
        random.seed(seed)
        return random.choice(self._words)

#--#
