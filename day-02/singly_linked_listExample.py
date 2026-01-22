## 🔹 Node Structure


class Node:
    def __init__(self,info,next=None):  # Initialize node with data and next pointer (we hve to allocate memory so that we need (constructor in c++ same as init) init function in python) write def to make function, self is used to refer to current object, _init__ is a special function which is called when object is created, info is data part, next is pointer part, next=None means by default next is None
        self.data = info
        self.next = next  # next is pointer part which is by default None
# ## 🔹 Singly Linked List Class
class SinglyLinkedList:
    def __init__(self, head=None):  # constructor to initialize head pointer, here head is pointer to first node
        self.head = head # head is pointer to first node

    def insertAtEnd(self, data):  # function to insert node at end
        temp = Node(data)  # create a new node with given data
        if(self.head != None): 
            t1 = self.head  # t1 is a temporary pointer to traverse the list
            while(t1.next != None):  # traverse to the last node
                t1 = t1.next
            t1.next = temp  # link the last node to the new node
        else:
            self.head = temp  # if list is empty, make new node as head
    
    def insertAtBeg(self, data):
        temp = Node(data)  # create a new node with given data
        temp.next = self.head  # link new node to current head
        self.head = temp  # update head to new node

    def insertinMid(self, data, x):  # function to insert node after a given node with data x
        temp = Node(data)  # create a new node with given data
        t1 = self.head  # t1 is a temporary pointer to traverse the list
        while(t1.next != None):  # traverse till the last node
            if(t1.data == x):  # if current node's data matches x
                temp.next = t1.next  # link new node to next of current node
                t1.next = temp  # link current node to new node
                return
            t1 = t1.next  # move to next nodeß

    def deleteLL(self, data):  # function to delete first occurrence of node with given data
        t1 = self.head  # t1 is a temporary pointer to traverse the list
        prev = t1  # prev is a pointer to keep track of previous node
        if(t1.data == data):  # if head node itself holds the key to be deleted
            self.head = t1.next  # change head
            return

        while(t1.next != None):  # traverse till the last node
            if(t1.data == data):  # if current node's data matches data
                prev.next = t1.next  # link previous node to next of current node
                break
            else:
                prev = t1  # update previous node
                t1 = t1.next  # move to next node

        if(t1.data == data):  # if last node is to be deleted
            prev.next = None  # unlink the last node

            
    
    def printLL(self):  # function to display the list
        t1 = self.head  # t1 is a temporary pointer to traverse the list
        while(t1.next != None):  # traverse till the last node
            print(t1.data)  # print data of current node
            t1 = t1.next  # move to next node
        print(t1.data)  # print data of last node


obj = SinglyLinkedList()  # create an object of SinglyLinkedList
obj.insertAtEnd(10)  # insert node with data 10 at end
obj.insertAtEnd(20)  # insert node with data 20 at end
obj.insertAtEnd(30)  # insert node with data 30 at end

obj.insertAtBeg(5)  # insert node with data 5 at beginning
obj.insertinMid(15, 10)  # insert node with data 15 after node with data 10
obj.deleteLL(20)  # delete node with data 20

obj.printLL()  # display the list

