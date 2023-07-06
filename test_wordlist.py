#!python3

import wordlist

import mock
import pytest

#---------------------------------------------------------------------#

class TestWordList:

    @pytest.fixture
    def wordlist(self):
        yield wordlist.WordList()

    def test_word_count(self, wordlist):
        # egrep '^.....$' /usr/share/dict/words
        # | tr '[:lower:]' '[:upper:]'
        # | sort -u | wc -l
        assert len(wordlist) == 9979

    def test_contains_valid_word(self, wordlist):
        assert 'CURLY' in wordlist
        assert 'WINDY' in wordlist

    def test_does_not_contain_invalid_words(self, wordlist):
        assert 'windy' not in wordlist	# Not capitalized
        assert 'FUBAR' not in wordlist	# Not a "real word"

    def test_random_word_seeds(self, wordlist):
        assert wordlist.random_word(1) == 'CURLY'
        assert wordlist.random_word(2) == 'BAUCH'
        assert wordlist.random_word(3) == 'HEMOL'
        assert wordlist.random_word(12365) == 'WINDY'

    def test_random_word_today(self, wordlist):
        with mock.patch('wordlist.random') as random:
            random.choice.return_value = 'WINDY'
            assert wordlist.random_word() == 'WINDY'

#--#
