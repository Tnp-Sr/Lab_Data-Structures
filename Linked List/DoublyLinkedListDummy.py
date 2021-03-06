class DoublyLinkedList : #Circular Doubly linked list with dummy
    class Node :
        def __init__(self,data,prev = None,next = None) :
            self.data = data
            if prev is None :
                self.prev = None
            else :
                self.prev = prev
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.dummy = self.Node(None,None,None)
            self.dummy.next = self.dummy.prev = self.dummy
            self.size = 0
            
    def __str__(self):
        s = 'linked data : '
        p = self.dummy.next
        for i in range(len(self)) :
            s += str(p.data) + ' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
        
    def isEmpty(self) :
        return self.size == 0
    
    def indexOf(self,data) :
        q = self.dummy.next
        for i in range(len(self)) :
            if q.data == data :
                return i
            q = q.next
        return -1
    
    def isIn(self,data) :
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :
        p = self.dummy
        for j in range(-1,i) :
            p = p.next
        return p
    
    def insertBefore(self,q,data) :
        p = q.prev
        x = self.Node(data,p,q)
        p.next = q.prev = x
        self.size += 1
        
    def append(self,data) :
        self.insertBefore(self.nodeAt(len(self)),data)
  
    def removeNode(self,q) :
        p = q.prev
        x = q.next
        p.next = x
        x.prev = p
        self.size -= 1
        
    def delete(self,i) :
        self.removeNode(self.nodeAt(i))


l2 = DoublyLinkedList()
l2.append('a')
l2.append('b')
l2.append('c')
l2.append('d')
l2.append('e')
l2.append('z')
print(l2)
l2.delete(5)
print(l2)
l2.delete(0)
print(l2)
l2.append('aa')
print(l2)
l2.delete(4)
print(l2)
print(l2.size)