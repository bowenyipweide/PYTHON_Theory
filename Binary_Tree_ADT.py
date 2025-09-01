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

#Sort all data in a list and reconstruct the tree
def tree_balance(data, first, last):
	if last >= first:
		middle = (first + last) // 2
		root = Node(data[middle])
		root.left = tree_balance(data, first, middle - 1)
		root.right =tree_balance(data, middle + 1, last)
		return root
	return None
	
#Balance factor: Height of left subtree - height of right subtree 
*Balance factor of each node in an AVL tree can only be -1, 0 or 1*
class AVLNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.height = 0 # New attribute for the height of the node
	def _get_height(self, node):
		if not node:
			return -1
		return node.height
	def _get_balance(self, node):
		if not node:
			return 0
		return self._get_height(node.left) - self._get_height(node.right)
	#Right / Left Rotation 
{left Subtree Left Node;
Right Subtree Right Node;
Right Subtree Left Node;
Left Subtree Right Node}
	def right_rotate(self, cur):
		x = cur.left
		xRChild = x.right
		# Perform rotation
		cur.left = xRChild #Step 1
		x.right = cur #Step 2
		# Update heights
		cur.height = 1 + max(self.get_height(cur.left), self.get_height(cur.right))
		x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
		# Return the new root
		return x
	
	
		

			
	
