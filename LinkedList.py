class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def __len__(self)->int:
        return self.count
    
    def insertHead(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
    
    def insertTail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        new_node.next = None
        self.count += 1 

    def insert(self, index, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        for i in range(index-1):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        self.count += 1
    
    def pop(self):
        if self.head is None:  # Check for empty list
            return None  # Indicate nothing was popped

        curr = self.head
        prev = None  # Keep track of the previous node

        while curr.next is not None:  # Iterate to the second-to-last node
            prev = curr
            curr = curr.next

        if prev is None:  # Handle removing the only node
            self.head = None
        else:
            prev.next = None  # Detach the last node

        self.count -= 1
    
    def PrintList(self):
        curr = self.head
        while curr != None:
            print(f"{curr.data}->", end='')
            curr = curr.next
        
if __name__ == "__main__":
    LIST = LinkedList()
    LIST.insertHead(50)
    LIST.insertHead(40)
    LIST.insertHead(30)
    LIST.insertHead(20)
    LIST.insertHead(10)
    print("\nBefore pop Operation\n")
    LIST.PrintList()
    print("\nAfter Pop Operation")
    LIST.pop()
    LIST.PrintList()
    print(f"\n{LIST.__len__()}")
