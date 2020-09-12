from dataclasses import dataclass
from typing import NamedTuple
from collections import namedtuple


@dataclass(frozen=True)
class Name:
    first_name: str
    last_name: str


class Money(NamedTuple):
    currency: str
    value: int


Line = namedtuple('Line', ['sku', 'qty'])


fiver = Money('INR', 5)
tenner = Money('INR', 10)


def test_equality_among_value_objects():
    assert Name('Ashish', 'Sheelavantar') == Name('Ashish', 'Sheelavantar')
    assert Name('Ashish', 'Sheelavantar') != Name('Another', 'Ashish')
    assert Money('gbp', 10) == Money('gbp', 10)
    assert Line('Desk', 3) == Line('Desk', 3)


# def test_can_add_objects_of_same_currency():
#     assert fiver * 2 == tenner


class Person:
    def __init__(self, name: Name):
        self.name = name


def test_harry_is_barry():
    harry = Person(Name('Harry', 'Smithsonian'))
    print(harry.name)
    barry = harry
    barry.name = Name('Barry', 'Smithsonian')
    print(barry.name)
    print(harry.name)
    assert harry is barry and barry is harry

