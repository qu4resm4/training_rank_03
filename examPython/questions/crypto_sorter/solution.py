from typing import List


def count_vowels(s: str) -> int:
    return sum(1 for c in s.lower() if c in "aeiou")


def crypto_sorter(words: List[str]) -> List[str]:
    return sorted(
        words,
        key=lambda w: (len(w), [ord(c) for c in w], count_vowels(w))
       )


def main():
    print(f"{crypto_sorter(['apple', 'Banana', 'kiwi', 'orange', 'Egg'])}")


main()
