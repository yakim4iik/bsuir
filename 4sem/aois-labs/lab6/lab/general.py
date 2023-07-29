from typing import List, Optional
from lab.constants import INCREASE, LENGTH
from prettytable import PrettyTable


class HashNode:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.count_elements = 0
        self.table: List[Optional[HashNode]] = [None] * size

    def __get_hash_address(self, key):
        return hash(key) % self.size

    def insert(self, key: str, value: str) -> None:
        if self.count_elements == self.size:
            self.change_length()
        hash_address = self.__get_hash_address(key)
        curr_node = self.table[hash_address]
        while curr_node is not None:
            if curr_node.key == key:
                curr_node.value = value
                return
            curr_node = curr_node.next
        if self.table[hash_address] is None:
            self.table[hash_address] = HashNode(key, value)
            self.count_elements += 1
        else:
            self._push_to_same_hash_list(self.table[hash_address], key, value)
            self.count_elements += 1

    def find(self, key: str) -> str:
        hash_address = self.__get_hash_address(key)

        curr_node = self.table[hash_address]
        while curr_node is not None:
            if curr_node.key == key:
                return curr_node.value
            curr_node = curr_node.next

        print(f"\"{key}\" no such element in hash table")
        return ""

    def delete(self, key: str) -> None:
        hash_address = self.__get_hash_address(key)
        curr_node = self.table[hash_address]

        if curr_node is None:
            return
        elif curr_node.key == key and curr_node.next is None:
            self.table[hash_address] = None
            self.count_elements -= 1
            return
        elif curr_node.key == key and curr_node.next is not None:
            self.table[hash_address] = curr_node.next
            self.count_elements -= 1
            return

        while curr_node is not None:
            if curr_node.key == key:
                curr_node.previous.next = curr_node.next
                if curr_node.next is not None:
                    curr_node.next.previous = curr_node.previous
                return
            curr_node = curr_node.next

    def _push_to_same_hash_list(self, node: HashNode, key: str, value: str) -> None:
        new_node = HashNode(key, value)
        node.previous = new_node
        new_node.next = node
        self.table[hash(key) % self.size] = new_node

    def change_length(self):
        self.size += INCREASE
        new_table: List[Optional[HashNode]] = [None] * self.size
        for i in range(self.size - INCREASE):
            if self.table[i] is not None:
                curr_node = self.table[i]
                while curr_node is not None:
                    next_node = curr_node.next
                    curr_hash = hash(curr_node.key)
                    position = curr_hash % self.size
                    if new_table[position] is None:
                        new_table[position] = curr_node
                        curr_node.next = None
                        curr_node.previous = None
                    else:
                        self._push_to_same_hash_list_copy(new_table[position], curr_node.key,
                                                          curr_node.value, new_table)
                    curr_node = next_node
        self.table = new_table

    def _push_to_same_hash_list_copy(self, node: HashNode, key: str, value: str, new_table) -> None:
        new_node = HashNode(key, value)
        node.previous = new_node
        new_node.next = node
        new_table[hash(key) % self.size] = new_node

    def print_table(self) -> None:
        table = PrettyTable()
        table.field_names = ["Hash Address", "Key", "Value"]

        for i in range(self.size):
            if self.table[i] is not None:
                curr_node = self.table[i]
                while curr_node is not None:
                    table.add_row([
                        hash(curr_node.key) % self.size,
                        curr_node.key,
                        curr_node.value if len(curr_node.value) < LENGTH else curr_node.value[:LENGTH] + '...'
                    ])
                    curr_node = curr_node.next

        print(table)
