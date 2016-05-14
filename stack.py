class stack:
	def __init__(self):
		self.items=[]

	def push(self,item):
	    self.items.append(item)

	def pop(self):
	    self.items.pop()

    def isEmpty(self):
    	return  (self.items == [])
    
def main():
	s=stack()
	s.push(5)
	s.push(6)
	print s.isEmpty()
	s.pop()
	s.pop()
	print s.isEmpty()

if __name__ == '__main__':
    main()	


