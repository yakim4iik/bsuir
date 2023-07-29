from rbt import *


def display_menu() -> None:
    print("1. Insert node")
    print("2. Delete node")
    print("3. Search node")
    print("4. In-order traversal")
    print("5. Exit")


def print_tree(node, level=0, indent="   "):
    if isinstance(node, Node):
        print_tree(node.right, level + 1)

        print(indent * level + f"({node.key}, {node.color})")
        print_tree(node.left, level + 1)
    elif isinstance(node, Leaf):
        print(indent * level + "(Leaf, 0)")

def get_input() -> Optional[int]:
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("Invalid choice. Please enter a number.")
        return None


def insert_node(tree: RedBlackTree) -> None:
    key = int(input("Enter the key to insert: "))
    tree.insert_node(key)
    print_tree(tree.root)
    print(f"Node with key {key} has been inserted.")


def delete_node(tree: RedBlackTree) -> None:
    key = int(input("Enter the key to delete: "))
    tree.delete_node(key)
    print_tree(tree.root)
    print(f"Node with key {key} has been deleted.")


def search_node(tree: RedBlackTree) -> None:
    key = int(input("Enter the key to search: "))
    node = tree.find_node(key)
    if node:
        print(f"Node with key {key} exists.")
    else:
        print(f"Node with key {key} does not exist.")


def inorder_traversal(tree: RedBlackTree) -> None:
    print("In-order traversal:")
    tree.inorder_traversal()
    print()


def main() -> None:
    tree = RedBlackTree()

    while True:
        display_menu()
        choice = get_input()

        if choice == 1:
            insert_node(tree)
        elif choice == 2:
            delete_node(tree)
        elif choice == 3:
            search_node(tree)
        elif choice == 4:
            inorder_traversal(tree)
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")


if __name__ == "__main__":
    main()
