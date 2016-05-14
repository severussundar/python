class Node :
	def __init__(self,data=None):
		self.data=data
		self.prev=None
		self.next=None
	
	def getData(self):
		return self.data

	def setData(self,data):
		self.data=data 

	def setNext(self,newNext):
		self.next=newNext

	def getNext(self):
		return self.next

	def getPrev(self):
		return self.prev 

	def setPrev(self,newPrev):
		self.prev=newPrev 

class lList :
	def __init__(self):
		self.head=None
	   
	def isEmpty(self):
		return self.head == None

	def addMember(self,data):
		newNode=Node(data)
		newNode.next=self.head
		newNode.prev=None
		self.head=newNode

	def removeMember(self,data):
		curr=self.head
		prev=None
		found=False
		while not found :
		   if curr.getData() == data :
			  found=True
		   else :
			  prev=curr
			  curr=curr.getNext()

		prev.setNext(curr.getNext())
		curr.getNext().setPrev(prev)
		curr.setPrev(None)
		curr.setNext(None) 

	def printList(self):
		temp=self.head
		while temp !=None :
			print temp.getData(),
			temp=temp.getNext()               

def main():
	l=lList()
	l.addMember(1)
	l.addMember(2)
	l.addMember(3)
	l.addMember(4)
	l.printList()
	print 
	l.removeMember(2)
	l.printList()

if __name__ == '__main__' :
	main()	
