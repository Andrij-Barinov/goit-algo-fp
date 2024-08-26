class Node:
    def __init__(self, data):
        # Ініціалізація вузла з даними та посиланням на наступний вузол
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Ініціалізація однозв'язного списку з головою, що вказує на перший вузол
        self.head = None

    def append(self, data):
        # Додавання нового вузла з даними в кінець списку
        new_node = Node(data)
        if not self.head:
            # Якщо список порожній, новий вузол стає головою
            self.head = new_node
            return
        # Інакше, знайти останній вузол і додати до нього новий
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        # Виведення всіх елементів списку
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse_list(self):
        # Реверсування однозв'язного списку
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Зберігаємо посилання на наступний вузол
            current.next = prev       # Змінюємо посилання на попередній вузол
            prev = current            # Переміщуємо prev вперед
            current = next_node       # Переміщуємо current вперед
        self.head = prev              # Новою головою стає останній оброблений вузол

    def merge_sort(self, head):
        # Сортування списку за допомогою алгоритму злиття
        if not head or not head.next:
            # Базовий випадок: список порожній або містить один елемент
            return head

        # Знаходимо середину списку для поділу
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        # Рекурсивно сортуємо ліву і праву половини
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        # Зливаємо дві відсортовані половини
        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def sorted_merge(self, left, right):
        # Злиття двох відсортованих списків
        if not left:
            return right
        if not right:
            return left

        # Вибираємо менший елемент з початку кожного списку і додаємо його до результату
        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)

        return result

    def get_middle(self, head):
        # Знаходження середини списку за допомогою двох покажчиків
        if head is None:
            return head
        slow = head
        fast = head

        # Поки fast може рухатися вперед на два кроки, slow рухається на один крок
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge_two_sorted_lists(self, list1, list2):
        # Об'єднання двох відсортованих списків в один відсортований список
        if not list1:
            return list2
        if not list2:
            return list1

        # Вибираємо менший елемент з початку кожного списку і додаємо його до результату
        if list1.data <= list2.data:
            result = list1
            result.next = self.merge_two_sorted_lists(list1.next, list2)
        else:
            result = list2
            result.next = self.merge_two_sorted_lists(list1, list2.next)

        return result


if __name__ == "__main__":
    # Створення першого списку та додавання елементів
    llist = LinkedList()
    llist.append(10)
    llist.append(30)
    llist.append(20)
    llist.append(40)
    
    # Виведення початкового списку
    print("Original list:")
    llist.print_list()
    
    # Реверсування списку
    print("Reversed list:")
    llist.reverse_list()
    llist.print_list()
    
    # Сортування списку
    print("Sorted list:")
    llist.head = llist.merge_sort(llist.head)
    llist.print_list()
    
    # Створення другого списку та додавання елементів
    llist2 = LinkedList()
    llist2.append(5)
    llist2.append(35)
    
    # Об'єднання двох відсортованих списків
    print("Merged list:")
    merged_list_head = llist.merge_two_sorted_lists(llist.head, llist2.head)
    llist.head = merged_list_head
    llist.print_list()
