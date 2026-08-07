import sys

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

def read_numbers():
    numbers = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            numbers.extend(map(float, line.split()))
    return numbers

def create_linked_renga(numbers):
    renga = LinkedList()
    i = 0
    stanza_count = 0
    while i < len(numbers):
        if stanza_count % 2 == 0:  # 3-line stanza
            for _ in range(3):
                if i < len(numbers):
                    renga.append(numbers[i])
                    i += 1
        else:  # 2-line stanza
            for _ in range(2):
                if i < len(numbers):
                    renga.append(numbers[i])
                    i += 1
        stanza_count += 1
    return renga

def print_renga_with_pivots(renga):
    current = renga.head
    stanza_count = 0
    while current:
        if stanza_count % 2 == 0:  # 3-line stanza
            print(f"{current.value} + {current.next.value} + {current.next.next.value} = ", end="")
            total = current.value + current.next.value + current.next.next.value
            print(total)
            current = current.next.next.next
        else:  # 2-line stanza
            print(f"{current.value} + {current.next.value} = ", end="")
            total = current.value + current.next.value
            print(total)
            current = current.next.next
        stanza_count += 1

def calculate_and_print_stats(renga):
    total_sum = 0
    count = 0
    current = renga.head
    while current:
        total_sum += current.value
        count += 1
        current = current.next

    average = total_sum / count if count > 0 else 0

    print(total_sum)
    print(count)
    print(average)

def main():
    numbers = read_numbers()
    renga = create_linked_renga(numbers)
    print_renga_with_pivots(renga)
    calculate_and_print_stats(renga)

if __name__ == "__main__":
    main()
