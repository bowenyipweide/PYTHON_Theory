#Binary tree operations INSERT NODE > DELETE NODE > SEARCH NODE > DEPTH / BREATH FIRST TRAVERSAL (IN / PRE / POST ORDER / LEVEL-BY-LEVEL)

#Initiate class node for left & right tree 
class Node: 
	def __init__(self, data):
		self.data = data 
		self.left = None
		self.right = None
#PRE-Order Depth first traversal
def pre_order_traversal(self, node):
	if node: 
		print(node.data, end = "")
		self.pre_order_traversal(node.left)
		self.pre_order_traversal(node.right)
#IN-Order Depth first traversal
def pre_order_traversal(self, node):
	if node: 
		self.pre_order_traversal(node.left)
		print(node.data, end = "")
		self.pre_order_traversal(node.right)
#POST-Order Depth first traversal
def pre_order_traversal(self, node):
	if node: 
		self.pre_order_traversal(node.left)
		self.pre_order_traversal(node.right)
		print(node.data, end = "")
	
	
