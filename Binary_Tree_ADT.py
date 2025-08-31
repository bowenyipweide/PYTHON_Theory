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
			
#Level-by-level Depth first traversal
#(1)Enqueue current node > (2) Dequeue node > (3) Enqueue children > (4) Repeat step (2) until the queue is empty
	def level_order_traversal(self):
		if not self.root:
			return
		queue = deque ([self.root])
		while queue:
			current_node = queue.popleft()
			print(current_node.data, end = "")
			if current_node.left:
				queue.append(current_node.left)
			if curren_node.right:
				queue.append(current_node.right)
				
#Count node in binary tree
	def count_node(self, node):
		if not node: 
			return 0
		return 1 + self.count_nodes(node.left) +\ self.count_nodes(node.right) 
		
#Find Kth-level descendant nodes
	def kth_level_descendants(self, node, k):
		if note is None:
			return []
		if k == 0:
			return [node.data]
		left_descendants = self.kth_level_descendants(node.left, k - 1)
		right_descendants = self.kth_level_descendants(node.left, k - 1)

		return left_descendants + right_descendants 
		
#Height of a node in a binary tree 
#The number of edge on the longest path from the root
	def calculate_height(self, node):
		if node is None:
			return -1 
		left_height = self.calculate_height(node.left)
		right_height = self.calculate_height(node.right)
		return 1 + max(left_height, right_height)
		
#Node insertion on a binary tree 
#First inserted as a root, No rule to insert subsequence node into a binary
	def insert(self, data):
		if self.root is None:
			self.root = Node (data)
		else:
			self._insert(data, self.root)

#Binary search tree: searching. [Decrease and conquer approach] divided into two smaller and similar sub-problems, reduce search space.
#n = 2^k -1 > K = log2(n+1) > k = log2(n+1)
	def _search(self, data, current_node):
		if current_node is None:
			return False
		elif data == current_node.data:
			return True
		elif data < current_node.data:
			return self._search(data, current_node.left)
		else: 
			return self._search(data, current_node.right)

#Binary search Tree(BST): insertion
#BST remains as BST. duplicate node is not allowed for insertion 
	def _insert(self, data, current_node):
		if data < current_node.data:
			if current_node.left is None:
				current_node.left = Node(data)
			else:
				self._insert(data, current_node.left)
		else:
			if current_node.right is None:
				current_node.right = Node(data)
			else:
				self._insert(data, current_node.right)
	
	
		

			
	
