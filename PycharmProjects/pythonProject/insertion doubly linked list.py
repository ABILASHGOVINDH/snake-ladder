class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class insertion:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_at_beinning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def insertion_at_end(self,data):
        new_node = Node(data)
        if new_node is None:
          self.head = new_node
          self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def print_values(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next



c = insertion()
c.insert_at_beinning(20)
c.insert_at_beinning(10)
c.insertion_at_end(30)
c.print_values()

