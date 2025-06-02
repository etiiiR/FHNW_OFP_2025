from typing import Callable


def mal(x: int) -> Callable[[int], int]:
    def mal_x(y: int) -> int:
        return x * y

    return mal_x


def multipliziere_liste_funktional(lst: list, k: int) -> list:
    mal_k = mal(k)
    print(list(map(mal_k, lst)))


multipliziere_liste_funktional([10, 20], 5)
