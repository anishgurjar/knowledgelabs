from .node import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def length(self):
        return self.length

    def append_value(self, value):
        node = Node()
        if(self.length == 0):
            self.head = node
        
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = node
        node.set_value(value)

        self.length +=1 

    def insert_value(self, position, value):
        #inserts the value of a node at the given position with a new value
        pass

    def update_value(self, position, new_value):
        #updates the value of a node at the given position with the new value
        pass 

    def display_values(self):
        res = ""
        if(self.head != None):
            temp = self.head
            while(temp != None):
                res += f"{temp.get_value()}-"
                temp = temp.next
        return res


    def remove_first_occurrence(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        prev = self.head
        temp = self.head.next

        while temp is not None:
            if temp.value == value:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next


    def remove_all_occurances(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next

        prev = self.head
        temp = self.head.next

        while temp is not None:
            if temp.value == value:
                prev.next = temp.next
            prev = temp
            temp = temp.next

    def pop(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None


    def reverse(self):

        head1 = None
        temp = self.head
        while(temp!=None):
            new_node = temp
            temp = temp.next
            new_node.next = head1
            head1 = new_node
        self.head = head1


    def search(self, value):
        pass
    
    def find_middle(self):
        #returns the middle value of the list
        
    
    def remove_duplicates(self):
        pass
