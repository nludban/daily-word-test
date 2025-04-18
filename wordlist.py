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
        words_set = set(( word.upper() for word in words
                          if filter(word) ))
        self._words = sorted(words_set)
        return

    def __len__(self):
        return len(self._words)

    def __contains__(self, word: str) -> bool:
        return word in self._words

    def random_word(self, seed: int=0) -> str:
        s = seed or time.strftime('%Y%m%d')
        random.seed(s)
        return random.choice(self._words)


if __name__ == '__main__':
    import sys
    target = sys.argv[1].upper()
    wl = WordList()
    for seed in range(100_000):
        if wl.random_word(seed) == target:
            print(seed)
            break
    else:
        print('No seed found.')

#--#
