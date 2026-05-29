#1. Primary sort: By string length (shortest first)
#2. Secondary sort: ASCII order, except letters are compared case-insensitively
#   (for strings of same length)
#3. Tertiary sort: By number of vowels (ascending, for same length and lexically equal)
#4. Equal strings will appear in the same order as in the input list.
from functools import cmp_to_key


def cryptic_sorter(strings: list[str]) -> list[str]:

    def conferir_ascii(string1: str, string2: str) -> int:
        if len(string1) != len(string2):
            return len(string1) - len(string2)
        else:
            for index in range(0, len(string1)):
                if string1[index].upper() != string2[index].upper():
                    return (
                        ord(string1[index].upper()) - ord(string2[index].upper())
                        )
        return 0

    ordenado = sorted(strings, key=cmp_to_key(conferir_ascii))

    return ordenado


result = cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"])
print(result)


result = cryptic_sorter(["aaa", "bbb", "AAA", "BBB"])
print(result)


result = cryptic_sorter(["hello", "world", "hi", "test"])
print(result)

result = cryptic_sorter([])
print(result)

result = cryptic_sorter([""])
print(result)
