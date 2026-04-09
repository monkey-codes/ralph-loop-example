"""Tests for TodoStore."""

import pytest

from todo import TodoStore, TodoItem, TodoNotFoundError


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


class TestComplete:
    def test_sets_completed_true(self):
        store = TodoStore()
        store.add("Task")
        item = store.complete(1)
        assert item.completed is True

    def test_returns_updated_item(self):
        store = TodoStore()
        store.add("Task")
        item = store.complete(1)
        assert item.id == 1
        assert item.description == "Task"

    def test_re_completing_is_noop(self):
        store = TodoStore()
        store.add("Task")
        store.complete(1)
        item = store.complete(1)
        assert item.completed is True

    def test_unknown_id_raises(self):
        store = TodoStore()
        with pytest.raises(TodoNotFoundError):
            store.complete(99)


class TestUpdate:
    def test_changes_description(self):
        store = TodoStore()
        store.add("Old")
        item = store.update(1, "New")
        assert item.description == "New"

    def test_returns_updated_item(self):
        store = TodoStore()
        store.add("Old")
        item = store.update(1, "New")
        assert item.id == 1

    def test_unknown_id_raises(self):
        store = TodoStore()
        with pytest.raises(TodoNotFoundError):
            store.update(99, "Nope")


class TestDelete:
    def test_removes_item(self):
        store = TodoStore()
        store.add("Task")
        store.delete(1)
        assert store.list() == []

    def test_does_not_renumber_remaining(self):
        store = TodoStore()
        store.add("First")
        store.add("Second")
        store.add("Third")
        store.delete(2)
        ids = [i.id for i in store.list()]
        assert ids == [1, 3]

    def test_unknown_id_raises(self):
        store = TodoStore()
        with pytest.raises(TodoNotFoundError):
            store.delete(99)
