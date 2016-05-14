class TreeNode :
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def insert(root,data):
	if not root :
		root=TreeNode(data)
	else :
		if root.data >= data :
		  if root.left :
			 insert(root.left,data)
		  else :
			 root.left=TreeNode(data)

		else :
		  if root.right :
			 insert(root.right,data)
		  else :
			 root.right=TreeNode(data)            

def inorder(root):
	if not root :
		return 

	inorder(root.left)
	print root.data,	
	inorder(root.right)

def preorder(root):
	if not root :
		return

	print root.data,
	preorder(root.left)
	preorder(root.right)

def postorder(root):
	if not root :
		return 
	
	preorder(root.left)
	preorder(root.right)
	print root.data,

def main():
	r=TreeNode(3)
	insert(r,4)
	insert(r,5)  
	insert(r,2) 
	insert(r,6)
	
	inorder(r)
	print 
	preorder(r)
	print
	postorder(r)
	print
	          	

if __name__ == '__main__' :
	main()