from typing import Any, Union
from copy import deepcopy


class List:
    def __init__(self, *args) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        for arg in args:
            self.push(arg)

    def push(self, x: Any) -> None:
        if not self.isEmpty():
            tail = Node(x, self.tail, None)
            self.tail.next = tail
            self.tail = self.tail.next
        else:
            self.head = Node(x)
            self.tail = self.head
        self.size += 1

    def pop(self, index: int = None) -> Any:
        if index is None:
            index = self.size - 1
        elif type(index) != int:
            raise TypeError(f'{type(index)} object cannot be interpreted as an integer')
        elif not (0 <= abs(index) < len(self)):
            raise IndexError('pop index out of range')
        else:
            index %= self.size
        node = self.getNode(index)
        deleted = node.data
        if self.size == 1:
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == len(self) - 1:
            self.tail.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.size -= 1
        return deleted

    def insert(self, data: Any, index: int) -> None:
        if type(index) != int:
            raise TypeError
        if not (0 <= index <= self.size) or self.isEmpty():
            raise IndexError
        if index == 0:
            self.head = Node(data, None, self.head)
            self.head.next.prev = self.head
        elif index == self.size:
            NewNode = Node(data, self.tail, None)
            self.tail.next = NewNode
            self.tail = NewNode
        else:
            NextNode = self.getNode(index)
            PrevNode = NextNode.prev
            NewNode = Node(data, PrevNode, NextNode)
            PrevNode.next = NextNode.prev = NewNode
        self.size += 1

    def getNode(self, index: int):
        index %= self.size
        if index < self.size // 2:
            node = self.head
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.size - 1, index, -1):
                node = node.prev
        return node

    def __getitem__(self, item: Union[int, slice]) -> ...:
        if not (type(item) in (int, slice)):
            raise TypeError(f'list indices must be integers or slices, not {type(item)}')
        if isinstance(item, slice):
            if item.step == 0:
                raise ValueError('slice step cannot be zero')
            if item.start is None:
                if item.stop is None:
                    if item.step is None:
                        start, stop, step = 0, self.size, 1
                    elif item.step > 0:
                        start, stop, step = 0, self.size, item.step
                    else:
                        start, stop, step = self.size - 1, -1, item.step
                else:
                    if item.step is None:
                        start, stop, step = 0, item.stop, 1
                    elif item.step > 0:
                        start, stop, step = 0, item.stop, item.step
                    else:
                        start, stop, step = self.size - 1, item.stop, item.step
            else:
                if item.stop is None:
                    if item.step is None:
                        start, stop, step = item.start, self.size, 1
                    elif item.step > 0:
                        start, stop, step = item.start, self.size, item.step
                    else:
                        start, stop, step = item.start, -1, item.step
                else:
                    if item.step is None:
                        if item.start < item.stop:
                            start, stop, step = item.start, item.stop, 1
                        else:
                            start, stop, step = item.start, item.stop, -1
                    else:
                        start, stop, step = item.start, item.stop, item.step
            if not (item.start is None) and item.start < 0:
                start %= self.size
            if not (item.stop is None) and item.stop < 0:
                stop %= self.size
            Slice = List()
            node = self.head
            idx = 0
            while not (node is None):
                if ((step > 0 and start <= idx < stop) or (step < 0 and start >= idx > stop)) and (
                        idx - start) % step == 0:
                    Slice.push(node)
                node = node.next
                idx += 1
            if step < 0:
                Slice.reverse()
            return Slice
        else:
            node = self.getNode(item)
            return node.data

    def __setitem__(self, key: int, value: Any) -> None:
        node = self.getNode(key)
        node.data = value

    def __str__(self) -> str:
        result = ''
        for data in self:
            result += str(data) + ', '
        return '[' + result[:-2] + ']'

    def __iter__(self):
        self.currentNode = self.head
        return self

    def __next__(self):
        if self.currentNode is None:
            del self.currentNode
            raise StopIteration
        else:
            data = self.currentNode.data
            self.currentNode = self.currentNode.next
            return data

    def __len__(self) -> int:
        return self.size

    def __bool__(self) -> bool:
        return not self.isEmpty()

    def __contains__(self, item: Any) -> bool:
        for data in self:
            if item == data:
                return True
        return False

    def __mul__(self, other: int):
        if type(other) != int:
            raise TypeError(f"can't multiply sequence by non-int of type {type(other)}")
        NewList = List()
        for _ in range(other):
            NewList += self.deepcopy()
        return NewList

    def __add__(self, other):
        if type(other) != List:
            raise TypeError(f'can only concatenate list (not {type(other)}) to list')
        NewList = self.deepcopy()
        if other.isEmpty():
            return NewList
        NewOtherList = other.deepcopy()
        if self.isEmpty():
            return NewOtherList
        NewList.tail.next = NewOtherList.head
        NewOtherList.head.prev = NewList.tail
        NewList.tail = NewOtherList.tail
        NewList.size += NewOtherList.size
        return NewList

    def __eq__(self, other: Any) -> bool:
        if type(other) != List or len(self) != len(other):
            return False
        node1, node2 = self.head, other.head
        for _ in range(len(self)):
            if node1.data != node2.data:
                return False
        return True

    def sort(self) -> None:
        if self.isEmpty():
            return None
        else:
            sorted_list = List(self.head.data)
        node = self.head.next
        for _ in range(1, self.size):
            if node.data <= sorted_list.head.data:
                sorted_list.insert(node.data, 0)
            elif node.data >= sorted_list.tail.data:
                sorted_list.push(node.data)
            else:
                other_node = sorted_list.head
                index = 0
                while not (other_node.data <= node.data <= other_node.next.data):
                    other_node = other_node.next
                    index += 1
                sorted_list.insert(node.data, index + 1)
            node = node.next
        self.head = sorted_list.head
        self.tail = sorted_list.tail

    def reverse(self) -> None:
        node = self.head
        for _ in range(len(self)):
            node.prev, node.next = node.next, node.prev
            node = node.prev
        self.head, self.tail = self.tail, self.head

    def index(self, x: Any) -> int:
        for idx, data in enumerate(self):
            if data == x:
                return idx
        raise ValueError(f'{x} is not in list')

    def count(self, x: Any) -> int:
        result = 0
        for data in self:
            if data == x:
                result += 1
        return result

    def find(self, x: Any) -> int:
        for idx, data in enumerate(self):
            if x == data:
                return idx
        return -1

    def remove(self, value: Any) -> bool:
        node = self.head
        for idx in range(len(self)):
            if node.data == value and type(node.data) == type(value):
                self.pop(idx)
                return True
            node = node.next
        return False

    def clear(self) -> None:
        self.__init__()

    def isEmpty(self) -> bool:
        return self.size == 0

    def copy(self):
        copied_list = List()
        for data in self:
            copied_list.push(data)
        return copied_list

    def deepcopy(self):
        copied_list = List()
        for data in self:
            if type(data) in (int, float, complex, str, bytes, tuple):
                copied_list.push(data)
            elif type(data) == List:
                copied_list.push(data.deepcopy())
            else:
                copied_list.push(deepcopy(data))
        return copied_list

    def length(self):
        result = 0
        node = self.head
        while not (node is None):
            result += 1
            node = node.next
        return result


class Node(List):
    def __init__(self, data: Any, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        if type(self.data) == str:
            return "'" + self.data + "'"
        else:
            return str(self.data)
