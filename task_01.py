"""
Завдання 1. 
Структури даних. Сортування. Робота з однозв'язним списком
Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None
    
    def insertion_sort(self):
        if not self.head or not self.head.next:
            return
        sorted_llist = None
    
        current = self.head
        while current:
            next_node = current.next
            sorted_llist = self.sorted_insert(sorted_llist, current)
            current = next_node
        self.head = sorted_llist
        
    def sorted_insert(self, sorted_head, new_node):
        if not sorted_head or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            sorted_head = new_node
        else:
            current = sorted_head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return sorted_head
    
    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next 
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def merge_sorted(self, other):
            # Initialize a dummy node to build the merged list
            dummy = Node(0)
            tail = dummy
            
            l1 = self.head
            l2 = other.head

            # Merge the two lists
            while l1 and l2:
                if l1.data < l2.data:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            self.head = dummy.next


    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print()


if __name__ == "__main__":

    llist_1 = SinglyLinkedList()
    # Вставляємо вузли в початок
    llist_1.insert_at_beginning(5)
    llist_1.insert_at_beginning(10)
    llist_1.insert_at_beginning(15)
    llist_1.insert_at_end(20)
    llist_1.insert_at_end(25)
    print("Зв'язний список до сортування:")
    llist_1.print_list()
    print("Реверсування однозв'язного списку:")
    llist_1.reverse()
    llist_1.print_list()

    llist_1.insertion_sort()
    print("Зв'язний список після сортування:")
    llist_1.print_list()



    llist_2 = SinglyLinkedList()
    # Вставляємо вузли в початок
    llist_2.insert_at_beginning(2)
    llist_2.insert_at_beginning(1)
    llist_2.insert_at_beginning(6)
    llist_2.insertion_sort()
    print("Зв'язний список 2 після сортування:")
    llist_2.print_list()


    llist_1.merge_sorted(llist_2)
    print("Зв'язний список після об'єднання 1 та 2:")
    llist_1.print_list()