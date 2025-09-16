"""
1. Insertion Sort
2. HEAP Sort
3. Merge Sort
4. Quick sort
5. Radix Sort """
def insertion_sort(arr):
	for i in range(1, len(arr)): #pick up an element from arr
		key = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > key: # Shift item to make room for key
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key #Insert key to the correct location
arr = [11, 14, 5, 13, 6]
insertion_sort(arr)
print("Sorted array:", arr)


#Heap structure
class Node: 
	def __init__(self,key):
		self.value = key
		self.left = None
		self.right = None
		self.parent = None #some funcitons in the class are required to know its parents and the last node
class BinaryTreeMinHeap:
	def __init__(self):
		self.root = None
		self.size = 0
		self.last_node = None

insert():
	Inserts a new element into the heap while maintain the heap property
	Time Complexity: O(log n)
get_min():
	Returns the minimum element without removing it
	Time Complexity: O(1)
extract_min():
	Removes and returns the min element from the heap while maintaining the heap property
	Time Complexity: O(log n)
build_heap():
	Converts an unsorted list into a valid heap structure

#Build a heap from a UNSORTED LIST 
"""1. Insert each element into a binary heap tree via level-by-level traversal"""
"""2. Use post-order traversal to adjust the binary tree to maintain the heap property
each subtree is processed before the current node, allowing us to effectively fix any violations of the heap property from the bottom up"""
def _heapify_down(self, node):
	while node:
		smallest = node
		if node.left and node.left.value < node.value:
			smallest = node.left
		if node.right and node.right.value < smallest.value:
			smallest = node.right
		if smallest != node:
			node.value, smallest.value = smallest.value, node.value
			node = smallest
		else:
			break
def build_heap(self, node):
	if not node:
		return
	if node.left:
		self.build_heap(node.left)
	if node.right:
		self.build_heap(node.right)
		self._heapify_down(node)
def build_heap_from_list(self, unsorted_list):
"""Convert an unsorted list into a binary heap."""
	new_node = Node(unsorted_list.pop(0))
	self.size += 1
	if not self.root:
		self.root = new_node
		self.last_node = new_node
	queue = [self.root]
	while unsorted_list:
		cur_q = queue[0]
		current = unsorted_list.pop(0)
	if not cur_q.left:
		cur_q.left = Node(current)
		cur_q.left.parent = cur_q
		self.last_node = new_node
		self.size += 1
		queue.append(cur_q.left)
	elif not cur_q.right:
		cur_q.right = Node(current)
		cur_q.right.parent = cur_q
		self.last_node = new_node
		self.size += 1
		queue.append(cur_q.right)
		queue.pop(0)
		self.build_heap(self.root
• Time Complexity: O(n)

#Implementation of insert() in a BINARY TREE 
def insert(self, key):
	"""Insert a node into the binary heap."""
	new_node = Node(key)
	self.size += 1
if not self.root:
	self.root = new_node
	self.last_node = new_node
	return
queue = [self.root]
while queue:
	current = queue.pop(0)
	if not current.left:
		current.left = new_node
		new_node.parent = current
		self.last_node = new_node
		break
	else:
		queue.append(current.left)
	if not current.right:
		current.right = new_node
		new_node.parent = current
		self.last_node = new_node
		break
	else:
		queue.append(current.right)
	self._heapify_up(self.last_node)
def _heapify_up(self, node):
	while node.parent and node.parent.value > node.value:
# Swap the current node with its parent
	node.value, node.parent.value = node.parent.value, node.value
	node = node.parent # Move up to the parent

#Implemention of insert() in a LIST
class BinaryTreeMinHeap:
	def __init__(self):
		self.heap = []
def insert(self, key):
	"""Inserts a new key into the heap."""
	self.heap.append(key)
	self._heapify_up(len(self.heap) - 1)
def _heapify_up(self, index):
	"""Restores the heap property by moving a node up."""
	parent_index = (index - 1) // 2
	while index > 0 and self.heap[parent_index] > self.heap[index]:
# Swap the current node with its parent
		self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
		index = parent_index
		parent_index = (index - 1) // 2

"""
Quick Sort
1. Pick a pivot element.
2. Partition the array into two sub-arrays: elements less than pivot and
elements greater than pivot.
3. Recursively sort the sub-arrays.
"""

def quick_sort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[(len(arr)-1) //2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quick_sort(left) + middle + quick_sort(right

"""
Radix Sort 
• Sort numbers by the least significant digit.
• Sort again by the next digit.
• Repeat until all digits are sorted.
"""

def counting_sort(arr, exp):
	n = len(arr)
	output = [0] * n
	count = [0] * 10
	for i in range(n):
		index = arr[i] // exp
		count[index % 10] += 1
	for i in range(1, 10):
		count[i] += count[i - 1]
	i = n - 1
while i >= 0:
	index = arr[i] // exp
	output[count[index % 10] - 1] = arr[i]
	count[index % 10] -= 1
	i -= 1
	for i in range(n):
		arr[i] = output[i]
def radix_sort(arr):
	max1 = max(arr)
	exp = 1
	while max1 // exp > 0:
		counting_sort(arr, exp)
		exp *= 10
	return arr												  
