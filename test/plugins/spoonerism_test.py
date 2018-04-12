from nose.tools import *
from steely.plugins.spoonerism import *


def test_spoonerising_bunches_of_words():
    data = [

        # single word is unaffected
        (["hello"], ["hello"]),
        
        # first letters get swapped
        (["Bad", "dog"],      ["dad", "Bog"]),
        (["Good", "boy"],     ["bood", "Goy"]),
        (["Go", "to", "bed"], ["bo", "to", "Ged"]),

        # complicated beginning patterns get swapped
        (["Chad", "Robins"],       ["Rad", "Chobins"]),
        (["chad", "Robins"],       ["Rad", "chobins"]),
        (["das", "phat"],          ["phas", "dat"]),
        (["don't", "say", "that"], ["thon't", "say", "dat"]),
        (["flash", "back"],        ["bash", "flack"]),
    ]
    for words, expected in data:
        yield assert_equal, expected, get_spoonerised(words)
