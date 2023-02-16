class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def list_to_linked_list(lst):
    head = Node(lst[0])
    current = head
    for i in range(1, len(lst)):
        current.next = Node(lst[i])
        current = current.next
    return head

def merge_sort_decorator(func):
    def wrapper(lst):
        sorted_lst = sorted(lst)
        return func(sorted_lst)
    return wrapper

@merge_sort_decorator
def list_to_linked_list(lst):
    head = Node(lst[0])
    current = head
    for i in range(1, len(lst)):
        current.next = Node(lst[i])
        current = current.next
    return head

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
my_linked_list = list_to_linked_list(my_list)

current = my_linked_list
while current is not None:
    print(current.data, end = ' -> ')
    current = current.next
print('None')


