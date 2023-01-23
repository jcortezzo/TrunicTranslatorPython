from constant.edges import Edge, Edges

# Vowels
OO: Edges = frozenset(Edge.OUT_UP_RIGHT, Edge.OUT_UP_LEFT, Edge.OUT_LEFT, Edge.OUT_DOWN_LEFT)

# Consonants
F: Edges = frozenset(Edge.IN_DOWN_LEFT, Edge.IN_UP_RIGHT, Edge.IN_MID, Edge.IN_DOWN)

# These are wrong... but close enough
IPA_TO_TRUNIC_EDGES: dict[str, Edges] = {
    "æ": OO,
    "ɑr": F
}