class Node:

    def __init__(self, key: int | str | tuple, value):
        self.key = key
        self.value = value
        self.next = None