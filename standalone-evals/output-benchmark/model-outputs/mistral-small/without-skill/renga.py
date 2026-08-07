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

    def get_values(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values

def read_numbers():
    numbers = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            try:
                num = float(line)
                numbers.append(num)
            except ValueError:
                continue
    return numbers

def create_linked_renga(numbers):
    ll = LinkedList()
    for num in numbers:
        ll.append(num)
    return ll

def print_renga_stanzas(ll):
    values = ll.get_values()
    stanzas = []
    i = 0
    stanza_num = 1
    while i < len(values):
        if stanza_num % 2 == 1:  # 3-line stanza
            stanza = values[i:i+3]
            i += 3
        else:  # 2-line stanza
            stanza = values[i:i+2]
            i += 2
        stanzas.append(stanza)
        stanza_num += 1

    for stanza in stanzas:
        for num in stanza:
            print(num)
        print("--")  # Pivot handoff

def calculate_and_print_stats(ll):
    values = ll.get_values()
    total = sum(values)
    count = len(values)
    average = total / count if count > 0 else 0
    print(total)
    print(count)
    print(average)

def main():
    numbers = read_numbers()
    ll = create_linked_renga(numbers)
    print_renga_stanzas(ll)
    calculate_and_print_stats(ll)

if __name__ == "__main__":
    main()
