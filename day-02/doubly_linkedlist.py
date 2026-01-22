 
class Node:
    def __init__(self, value=None): # Node class to create a node
      self.data = value #  data part of node
      self.next = None # pointer part of node
      self.prev = None  # pointer to previous node


class DoublyLL: # Doubly Linked List class
    def __init__(self): # constructor to initialize head pointer
     self.head = None # head is pointer to first node

    def insertAtEnd(self, value): # function to insert node at end
      temp = Node(value) # create a new node with given value
      if(self.head == None):
        self.head = temp # if list is empty, make new node as head
        return
      t = self.head # t is a temporary pointer to traverse the list
      while (t.next != None): # traverse to the last node
        t = t.next
      t.next = temp # link the last node to the new node
      temp.prev = t  # link new node's prev to last node


    def insertAtBeg(self, value):
       temp = Node(value)  # create a new node with given value
       if(self.head == None):
         self.head = temp  # if list is empty, make new node as head
         return
       temp.next = self.head  # link new node to current head
       self.head.prev = temp  # link current head's prev to new node
       self.head = temp  # update head to new node

    def insertinMid(self, value, x):  # function to insert node after a given node with data x
       tmp = Node(value)  # create a new node with given value
       t1 = self.head # t1 is a temporary pointer to traverse the list
       while(t1 != None):  # traverse till the last node
              if(t1.data == x):  # if current node's data matches x
                tmp.next = t1.next  # link new node to next of current node
                tmp.prev = t1  # link new node's prev to current node
                if(t1.next != None):
                     t1.next.prev = tmp  # link next node's prev to new node
                t1.next = tmp  # link current node to new node
                return
              t1 = t1.next  # move to next node


    def deletionDLL(self, value):  # function to delete first occurrence of node with given value 
       if(self.head == None):
          print("List is empty")
          return  # if list is empty, return
       
       t1 = self.head  # t1 is a temporary pointer to traverse the list
       if(t1.data == value):  # if head node itself holds the key to be deleted
          self.head = t1.next  # change head
          self.head.prev = None  # change prev of new head to None
          return

       while(t1.next != None):  # traverse till the last node
           if(t1.data == value):  # if current node's data matches value
              t1.prev.next = t1.next  # link previous node to next of current node
              t1.next.prev = t1.prev  # link next node's prev to previous node
              return
           t1 = t1.next  # move to next node

           
       if(t1.data == value):  # if last node's data matches value
            t1.prev.next = None  # unlink the last node
            return
              
              
       
           
               

    def printLL(self):  # function to display the list
        t1 = self.head  # t1 is a temporary pointer to traverse the list
        while(t1.next != None):  # traverse till the last node
            print(t1.data)  # print data of current node
            t1 = t1.next  # move to next node
        print(t1.data)  # print data of last node

obj = DoublyLL() # create an object of Doubly Linked List   



obj.insertAtEnd(10) # insert node with data 10 at end
obj.insertAtEnd(20) # insert node with data 20 at end
obj.insertAtEnd(30) # insert node with data 30 at end
obj.insertAtBeg(5) # insert node with data 5 at beginning
obj.insertinMid(15,10) # insert node with data 15 after node with data 10
obj.deletionDLL(20) # delete node with data 20
obj.printLL() # print the linked list