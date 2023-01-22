import constant.constant as constant

class TrunicCharacter:
    def __init__(self, character: str = '') -> None:
        self.__edges: list[bool] = []
        if character:
            self.__edges += constant.IPA_TO_TRUNIC_EDGES[character]

    def get_edges(self) -> list[bool]:
        return self.__edges

    def __add__(self, other: 'TrunicCharacter') -> 'TrunicCharacter':
        result: 'TrunicCharacter' = TrunicCharacter()
        max_len: int = max(len(self.__edges), len(other.__edges))

        for i in range(max_len):
            if i < len(self.__edges) and i < len(other.__edges):
                result.__edges += [(self.__edges[i] or other.__edges[i])]
            elif i < len(self.__edges):
                result.__edges += [self.__edges[i]]
            else:
                result.__edges += [other.__edges[i]]
        return result