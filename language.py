import cmudict
from string import digits, punctuation
from trunic.trunic_character import TrunicCharacter
from trunic.trunic_word import TrunicWord

VOWEL_STR: str = 'vowel'
ALL_PHONES: dict[str, list[str]] = {}
for phone, part in cmudict.phones():
    ALL_PHONES.setdefault(phone, []).append(part)

CMU_DICTIONARY: dict[str, list[list[str]]] = cmudict.dict()

REMOVE_DIGITS: dict[int, int | None] = str.maketrans('', '', digits + punctuation)

def get_trunic_word_from_phones_list(syllables: list[str]) -> list[TrunicCharacter]:
    syllables = list(map(lambda syllable: to_alpha(syllable).upper(), syllables))
    print(syllables)
    trunic_characters: list[TrunicCharacter] = []
    for i in range(len(syllables)):
        combine: bool = False
        needs_dot: bool = False
        character = TrunicCharacter(syllables[i])
        if i + 1 < len(syllables):
            combine = is_vowel(syllables[i]) == is_vowel(syllables[i + 1])
            needs_dot = is_vowel(syllables[i])
        if combine:
            character = character + TrunicCharacter(syllables[i])
            i = i + 1
        if needs_dot:
            print("Placeholder for adding dot")
        trunic_characters += [character]
    return trunic_characters


def get_word_phones(word: str) -> list[str]:
    return CMU_DICTIONARY[word][0]

def to_alpha(s: str) -> str:
    #return "".join(filter(lambda c: c.isalpha(), s))
    return s.translate(REMOVE_DIGITS)

def is_vowel(s: str) -> bool:
    if s not in ALL_PHONES:
        raise ValueError(f"Token {s} is not a valid CMU phone!")
    else:
        return ALL_PHONES[s][0] == VOWEL_STR