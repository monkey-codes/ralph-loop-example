"""Simple in-memory TODO CLI application."""

from dataclasses import dataclass


class TodoNotFoundError(Exception):
    """Raised when a TODO item with the given ID does not exist."""


@dataclass
class TodoItem:
    id: int
    description: str
    completed: bool = False


class TodoStore:
    def __init__(self):
        self._items: dict[int, TodoItem] = {}
        self._next_id = 1

    def add(self, description: str) -> TodoItem:
        item = TodoItem(id=self._next_id, description=description)
        self._items[self._next_id] = item
        self._next_id += 1
        return item

    def list(self) -> list[TodoItem]:
        return list(self._items.values())


def main():
    store = TodoStore()
    print("TODO App")
    print("Commands: add, list, done, edit, delete, quit/exit")

    while True:
        try:
            line = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not line:
            continue

        parts = line.split(maxsplit=1)
        command = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        if command in ("quit", "exit"):
            break
        elif command == "add":
            if not arg:
                print("Usage: add <description>")
                continue
            item = store.add(arg)
            print(f"Added TODO #{item.id}: {item.description}")
        elif command == "list":
            items = store.list()
            if not items:
                print("No TODOs yet.")
            else:
                for item in items:
                    status = "[x]" if item.completed else "[ ]"
                    print(f"  {item.id}. {status} {item.description}")
        else:
            print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
