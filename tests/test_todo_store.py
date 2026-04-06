"""Tests for TodoStore."""

from todo import TodoStore, TodoItem


class TestAdd:
    def test_returns_todo_item_with_correct_description(self):
        store = TodoStore()
        item = store.add("Buy milk")
        assert isinstance(item, TodoItem)
        assert item.description == "Buy milk"
        assert item.completed is False

    def test_ids_are_unique_and_increment(self):
        store = TodoStore()
        first = store.add("First")
        second = store.add("Second")
        third = store.add("Third")
        assert first.id == 1
        assert second.id == 2
        assert third.id == 3


class TestList:
    def test_empty_store_returns_empty_list(self):
        store = TodoStore()
        assert store.list() == []

    def test_returns_items_in_insertion_order(self):
        store = TodoStore()
        store.add("First")
        store.add("Second")
        store.add("Third")
        items = store.list()
        assert [i.description for i in items] == ["First", "Second", "Third"]
