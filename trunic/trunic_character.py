import constant.constant as constant

class TrunicCharacter:

    def __init__(self, character: str) -> None:
        self.__edges: list[bool] = constant.IPA_TO_TRUNIC_EDGES[character]

    def get_edges(self) -> list[bool]:
        return self.__edges