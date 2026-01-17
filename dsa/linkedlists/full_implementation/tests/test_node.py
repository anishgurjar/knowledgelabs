from linked_list.node import Node

def test_node_gets_created():
    node = Node()
    assert node.value == None
    assert node.next == None

def test_node_can_insert_value():
    node = Node()
    node.set_value(23)
    assert node.value == 23

def test_we_can_see_value():
    node = Node()
    node.value = "anish"
    assert node.get_value() == "anish"
 
def test_we_can_set_next_pointer():
    node1 = Node()
    node2 = Node()
    node2.set_next(node1)
    assert node2.next == node1