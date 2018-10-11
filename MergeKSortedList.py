'''
Problem : Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
Link : https://leetcode.com/problems/merge-k-sorted-lists/description/
Solutions : https://leetcode.com/problems/merge-k-sorted-lists/solution/
'''

class ListNode(object):
	def __init__(self, value):
		self.value = value
		self.next = None
	def display(self):
		point = self
		while point :
			print(point.value)
			point = point.next

class MergeKSortedList(object):

	def mergeLists(self, lists):
		amount = len(lists)
		interval = 1
		while interval < amount:
			for i in range(0, amount - interval, interval * 2):
				lists[i] = self.merge2Lists(lists[i], lists[i + interval])
			interval *= 2
		return lists[0] if amount > 0 else lists

	'''
	This function merge two sorted lists into a list, the complexity is O(N)
	'''
	def merge2Lists(self, l1, l2):
		head = point = ListNode(0)
		while l1 and l2:
			if l1.value <= l2.value:
				point.next = l1
				l1 = l1.next
			else:
				point.next = l2
				l2 = l2.next
			point = point.next
		if l1 :
			point.next = l1
		else:
			point.next = l2
		return head.next









if __name__ == '__main__':
	node1 = ListNode(1)
	node2 = ListNode(4)
	node3 = ListNode(5)
	node4 = ListNode(1)
	node5 = ListNode(3)
	node6 = ListNode(4)
	node7 = ListNode(2)
	node8 = ListNode(6)
	node1.next = node2
	node2.next = node3
	node4.next = node5
	node5.next = node6
	node7.next = node8
	lists = [node1, node4, node7]
	sortedList = MergeKSortedList().mergeLists(lists)
	print("{0}".format(sortedList.display()))