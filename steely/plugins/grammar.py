from collections import namedtuple


Requirement = namedtuple("Requirement", "name checker")


def _result_type(symbol):
    class Result:

        def __init__(self, name):
            self.name = name

        def __eq__(self, other):
            types_match = type(self) == type(other)
            names_match = self.name == other.name
            return types_match and names_match

        def __str__(self, other):
            return f"{self.name}: {self.symbol}\n"

    return Result


Pass = _result_type("✓")
Fail = _result_type("x")


def generate_report(compliances):
    pass

def _all_compliant(compliances):
    return


def compliances(requirements, message):
    GET_COMPLIANCE = lambda requirement: _compliance(requirement, message)
    return list(map(GET_COMPLIANCE, requirements))


def _compliance(requirement, message):
    compliant = requirement.checker(message)
    result_type = Pass if compliant else Fail
    return result_type(requirement.name)


def _compliant_if_empty(function):
    return lambda message: True if message == "" else function(message)


@_compliant_if_empty
def capitalised_properly(message):
    return message[0].isupper()


@_compliant_if_empty
def punctuated_properly(message):
    PUNCTUATION = [".", "?", "!"]
    return message[-1] in PUNCTUATION
