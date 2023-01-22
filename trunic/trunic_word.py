from trunic.trunic_character import TrunicCharacter

class TrunicWord:
    def __init__(self, characters: list[TrunicCharacter]) -> None:
        self.__characters: list[TrunicCharacter] = characters

    def get_characters(self) -> list[TrunicCharacter]:
        """
        TODO: Make class iterable
        """
        return self.__characters