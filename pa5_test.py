from pa5 import euclid_gcd, remove_pairs
import pytest

# @pytest.mark.parametrize("a, b, expected",
#                          [[0, 2, 2],
#                           [3, 0, 3],
#                           [10, 15, 5],
#                           [6, 3, 3],
#                           [42, 36, 6],
#                           [42, 35, 7],
#                           [12, 346, 2],
#                           [1012, 88, 44],
#                           [63, 10943975, 7]])

@pytest.mark.parametrize("a, b, expected",
                         [(0, 2, 2),
                          (3, 0, 3),
                          (10, 15, 5),
                          (6, 3, 3),
                          (42, 36, 6),
                          (42, 35, 7),
                          (12, 346, 2),
                          (1012, 88, 44),
                          (63, 10943975, 7)])

def test_euclid_gcd(a: int, b: int, expected: int) -> None:
    actual = euclid_gcd(a, b)
    assert actual == expected, 'gcd(' + str(a) + ',' + str(b) \
        + ') is ' + str(expected) + '. Got ' + str(actual)


@pytest.mark.parametrize("path, expected",
                         [('W', 'W'),
                          ('', ''),
                          ('ES', 'ES'),
                          ('EW', ''),
                          ('SWE', 'S'),
                          ('NS', ''),
                          ('SSENWE', 'SSEN'),
                          ('EEWSES', 'ESES'),
                          ('ESSNNSWWEWEN', 'ESWN'),
                          ('SWEWEWESS', 'SSS'),
                          ('EEEWWSES','EEWSES')])

def test_remove_pairs(path: str, expected: str) -> None:
    actual = remove_pairs(path)
    assert actual == expected, 'Got: ' + actual + '\nExpected: ' + expected
