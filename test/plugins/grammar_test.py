from steely.formatting import *
from steely.plugins.grammar import *
from nose.tools import *


def test_capitalisation_requirement():
    data = [
        ("",             True),
        ("hello!",       False),
        ("Hello!",       True),
        ("How are you?", True),
        ("I am well",    True),
        ("i am well",    False),
    ]
    for message, expected_result in data:
        yield assert_equal, expected_result, capitalised_properly(message)


def test_punctuation_requirement():
    data = [
        ("",             True),
        ("test.",        True),
        ("how are you",  False),
        ("how are you?", True),
        ("I am good!",   True),
        ("I am bad",     False),

    ]
    for message, expected_result in data:
        yield assert_equal, expected_result, punctuated_properly(message)


def test_requirement_checker():

    _ALWAYS_TRUE = lambda message: True
    _ALWAYS_FALSE = lambda message: False

    data = [
        ([], []),
        ([Requirement("A", _ALWAYS_TRUE)],  [Pass("A")]),
        ([Requirement("A", _ALWAYS_FALSE)], [Fail("A")]),
        ([Requirement("B", _ALWAYS_TRUE)],  [Pass("B")]),
        ([Requirement("B", _ALWAYS_FALSE)], [Fail("B")]),

        ([Requirement("C", _ALWAYS_FALSE), Requirement("D", _ALWAYS_TRUE)],
         [Fail("C"), Pass("D")]),

        ([Requirement("E", _ALWAYS_TRUE), Requirement("F", _ALWAYS_FALSE)],
         [Pass("E"), Fail("F")]),

        ([Requirement("E", _ALWAYS_TRUE),
          Requirement("F", _ALWAYS_TRUE),
          Requirement("G", _ALWAYS_TRUE)],
         [Pass("E"), Pass("F"), Pass("G")]),
    ]
    for requirements, expected_results in data:
        yield assert_equal, expected_results, compliances(requirements, "")


def test_report_generation():

    _PASS_MESSAGE = lambda name: f"{name}: ✓\n"
    _FAIL_MESSAGE = lambda name: f"{name}: x\n"

    # data = [
    #     ([], ""),
    #     ([Pass("A")], ""),
    #     ([Fail("A")], f"{_FAIL_MESSAGE('A')}"),
    # ]
    # for compliances, expected_report in data:
    #     yield assert_in, expected_report, generate_report(compliances)
