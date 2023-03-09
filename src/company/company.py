import random as rnd

from user.person import Person

class Company:

    def __init__(self, name: str, age: int) -> None:
        self.id = rnd.randint(0, 9)
        self.person = Person(name, age)

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}('
            f'{self.id}, '
            f'{self.person}'
            f')'
        )