import sys
from itertools import combinations, permutations

import pytest

from symspellpy.editdistance import Levenshtein, Ukkonen


@pytest.fixture(params=[0, 1, 3, sys.maxsize])
def get_strings(request):
    alphabet = "abcd"
    strings = [""]
    for i in range(1, len(alphabet) + 1):
        for combi in combinations(alphabet, i):
            strings += ["".join(p) for p in permutations(combi)]
    yield strings, request.param


class TestUkkonen:
    def test_distance(self):
        """Sample test cases used by the original repo."""
        cases = [
            ("ABCDE", "FGHIJ", 5),
            ("AVERY", "GARVEY", 3),
            ("ADCROFT", "ADDESSI", 5),
            ("BAIRD", "BAISDEN", 3),
            ("BOGGAN", "BOGGS", 2),
            ("CLAYTON", "CLEARY", 5),
            ("DYBAS", "DYCKMAN", 4),
            ("EMINETH", "EMMERT", 4),
            ("GALANTE", "GALICKI", 4),
            ("HARDIN", "HARDING", 1),
            ("KEHOE", "KEHR", 2),
            ("LOWRY", "LUBARSK", 5),
            ("MAGALLAN", "MAGANA", 3),
            ("MAYO", "MAYS", 1),
            ("MOENY", "MOFFETT", 4),
            ("PARE", "PARENT", 2),
            ("RAMEY", "RAMFREY", 2),
            ("ofosid", "daej", 6),
            ("of", "lisib", 5),
            ("nuhijoow", "ru", 7),
            ("w", "4", 1),
            ("", "", 0),
            ("", "wat", 3),
            ("wat", "", 3),
            ("wat", "wat", 0),
            ("Ukkonen", "Levenshtein", 8),
        ]
        ukkonen = Ukkonen()
        for case in cases:
            assert case[2] == ukkonen.distance(case[0], case[1], sys.maxsize)

    def test_match_levenshtein(self, get_strings):
        leven = Levenshtein()
        ukkonen = Ukkonen()
        strings, max_distance = get_strings
        for s1 in strings:
            for s2 in strings:
                assert leven.distance(s1, s2, max_distance) == ukkonen.distance(
                    s1, s2, max_distance
                )
