from linked_list.linked_list import LinkedList

def test_linked_list_gets_created():
    list = LinkedList()
    assert list.head == None

def test_we_can_append_value():
    list = LinkedList()
    list.append_value(23)
    assert list.head.get_value() == 23
    list.append_value(35)
    assert list.head.next.get_value() == 35
    list.append_value("anish")
    assert list.head.next.next.get_value() == "anish"

def test_we_can_display_values():
    list = LinkedList()
    list.append_value(23)
    list.append_value(35)
    list.append_value("anish")
    
    assert list.display_values() == "23-35-anish-"

def test_we_can_reverse_array():
    list = LinkedList()
    list.append_value(23)
    list.append_value(35)
    list.append_value("anish")
    list.reverse()
    assert list.display_values() == "anish-35-23-"

    list1 = LinkedList()
    list1.append_value(23)
    list1.append_value(35)
    list1.append_value("anish")
    list1.append_value("12")
    list1.reverse()
    assert list1.display_values() == "12-anish-35-23-"

def test_remove_first_occurance():
    list1 = LinkedList()
    list1.append_value(23)
    list1.append_value(35)
    list1.append_value("anish")
    list1.append_value("12")
    list1.remove_first_occurrence(23)
    assert list1.display_values() == "35-anish-12-"

def test_remove_all_occurances():
    list1 = LinkedList()
    list1.append_value(23)
    list1.append_value(35)
    list1.append_value("anish")
    list1.append_value(23)
    list1.append_value("12")
    list1.remove_all_occurances(23)
    assert list1.display_values() == "35-anish-12-"

def test_remove_all_occurances():
    list1 = LinkedList()
    list1.append_value(23)
    list1.append_value(35)
    list1.append_value("anish")
    list1.append_value(23)
    list1.append_value("12")
    list1.pop()
    assert list1.display_values() == "23-35-anish-23-"
