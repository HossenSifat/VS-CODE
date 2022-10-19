#link-list


class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value

class DoubleLinkedList:
    def __init__(self):
        self.head =None
        self.tail = None
        self.size = 0
    
    def add(self, val):
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1
    
    def front(self):
        return self.head.val
    
    def back(self):
        return self.tail.val
    
    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        self.size -= 1
    
    def remove(self, value):
        node = self.head
        while node is not None:
            if node.val == value:
                self.__remove_node(node)
            node = node.next

    def __str__(self):
        vals=[]
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{','.join(str(val) for val in vals)}]"

# my_list = DoubleLinkedList()
# my_list.add(1)
# my_list.add(4)
# my_list.add(3)
# my_list.add(9)
# my_list.add(7)
# my_list.add(13)
# my_list.add(3)
# my_list.add(6)

# print(my_list)
# print(my_list.size)
# my_list.remove(4)
# print(my_list)

#stack

class Stack:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def push(self, val):
        self.__list.add(val)

    def pop(self):
        val = self.__list.back()
        self.__list.remove(val)
        return val

    def is_empty(self):
        return self.__list.size == 0

    def peak(self):
        return self.__list.back()

    def __len__(self):
        return self.__list.size



my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print(my_stack.peak())
my_stack.push(5)
my_stack.push(8)
print(len(my_stack))
print(my_stack.pop())
print(len(my_stack))
print(my_stack.peak())