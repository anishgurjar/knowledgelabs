from stack.stack import Stack
import pytest

def test_stack_size_is_correct():
    mystack = Stack()
    mystack.push(2)
    mystack.push(3)
    assert mystack._length == 2

def test_stack_can_push_elements_correctly():
    mystack = Stack()
    mystack.push(1)
    mystack.push(1)
    mystack.push(1)
    assert mystack._stack == [1,1,1]

def test_stack_can_pop_elements_correctly():
    mystack = Stack()
    mystack.push(1)
    mystack.push(1)
    mystack.push(1)
    item = mystack.pop()
    assert mystack._stack == [1,1]
    assert item == 1

def test_peek_returns_correct_top_element():
    mystack = Stack()
    mystack.push(1)
    assert mystack.peek() == 1