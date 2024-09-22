class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
def reverse(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def print_list(head):
    current = head
    while current is not None:
        print(current.data,end=" -> " if current.next else "\n")
        current = current.next

def create_linked_list(val):
    if not val:
        return None
    head = ListNode(val[0])
    current = head
    for i in val[1:]:
        current.next = ListNode(i)
        current = current.next
    return head


head_list = [1,2,3,4,5]
print_list(create_linked_list(head_list))
print_list(reverse(create_linked_list(head_list)))