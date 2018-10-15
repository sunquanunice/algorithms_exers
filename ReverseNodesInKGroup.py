'''
Problem : Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

          k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

   Example:

   Given this linked list: 1->2->3->4->5

   For k = 2, you should return: 2->1->4->3->5

   For k = 3, you should return: 3->2->1->4->5

   Note:

	- Only constant extra memory is allowed.
	- You may not alter the values in the list's nodes, only nodes itself may be changed.


Link : https://leetcode.com/problems/reverse-nodes-in-k-group/description/

'''

class LinkedNode(object):
	def __init__(self, value):
		self.value = value
		self.next = None
	def size(self):
		count = 0 
		point = self
		while point :
			count += 1
			point = point.next
		return count
	def display(self):
		point = self
		while point :
			print(point.value)
			point = point.next

class ReverseNodesInKGroup(object):
	def  reverseNodes(self, k, linkNodes):
		reverseGroupNum = linkNodes.size() // k;
		count = 0
		idx = 0
		lastGroupTailNode = None
		headNode = linkNodes
		currNode = linkNodes
		prevNode = None
		while  count < reverseGroupNum and idx < k :
			nextNode = currNode.next		
			if idx == 0:
				groupTailNode = currNode
				currNode.next = None 
				prevNode = currNode
				idx += 1
			elif idx == k - 1:
				currNode.next = prevNode
				if count == 0:
					headNode = currNode
				else:
					lastGroupTailNode.next = currNode
				lastGroupTailNode = groupTailNode
				prevNode = groupTailNode
				count += 1
				idx = 0
			else:
				currNode.next = prevNode
				idx += 1
				prevNode = currNode
			currNode = nextNode
		if lastGroupTailNode:
			lastGroupTailNode.next = currNode
		return headNode			


if __name__ == '__main__' :
	node1 = LinkedNode(1)
	node2 = LinkedNode(2)
	node3 = LinkedNode(3)
	node4 = LinkedNode(4)
	node5 = LinkedNode(5)
	node6 = LinkedNode(6)
	node7 = LinkedNode(7)
	node8 = LinkedNode(8)
	node1.next = node2
	node2.next = node3
	node3.next = node4
	node4.next = node5
	node5.next = node6
	node6.next = node7
	node7.next = node8
	reverseNodes = ReverseNodesInKGroup()
	#reverseNodes.reverseNodes(2, node1).display()
	reverseNodes.reverseNodes(3, node1).display()