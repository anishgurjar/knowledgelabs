
from collections import defaultdict


def main(s: str, t: str):

    smap, tmap = defaultdict(int), defaultdict(int)

    for char in s:
        smap[char] += 1

    for char in t:
        tmap[char] += 1

    return smap == tmap

if __name__ == "__main__":
    main()