from dataclasses import dataclass
from typing import Union, Optional
from enum import IntEnum


class Color(IntEnum):
    BLACK = 0
    RED = 1


@dataclass
class Leaf:
    color = Color.BLACK


@dataclass
class Node:
    key: any
    left: Union["Node", Leaf] = Leaf()
    right: Union["Node", Leaf] = Leaf()
    parent: Union["Node", Leaf] = Leaf()
    color: Color = Color.RED


class RedBlackTree:
    def __init__(self) -> None:
        self.NIL: Leaf = Leaf()
        self.root: Union[Node, Leaf] = self.NIL

    def inorder_traversal(self) -> None:
        return self._inorder_traversal(node=self.root)

    def find_node(self, key: any) -> Optional[Node]:
        current = self.root

        while isinstance(current, Node):
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current

        return None

    def insert_node(self, key: any) -> None:
        new_node = Node(key=key, color=Color.RED)
        parent: Union[Node, Leaf] = self.NIL
        current: Union[Node, Leaf] = self.root

        while isinstance(current, Node):
            parent = current
            if new_node.key < current.key:
                current = current.left
            elif new_node.key > current.key:
                current = current.right
            else:
                print("[ERROR] Duplicate key.")
                return

        new_node.parent = parent
        if isinstance(parent, Leaf):
            new_node.color = Color.BLACK
            self.root = new_node
        else:
            if new_node.key < parent.key:
                parent.left = new_node
            else:
                parent.right = new_node

        self._insert_fixup(new_node)

    def delete_node(self, key: any) -> None:
        if (deleting_node := self.find_node(key=key)) and (
                not isinstance(deleting_node, Leaf)
        ):
            original_color = deleting_node.color

            # Case 1: no clildren or 1 right child
            if isinstance(deleting_node.left, Leaf):
                replacing_node = deleting_node.right
                self._transplant(
                    deleting_node=deleting_node, replacing_node=replacing_node
                )

                if original_color == Color.BLACK:
                    if isinstance(replacing_node, Node):
                        self._delete_fixup(fixing_node=replacing_node)

            # Case 2: only one left child
            elif isinstance(deleting_node.right, Leaf):
                replacing_node = deleting_node.left
                self._transplant(
                    deleting_node=deleting_node, replacing_node=replacing_node
                )

                if original_color == Color.BLACK:
                    self._delete_fixup(fixing_node=replacing_node)

            # Case 3: two children
            else:
                replacing_node = self.minimum_element(deleting_node.right)
                original_color = replacing_node.color
                replacing_replacement = replacing_node.right

                if replacing_node.parent != deleting_node:
                    self._transplant(replacing_node, replacing_node.right)
                    replacing_node.right = deleting_node.right
                    replacing_node.right.parent = replacing_node

                self._transplant(deleting_node, replacing_node)
                replacing_node.left = deleting_node.left
                replacing_node.left.parent = replacing_node
                replacing_node.color = deleting_node.color

                if original_color == Color.BLACK:
                    if isinstance(replacing_replacement, Node):
                        self._delete_fixup(fixing_node=replacing_replacement)

    @staticmethod
    def minimum_element(node: Node) -> Node:
        current = node
        while isinstance(current.left, Node):
            current = current.left
        return current

    @staticmethod
    def maximum_element(node: Node) -> Node:
        current = node
        while isinstance(current.right, Node):
            current = current.right
        return current

    def _inorder_traversal(self, node: Node) -> None:
        if isinstance(node, Node):
            self._inorder_traversal(node.left)
            print(str(node.key) + "(" + str(node.color) + ")", end=" ")
            self._inorder_traversal(node.right)

    def _left_rotate(self, node_x: Node) -> None:
        node_y = node_x.right
        if isinstance(node_y, Leaf):
            print("[ERROR] node_x.right must be instance of a node class.")
            return

        node_x.right = node_y.left
        if isinstance(node_y.left, Node):
            node_y.left.parent = node_x
        node_y.parent = node_x.parent

        if isinstance(node_x.parent, Leaf):
            self.root = node_y
        elif node_x == node_x.parent.left:
            node_x.parent.left = node_y
        else:
            node_x.parent.right = node_y

        node_y.left = node_x
        node_x.parent = node_y

    def _right_rotate(self, node_x: Node) -> None:
        node_y = node_x.left
        if isinstance(node_y, Leaf):
            print("[ERROR] node_x.left must be instance of a node class.")
            return

        node_x.left = node_y.right
        if isinstance(node_y.right, Node):
            node_y.right.parent = node_x
        node_y.parent = node_x.parent

        if isinstance(node_x.parent, Leaf):
            self.root = node_y
        elif node_x == node_x.parent.right:
            node_x.parent.right = node_y
        else:
            node_x.parent.left = node_y

        node_y.right = node_x
        node_x.parent = node_y

    def _insert_fixup(self, fixing_node: Node) -> None:
        while fixing_node.parent.color == Color.RED:
            if fixing_node.parent == fixing_node.parent.parent.left:
                parent_sibling = fixing_node.parent.parent.right
                if parent_sibling.color == Color.RED:  # Case 1
                    fixing_node.parent.color = Color.BLACK
                    parent_sibling.color = Color.BLACK
                    fixing_node.parent.parent.color = Color.RED
                    fixing_node = fixing_node.parent.parent
                else:
                    if fixing_node == fixing_node.parent.right:  # Case 2
                        fixing_node = fixing_node.parent
                        self._left_rotate(fixing_node)
                    fixing_node.parent.color = Color.BLACK  # Case 3
                    fixing_node.parent.parent.color = Color.RED
                    self._right_rotate(fixing_node.parent.parent)
            else:
                parent_sibling = fixing_node.parent.parent.left
                if parent_sibling.color == Color.RED:  # Case 4
                    fixing_node.parent.color = Color.BLACK
                    parent_sibling.color = Color.BLACK
                    fixing_node.parent.parent.color = Color.RED
                    fixing_node = fixing_node.parent.parent
                else:
                    if fixing_node == fixing_node.parent.left:  # Case 5
                        fixing_node = fixing_node.parent
                        self._right_rotate(fixing_node)
                    fixing_node.parent.color = Color.BLACK  # Case 6
                    fixing_node.parent.parent.color = Color.RED
                    self._left_rotate(fixing_node.parent.parent)

        self.root.color = Color.BLACK

    def _delete_fixup(self, fixing_node: Union[Leaf, Node]) -> None:
        while (fixing_node is not self.root) and (fixing_node.color == Color.BLACK):
            if fixing_node == fixing_node.parent.left:
                sibling = fixing_node.parent.right

            # Case 1: the sibling is red.
            if sibling.color == Color.RED:
                sibling.color == Color.BLACK
                fixing_node.parent.color = Color.RED
                self._left_rotate(fixing_node.parent)
                sibling = fixing_node.parent.right

            # Case 2: the sibling is black and its children are black.
            if (sibling.left.color == Color.BLACK) and (
                    sibling.right.color == Color.BLACK
            ):
                sibling.color = Color.RED
                fixing_node = fixing_node.parent  # new fixing node

            # Cases 3 and 4: the sibling is black and one of
            # its child is red and the other is black.
            else:
                # Case 3: the sibling is black and its left child is red.
                if sibling.right.color == Color.BLACK:
                    sibling.left.color = Color.BLACK
                    sibling.color = Color.RED
                    self._right_rotate(node_x=sibling)

                # Case 4: the sibling is black and its right child is red.
                sibling.color = fixing_node.parent.color
                fixing_node.parent.color = Color.BLACK
                sibling.right.color = Color.BLACK
                self._left_rotate(node_x=fixing_node.parent)
                # Once we are here, all the violation has been fixed, so
                # move to the root to terminate the loop.
                fixing_node = self.root
        else:
            sibling = fixing_node.parent.left

            # Case 5: the sibling is red.
            if sibling.color == Color.RED:
                sibling.color == Color.BLACK
                fixing_node.parent.color = Color.RED
                self._right_rotate(node_x=fixing_node.parent)
                sibling = fixing_node.parent.left

            # Case 6: the sibling is black and its children are black.
            if (sibling.right.color == Color.BLACK) and (
                    sibling.left.color == Color.BLACK
            ):
                sibling.color = Color.RED
                fixing_node = fixing_node.parent
            else:
                # Case 7: the sibling is black and its right child is red.
                if sibling.left.color == Color.BLACK:
                    sibling.right.color = Color.BLACK
                    sibling.color = Color.RED
                    self._left_rotate(node_x=sibling)
                # Case 8: the sibling is black and its left child is red.
                sibling.color = fixing_node.parent.color
                fixing_node.parent.color = Color.BLACK
                sibling.left.color = Color.BLACK
                self._right_rotate(node_x=fixing_node.parent)
                # Once we are here, all the violation has been fixed, so
                # move to the root to terminate the loop.
                fixing_node = self.root

        fixing_node.color = Color.BLACK

    def _transplant(self, deleting_node: Node, replacing_node: Union[Node, Leaf]) -> None:
        if isinstance(deleting_node.parent, Leaf):
            self.root = replacing_node
        elif deleting_node == deleting_node.parent.left:
            deleting_node.parent.left = replacing_node
        else:
            deleting_node.parent.right = replacing_node

        if isinstance(replacing_node, Node):
            replacing_node.parent = deleting_node.parent
