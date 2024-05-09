class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def __len__(self) -> int:
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

    def Deletehead(self):

        if self.head is None:
            raise "Given List is Empty"

        self.head = self.head.next
        self.count -=1

    def DeleteByVal(self, val):
        if self.head is None:
            raise "Given List is Empty"
            return
        curr = self.head

        if self.head.data == val:
            self.Deletehead()

        while curr.next != None:
            if curr.next.data == val:
                break
            curr = curr.next

        if curr.next is None:
            print("Not Found")
            return
        else:
            curr.next = curr.next.next
            self.count-=1

    def SearchByVal(self, value):
        if self.head is None:
            raise "Empty List"
        
        while self.head.next != None:
            if self.head.data == value:
                print("Found")
                return
            self.head = self.head.next

        print("Not Found")

    def SearchIndex(self, index:int):
        if self.head is None:
            raise "List is empty"
        if index < self.count:
            raise IndexError("Index Out of Range....")
        for i in range(index-1):
            self.head = self.head.next
        print(f"Value at given Index: {self.head.data}")

    def PrintList(self):
        curr = self.head
        while curr != None:
            print(f"{curr.data}->", end='')
            curr = curr.next
        print("NULL")


if __name__ == "__main__":
    LIST = LinkedList()
    LIST.insertHead(50)
    LIST.insertHead(40)
    LIST.insertHead(30)
    LIST.insertHead(20)
    LIST.insertHead(10)
    LIST.SearchIndex(5)
