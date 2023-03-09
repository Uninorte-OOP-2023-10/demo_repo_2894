class Person:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}('
            f'{self.name}, '
            f'{self.age}'
            f')'
        )
    
    def hello(self) -> str:
        return f'Hello, my name is {self.name}'