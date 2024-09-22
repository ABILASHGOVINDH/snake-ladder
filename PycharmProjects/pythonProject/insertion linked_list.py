class Node:
    def __init__(self,data):
            self.data = data
            self.next = None
class insertion:
    def __init__(self):
        self.head =None

    def add(self,data):
        n = Node(data)
        if self.head is None or self.head.data>data:
            n.next = self.head
            self.head = n
        else:
            current = self.head
            while(current.next is not None and current.next.data<data):
                current = current.next
            n.next = current.next
            current.next = n
    def print_values(self):
        current = self.head
        while current:
            print(f" {current.data}", end=" ")

            current = current.next

        return None

linked_list = insertion()
names = ["John", "Abi", "Avi", "Praveen"]
for name in names:
    linked_list.add(name)

print(linked_list.print_values())

print()
print()
names = ['john', 'abi', 'avi', 'praveen']

sorted_names = []

for name in names:
    for i in range(len(sorted_names)):
        if name < sorted_names[i]:
           sorted_names.insert(i,name)
           break

    else:
      sorted_names.append(name)
print(sorted_names)
