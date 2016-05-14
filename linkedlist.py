class Node :
	def __init__(self,data=None):
		 self.data=data
		 self.next=None

	def getNext(self):
		 return self.next

	def setData(self,data):
		 self.data=data 

	def getData(self):
		 return self.data 

	def setNext(self,newNext):
		 self.next=newNext 
 
class lList:
	def __init__(self):
		 self.head=None

	def isEmpty(self):
		 return self.head == None

	def addMember(self,data):
		 newNode=Node(data)
		 newNode.setNext(self.head)
		 self.head=newNode 
	 
	def printList(self):
		 temp=self.head
		 while temp !=None :
			 print temp.getData(),
			 temp=temp.getNext() 
	
	def search(self,data):
		 temp=self.head
		 while temp != None :
			 if temp.getData() == data :
				 return True
			 temp=temp.getNext() 	 

		 return False 
	
	def removeMember(self,data):
			
		 found=False
		 prev=None	 
		 curr=self.head
		 
		 while not found :
			 if curr.getData() == data :
					found= True
			 else :
					prev=curr
					curr=curr.getNext()
	 
		 if prev == None :
			 self.head=curr.getNext()  
		 else :
			 prev.setNext(curr.getNext())
			 curr.setNext(None)           


def main():
	l=lList()
	l.addMember(1)
	l.addMember(3)
	l.addMember(7)
	l.printList()
	l.removeMember(3)
	l.addMember(4)
	l.addMember(5)
	print 
	l.printList()
	print 
	print l.search(4)
	l.removeMember(4)
	print l.search(4)

if __name__ == '__main__':
	main()    
